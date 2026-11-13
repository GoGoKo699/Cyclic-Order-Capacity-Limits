# Cyclic Order Capacity Limits

**Exact limits on unassisted communication through completely depolarizing channels arranged in cyclic order superpositions.**

An accepted output can approach perfect quantum transmission while the complete device has zero quantum and private capacity. This project identifies an exact antidegradability boundary for the cyclic construction and a specified control-noise regime in which no finite number of cyclic orders escapes that obstruction.

## Main results

Let $N$ independent completely depolarizing channels act on a $d$-dimensional target, with $d\ge2$, in a coherent superposition of their $N$ cyclic orders. The receiver retains the target and the complete controller output. For uniform ideal control,

$$
\boxed{\mathcal C_{N,d}\text{ is antidegradable}
\quad\Longleftrightarrow\quad N\le(d^2-1)^2.}
$$

Every fixed controller preparation independent of the complete encoded input is simulated by receiver postprocessing of uniform control. This includes retained preparation ancillas and controller correlations across blocks of disjoint devices. Consequently, every such preparation has zero unassisted quantum and private capacity throughout the stated region, even with arbitrary payload block coding.

Under actual unobserved order-register dephasing $\mathcal D_v=v\,\mathrm{id}+(1-v)\Delta_C$,

$$
\boxed{v\le\frac{d^2}{d^2+1}
\quad\Longrightarrow\quad Q=P=0\text{ for every finite }N.}
$$

For a qubit target with $v=4/5$ and $N=1000$, the accepted outcome occurs with probability **0.2008** and has entanglement fidelity **0.996265**, while the complete device has zero unassisted quantum and private capacities. The inaccessible noise environment is essential; a reduced-register visibility alone is not the noise assumption.

The exact ideal threshold is a boundary of **antidegradability**. Positive capacity above it is not established. One effective invocation consumes $N$ underlying channel uses. The model excludes message encoding in the controller, target-carrying bypasses, interleaved target operations, feedback and preshared entanglement. The private-capacity statement gives the eavesdropper the full complementary environment.

## Reading route

| Question | Authoritative account |
| --- | --- |
| What device and communication task are being studied? | [Channel model and controller reduction](science/channel_model.md) |
| Why is the ideal threshold exact? | [Antidegradability boundary](science/ideal_boundary.md) |
| How does inaccessible control noise change the result? | [Unobserved dephasing](science/unobserved_dephasing.md) |
| What do the capacities, heralding figures and resource costs mean? | [Operational consequences](science/operational_consequences.md) |
| Which results and proof tools are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/REFERENCES.bib) |
| How can the finite calculations be reproduced? | [Verification guide](verification/README.md) |

The cyclic channel and its heralded and two-way-assisted communication properties were established by [Chiribella, Wilson and Chau](https://arxiv.org/abs/2005.00618). The present results concern the complete channel's unassisted capacities. The proofs use established isotropic-state compatibility geometry; the [related-work account](references/RELATED_WORK.md) identifies the channel-specific addition and the shared foundations.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
