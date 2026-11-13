# Exact antidegradability boundary for ideal cyclic control

For $`N`$ independent completely depolarizing channels of dimension $`d`$, superposed in their $`N`$ cyclic orders with uniform coherent control, the complete effective channel is antidegradable exactly when

```math
\boxed{N\le(d^2-1)^2.}
\qquad\text{(1)}
```

The complete output retains both the target and controller. This statement concerns the full communication channel, including unsuccessful outcomes, and is distinct from the fidelity or capacity of a postselected branch. The proof below gives an explicit symmetric Choi extension throughout the allowed region and a matching obstruction outside it.

The underlying cyclic channel and its flag decomposition are due to Chiribella, Wilson, and Chau [1]. Antidegradability through symmetric Choi extension is standard [2]. The Bell-projector geometry used here is a special case of isotropic-state compatibility and asymmetric cloning [3,4]; the calculation is included to make the flagged-channel boundary self-contained.

## 1. Channel and theorem

Let $`d\ge2`$, $`N\ge1`$, and let

```math
\Phi=|\phi_d\rangle\langle\phi_d|,
\qquad
|\phi_d\rangle=\frac1{\sqrt d}\sum_{x=0}^{d-1}|x\rangle_R|x\rangle_B.
\qquad\text{(2)}
```

Use normalized Choi operators, with trace one. The uniform cyclic channel is equivalent, by channels at the receiver in both directions, to the binary flagged channel $`\mathcal C_{N,d}`$ with Choi operator

```math
\begin{aligned}
J_{N,d}
&=|0\rangle\langle0|_F\otimes\sigma_0
 +|1\rangle\langle1|_F\otimes\sigma_1,\\
\sigma_0
&=\frac{\Phi}{d^2}+\frac{I_{RB}-\Phi}{Nd^2},\\
\sigma_1
&=\frac{N-1}{Nd^2}(I_{RB}-\Phi).
\end{aligned}
\qquad\text{(3)}
```

The label $`0`$ denotes the good branch. Its probability and unnormalized Bell weight are

```math
p_0=\mathrm{Tr}\sigma_0=\frac{N+d^2-1}{Nd^2},
\qquad
\mathrm{Tr}(\Phi\sigma_0)=\frac1{d^2}.
\qquad\text{(4)}
```

The bad branch obeys $`\mathrm{Tr}(\Phi\sigma_1)=0`$. The physical channel, compression maps, preparation assumptions, and $`N`$-slot cost are derived in [channel_model.md](channel_model.md).

**Theorem 1.** The uniform-control channel $`\mathcal C_{N,d}`$ is antidegradable if and only if (1) holds. In this region its unassisted quantum capacity $`Q`$ and private classical capacity $`P`$ are zero.

Every fixed controller preparation independent of the target input, including an arbitrary retained preparation ancilla, is a receiver postprocessing of uniform control. The same zero-capacity conclusion therefore holds for all such preparations. It also holds for correlated preparations across blocks of disjoint cyclic devices as specified in Proposition 2 of the channel model.

The “if and only if” classifies antidegradability of the uniform-control channel. It does not assert positive capacity above (1), and it does not assert that every other controller becomes non-antidegradable there.

## 2. Why a symmetric Choi extension is the right criterion

A channel $`\mathcal N:T\to O`$ is antidegradable if there is a channel $`\mathcal A:E\to O`$ such that $`\mathcal N=\mathcal A\circ\mathcal N^c`$, where $`\mathcal N^c`$ is a complementary channel. The property is independent of the chosen Stinespring dilation.

The equivalent Choi criterion [2] is the existence of a density operator $`W_{RO_1O_2}`$ satisfying

```math
\mathrm{Tr}_{O_2}W=J(\mathcal N),
\qquad
\mathsf S_{12}W\mathsf S_{12}=W,
\qquad\text{(5)}
```

where $`O_1,O_2`$ are copies of the complete output and $`\mathsf S_{12}`$ swaps them. Swap invariance is sufficient; support entirely in the symmetric subspace is not required.

