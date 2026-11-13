# From Wilde's channel theory to cyclic-order capacity limits

An accepted transmission can be accurate even when the complete device cannot carry quantum information at a positive unassisted rate. This project identifies that separation for coherent cyclic orders of completely depolarizing channels. The learning route starts with the channel, its classical output flag, and its environment; it then turns the capacity question into an explicit extension problem.

## 1. Selected source and version

The educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition, Cambridge University Press (2017)**. [Publisher record](https://www.cambridge.org/core/books/quantum-information-theory/247A740E156416531AA8CB97DFDAE438), [book DOI](https://doi.org/10.1017/9781316809976).

The author's freely accessible [*From Classical to Quantum Shannon Theory* PDF](https://markwilde.com/qit-notes.pdf), dated **5 December 2021**, supplies an accessible version of this material. Its front matter identifies it as an author draft associated with the second edition. The detailed section, definition, and exercise locators below were checked in that version. They are not assertions that its pagination is identical to the 2017 published book. The publisher independently identifies Chapter 23 as [Private Classical Communication](https://doi.org/10.1017/9781316809976.027) and Chapter 24 as [Quantum Communication](https://doi.org/10.1017/9781316809976.028).

This is one educational anchor. The research papers in [related work](../references/RELATED_WORK.md) provide attribution and specialized proof ingredients, rather than a second prerequisite syllabus.

## 2. A selective route through the source

Read the indicated material when its question arises. The project does not require a sequential reading of the entire book.

| Question in this project | Wilde locator | Continue in the project |
| --- | --- | --- |
| How does a channel act on a target entangled with a reference? | Section 4.4; Choi operator, Definition 4.4.4 | [Channel model, Sections 1–3](../science/channel_model.md) |
| What does an environment retain, and what is a complementary channel? | Section 5.2.2, Definitions 5.2.1–5.2.2 | [Ideal boundary, Section 2](../science/ideal_boundary.md) |
| How do an outcome and its conditional quantum state form one output? | Sections 4.6 and 5.3 | [Lossless flag reduction, Section 3](../science/channel_model.md) |
| Which fidelity is being reported? | Section 9.5.2 | [Accepted fidelities, Section 8](../science/unobserved_dephasing.md) |
| Why does an environment simulation prevent communication? | Sections 13.5–13.6; Exercise 13.5.6 | [Capacity consequences, Section 7](../science/ideal_boundary.md) |
| How does a statement about all blocks become a capacity converse? | Sections 23.1–23.2 and 24.1–24.3 | [Operational consequences, Section 1](../science/operational_consequences.md) |

The [30-milestone map](MILESTONES.md) organizes these foundations around the project's argument. Its later milestones use the derivations in `science/`; Wilde is not being cited as a source of the cyclic-order thresholds.

## 3. Translate the notation before calculating

### Registers and resources

| Symbol here | Meaning |
| --- | --- |
| $`T`$, $`B`$, $`d`$ | Input target, delivered target, and their common dimension. |
| $`R`$ | An untouched reference used to test preservation of quantum correlations. |
| $`C`$, $`N`$ | Order controller and the number of cyclic orders. There are also $`N`$ physical depolarizing slots per effective invocation. |
| $`F`$ | Binary output flag obtained by an exact compression of the uniform controller. |
| $`Z`$ or $`A`$ | Retained preparation ancilla; the two scientific pages use these respective labels. It carries no encoded message. |
| $`E`$ | The full complementary environment for the effective channel. |
| $`m`$ | Number of effective invocations in a coding block, costing $`mN`$ raw slots. |

The receiver's complete output includes its target, controller or equivalent flag, and any permitted retained ancilla. When the capacity discussion calls this output “Bob,” it means the whole delivered system, not just the target register $`B`$.

### Choi normalization

Wilde's Definition 4.4.4 uses the unnormalized vector $`|\Gamma\rangle=\sum_x|x,x\rangle`$. This repository uses

$$
\Phi=\frac{|\Gamma\rangle\langle\Gamma|}{d},
\qquad
J(\mathcal N)=(\mathrm{id}_R\otimes\mathcal N)(\Phi).
$$

Thus the repository's $`J`$ is the Choi operator in that definition divided by the input dimension $`d`$. For a trace-preserving channel, $`\mathrm{Tr}J=1`$ and its reference marginal is $`I_R/d`$. In a flagged channel, the individual Choi blocks are subnormalized: their traces are branch probabilities. Normalizing a block changes the question to a conditional channel.

The symbol $`\Phi_d`$ in the dephasing proof denotes the same normalized maximally entangled projector as $`\Phi`$ in the ideal proof. The identity $`I_{RB}`$ has trace $`d^2`$; it is not the maximally mixed state.

### Information, capacity, and fidelity

The source's optimized one-use information quantities in Sections 13.5–13.6 must be distinguished from the regularized operational capacities. Here $`Q`$ and $`P`$ always denote the unassisted quantum capacity and the standard private classical capacity. One unsuccessful coherent-information calculation does not establish either capacity is zero. The proof instead supplies an environment simulation that persists through every coding block.

Here $`F_e`$ is entanglement fidelity for the maximally mixed target input, evaluated by retaining its maximally entangled purification. For a conditional channel $`\mathcal E_0`$,

$$
F_e=\mathrm{Tr}\!\left[\Phi J(\mathcal E_0)\right].
$$

This differs from fidelity of a single pure target state. Both conventions appear in the worked example below.

## 4. The steps from the foundations to the result

### Build the physical channel and keep its whole output

A completely depolarizing slot produces $`I_d/d`$ on any density operator. A definite sequence of such slots also erases the target. In the coherent cyclic construction, however, the off-diagonal blocks of the order register contain a contribution proportional to the input operator. The [Kraus derivation](../science/channel_model.md) shows that the target map in each unequal pair of cyclic-order labels is $`X/d^2`$.

For uniform control, all this output information can be represented by two orthogonal flag sectors. The receiver can compress the controller to a binary flag and reconstruct the original controller output from that flag. This reversibility distinguishes the reduction from discarding an unsuccessful outcome. The resulting complete channel is the object whose capacity is bounded.

### Show that other allowed preparations do not improve the bound

Uniform control is sufficient to simulate every fixed input-independent controller preparation, including a controller entangled with a retained ancilla. The simulator acts entirely at the receiver. [Proposition 2 of the channel model](../science/channel_model.md) proves the stronger statement for preparations correlated across a block of disjoint devices. It uses invariance of each target map under simultaneous cyclic shifts of its two order labels.

The independence condition is the factorization of the full preparation from the encoded target and reference. A controller marginal that happens to hide a classical message is not an adequate substitute. The physical slot noise remains independent across devices. These assumptions make the receiver simulation a legitimate channel comparison.

### Replace a capacity optimization by an extension problem

Antidegradability means that a channel's environment can simulate its complete receiver output. The [ideal proof, Section 2](../science/ideal_boundary.md), translates that property into a symmetric extension of the normalized Choi state. Both output copies include the flag as well as the target. This equivalence is a standard research ingredient, and its derivation is included locally.

The four joint flag sectors allow the two hypothetical receivers to have different outcomes. The bad marginal's zero Bell overlap constrains the cross sectors. Bell-projector geometry then gives a necessary inequality; an explicit positive extension attains it. Together these yield

$$
\mathcal C_{N,d}\text{ is antidegradable}
\quad\Longleftrightarrow\quad
N\le(d^2-1)^2.
$$

The equivalence concerns uniform control. Other allowed preparations inherit the zero-capacity region by receiver simulation. Above the boundary, this proof establishes non-antidegradability of the uniform channel, without determining its capacity.

### Specify the control noise and take a controlled limit

The [dephasing model](../science/unobserved_dephasing.md) applies the physical channel

$$
\mathcal D_v=v\mathrm{id}_C+(1-v)\Delta_C
$$

to the prepared order register, with its environment or random phase label unavailable to the receiver. A reduced controller state alone does not determine whether this physical noise has occurred: a retained phase record can permit recovery. The proof therefore keeps the channel, its placement, and the unavailable record explicit.

After exact flag compression, the output dimension is fixed. The limiting channel has a pure successful Choi block. That purity forbids both receivers from occupying the successful sector simultaneously. The cross sectors are fixed, and the remaining bad marginal must be positive. An explicit separable extension proves that the positivity condition is sufficient here. The result is

$$
\mathcal N_{\infty,v}\text{ is antidegradable}
\quad\Longleftrightarrow\quad
v\le\frac{d^2}{d^2+1}.
$$

Every finite channel is a convex mixture of this limit and a completely depolarizing channel with a fixed flag. Consequently the same range of $`v`$ guarantees antidegradability at every finite $`N`$. The proof does not exchange a capacity limit with an infinite physical device, and it does not claim the complete finite-$`N`$ noisy boundary.

### Return to the communication task

Once the environment can reproduce the receiver output, it can reproduce any decoder applied to that output. This survives arbitrary entangled target inputs across the block, tensor products of the effective channel, and the allowed receiver simulations. The [capacity argument](../science/operational_consequences.md) therefore gives $`Q=P=0`$ in the established regimes.

Private capacity uses the complete complementary environment, including noise and preparation purifications. Treating some environmental information as trusted and hidden from an eavesdropper would change the privacy model. Likewise, a classical return channel or preshared entanglement changes the supplied communication resources.

## 5. Work through one complete device

Take a qubit target, $`d=2`$, with $`N=1000`$ cyclic orders and physical dephasing parameter $`v=4/5`$. Prepare the uniform order controller independently of the input. Send the target through all 1000 depolarizing slots and deliver the target and controller to the receiver. The receiver measures the two controller sectors and retains the flag.

For flag $`0`$, the probability and normalized target channel are

$$
p_0=\frac{4+(4/5)999}{4000}=\frac{251}{1250},
\qquad
\mathcal E_0(\rho)=\frac{999}{1004}\rho
  +\frac{5}{1004}\frac{I_2}{2}.
$$

For any pure target input, the accepted fidelity is $`2003/2008`$, about $`99.751\%`$. To test entanglement preservation, prepare a Bell pair and send one half; conditioned on flag $`0`$, its overlap with the original Bell state is $`4001/4016`$, about $`99.626\%`$. These values follow from the same conditional channel with different input tests. Flag $`0`$ occurs with probability $`20.08\%`$.

The complete device remains antidegradable because $`v=4/5`$ is the qubit ceiling. Every flag string and every target output remains available to a joint decoder, yet the environment can simulate that complete decoding input. Hence $`Q=P=0`$. High fidelity on the selected outputs does not alter that simulation.

The invocation consumed 1000 raw slots. Its accepted-output frequency per raw slot is $`p_0/1000=0.0002008`$; this is a yield count, not an unassisted quantum communication rate. Reporting successful locations back to the sender would introduce a return channel. At fixed $`v=4/5`$, increasing $`N`$ makes the accepted channel approach the identity and the acceptance probability approach $`1/5`$, while every finite device retains zero unassisted capacities.

The [operational account](../science/operational_consequences.md) contains the corresponding plot and the assistance comparison. The [verification guide](../verification/README.md) documents independent finite calculations of the channel, extension certificates, and this example.

## 6. What the bridge leaves to the scientific account

The complete proofs, quantifiers, and attribution remain in the topic pages. The ideal boundary uses established isotropic compatibility geometry; the noisy proof uses rank-one factorization and an explicitly shareable quantum residual. Their evaluation for this architecture is the project's contribution. The [related-work account](../references/RELATED_WORK.md) distinguishes those inherited tools from the channel-specific classification and controller-simulation results.

Continue through [the milestone map](MILESTONES.md) for the full conceptual route, or go directly to the [ideal proof](../science/ideal_boundary.md) and [noise proof](../science/unobserved_dephasing.md) with these conventions in place.
