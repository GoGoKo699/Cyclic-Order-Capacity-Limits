# Learning route

How can a device deliver an almost perfect accepted quantum state while its unassisted quantum and private capacities are both zero? This project answers that question for coherent cyclic orders of completely depolarizing channels.

The receiver keeps every output flag and may decode jointly across arbitrarily many targets. The converse arises because the complementary environment can simulate that complete receiver output. The distinction between a conditional transmission and a communication rate is the thread connecting the learning material.

## Start here

1. Read the [anchor and project bridge](ANCHOR_AND_BRIDGE.md). It identifies the selected edition of Wilde, gives a selective source route, translates Choi normalization and capacity notation, and follows a qubit device through preparation, transmission, flag measurement, and resource accounting.
2. Use the [30-milestone map](MILESTONES.md) to connect the prerequisites to the full argument. Each milestone records a central question, an understanding target, dependencies, its role in the scientific story, and source pointers.
3. Follow the [scientific reading route](../science/channel_model.md) for exact definitions and proofs, then reproduce the [finite checks](../verification/README.md).

The educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition (Cambridge, 2017)**. [Publisher](https://doi.org/10.1017/9781316809976). The bridge also identifies the dated author version used to verify detailed section locators. Specialized primary research sources remain in [related work](../references/RELATED_WORK.md).

## Follow the argument

| Scientific question | Authoritative account |
| --- | --- |
| What physical device is supplied, which registers reach the receiver, and what does one use cost? | [Channel model, Sections 1–3](../science/channel_model.md) |
| Why does uniform control suffice even when preparation registers are correlated across devices? | [Controller simulation, Sections 4–5](../science/channel_model.md) |
| Where is the exact antidegradability boundary under ideal control? | [Ideal boundary](../science/ideal_boundary.md) |
| Which specified control noise obstructs unassisted capacity for every finite order count? | [Unobserved dephasing](../science/unobserved_dephasing.md) |
| How do accepted fidelity, success probability, feedback, and raw-slot cost fit together? | [Operational consequences](../science/operational_consequences.md) |

The target register alone is completely depolarized; the useful conditional information resides in its correlations with the output controller. Binary flag compression preserves those correlations exactly. Keeping that full output makes both the opportunity for heralding and the capacity obstruction visible in the same description.

The ideal theorem exactly classifies antidegradability of the uniform channel. The noise theorem gives an exact threshold for its fixed-output limit and a sufficient range for every finite device. Neither result identifies positive capacity outside the proved zero-capacity regions. The map retains this distinction, the input-independence assumption, and the requirement that the physical dephasing record be inaccessible to the receiver.
