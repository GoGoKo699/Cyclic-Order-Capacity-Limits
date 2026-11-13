# Reproducing the finite checks

The analytical proofs in [science/](../README.md#reading-route) establish the dimension-independent claims. The script here checks explicit finite certificates and independently reconstructs selected channel instances from their physical Kraus operators.

From the repository root, with Python 3.10 or later:

```bash
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 python verification/verify_results.py --output verification/results.json
```

`OPENBLAS_NUM_THREADS=1` keeps these small matrix calculations predictable; it is not a mathematical requirement. The script uses NumPy, no optimization solver, external data or network service. It exits with an error if a tested assertion fails. Its checks remain active under Python's optimization flag.

## What is tested

| Check | Finite scope | Purpose |
| --- | --- | --- |
| Physical Kraus enumeration | Qubits with 1–5 cyclic orders; qutrits with 2–3 orders | Reconstruct the normalized Choi state from independent matrix-unit Kraus operators and compare with the closed cyclic formula. |
| Ideal extension | Dimensions 2–6 | Check positivity, trace, both flag marginals, Bell compression norm, symmetric overlap bound and violation at the next integer beyond the threshold. |
| Noisy limiting extension | Dimensions 2–5; zero, half-ceiling and ceiling visibility | Check explicit positive extension blocks and their marginals, and the required negative residual Bell weight above the ceiling. |
| Correlated controllers | Two three-order qubit devices with a two-dimensional preparation ancilla; visibility 0, 0.8 and 1 | Check the receiver simulation on the normalized Choi input, including trace preservation, for a fixed reproducible correlated preparation. |
| Finite noisy examples | Seven order counts from 1 to 1,000,000 | Check the exact affine decomposition, normalization, success probability and both fidelity conventions. |

The raw Kraus calculation is independent of the simplified channel formula. The controller calculation tests the entire finite map via a Choi input rather than one selected target state. Its preparation is generated with a fixed pseudorandom seed; the analytical controller theorem covers all valid preparations.

## Saved result and limitations

[results.json](results.json) records the output, numerical tolerance, NumPy version and SHA256 of the exact verification script. The saved run passed all listed assertions with NumPy 2.3.5 and tolerance $`2\times10^{-11}`$. Small negative eigenvalues at floating-point roundoff are interpreted using that tolerance.

The calculations do not infer an arbitrary-dimension theorem from a finite sample, estimate quantum or private capacities above the antidegradability boundary, optimize arbitrary permutations, or validate a hardware noise model. The proof files give those boundaries explicitly.

The shared-kernel construction used in the numerical noisy certificate and the separable extension described in the analytical noise proof are two valid extensions of the same residual marginal. A symmetric extension need not be unique.

## Regenerate the explanatory figure

The figure evaluates exact formulas at integer order counts; it does not fit or sample experimental data. Regenerate it with:

```bash
python -m pip install -r requirements-figures.txt
python verification/plot_example.py
```

The saved [SVG](../figures/qubit_dephasing.svg) was generated with Matplotlib 3.10.8. Figure generation is optional and is not needed to run the matrix checks.
