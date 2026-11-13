# Unobserved control dephasing

For the cyclic-order architecture, a specified amount of unobserved noise on the order register prevents antidegradability from disappearing as the number of orders increases. This remains true when the sender uses arbitrary entangled target inputs and the controller preparation contains correlations between devices and with retained receiver ancillas.

Let $`d\geq2`$ be the target dimension and $`0\leq v\leq1`$. The result is

```math
\boxed{\quad
\mathcal N_{\infty,v}\text{ is antidegradable}
\quad\Longleftrightarrow\quad
v\leq\frac{d^2}{d^2+1}.
\quad}
```

Here $`\mathcal N_{\infty,v}`$ is the limit of the uniformly controlled channels after their exact compression to two output flags. Every finite-order channel is antidegradable throughout this range of $`v`$. For qubits at $`v=4/5`$, the successful branch approaches the identity with probability approaching $`1/5`$, while the complete channel has zero unassisted quantum and standard private classical capacities at every finite $`N`$.

## 1. Physical channel and noise placement

Each device uses $`N`$ independent completely depolarizing channels on a $`d`$-dimensional target, with the target traversing every channel in one of the $`N`$ cyclic orders. The order register $`C`$ has basis $`\{|j\rangle:0\leq j\lt N\}`$. There is no target-carrying bypass, and the controller is prepared independently of the entire encoded target and reference.

Write

```math
\tau_d=\frac{I_d}{d},\qquad
\mathcal T(X)=\mathrm{Tr}(X)\tau_d,\qquad
\Delta_C(Y)=\sum_{j=0}^{N-1}|j\rangle\langle j|Y|j\rangle\langle j|.
```

The specified noise is the physical channel

```math
\mathcal D_v=v\,\mathrm{id}_C+(1-v)\Delta_C.
\qquad\text{(1)}
```

It acts on $`C`$ after preparation and immediately before the controlled traversal, and as the identity on any preparation ancilla $`A`$. Its environment or random phase label is unavailable to the receiver. No recovery, re-preparation, or controller-target operation is inserted between this noise and the traversal. The receiver may process all delivered target, controller, and retained ancilla registers arbitrarily afterward.

This placement can equivalently be moved to the output of the controlled traversal, before receiver processing. Indeed, each controlled Kraus operator is block diagonal in the order basis. It commutes with every diagonal phase unitary $`Z^\ell`$, where $`Z|j\rangle=e^{2\pi i j/N}|j\rangle`$, and

```math
\Delta_C(Y)=\frac1N\sum_{\ell=0}^{N-1}Z^\ell YZ^{-\ell}.
```

Consequently the traversal intertwines $`\mathcal D_v`$ at input and output, including when $`C`$ is entangled with $`A`$. This assertion uses the specified controlled device; it does not cover an intervening operation that changes the control basis or corrects the noise.

