# Channel model, flag reduction, and optimal controller

The communication resource considered here is a coherent superposition of the cyclic orders of independent completely depolarizing channels. The complete receiver output includes the target and controller. For a controller prepared independently of the input, the effective channel has an exact two-term form. Uniform coherent control is sufficient for every controller choice: its output can be processed at the receiver to reproduce any other fixed preparation, including correlated preparations across a block and an arbitrary retained preparation ancilla.

The cyclic channel formula and its uniform-control flag decomposition originate in Chiribella, Wilson, and Chau [1]. This document derives the formulas with explicit conventions, proves the receiver-side simulation, and fixes the communication resources to which the [antidegradability theorem](ideal_boundary.md) applies.

## 1. Registers, independence, and resource accounting

Let $`d\ge 2`$ and $`N\ge 1`$ be integers. The input target $`T`$ and output target $`B`$ have dimension $`d`$. Each of the $`N`$ physical slots implements

```math
\mathcal D_d(X)=\mathrm{Tr}(X)\frac{I_d}{d}.
\qquad\text{(1)}
```

The slots have independent noise. The order controller $`C`$ has basis $`|i\rangle`$, $`i\in\mathbb Z_N`$. Its value $`i`$ selects the chronological order

```math
i+1,i+2,\ldots,N,1,\ldots,i.
\qquad\text{(2)}
```

An optional preparation ancilla $`Z`$ can be correlated or entangled with $`C`$ and is delivered to the receiver without interacting with the target. The fixed preparation is a density operator $`\omega_{CZ}`$. For every target input, including one entangled with a reference $`R`$, the initial state is

```math
\omega_{CZ}\otimes\rho_{RT}.
\qquad\text{(3)}
```

Equation (3) is the independence assumption. Independence of the controller marginal from a classical message label would be weaker and does not suffice: input-controller correlations could themselves supply an additional communication resource.

The receiver retains all of $`BCZ`$ and may perform arbitrary decoding. The encoder acts on the target inputs. The model supplies no message encoding into the controller or preparation ancilla, no target bypass, no additional operations on the target between slots, no access to the slot environments, and no feedback from receiver to sender. The order register is not re-prepared or coupled to an input-dependent system inside an invocation.

One effective invocation uses **$`N`$ raw depolarizing slots**, not one. A block of $`m`$ effective invocations uses $`mN`$ raw slots. A rate of $`r`$ qubits or private bits per effective invocation is $`r/N`$ per raw slot. The controller has dimension $`N`$ per invocation. The ancillary preparation is input independent; it does not convey a message or provide sender-receiver entanglement with an encoding register.

For ordinary quantum and private capacities, the effective channel is used through tensor powers, with arbitrary encoding over the target inputs and arbitrary joint decoding. Section 5 additionally permits a fixed joint preparation of all controllers and a receiver ancilla across the block. These blocks still consist of disjoint cyclic devices with independent slot noise.

## 2. Exact effective channel

Write

```math
\omega_{CZ}=\sum_{i,j=0}^{N-1}|i\rangle\langle j|_C\otimes\omega_{ij}^Z,
\qquad
\Delta_C(\omega)=\sum_i|i\rangle\langle i|_C\otimes\omega_{ii}^Z.
\qquad\text{(4)}
```

The output channel, with register order $`CZB`$, is

```math
\boxed{
\mathcal S_\omega(X)
=\Delta_C(\omega)\otimes\mathrm{Tr}(X)\frac{I_d}{d}
+\bigl[\omega-\Delta_C(\omega)\bigr]\otimes\frac{X}{d^2}.
}
\qquad\text{(5)}
```

All equations are linear identities on arbitrary operators $`X`$, not only on density operators. They consequently remain valid when a reference system is retained.

### Direct Kraus derivation

Use matrix-unit Kraus operators for each physical slot:

```math
K_{a_jb_j}=\frac{|a_j\rangle\langle b_j|}{\sqrt d},
\qquad a_j,b_j\in\{0,\ldots,d-1\}.
\qquad\text{(6)}
```

For a fixed tuple of slot indices, abbreviate $`K_{a_jb_j}`$ by $`K_j`$. The ordered product for controller value $`i`$ is

```math
L_i=K_i\cdots K_1K_N\cdots K_{i+1},
\qquad\text{(7)}
```

