#!/usr/bin/env python3
"""Finite checks of channel identities and explicit extension certificates.

The all-dimension statements are proved in science/. These calculations test
finite cases, including a Kraus enumeration independent of the closed formula.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np

TOL = 2e-11


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def bell(d):
    vector = np.eye(d).reshape(-1) / np.sqrt(d)
    return np.outer(vector, vector)


def trace_last(matrix, d):
    return np.einsum('abcdec->abde', matrix.reshape(d, d, d, d, d, d)).reshape(d*d, d*d)


def geometry(d):
    phi = bell(d)
    p1 = np.kron(phi, np.eye(d))
    swap = np.zeros((d**3, d**3))
    for r, b, c in itertools.product(range(d), repeat=3):
        swap[(r*d+c)*d+b, (r*d+b)*d+c] = 1
    p2 = swap @ p1 @ swap
    eye = np.eye(d**3)
    t = 1 - 1/d**2
    cross = (eye-p2) @ p1 @ (eye-p2) / (d*t)
    union = (p1+p2-p1@p2-p2@p1)/t
    common_kernel = (eye-union)/(d**3-2*d)
    return phi, p1, p2, swap, cross, common_kernel


def ideal_certificate(d):
    phi, p1, p2, swap, cross, kernel = geometry(d)
    nstar = (d*d-1)**2
    b = 1/(d*d-1)
    good = b*trace_last(cross, d)
    bad = b*trace_last(swap@cross@swap, d)+(1-2*b)*trace_last(kernel, d)
    good_expected = phi/d**2+(np.eye(d*d)-phi)/(nstar*d*d)
    bad_expected = (nstar-1)*(np.eye(d*d)-phi)/(nstar*d*d)
    q2 = np.eye(d**3)-p2
    t = 1-1/d**2
    row = {
        'dimension': d, 'boundary_orders': nstar,
        'cross_min_eigenvalue': float(np.linalg.eigvalsh(cross).min()),
        'kernel_min_eigenvalue': float(np.linalg.eigvalsh(kernel).min()),
        'cross_trace_error': float(abs(np.trace(cross)-1)),
        'kernel_trace_error': float(abs(np.trace(kernel)-1)),
        'good_marginal_error': float(np.linalg.norm(good-good_expected)),
        'bad_marginal_error': float(np.linalg.norm(bad-bad_expected)),
        'bell_compression_error': float(abs(np.linalg.eigvalsh(q2@p1@q2).max()-t)),
        'symmetric_bell_bound_error': float(abs(np.linalg.eigvalsh(p1+p2).max()/2-(1+1/d)/2)),
        'next_integer_witness_violation': float(1/d**2-t*(nstar+d*d)/((nstar+1)*d*d)),
    }
    require(row['cross_min_eigenvalue'] > -TOL, 'Cross certificate is not positive')
    require(row['kernel_min_eigenvalue'] > -TOL, 'Kernel certificate is not positive')
    require(all(v < TOL for k, v in row.items() if k.endswith('_error')), 'Ideal certificate mismatch')
    require(row['next_integer_witness_violation'] > 0, 'Converse witness failed')
    return row


def noisy_certificate(d, fraction):
    phi, _, _, swap, _, kernel = geometry(d)
    ceiling = d*d/(d*d+1)
    v = fraction*ceiling
    q = v/d**2
    cross = q*np.kron(phi, np.eye(d)/d)
    a = 1-(1+1/d**2)*v
    b = v*(1-1/d**2)
    both_bad = a*np.eye(d**3)/d**3+b*kernel
    good = trace_last(cross, d)
    bad = trace_last(swap@cross@swap+both_bad, d)
    good_expected = v*phi/d**2
    bad_expected = (np.eye(d*d)-v*phi)/d**2
    row = {
        'dimension': d, 'visibility_fraction_of_ceiling': fraction, 'visibility': v,
        'both_bad_min_eigenvalue': float(np.linalg.eigvalsh(both_bad).min()),
        'good_marginal_error': float(np.linalg.norm(good-good_expected)),
        'bad_marginal_error': float(np.linalg.norm(bad-bad_expected)),
        'normalization_error': float(abs(2*np.trace(cross)+np.trace(both_bad)-1)),
    }
    require(row['both_bad_min_eigenvalue'] > -TOL, 'Noisy certificate is not positive')
    require(all(v < TOL for k, v in row.items() if k.endswith('_error')), 'Noisy certificate mismatch')
    above = ceiling+0.01*(1-ceiling)
    required_residual_bell = (d*d-(d*d+1)*above)/d**4
    require(required_residual_bell < 0, 'Limiting converse failed')
    row['above_ceiling_residual_bell_weight'] = required_residual_bell
    return row


def raw_cyclic_choi(d, n):
    """Enumerate products of K_ab=|a><b|/sqrt(d) for independent slots."""
    kraus = []
    for a, b in itertools.product(range(d), repeat=2):
        k = np.zeros((d, d))
        k[a, b] = 1/np.sqrt(d)
        kraus.append(k)
    size = n*d*d
    actual = np.zeros((size, size))
    for labels in itertools.product(range(d*d), repeat=n):
        vectors = []
        for shift in range(n):
            product = np.eye(d)
            for step in range(n):
                product = kraus[labels[(shift+step) % n]] @ product
            vectors.append(product.T.reshape(-1)/np.sqrt(d*n))
        vector = np.concatenate(vectors)
        actual += np.outer(vector, vector)
    phi = bell(d)
    expected = np.kron(np.eye(n)/n, np.eye(d*d)/d**2)
    expected += np.kron((np.ones((n, n))-np.eye(n))/n, phi/d**2)
    error = float(np.linalg.norm(actual-expected))
    require(error < TOL, 'Raw cyclic Kraus formula failed')
    return {'dimension': d, 'orders': n, 'kraus_tuples': (d*d)**n, 'choi_error': error}


def correlated_controller(n=3, m=2, d=2, ancilla=2, visibility=0.8):
    """Check the block simulation on a normalized Choi input, not one state."""
    labels = list(itertools.product(range(n), repeat=m))
    position = {label: i for i, label in enumerate(labels)}
    count = len(labels)
    rng = np.random.default_rng(20261113)
    a = rng.normal(size=(count, ancilla))+1j*rng.normal(size=(count, ancilla))
    a /= np.linalg.norm(a)
    payload = d**(2*m)
    uniform = np.zeros((count*payload, count*payload), dtype=complex)
    actual = np.zeros((count*ancilla*payload, count*ancilla*payload), dtype=complex)
    j_same = np.eye(d*d)/d**2
    j_different = bell(d)/d**2
    for i, row in enumerate(labels):
        for j, col in enumerate(labels):
            block = np.ones((1, 1))
            for x, y in zip(row, col):
                block = np.kron(block, j_same if x == y else visibility*j_different)
            uniform[i*payload:(i+1)*payload, j*payload:(j+1)*payload] = block/count
            actual[i*ancilla*payload:(i+1)*ancilla*payload,
                   j*ancilla*payload:(j+1)*ancilla*payload] = np.kron(np.outer(a[i], a[j].conj()), block)
    simulated = np.zeros_like(actual)
    completeness = np.zeros((count, count), dtype=complex)
    for shift in labels:
        k = np.zeros((count*ancilla, count), dtype=complex)
        for i, row in enumerate(labels):
            source = position[tuple((x-s) % n for x, s in zip(row, shift))]
            k[i*ancilla:(i+1)*ancilla, source] = a[i]
        completeness += k.conj().T@k
        big = np.kron(k, np.eye(payload))
        simulated += big@uniform@big.conj().T
    error = float(np.linalg.norm(simulated-actual))
    tp_error = float(np.linalg.norm(completeness-np.eye(count)))
    require(error < TOL and tp_error < TOL, 'Correlated-controller simulation failed')
    return {'orders_per_device': n, 'devices': m, 'dimension': d,
            'ancilla_dimension': ancilla, 'visibility': visibility,
            'choi_simulation_error': error, 'trace_preserving_error': tp_error}


def finite_examples():
    rows = []
    for n in [1, 2, 9, 10, 100, 1000, 1000000]:
        d, v = 2, 0.8
        denominator = d*d+v*(n-1)
        p = denominator/(n*d*d)
        entanglement_fidelity = (1+v*(n-1))/denominator
        pure_fidelity = (d+v*(n-1))/denominator
        phi = bell(d)
        j0 = (v+(1-v)/n)*phi/d**2+(np.eye(d*d)-phi)/(n*d**2)
        j1 = (n-1)*(np.eye(d*d)-v*phi)/(n*d**2)
        limit0 = v*phi/d**2
        limit1 = (np.eye(d*d)-v*phi)/d**2
        mixture0 = (1-1/n)*limit0+np.eye(d*d)/(n*d*d)
        mixture1 = (1-1/n)*limit1
        require(np.linalg.norm(j0-mixture0)+np.linalg.norm(j1-mixture1) < TOL, 'Affine noise identity failed')
        require(abs(np.trace(j0)-p) < TOL, 'Success probability mismatch')
        require(abs(np.trace(phi@j0)/p-entanglement_fidelity) < TOL, 'Fidelity mismatch')
        require(abs(d*j0[0, 0]/p-pure_fidelity) < TOL, 'Pure-state fidelity mismatch')
        require(abs(np.trace(j0+j1)-1) < TOL, 'Finite-channel normalization mismatch')
        rows.append({'orders': n, 'success_probability': p,
                     'entanglement_fidelity': entanglement_fidelity,
                     'pure_state_fidelity': pure_fidelity})
    require(abs(rows[-2]['success_probability']-0.2008) < TOL, 'Example probability changed')
    require(abs(rows[-2]['entanglement_fidelity']-4001/4016) < TOL, 'Example fidelity changed')
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional JSON report destination')
    args = parser.parse_args()
    report = {
        'status': 'pass', 'scope': 'Finite identities and certificates; analytical proofs remain authoritative.',
        'numpy_version': np.__version__, 'tolerance': TOL,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'ideal_certificates': [ideal_certificate(d) for d in range(2, 7)],
        'noisy_certificates': [noisy_certificate(d, f) for d in range(2, 6) for f in [0, 0.5, 1]],
        'raw_kraus_checks': [raw_cyclic_choi(d, n) for d, n in [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 2), (3, 3)]],
        'controller_checks': [correlated_controller(visibility=v) for v in [0, 0.8, 1]],
        'qubit_noisy_examples': finite_examples(),
    }
    text = json.dumps(report, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text)


if __name__ == '__main__':
    main()