The cyclic-order calculation of [Chiribella, Wilson, and Chau](https://arxiv.org/abs/2005.00618v5) gives, for target and controller operators $`X,Y`$,

```math
\mathcal S_{N,v}(X\otimes Y)
=\mathcal T(X)\otimes\Delta_C(Y)
+\frac{v}{d^2}X\otimes\bigl[Y-\Delta_C(Y)\bigr].
\qquad\text{(2)}
```

The formula is an equality of linear maps and extends to arbitrary ancillas by the identity map. The diagonal order blocks give $`\mathcal T`$ and every off-diagonal cyclic-order block gives $`\mathrm{id}/d^2`$ before the factor $`v`$ from (1).

The number $`v`$ therefore describes a channel on the order register, rather than just the visibility of its reduced state. For example, a known random phase $`Z^\ell|+\rangle`$, with $`\ell`$ retained in an accessible register, can have the completely mixed reduced control state. The receiver can nevertheless undo $`Z^\ell`$ after traversal and recover ideal uniform-control performance. That preparation has low reduced visibility but has not suffered inaccessible physical noise of the form (1). Likewise, a global channel (1) is not a general description of independent phase errors on a multi-qubit implementation of $`C`$.

## 2. Exact binary-flag channel

Prepare $`|+\rangle=N^{-1/2}\sum_j|j\rangle`$ and write $`P_+=|+\rangle\langle+|`$. For $`N>1`$, (2) is exactly

```math
\mathcal S_{N,v}(X\otimes P_+)
=\mathcal A^{N,v}_0(X)\otimes P_+
+\mathcal A^{N,v}_1(X)\otimes\frac{I_C-P_+}{N-1},
\qquad\text{(3)}
```

where the completely positive, trace-nonincreasing branches are

```math
\begin{aligned}
\mathcal A^{N,v}_0(X)
&=\frac1N\mathcal T(X)+\frac{v(N-1)}{Nd^2}X,\\
\mathcal A^{N,v}_1(X)
&=\frac{N-1}{N}\mathcal T(X)-\frac{v(N-1)}{Nd^2}X.
\end{aligned}
\qquad\text{(4)}
```

The two control states in (3) have orthogonal supports. Measuring these supports yields a classical flag $`F\in\{0,1\}`$; conversely, preparing the corresponding control state from that flag reconstructs (3). Both conversions are receiver channels. Thus compression loses no information, including information accessible by joint measurements on target and controller.

Use the fixed output space $`B\otimes F`$, with $`\dim B=d`$, and define

```math
\mathcal N_{N,v}(X)=
\mathcal A^{N,v}_0(X)\otimes|0\rangle\langle0|
+\mathcal A^{N,v}_1(X)\otimes|1\rangle\langle1|.
\qquad\text{(5)}
```

For the normalized Choi convention

```math
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{j=1}^d|j,j\rangle,\qquad
\Phi_d=|\Phi_d\rangle\langle\Phi_d|,
```

the two reference-target blocks of $`J_{N,v}=(\mathrm{id}_R\otimes\mathcal N_{N,v})(\Phi_d)`$ are

```math
J^{N,v}_0=\frac{I_{RB}+v(N-1)\Phi_d}{Nd^2},\qquad
J^{N,v}_1=\frac{N-1}{Nd^2}(I_{RB}-v\Phi_d).
\qquad\text{(6)}
```

Their positivity for $`0\leq v\leq1`$ verifies complete positivity of (4), including its negative coefficient in the second line. Their sum is $`I_{RB}/d^2`$, so the target marginal alone is completely depolarizing.

At $`N=1`$ the channel is simply $`\mathcal T`$ with flag $`0`$. Formulae (4)--(6) remain valid; the absent bad control sector in (3) need not be defined.

## 3. Fixed-dimensional limit and affine identity

Define the channel

```math
\mathcal N_{\infty,v}(X)
=\frac{v}{d^2}X\otimes|0\rangle\langle0|
+\left[\mathcal T(X)-\frac{v}{d^2}X\right]\otimes|1\rangle\langle1|.
\qquad\text{(7)}
```

Its Choi blocks are

```math
J^{\infty,v}_0=\frac v{d^2}\Phi_d,\qquad
J^{\infty,v}_1=\frac1{d^2}(I_{RB}-v\Phi_d).
\qquad\text{(8)}
```

Let $`\mathcal T_0(X)=\mathcal T(X)\otimes|0\rangle\langle0|`$. Direct substitution gives the channel identity

```math
\boxed{\quad
\mathcal N_{N,v}
=\left(1-\frac1N\right)\mathcal N_{\infty,v}
+\frac1N\mathcal T_0.
\quad}
\qquad\text{(9)}
```

In particular,

```math
\Vert \mathcal N_{N,v}-\mathcal N_{\infty,v}\Vert _\diamond\leq\frac2N.
\qquad\text{(10)}
```

This is convergence on the common $`2d`$-dimensional output space in (5). It does not assume an infinite-dimensional physical controller, an actual device with infinitely many uses, or an interchange of capacity limits. Exact compression is what makes the limiting channel well defined.

## 4. Exact antidegradability of the limit

A channel is antidegradable if its receiver output can be generated from a complementary environment output by a channel. Equivalently, it has a joint channel to two receivers with the original channel at both marginals; equivalently, its Choi state has a symmetric extension on its output. These standard equivalences are reviewed by [Heinosaari and Miyadera, Section 4.3](https://arxiv.org/abs/1608.01794).

For the forward implication, apply an antidegrading map to the environment of a Stinespring dilation while keeping its original receiver output. The two resulting receiver marginals are the same channel, and averaging over exchange makes the extension symmetric. The reverse implication follows from a dilation of the joint channel, as explained in Section 7 below.

Set

```math
q=\frac v{d^2}.
```

We prove that (8) admits such an extension exactly when $`v\leq d^2/(d^2+1)`$.

### Necessity: a pure successful marginal fixes the cross sectors

Suppose $`\Omega_{R B_1F_1 B_2F_2}`$ is an extension with both one-receiver marginals equal to (8). Dephase $`F_1,F_2`$, average over receiver exchange, and average over

```math
\overline U_R\otimes U_{B_1}\otimes U_{B_2}
```

with the same Haar-distributed $`U`$. These operations preserve positivity, exchange symmetry, and the required isotropic marginals. Let $`\Omega_{fg}`$ denote the resulting subnormalized operator on $`RB_1B_2`$ in flags $`(f,g)`$.

The first receiver's good marginal is

```math
\mathrm{Tr}_{B_2}(\Omega_{00}+\Omega_{01})=q\Phi_{RB_1}.
\qquad\text{(11)}
```

A positive operator with a rank-one marginal factorizes across that marginal: if $`\mathrm{Tr}_Z X=c|\phi\rangle\langle\phi|`$, then $`X=|\phi\rangle\langle\phi|\otimes M_Z`$ for a positive $`M_Z`$ of trace $`c`$. Positivity removes every joint vector outside the rank-one marginal support.

There is no nonzero $`\Omega_{00}`$. Indeed, the first good marginal would force $`\Omega_{00}=\Phi_{RB_1}\otimes M_{B_2}`$. Its $`RB_2`$ marginal is $`I_R/d\otimes M_{B_2}`$. If nonzero, this has rank at least $`d`$, whereas it must be supported inside the rank-one projector $`\Phi_{RB_2}`$ required by the other good marginal. Since $`d\geq2`$, this is impossible.

It follows from (11) that $`\Omega_{01}=\Phi_{RB_1}\otimes M_{B_2}`$ with $`\mathrm{Tr}M=q`$. The covariance average makes $`M=qI_{B_2}/d`$. Exchange symmetry fixes the other cross sector:

```math
\Omega_{01}=q\Phi_{RB_1}\otimes\frac{I_{B_2}}d,\qquad
\Omega_{10}=q\Phi_{RB_2}\otimes\frac{I_{B_1}}d.
\qquad\text{(12)}
```

The contribution of $`\Omega_{10}`$ to the first receiver's bad marginal is $`qI_{RB_1}/d^2`$. The remaining both-bad sector must therefore have marginal

```math
\begin{aligned}
R_v
&=J^{\infty,v}_1-\frac q{d^2}I_{RB}\\
&=\frac{d^2-v}{d^4}I_{RB}-\frac v{d^2}\Phi_d.
\end{aligned}
\qquad\text{(13)}
```

This operator must be positive. Its eigenvalue in the maximally entangled direction is

```math
r_\Phi=\frac{d^2-v(d^2+1)}{d^4},
\qquad\text{(14)}
```

and every orthogonal eigenvalue is $`(d^2-v)/d^4>0`$. Thus positivity forces

```math
v\leq\frac{d^2}{d^2+1}.
\qquad\text{(15)}
```

At $`v=0`$, the good marginal and both cross sectors vanish, and the same argument is understood with $`q=0`$.

### Sufficiency: the residual is separable and can be shared

Assume (15). The residual (13) is not only positive but separable. An explicit decomposition is

```math
R_v=\alpha_v\frac{I_{RB}}{d^2}
+\beta_v\frac{I_{RB}-\Phi_d}{d^2-1},
\qquad\text{(16)}
```

where

```math
\alpha_v=\frac{d^2-v(d^2+1)}{d^2}\geq0,\qquad
\beta_v=\frac{v(d^2-1)}{d^2}\geq0.
\qquad\text{(17)}
```

The weights sum to $`1-2v/d^2=\mathrm{Tr}R_v`$. The first state in (16) is a product state. For the second, choose two distinct computational basis vectors $`e_0,e_1\in\mathbb C^d`$ and use the identity

```math
\frac{I_{RB}-\Phi_d}{d^2-1}
=\int
|\overline Ue_0\rangle\langle\overline Ue_0|_R
\otimes|Ue_1\rangle\langle Ue_1|_B\,dU.
\qquad\text{(18)}
```

The integrand is product. The average is isotropic, has trace one, and has zero overlap with $`\Phi_d`$, which uniquely identifies the left side. This supplies separability directly, including the boundary $`r_\Phi=0`$.

For any separable representation $`R_v=\sum_x r_x a_x\otimes b_x`$, with $`a_x,b_x`$ normalized states and $`r_x\geq0`$, set

```math
\Omega_{11}=\sum_x r_x\,a_x\otimes b_x\otimes b_x.
\qquad\text{(19)}
```

An integral representation is equally valid. This is a positive symmetric extension of $`R_v`$. Combining (19) with (12) and $`\Omega_{00}=0`$ gives an extension of (8): its trace is $`2q+(1-2q)=1`$, its reference marginal is $`I_R/d`$, and both flagged receiver marginals are exactly (8). This proves sufficiency and the boxed equivalence.

The construction extends the entanglement-breaking residual map; it does not broadcast the unknown quantum target in a successful branch. Only one receiver can occupy that branch in the extension.

## 5. Every finite number of orders below the same visibility

The channel $`\mathcal T_0`$ is entanglement breaking and has a two-receiver extension that prepares $`\tau_d`$ and flag $`0`$ at both outputs. Antidegradable channels form a convex set: mix their two-receiver extensions with the same mixing probabilities. Equation (9) therefore proves

```math
0\leq v\leq\frac{d^2}{d^2+1}
\quad\Longrightarrow\quad
\mathcal N_{N,v}\text{ is antidegradable for every finite }N.
\qquad\text{(20)}
```

The exact finite-$`N`$ boundary at general $`v`$ is not needed for (20). Above (15), the limiting channel is non-antidegradable. Since symmetric-extension feasibility is closed in this fixed finite-dimensional space, (10) also implies that sufficiently large finite $`N`$ are then non-antidegradable. This is only a statement about antidegradability, not a positive-capacity conclusion.

## 6. Arbitrary controllers, ancillas, and correlated preparations

For $`N>1`$, define the channel on the order register

```math
\mathcal L=\frac{N\Delta_C-\mathrm{id}_C}{N-1},
\qquad
\mathcal L_0=\mathrm{id}_C,\quad\mathcal L_1=\mathcal L.
\qquad\text{(21)}
```

It is completely positive and trace preserving. It is the Schur multiplier with diagonal entries $`1`$ and off-diagonal entries $`-1/(N-1)`$, whose multiplier matrix is

```math
M=\frac{N}{N-1}I_N-\frac1{N-1}\mathbf1\mathbf1^\dagger.
```

The eigenvalues of $`M`$ are $`0`$ on the uniform vector and $`N/(N-1)`$ on its orthogonal complement. Thus the Schur map is completely positive, and the unit diagonal ensures trace preservation. This also proves positivity when $`\mathcal L`$ acts on one part of an entangled controller preparation.

The two channels in (21) commute with $`\Delta_C`$ and $`\mathcal D_v`$. Substituting (4) and (21) gives the exact superoperator identity

```math
\mathcal S_{N,v}
=\mathcal A^{N,v}_0\otimes\mathcal L_0
+\mathcal A^{N,v}_1\otimes\mathcal L_1.
\qquad\text{(22)}
```

For example, the coefficient of $`\mathcal T(X)`$ is
$`(Y+(N-1)\mathcal L(Y))/N=\Delta_C(Y)`$, and the coefficient of $`vX/d^2`$ is $`Y-\Delta_C(Y)`$, as in (2). Hence the controller simulation uses the same map for all $`v`$ and is compatible with the physical placement of the dephasing.

For one arbitrary input-independent state $`\omega_{CA}`$, prepare $`\omega`$ after observing flag $`0`$, or prepare $`(\mathcal L\otimes\mathrm{id}_A)(\omega)`$ after observing flag $`1`$. Keep the received target unchanged. This is a receiver channel $`\mathcal R_\omega`$ and satisfies

```math
\mathcal S_{N,v}(\,\cdot\,\otimes\omega)
=\mathcal R_\omega\circ\mathcal N_{N,v}.
\qquad\text{(23)}
```

The statement includes mixed preparations and arbitrary finite ancillas without assuming that $`\omega_C`$ is pure or uncorrelated with $`A`$.

More generally, consider $`m`$ distinct devices with independent physical channels and independent noise (1), and a fixed joint preparation $`\omega_{C_1\cdots C_mA}`$. This state may have arbitrary entanglement or classical correlations between controls and with $`A`$, but factors from the complete encoded target-reference state. Tensorizing (22) yields, for any target input $`\rho_{T_1\cdots T_m}`$,

```math
\sum_{\mathbf f\in\{0,1\}^m}
\left(\bigotimes_{i=1}^m\mathcal A^{N,v}_{f_i}\right)(\rho)
\otimes
\left(\bigotimes_{i=1}^m\mathcal L_{f_i}\otimes\mathrm{id}_A\right)(\omega).
\qquad\text{(24)}
```

Each controller state in (24) is normalized and positive. Therefore (24) is obtained by applying $`\mathcal N_{N,v}^{\otimes m}`$ to the targets, reading its classical flag string, and preparing the corresponding joint state of all controllers and $`A`$. This is one receiver postprocessing map. Equality holds also with an untouched target reference, so it covers entangled payloads.

Consequently, in the range (20), every such block channel is antidegradable. Tensor products preserve the two-receiver extension, and receiver postprocessing preserves it by applying the same postprocessing separately at each receiver.

The correlation statement concerns preparations. It does not assume correlated dephasing environments, controller adaptation between uses, or operations that correlate the controllers with the encoded payload before traversal. Product physical noise and fresh independent depolarizing-channel environments are part of (24). A controller or ancilla used to encode the message, preshared entanglement used for communication, and sender-receiver feedback define different communication resources. For $`N=1`$, the same conclusion holds trivially because the target is completely depolarized and the independent controller state carries no input information.

## 7. Environment simulation and the capacity consequence

A two-receiver extension gives antidegradability by Stinespring dilation: dilate the extension, regard receiver $`2`$ and the remaining dilation system as an environment for receiver $`1`$, and recover receiver $`2`$ by discarding that remaining system. Equivalence of Stinespring dilations then gives an antidegrading map for a complementary channel of the original device.

The postprocessing in (23) or (24) does not invalidate this implication. If $`\mathcal N=\mathcal A\circ\mathcal N^c`$ and $`\mathcal M=\Lambda\circ\mathcal N`$, a dilation of $`\mathcal M`$ has the old environment $`E`$ and the extra environment of $`\Lambda`$. Discarding the latter, applying $`\mathcal A`$, and then applying $`\Lambda`$ simulates $`\mathcal M`$. Thus the complete environment can simulate the receiver even after arbitrary decoding.

For independent channel uses, antidegradability is preserved under tensor powers and input encoding. It rules out asymptotically faithful unassisted quantum transmission by the usual no-cloning argument. It also rules out private classical transmission: for every encoded classical label $`X`$, the environmental simulation gives

```math
I(X;B)\leq I(X;E).
\qquad\text{(25)}
```

This applies to every blocklength and every input ensemble. Equivalently, any decoder that reliably recovers a private message at the receiver can be run after the environment's simulation with the same output statistics. Receiver reliability and secrecy from that environment cannot both tend to one.

Here the private classical capacity $`P`$ has its standard channel meaning: Eve holds the complete complementary environment, including any noise or preparation purifications. The dephasing environment is unavailable to the legitimate receiver. A wiretap model in which some environmental registers are trusted and inaccessible to Eve is a different model, to which (25) need not apply.

Accordingly, throughout (20),

```math
Q(\mathcal N_{N,v})=P(\mathcal N_{N,v})=0.
\qquad\text{(26)}
```

The same zero-rate conclusion holds for the allowed correlated-controller blocks in (24), even if the independent controller preparation is chosen separately for each blocklength. Heralding and two-way assisted protocols are not excluded by (26). In particular, [Chiribella, Wilson, and Chau, Appendices D--F](https://arxiv.org/html/2005.00618v5) explicitly analyze heralded and two-way assisted transmission; the present unassisted converse is consistent with those results.

## 8. High accepted fidelity at nonvanishing success probability

For any normalized target state, the good flag has probability

```math
p_{N,v}=\frac{d^2+v(N-1)}{Nd^2}.
\qquad\text{(27)}
```

Its normalized channel is depolarizing:

```math
\mathcal E^{N,v}_0(\rho)
=\lambda_{N,v}\rho+(1-\lambda_{N,v})\tau_d,
\qquad
\lambda_{N,v}=\frac{v(N-1)}{d^2+v(N-1)}.
\qquad\text{(28)}
```

For every pure input, its accepted output fidelity is the same:

```math
F_{\mathrm{pure}}(N,v)
=\frac{v(N-1)+d}{v(N-1)+d^2}.
\qquad\text{(29)}
```

The accepted entanglement fidelity, using one half of $`\Phi_d`$, is instead

```math
F_e(N,v)
=\frac{v(N-1)+1}{v(N-1)+d^2}.
\qquad\text{(30)}
```

At fixed $`v>0`$ and fixed $`d`$, both fidelities tend to one and $`p_{N,v}\to v/d^2`$. At $`v=0`$, the good branch remains completely depolarizing and its probability is $`1/N`$; the high-fidelity statement does not include this endpoint.

For $`d=2`$, $`v=4/5`$, and $`N=1000`$, the exact values are:

| Quantity | Exact value | Decimal value |
|---|---:|---:|
| Good-flag probability | $`251/1250`$ | $`0.2008`$ |
| Depolarizing coefficient $`\lambda`$ | $`999/1004`$ | $`0.9950199203`$ |
| Accepted pure-state fidelity | $`2003/2008`$ | $`0.9975099602`$ |
| Accepted entanglement fidelity | $`4001/4016`$ | $`0.9962649402`$ |

This value of $`v`$ is exactly the limiting antidegradability boundary for qubits. Every finite-$`N`$ full device in this family has $`Q=P=0`$, while the limit of the accepted fidelity is one and the limiting success probability is $`1/5`$. The noise parameter means a $`1/5`$ mixture with complete order-basis dephasing in (1); it is not a generic $`1/5`$ Pauli-error probability.

## 9. Mathematical inheritance and model comparison

The pure-good-marginal argument has the same structure as the exact shareability theorem in [Quantum-Monitoring-Thresholds, Shareability and universal coding bounds](https://github.com/GoGoKo699/Quantum-Monitoring-Thresholds/blob/3f451dc0b63068a256f193e64f7ea8b83f2c1d6b/science/shareability.md). That theorem studies

```math
\delta\,\mathrm{id}\ \oplus\ p\,\mathcal M,
\qquad
\mathcal M(\rho)=\sum_y\mathrm{Tr}(E_y\rho)|y\rangle\langle y|,
```

and obtains $`k`$-self-compatibility exactly when
$`(k-1)\delta\leq p\sum_y\lambda_{\min}(E_y)`$. Rank-one factorization, exclusion of simultaneous intact outputs, and positivity of the remaining marginal are inherited proof ingredients here. The present bad branch is a quantum channel with noncommuting outputs, so that measurement-channel criterion does not directly apply. Equations (16)--(19) establish the additional separability needed to share this quantum residual.

The direct-sum identity-plus-noise architecture belongs to the established incomplete-erasure framework of [Siddhu and Griffiths, Equation (35)](https://arxiv.org/html/2003.00583v2). Flagged channel extensions and their relation to depolarizing-channel capacity are also established tools; see [Fanizza, Kianvash, and Giovannetti](https://arxiv.org/abs/1911.01977). Their displayed flagged identity/completely-depolarizing convex mixture is not a direct parameterization of (7): the bad branch of (7) has a negative coefficient of the input state.

Isotropic covariance, extension geometry, and their relation to cloning are established by [Johnson and Viola](https://arxiv.org/abs/1305.1342) and [Nechita, Pellegrini, and Rochette](https://arxiv.org/abs/2106.09655). No new general monogamy or isotropic-separability inequality is claimed. The result here evaluates the exact limiting antidegradability condition for the noisy cyclic-order channel and propagates it, through an affine identity and a commuting controller simulation, to the finite-device communication model.