For completeness, suppose first that $`\mathcal N`$ is antidegradable. Apply its Stinespring isometry, then apply $`\mathcal A`$ to the environment. This gives a channel with two output marginals equal to $`\mathcal N`$. Averaging it with the channel whose outputs are swapped gives (5).

Conversely, $`W`$ in (5) has $`R`$ marginal $`I_R/d`$ and hence defines a channel $`\mathcal M:T\to O_1O_2`$ whose two marginals equal $`\mathcal N`$. Fix a minimal Stinespring dilation of the first marginal. Uniqueness of dilation implies that its environment can be processed to generate the second output of $`\mathcal M`$. Tracing the first output then gives $`\mathcal N`$ from $`\mathcal N^c`$. Thus $`\mathcal N`$ is antidegradable.

Here each output is $`O_i=F_iB_i`$. The extension must copy the availability of the classical flag as well as the quantum target.

## 3. Two Bell projectors

On $`\mathcal H_R\otimes\mathcal H_{B_1}\otimes\mathcal H_{B_2}`$, define

```math
P_1=\Phi_{RB_1}\otimes I_{B_2},
\qquad
P_2=\Phi_{RB_2}\otimes I_{B_1},
\qquad\text{(6)}
```

with tensor factors put in the order $`RB_1B_2`$. Write

```math
c=\frac1{d^2},
\qquad
t=1-c,
\qquad
s=\frac{1+1/d}{2}.
\qquad\text{(7)}
```

The elementary identities are

```math
P_1P_2P_1=cP_1,
\qquad
P_2P_1P_2=cP_2,
\qquad
\Vert P_1+P_2\Vert _\infty=1+\frac1d.
\qquad\text{(8)}
```

To verify them, let $`V_1|x\rangle=|\phi_d\rangle_{RB_1}|x\rangle_{B_2}`$ and $`V_2|x\rangle=|\phi_d\rangle_{RB_2}|x\rangle_{B_1}`$. In the chosen basis, $`V_1^\dagger V_2=I_d/d`$ and $`P_i=V_iV_i^\dagger`$. This proves the first two identities. On the spans of $`V_1|x\rangle\pm V_2|x\rangle`$, the sum $`P_1+P_2`$ has eigenvalues $`1\pm1/d`$; it vanishes on the common kernel.

Let $`Q_2=I-P_2`$. The positive operator $`Q_2P_1Q_2`$ satisfies

```math
(Q_2P_1Q_2)^2=t\,Q_2P_1Q_2,
\qquad
\mathrm{Tr}(Q_2P_1Q_2)=dt.
\qquad\text{(9)}
```

Consequently,

```math
\Vert Q_2P_1Q_2\Vert _\infty=t.
\qquad\text{(10)}
```

This is the relevant constrained overlap: when the second pair has zero Bell overlap, the first pair can have Bell overlap at most $`1-d^{-2}`$. It is the endpoint of the familiar asymmetric isotropic-compatibility region [3,4].

## 4. Necessity: a witness for every flagged extension

Suppose $`J_{N,d}`$ has a symmetric extension. Dephase both flags in their computational bases. This is a local channel on each output copy, preserves swap invariance, and leaves the required marginals unchanged. Thus an extension may be taken to have the form

```math
W=\sum_{a,b=0}^1
|a\rangle\langle a|_{F_1}\otimes
|b\rangle\langle b|_{F_2}\otimes W_{ab},
\qquad\text{(11)}
```

where every $`W_{ab}`$ is a positive, subnormalized operator on $`RB_1B_2`$. If $`V`$ swaps $`B_1,B_2`$, symmetry gives

```math
W_{ba}=VW_{ab}V,
\qquad
\sum_b\mathrm{Tr}_{B_2}W_{ab}=\sigma_a.
\qquad\text{(12)}
```

The second bad marginal has zero Bell weight. Therefore

```math
0=\mathrm{Tr}\!\left[P_2(W_{01}+W_{11})\right].
\qquad\text{(13)}
```

Both terms are nonnegative. For a positive operator $`X`$ and projector $`P`$, $`\mathrm{Tr}(PX)=0`$ implies $`PX=XP=0`$. It follows that $`W_{01}=Q_2W_{01}Q_2`$, and (10) yields