where the first factor is empty for $`i=0`$, so $`L_0=K_N\cdots K_1`$. A Kraus representation of the controlled device is obtained by replacing each tuple of slot Kraus operators with $`\sum_i|i\rangle\langle i|_C\otimes L_i`$. Therefore its $`(i,j)`$ control block applies the target map

```math
\mathcal T_{ij}(X)=\sum_{\{a_\ell,b_\ell\}}L_iXL_j^\dagger.
\qquad\text{(8)}
```

For $`i=j`$, this is a composition of completely depolarizing channels and equals $`\mathcal D_d(X)`$.

For $`i\ne j`$, cyclic relabeling reduces the calculation to $`i=0`$ and $`j=k`$, with $`1\le k<N`$. Set $`a_0=a_N`$. In $`L_0`$, the matrix-unit contractions impose $`b_j=a_{j-1}`$ for every $`j`$ except $`j=1`$. In $`L_k`$, the only omitted constraint is $`j=k+1`$. Together the two products impose all $`N`$ constraints. The cross term is consequently

```math
d^{-N}|a_N\rangle
  \langle a_N|X|a_k\rangle
  \langle a_k|.
\qquad\text{(9)}
```

The remaining $`N-2`$ indices $`a_j`$ contribute a factor $`d^{N-2}`$. Summing $`a_N`$ and $`a_k`$ gives

```math
\mathcal T_{ij}(X)=
\begin{cases}
\mathcal D_d(X),&i=j,\\[2mm]
X/d^2,&i\ne j.
\end{cases}
\qquad\text{(10)}
```

For $`N=1`$ there are no cross terms. Substituting (10) into (8), with the untouched ancillary blocks $`\omega_{ij}^Z`$, proves (5).

## 3. Uniform control and lossless binary flags

Let

```math
|+\rangle=\frac1{\sqrt N}\sum_{i=0}^{N-1}|i\rangle,
\qquad
\Pi_0=|+\rangle\langle+|,
\qquad
\Pi_1=I_C-\Pi_0.
\qquad\text{(11)}
```

Without a preparation ancilla, uniform coherent control gives

```math
\mathcal S_+(X)
=\frac{I_C}{N}\otimes\mathrm{Tr}(X)\frac{I_d}{d}
+\left(\Pi_0-\frac{I_C}{N}\right)\otimes\frac{X}{d^2}.
\qquad\text{(12)}
```

For $`N>1`$, define the completely positive, trace-nonincreasing branch maps

```math
\begin{aligned}
\mathcal A_0(X)
&=\frac{\mathrm{Tr}(X)I_d}{Nd}
  +\frac{N-1}{Nd^2}X,\\
\mathcal A_1(X)
&=\frac{N-1}{Nd}\mathrm{Tr}(X)I_d
  -\frac{N-1}{Nd^2}X.
\end{aligned}
\qquad\text{(13)}
```

Equation (12) becomes

```math
\mathcal S_+(X)
=\Pi_0\otimes\mathcal A_0(X)
+\frac{\Pi_1}{N-1}\otimes\mathcal A_1(X).
\qquad\text{(14)}
```

Measure the orthogonal subspaces $`\Pi_0,\Pi_1`$ and retain their label in a binary register $`F`$. This produces

```math
\mathcal C_{N,d}(X)
=|0\rangle\langle0|_F\otimes\mathcal A_0(X)
+|1\rangle\langle1|_F\otimes\mathcal A_1(X).
\qquad\text{(15)}
```

Conversely, prepare $`\Pi_0`$ on flag $`0`$ and $`\Pi_1/(N-1)`$ on flag $`1`$. This reconstructs (14) exactly. Both transformations are channels at the receiver; no branch is discarded. Thus $`\mathcal S_+`$ and $`\mathcal C_{N,d}`$ are equivalent for quantum capacity, private capacity, and antidegradability. The compression loses no information about the input. At $`N=1`$, the channel is $`\mathcal D_d`$ with a deterministic flag $`0`$.

The flag probabilities are input independent:

```math
p_0=\frac{N+d^2-1}{Nd^2},
\qquad
p_1=\frac{(N-1)(d^2-1)}{Nd^2}.
\qquad\text{(16)}
```

The normalized conditional channels are

