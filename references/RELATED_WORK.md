# Related work and attribution

This project classifies antidegradability of the complete receiver output of the cyclic-order switch of independent, identical completely depolarizing channels. The receiver retains the target and the order register. The sender encodes only in the target, and ordinary unassisted quantum and private capacities refer to arbitrary codes over independent uses of this effective channel. Each effective use consumes all $N$ supplied channel slots.

## The cyclic channel and its heralded communication advantage

[Chiribella, Wilson and Chau (2021)](https://doi.org/10.1103/PhysRevLett.127.190502), especially Eqs. (5)–(9) and Appendices D–F of [arXiv:2005.00618v5](https://arxiv.org/abs/2005.00618v5), supply the cyclic-order channel, its good and bad branches, and the heralded high-fidelity transmission mechanism. Those are antecedents of this project.

For uniform control, their effective channel has a good-branch probability

```math
p_0=\frac{N+d^2-1}{Nd^2},\qquad
\mathcal E_0(\rho)=\frac{(N-1)\rho+dI}{N+d^2-1},\qquad
\mathcal E_1(\rho)=\frac{dI-\rho}{d^2-1}.
```

The original paper explicitly distinguishes the selected branch from the complete channel and establishes a positive **two-way-assisted** quantum capacity when $N\ge d+2$. Its argument about positive quantum capacity of $\mathcal E_0$ is used to obtain an assisted communication protocol. The zero **unassisted** capacities established here are compatible with those results.

[Wu et al. (2025)](https://doi.org/10.1103/PhysRevA.111.012605) study communication enhancement from forward and reverse order superpositions for general Pauli channels and related noise families. Their order family and enhancement questions differ from the exact antidegradability classification of the full $N$-cyclic output considered here.

## Antidegradability, broadcasting and familiar heralding distinctions

The equivalence between antidegradability and compatibility of a channel with itself is established channel theory; see [Heinosaari and Miyadera (2017), Section 4.3](https://arxiv.org/abs/1608.01794v2). In the Choi representation it becomes a symmetric-extension problem. Vanishing unassisted quantum and private capacities then follows from the environment's ability to simulate the receiver, including for arbitrary block codes.

Perfect transmission on a heralded branch can coexist with zero unassisted capacity. The quantum erasure channel already exhibits that distinction; see [Bennett, DiVincenzo and Smolin (1997)](https://doi.org/10.1103/PhysRevLett.78.3217). The contribution here is the exact obstruction for this cyclic architecture and its specified controller-noise model, rather than that general distinction.

## Isotropic compatibility and the Bell-projector geometry

[Johnson and Viola (2013)](https://doi.org/10.1103/PhysRevA.88.032323) give necessary and sufficient isotropic joinability conditions. Their Corollary III.4, Eq. (23), determines the two-marginal region. In normalized Bell fractions $F_i=\operatorname{Tr}(\Phi\rho_i)$, its boundary with $F_2=0$ is

```math
0\le F_1\le 1-d^{-2}.
```

Their Theorem III.8 gives the symmetric two-output bound $F\le(1+d^{-1})/2$. These are the two geometric bounds used for the cross-flag and equal-good-flag sectors of this project's proof. The projector identities used to derive them directly are an explicit realization of established cloning and compatibility geometry.

[Nechita, Pellegrini and Rochette (2021)](https://doi.org/10.1007/s11128-021-03258-y), particularly Theorem 6 of [arXiv:2106.09655](https://arxiv.org/abs/2106.09655), characterize the full universal asymmetric-cloning region, including negative depolarizing coefficients. Their parameter $p_i$ in $\rho\mapsto p_i\rho+(1-p_i)I/d$ is related to the normalized Bell fraction by $F_i=[1+(d^2-1)p_i]/d^2$. Negative $p_i$ must not be confused with a negative Bell fraction.

The application here introduces the channel's two output flags into this known marginal geometry. After dephasing both flags in a hypothetical extension, one must distribute positive operators across the $00,01,10,11$ sectors while matching the prescribed branch probabilities. The zero Bell weight of the bad branch constrains the cross sectors. The exact witness and a matching extension then give

```math
\mathcal C_N\text{ is antidegradable}
\quad\Longleftrightarrow\quad
N\le(d^2-1)^2.
```

Thus the result is an exact cyclic-channel application of established isotropic compatibility, with an explicit solution of its flag-allocation problem. It does not establish a new general monogamy inequality. Applying antidegradability separately to the two conditional branches gives only $N\le(d+1)^2$. The complete flagged-channel analysis is stronger for $d>2$; at $d=2$ these two bounds coincide at $N=9$.

## Flagged extensions and capacity bounds

[Fanizza, Kianvash and Giovannetti (2020)](https://doi.org/10.1103/PhysRevLett.125.020503) develop capacity bounds using flags for the identity and completely depolarizing components, allowing overlapping and mixed flag states. Their displayed family has the form

```math
(1-p)\rho\otimes\sigma_0+p(I/d)\otimes\sigma_1.
```

For $N>1$, the cyclic channel is not obtained by assigning parameters to this particular two-component family: its coefficient of $\rho$ on the flag register has positive and negative eigenvalues. This observation concerns the displayed family, not the applicability of general flagged-channel methods.

[Kianvash, Fanizza and Giovannetti (2022)](https://doi.org/10.22331/q-2022-02-09-647) extend those methods. Proposition 3.1 supplies sufficient **degradability** conditions expressed through Kraus products and flag overlaps. Section 4.1 treats a unitary component mixed with an arbitrary channel, and Proposition 5.1 constructs capacity upper bounds from flagged Pauli extensions. These results concern constructing suitable degradable extensions; they do not give a necessary and sufficient antidegradability criterion for the complete cyclic output.

There is nevertheless a direct connection to the flagged Weyl-channel framework. With $W_0=I$ and a full orthogonal Weyl family,

```math
\mathcal C_N(\rho)=\frac{1}{d^2}\rho\otimes|0\rangle\langle0|
+\frac{1}{d^2}\sum_{x\ne0}W_x\rho W_x^\dagger\otimes
\left[\frac1N|0\rangle\langle0|
+\frac{N-1}{N}|1\rangle\langle1|\right].
```

This is a legitimate positive mixture with mixed flags. Consequently, the negative depolarizing coefficient of $\mathcal E_1$ does not place this problem outside general flagged-channel theory. The distinction is the exact self-compatibility calculation and its cyclic-order operational interpretation.

## Controller noise and incomplete erasure

[Molitor et al. (2024)](https://doi.org/10.1038/s42005-024-01843-y) analyze a two-order switch with an open controller, including suppression of interference and changes in postselected outputs. Controller sensitivity is therefore an established subject. The present noise result instead concerns all $N$ cyclic orders under the particular unmonitored dephasing map $\mathcal D_v=v\,\mathrm{id}+(1-v)\Delta$.

The limiting channel has an intact quantum branch and a flagged noisy quantum branch. Such direct-sum structures belong to the generalized and incomplete-erasure framework of [Siddhu and Griffiths (2021), Eq. (35)](https://arxiv.org/html/2003.00583v2). Their analyzed amplitude-damping and dephasing examples do not supply the cyclic isotropic threshold.

Here the limiting channel is antidegradable exactly when $v\le d^2/(d^2+1)$; convexity transfers this obstruction to every finite $N$. The conclusion assumes that the dephasing environment or random phase label is unavailable. A reduced-controller visibility alone is insufficient when a receiver has side information that can undo the phase randomization.

## The 2025 preprint and 2026 cyclic-order experiment

[Wang et al. (2026)](https://doi.org/10.1038/s42005-026-02698-1), preceded by [arXiv:2510.07127 (2025)](https://arxiv.org/abs/2510.07127), implement four cyclic orders of completely depolarizing qubit channels on a silicon photonic chip. Their selected controller outcome gives a reported state fidelity $0.712\pm0.013$, above $2/3$. This is evidence about the heralded output. It does not determine the unassisted capacity of the complete flagged channel.

The ideal $N=4,d=2$ model lies in the antidegradable regime, a fact already implied by the simpler branchwise bound. The exact higher-dimensional classification and the all-$N$ noise obstruction are the additional mathematical conclusions here. They do not invalidate the measured conditional fidelity or the assisted communication interpretation.

## Related research notes

The following public research records address adjacent questions. Links identify fixed scientific versions so the attribution is reproducible.

| Research record | Shared ingredient and distinct result |
|---|---|
| [Quantum-Monitoring-Thresholds, shareability theorem](https://github.com/GoGoKo699/Quantum-Monitoring-Thresholds/blob/3f451dc0b63068a256f193e64f7ea8b83f2c1d6b/science/shareability.md) | Its channel has an intact quantum branch and a classical measurement record. Its exact shareability proof already uses rank-one good-marginal factorization, exclusion of two simultaneous good flags, and positivity of the remaining branch. Those are inherited ingredients of the present visibility-limit proof. Here the failure output is quantum; sufficiency also requires extending the residual isotropic state. The finite-$N$ ideal good branch is mixed and requires the Bell-compatibility analysis above. |
| [Quantum-Order-Distillation, query characterization](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/2f00d79bafb4d8bc0481678bf503b19605a7ecc1/science/query_threshold.md) | It characterizes exact heralded identity transmission for full-Choi-rank channels using central polynomials and general permutation superpositions. It shares the independent-slot, order-only architecture. A positive successful branch is a different output guarantee from the unassisted capacity of the complete channel, and its larger order family is outside this project's cyclic restriction. |
| [Quantum-Order-Entanglement, order-support criterion](https://github.com/GoGoKo699/Quantum-Order-Entanglement/blob/c00e4394e916c0936b18e6300f9db78cc03f0631/science/order_criterion.md) | It characterizes order families that preserve controller–target separability for every identical channel through the commutativity of relative permutations. Cyclic families are covered by that separability result. Capacity and antidegradability here concern the reference versus the complete receiver output, a different bipartition. |
| [Correlated-Erasure-Capacity, flagged subset model](https://github.com/GoGoKo699/Correlated-Erasure-Capacity/blob/24ea84adea0f0b6455a17914fbd26a6169d557fe/science/model.md) | It bounds unassisted capacity using overlap couplings of retained tensor-factor sets and entropy inequalities. The common feature is a complete, input-independent output flag with unrestricted coding. The present bad branch is a quantum map, not a literal erased subset, so that overlap converse does not calculate the cyclic boundary. |

## Scope of the conclusions

The ideal threshold is an antidegradability boundary, not a positive-capacity threshold. Failure of antidegradability above it does not prove $Q>0$ or $P>0$. The visibility result does not classify the full finite-$N$ noisy boundary. The controller comparison concerns input-independent preparation and the stipulated noise placement. Arbitrary permutation families, target interleavings, correlated channel slots, a controller carrying the sender's message, an accessible noise record, and a quantum system bypassing the channels require separate models.

Complete bibliographic entries are in [REFERENCES.bib](REFERENCES.bib).