```math
\mathrm{Tr}(P_1W_{01})
\le t\,\mathrm{Tr}W_{01}.
\qquad\text{(14)}
```

The block $`W_{00}`$ is invariant under $`V`$, so (8) gives

```math
\begin{aligned}
2\mathrm{Tr}(P_1W_{00})
&=\mathrm{Tr}[(P_1+P_2)W_{00}]\\
&\le \left(1+\frac1d\right)\mathrm{Tr}W_{00}.
\end{aligned}
\qquad\text{(15)}
```

For every $`d\ge2`$,

```math
t-s=\frac{(d-2)(d+1)}{2d^2}\ge0.
\qquad\text{(16)}
```

Combining (14)–(16), and using the first good marginal, gives the necessary inequality

```math
\begin{aligned}
\frac1{d^2}
&=\mathrm{Tr}\!\left[P_1(W_{00}+W_{01})\right]\\
&\le t\left(\mathrm{Tr}W_{00}+\mathrm{Tr}W_{01}\right)\\
&=t p_0.
\end{aligned}
\qquad\text{(17)}
```

Substitute (4):

```math
\frac1{d^2}
\le
\left(1-\frac1{d^2}\right)
\frac{N+d^2-1}{Nd^2}
\quad\Longleftrightarrow\quad
N\le(d^2-1)^2.
\qquad\text{(18)}
```

This rules out every symmetric extension above the threshold, including extensions with correlations or coherence before flag dephasing. No restriction to a guessed extension ansatz was made.

## 5. Sufficiency: explicit extension at the endpoint

Set

```math
r=d^2-1,\qquad N_\star=r^2,\qquad p_\star=\frac1r.
\qquad\text{(19)}
```

Two normalized states on $`RB_1B_2`$ suffice.

### 5.1 Cross-flag state

Define

```math
S=\frac{Q_2P_1Q_2}{dt}.
\qquad\text{(20)}
```

Equation (9) proves positivity and normalization. Its Bell weights are

```math
\mathrm{Tr}(P_1S)=t,
\qquad
\mathrm{Tr}(P_2S)=0.
\qquad\text{(21)}
```

For example, the first equality follows from
$`\mathrm{Tr}(P_1Q_2P_1Q_2)=dt^2`$.

Every $`P_i`$ is invariant under $`U_R^*\otimes U_{B_1}\otimes U_{B_2}`$. The same holds for $`S`$. Its pair marginals are therefore isotropic. Define the normalized isotropic state with Bell fraction $`f`$ by

```math
\tau_f=f\Phi+(1-f)\frac{I_{RB}-\Phi}{d^2-1}.
\qquad\text{(22)}
```

Covariance and (21) determine the marginals exactly:

```math
\mathrm{Tr}_{B_2}S=\tau_t,
\qquad
\mathrm{Tr}_{B_1}S=\tau_0.
\qquad\text{(23)}
```

### 5.2 Both-bad state

The orthogonal projector onto $`\mathrm{ran}P_1+\mathrm{ran}P_2`$ is

```math
H=\frac{P_1+P_2-P_1P_2-P_2P_1}{t}.
\qquad\text{(24)}
```

Indeed, (8) gives $`HP_i=P_i`$, while $`H`$ vanishes on $`\ker P_1\cap\ker P_2`$. It is Hermitian and its range is contained in $`\mathrm{ran}P_1+\mathrm{ran}P_2`$, proving that it is the orthogonal projector onto that span. The two ranges intersect trivially because $`c\lt 1`$, so $`\mathrm{rank}H=2d`$.

Consequently,

```math
K=I-H,\qquad
\mathrm{Tr}K=d^3-2d>0,\qquad
B=\frac{K}{d^3-2d}
\qquad\text{(25)}
```

define a positive normalized state. It is invariant under swapping $`B_1,B_2`$ and under the same unitary covariance. Both its Bell weights vanish, hence

```math
\mathrm{Tr}_{B_2}B
=\mathrm{Tr}_{B_1}B
=\tau_0.
\qquad\text{(26)}
```

### 5.3 Assemble the flagged extension

At $`N=N_\star`$, take the four blocks in (11) to be