```math
\begin{aligned}
\mathcal E_0(X)
&=\frac{(N-1)X+d\,\mathrm{Tr}(X)I_d}{N+d^2-1},\\
\mathcal E_1(X)
&=\frac{d\,\mathrm{Tr}(X)I_d-X}{d^2-1},
\end{aligned}
\qquad
\mathcal C_{N,d}(X)=\sum_{a=0}^1p_a|a\rangle\langle a|\otimes\mathcal E_a(X).
\qquad\text{(17)}
```

The second branch is unused when $`N=1`$. Calling flag $`0`$ “good” or “successful” refers to its conditional fidelity; capacity of the complete device retains both flags.

### Normalized Choi convention

Define

```math
|\phi_d\rangle=\frac1{\sqrt d}\sum_{x=0}^{d-1}|x\rangle_R|x\rangle_T,
\qquad
\Phi=|\phi_d\rangle\langle\phi_d|.
\qquad\text{(18)}
```

For a trace-preserving channel $`\mathcal N`$, its normalized Choi operator is $`J(\mathcal N)=(\mathrm{id}_R\otimes\mathcal N)(\Phi)`$; it has trace one and $`R`$ marginal $`I_R/d`$. With $`I_{RB}`$ denoting the identity on a space of dimension $`d^2`$,

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
\qquad\text{(19)}
```

The blocks $`\sigma_a`$ are subnormalized: $`\mathrm{Tr}\sigma_a=p_a`$. In particular,

```math
\mathrm{Tr}(\Phi\sigma_0)=\frac1{d^2},
\qquad
\mathrm{Tr}(\Phi\sigma_1)=0.
\qquad\text{(20)}
```

These two weights drive the exact boundary proof.

## 4. Uniform control dominates every independent preparation

**Proposition 1.** For every fixed density operator $`\omega_{CZ}`$, there is a receiver channel $`\Lambda_\omega:C\to CZ`$ such that

```math
\boxed{
\mathcal S_\omega
=(\Lambda_\omega\otimes\mathrm{id}_B)\circ\mathcal S_+.
}
\qquad\text{(21)}
```

The preparation ancilla can have arbitrary finite dimension and arbitrary entanglement with the controller.

**Proof.** First take a pure preparation

```math
|\psi\rangle_{CZ}=\sum_{i=0}^{N-1}|i\rangle_C|a_i\rangle_Z,
\qquad
\sum_i\langle a_i|a_i\rangle=1.
\qquad\text{(22)}
```

The vectors $`|a_i\rangle`$ need not be normalized or orthogonal. Define Kraus operators

```math
K_s=\sum_{i=0}^{N-1}|i\rangle_C|a_i\rangle_Z\langle i-s|_C,
\qquad s\in\mathbb Z_N.
\qquad\text{(23)}
```

All control indices are modulo $`N`$. Orthogonality of the output control basis gives

```math
\sum_sK_s^\dagger K_s
=\sum_{s,i}\|a_i\|^2|i-s\rangle\langle i-s|
=I_C.
\qquad\text{(24)}
```

Thus $`\Lambda_\psi(Y)=\sum_sK_sYK_s^\dagger`$ is a channel. It satisfies

```math
\Lambda_\psi(I_C/N)=\Delta_C(|\psi\rangle\langle\psi|),
\qquad
\Lambda_\psi(\Pi_0)=|\psi\rangle\langle\psi|.
\qquad\text{(25)}
```

The first identity follows by summing the diagonal terms; for the second, each $`K_s|+\rangle=|\psi\rangle/\sqrt N`$. Equations (12) and (25) prove (21) for a pure preparation. If $`\omega=\sum_\ell q_\ell|\psi_\ell\rangle\langle\psi_\ell|`$, use the channel $`\Lambda_\omega=\sum_\ell q_\ell\Lambda_{\psi_\ell}`$. Linearity proves the result. $`\square`$

The simulation is deterministic and preserves the full target output. It does not send a selected success flag back to the encoder. Since antidegradability is preserved under receiver channels, the antidegradable regime of uniform control applies to every preparation covered by (3).

## 5. Correlated controllers across a block

Single-use controller dominance does not by itself establish a claim about correlated preparations across uses. The stronger block statement follows from the equality structure in (10).

**Proposition 2.** Fix $`m`$ disjoint cyclic devices, each with $`N`$ slots of dimension $`d`$. Let $`\omega_{C^m Z}`$ be any joint preparation, independent of $`\rho_{RT^m}`$. The controls may be entangled with one another and with $`Z`$. There exists a receiver channel $`\Lambda_\omega^{(m)}:C^m\to C^mZ`$ for which the complete block channel obeys

```math
\boxed{
\mathcal S_\omega^{(m)}
=\bigl(\Lambda_\omega^{(m)}\otimes\mathrm{id}_{B^m}\bigr)
  \circ\mathcal S_+^{\otimes m}.
}
\qquad\text{(26)}
```

This equality holds on arbitrary entangled inputs to the $`m`$ targets.

**Proof.** Write $`\mathbf i,\mathbf j,\mathbf s\in G=(\mathbb Z_N)^m`$ and

```math
\mathcal T_{\mathbf i,\mathbf j}
=\bigotimes_{\ell=1}^m\mathcal T_{i_\ell j_\ell}.
\qquad\text{(27)}
```

The tensor product in (27) is a tensor product of linear maps, so it acts on any operator on $`T^m`$, including entangled states. Equation (10) implies

```math
\mathcal T_{\mathbf i-\mathbf s,\mathbf j-\mathbf s}
=\mathcal T_{\mathbf i,\mathbf j}
\quad\text{for every }\mathbf s\in G.
\qquad\text{(28)}
```

For a pure joint preparation, write

```math
|\psi\rangle=\sum_{\mathbf i\in G}|\mathbf i\rangle|a_{\mathbf i}\rangle,
\qquad
\sum_{\mathbf i}\|a_{\mathbf i}\|^2=1,
\qquad\text{(29)}
```

and define

```math
K_{\mathbf s}
=\sum_{\mathbf i\in G}
|\mathbf i\rangle|a_{\mathbf i}\rangle
\langle\mathbf i-\mathbf s|.
\qquad\text{(30)}
```

The same calculation as (24) gives $`\sum_{\mathbf s}K_{\mathbf s}^\dagger K_{\mathbf s}=I_{C^m}`$. Meanwhile, the product-uniform output is

```math
\mathcal S_+^{\otimes m}(X)
=\frac1{N^m}\sum_{\mathbf k,\mathbf l\in G}
|\mathbf k\rangle\langle\mathbf l|
\otimes\mathcal T_{\mathbf k,\mathbf l}(X).
\qquad\text{(31)}
```

After applying the Kraus map (30), set $`\mathbf i=\mathbf k+\mathbf s`$ and $`\mathbf j=\mathbf l+\mathbf s`$. Each of the $`N^m`$ values of $`\mathbf s`$ contributes the same target operator by (28). The result is

```math
\sum_{\mathbf i,\mathbf j}
|\mathbf i\rangle\langle\mathbf j|
\otimes|a_{\mathbf i}\rangle\langle a_{\mathbf j}|
\otimes\mathcal T_{\mathbf i,\mathbf j}(X),
\qquad\text{(32)}
```

which is exactly the output for the joint preparation (29). Mixed preparations follow by convexity as in Proposition 1. $`\square`$

The equivalent binary channels $`\mathcal C_{N,d}^{\otimes m}`$ suffice as well: first decompress each binary flag using Section 3, then apply $`\Lambda_\omega^{(m)}`$.

### Operational scope

If $`\mathcal C_{N,d}`$ is antidegradable, then every tensor power is antidegradable. Receiver postprocessing preserves this property. Equation (26) therefore rules out positive unassisted quantum or private communication rates even if, at every block length, a different correlated controller preparation and retained receiver ancilla are chosen. Arbitrary target encoding and joint decoding are already included.

This statement does not cover a global superposition of permutations that interleaves slots belonging to different devices, correlations among slot environments, feedback-dependent preparations, input-controller interactions, or a joint input state that violates (3). These modify the channel or communication resource.

The block proof also applies whenever each local cross map is multiplied by a fixed visibility $`v`$: the map then depends on whether $`i_\ell=j_\ell`$, and (28) remains true. The specific unobserved-dephasing model and its threshold are treated in [unobserved_dephasing.md](unobserved_dephasing.md).

## Reference

[1] G. Chiribella, M. Wilson, and H. F. Chau, “Quantum and Classical Data Transmission through Completely Depolarising Channels in a Superposition of Cyclic Orders,” *Physical Review Letters* **127**, 190502 (2021). [Published article](https://doi.org/10.1103/PhysRevLett.127.190502); [arXiv:2005.00618v5](https://arxiv.org/abs/2005.00618v5). The cyclic-channel reduction, conditional channels, and original heralded and assisted communication results appear there.