```math
\boxed{
\begin{aligned}
W^\star_{00}&=0,\\
W^\star_{01}&=p_\star S,\\
W^\star_{10}&=p_\star VSV,\\
W^\star_{11}&=(1-2p_\star)B.
\end{aligned}}
\qquad\text{(27)}
```

All coefficients are nonnegative: $`d\ge2`$ implies $`p_\star\le1/3`$. The total trace is one and swapping the two complete outputs leaves $`W^\star`$ invariant.

Its first good marginal is $`p_\star\tau_t`$. Using $`t=r/d^2`$ gives

```math
p_\star\tau_t
=\frac{\Phi}{d^2}+\frac{I_{RB}-\Phi}{r^2d^2}
=\sigma_0\big|_{N=N_\star}.
\qquad\text{(28)}
```

The first bad marginal is

```math
\begin{aligned}
(1-p_\star)\tau_0
&=\frac{r-1}{r^2}(I_{RB}-\Phi)\\
&=\frac{N_\star-1}{N_\star d^2}(I_{RB}-\Phi)
=\sigma_1\big|_{N=N_\star},
\end{aligned}
\qquad\text{(29)}
```

where $`d^2=r+1`$ was used. Thus (27) is an explicit symmetric extension with the exact required marginals.

## 6. Explicit extension for every smaller integer

All $`J_{N,d}`$ in (3) act on the same binary-flag output space and depend affinely on $`1/N`$. For $`1\le N\le N_\star`$, set

```math
\lambda_N
=\frac{N^{-1}-N_\star^{-1}}{1-N_\star^{-1}}
=\frac{N_\star-N}{N(N_\star-1)}.
\qquad\text{(30)}
```

Then $`0\le\lambda_N\le1`$ and

```math
J_{N,d}=\lambda_NJ_{1,d}+(1-\lambda_N)J_{N_\star,d}.
\qquad\text{(31)}
```

At $`N=1`$, both extension flags can be fixed to $`0`$, with target-reference state $`I_{RB_1B_2}/d^3`$:

```math
W^{(1)}_{00}=\frac{I_{RB_1B_2}}{d^3},
\qquad
W^{(1)}_{01}=W^{(1)}_{10}=W^{(1)}_{11}=0.
\qquad\text{(32)}
```

Its first marginal is $`|0\rangle\langle0|\otimes I_{RB}/d^2=J_{1,d}`$. Therefore

```math
\boxed{W^{(N)}=\lambda_NW^{(1)}+(1-\lambda_N)W^\star}
\qquad\text{(33)}
```

is the promised explicit extension for every $`N`$ satisfying (1). Together with (18), this proves Theorem 1. The full $`N`$-dimensional controller can be restored by applying the decompression channel to each of the two output copies.

## 7. Capacity consequences and their limits

### 7.1 Quantum and private capacity vanish

An antidegradable channel lets its environment reproduce the receiver output. This property survives tensor products and arbitrary receiver processing.

For a pure Stinespring output $`RBE`$, data processing under $`E\to B`$ gives

```math
I(R\rangle B)\le I(R\rangle E)=-I(R\rangle B),
\qquad\text{(34)}
```

so its coherent information is nonpositive. The same is true for every block input to every tensor power. For a classical input label $`X`$, data processing gives $`I(X:B)\le I(X:E)`$, so private information is also nonpositive. The standard regularized capacity formulas [5] then give $`Q=P=0`$.

These are capacities of the complete unassisted channel, with the usual complementary environment in the private-capacity definition. The receiver may decode jointly over all flags and targets. The [controller simulation](channel_model.md#5-correlated-controllers-across-a-block) extends the conclusion to any fixed input-independent correlated preparation across a block, even when that preparation is changed with block length.

One effective invocation consumes $`N`$ raw slots. Both the per-invocation and per-raw-slot capacities vanish in the stated region.

### 7.2 Accuracy of the successful branch at the endpoint

The normalized good-branch Choi operator is

```math
J(\mathcal E_0)
=\frac{(N-1)\Phi+I_{RB}}{N+d^2-1},
\qquad
F_e(\mathcal E_0)=\frac{N}{N+d^2-1}.
\qquad\text{(35)}
```

At $`N=N_\star`$,

```math
F_e(\mathcal E_0)=1-\frac1{d^2},
\qquad
p_0=\frac1{d^2-1},
\qquad
Q(\mathcal C_{N_\star,d})=P(\mathcal C_{N_\star,d})=0.
\qquad\text{(36)}
```

The conditional error has an exact diamond-norm interpretation:

```math
\frac12\Vert \mathcal E_0-\mathrm{id}\Vert _\diamond
=1-F_e(\mathcal E_0)
=\frac{d^2-1}{N+d^2-1}.
\qquad\text{(37)}
```

To see this, express the completely depolarizing channel as the uniform mixture of the $`d^2`$ Weyl conjugations. The good branch is a Weyl mixture with identity weight $`F_e`$ and nonidentity weights summing to $`1-F_e`$. The triangle inequality bounds the diamond distance by $`2(1-F_e)`$; a maximally entangled input attains that value because the Weyl Choi vectors are orthogonal.

Thus the conditional error at the antidegradable endpoint is $`1/d^2`$. This limiting accuracy is accompanied by success probability of order $`d^{-2}`$ and $`N_\star`$ of order $`d^4`$ raw slots per invocation. Those costs are part of the statement.

### 7.3 Why the complete flag analysis matters

For an unflagged isotropic Choi state, the familiar symmetric-extension boundary is $`F_e\le s=(1+1/d)/2`$ [3]. Applying that test only to the good conditional channel in (35) gives

```math
N\le(d+1)^2.
\qquad\text{(38)}
```

The bad branch has Bell fraction zero and is itself antidegradable. Hence treating both branches separately yields only the region (38). The exact complete-channel boundary extends it to $`(d^2-1)^2`$. For $`d=2`$, the two bounds coincide at $`N=9`$. For $`d=3`$, the separate-branch argument stops at $`N=16`$, whereas the complete channel remains antidegradable through $`N=64`$.

The original cyclic-order work establishes two-way-assisted activation for $`N\ge d+2`$ [1]. Its successful-branch capacity statements do not establish positive unassisted capacity for the complete flagged device. There is no contradiction: feedback that identifies successful outcomes changes the communication resource.

Above (1), the witness proves that uniform control is not antidegradable. Its unassisted quantum and private capacities are not determined by this proof. Nor does the theorem cover arbitrary permutation superpositions, correlated slot noise, message-bearing controllers, target bypasses, or target operations between slots.

## References

[1] G. Chiribella, M. Wilson, and H. F. Chau, “Quantum and Classical Data Transmission through Completely Depolarising Channels in a Superposition of Cyclic Orders,” *Physical Review Letters* **127**, 190502 (2021). [DOI](https://doi.org/10.1103/PhysRevLett.127.190502); [arXiv:2005.00618v5](https://arxiv.org/abs/2005.00618v5).

[2] G. O. Myhr and N. Lütkenhaus, “Spectrum conditions for symmetric extendible states,” *Physical Review A* **79**, 062307 (2009), especially the connection between channels and symmetric extensions. [DOI](https://doi.org/10.1103/PhysRevA.79.062307); [arXiv:0812.3667](https://arxiv.org/abs/0812.3667).

[3] P. D. Johnson and L. Viola, “Compatible quantum correlations: on extension problems for Werner and isotropic states,” *Physical Review A* **88**, 032323 (2013). [DOI](https://doi.org/10.1103/PhysRevA.88.032323); [arXiv:1305.1342v3](https://arxiv.org/abs/1305.1342v3).

[4] I. Nechita, C. Pellegrini, and D. Rochette, “A geometrical description of the universal $`1\to2`$ asymmetric quantum cloning region,” *Quantum Information Processing* **20**, 333 (2021). [DOI](https://doi.org/10.1007/s11128-021-03258-y); [arXiv:2106.09655](https://arxiv.org/abs/2106.09655).

[5] I. Devetak, “The private classical capacity and quantum capacity of a quantum channel,” *IEEE Transactions on Information Theory* **51**, 44–55 (2005). [arXiv:quant-ph/0304127v6](https://arxiv.org/abs/quant-ph/0304127v6).
