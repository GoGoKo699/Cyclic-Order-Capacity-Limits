# Thirty milestones for cyclic-order capacity limits

This map develops the distinction between an accurate accepted transmission and a positive communication rate for the complete device. It is a common understanding map: each milestone identifies a question, the reasoning needed to answer it, and the sources that support that reasoning. The exact statements and proofs remain in the linked scientific pages.

The single educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition (Cambridge University Press, 2017)**. See the [anchor and bridge](ANCHOR_AND_BRIDGE.md) for the reading route and notation. Detailed section numbers below refer to the [author's public manuscript dated December 5, 2021](https://markwilde.com/qit-notes.pdf), associated with that edition. They are not claims about the pagination of the 2017 printed book. Wilde supplies the channel and capacity foundations; the cyclic model, controller simulation, and flagged-extension arguments are supplied in this repository with their primary research attribution.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The first phase connects individual states and channels to a complete communication task. The second follows the cyclic mechanism, its ideal extension boundary, and the dephasing obstruction, ending with the capacities, costs, and scope of the whole result. Dependencies point only to earlier milestones. A dependency identifies a useful conceptual prerequisite, rather than a required examination or learner record.

## Background and preliminaries

### M01 — States, correlations, and the reference

**Phase:** Background/preliminaries.

**Central question:** What must a quantum transmission preserve when its input can be entangled with another system?

**Understanding target:** Distinguish a target density operator from its joint state with a reference. Explain why preserving a few target states does not by itself establish preservation of arbitrary reference correlations.

**Dependencies and story role:** None. Introduce the physical systems whose correlations the later channel statements must preserve.

**Conceptual connection:** The reference makes the controller-independence assumption a condition on the complete encoded input, rather than only on the marginal seen by the sender.

**Source pointers:** Wilde §§3.5–3.8 and §§4.1, 4.3; [channel model, §1](../science/channel_model.md#1-registers-independence-and-resource-accounting).

### M02 — Noise as a channel on arbitrary operators

**Phase:** Background/preliminaries.

**Central question:** How can a map erase the target completely while remaining a valid operation on an entangled input?

**Understanding target:** Explain complete positivity, trace preservation, and a Kraus representation. Recognize the completely depolarizing map as a linear map on all operators, with the identity action on any reference understood.

**Dependencies and story role:** M01. Replace a description of noisy states by a physical transformation that can be composed inside the device.

**Conceptual connection:** Matrix-unit Kraus operators make the later diagonal and off-diagonal order-block calculation explicit.

**Source pointers:** Wilde §§4.4, 4.7; [channel model, §§1–2](../science/channel_model.md#2-exact-effective-channel).

### M03 — A channel represented by a normalized Choi state

**Phase:** Background/preliminaries.

**Central question:** How can one bipartite operator encode the channel's action on every input?

**Understanding target:** Construct the normalized Choi state from one half of a maximally entangled state. Track its unit trace and maximally mixed reference marginal, and distinguish it from an unnormalized Choi operator.

**Dependencies and story role:** M01–M02. Introduce the representation used by both extension proofs.

**Conceptual connection:** Positivity and partial-trace constraints on Choi operators become concrete conditions on possible output channels.

**Source pointers:** Wilde §4.4; [channel model, normalized Choi convention in §3](../science/channel_model.md#normalized-choi-convention).

### M04 — Instruments, outcome flags, and conditioning

**Phase:** Background/preliminaries.

**Central question:** What changes when an outcome is retained, ignored, or selected?

**Understanding target:** Distinguish a trace-nonincreasing branch map from the trace-preserving channel containing all branches. Explain why an input-independent branch probability allows a normalized conditional channel, while discarding the other outcomes changes the operational question.

**Dependencies and story role:** M02–M03. Separate the three objects whose confusion would obscure the project.

**Conceptual connection:** The receiver's binary flag is part of the complete channel output and must also appear in a symmetric extension.

**Source pointers:** Wilde §§4.6, 5.3; [channel model, §3](../science/channel_model.md#3-uniform-control-and-lossless-binary-flags).

### M05 — Two fidelities and the probability of seeing them

**Phase:** Background/preliminaries.

**Central question:** What does high accepted fidelity say about the experiment being counted?

**Understanding target:** Distinguish pure-state fidelity, entanglement fidelity, and the probability of the accepted flag. Explain why a conditional fidelity must be accompanied by its conditioning event and success probability.

**Dependencies and story role:** M01, M03–M04. Prepare the measures used to compare the accepted branch with the complete communication task.

**Conceptual connection:** The noisy qubit example reports both fidelity conventions because they have different exact values for the same conditional channel.

**Source pointers:** Wilde §§9.2, 9.5; [unobserved dephasing, §8](../science/unobserved_dephasing.md#8-high-accepted-fidelity-at-nonvanishing-success-probability).

### M06 — Purification and the complementary output

**Phase:** Background/preliminaries.

**Central question:** Where can the information missing from the receiver's state reside?

**Understanding target:** Describe a channel through an isometry to receiver and environment, and obtain complementary outputs by tracing different registers. Include purifications of mixed preparations and noise in the complete environment when the communication model requires them.

**Dependencies and story role:** M01–M02. Add the environmental viewpoint that will turn an extension into a communication obstruction.

**Conceptual connection:** Receiver access to a noise record and an eavesdropper's possession of the complementary environment are distinct assumptions.

**Source pointers:** Wilde §§5.1–5.2; [unobserved dephasing, §7](../science/unobserved_dephasing.md#7-environment-simulation-and-the-capacity-consequence).

### M07 — Rates for complete communication tasks

**Phase:** Background/preliminaries.

**Central question:** What do quantum capacity and private classical capacity optimize?

**Understanding target:** Explain asymptotically reliable quantum transmission and reliable classical transmission secret from the complementary environment. Allow encoding over many channel inputs and joint decoding, while stating whether feedback or preshared entanglement is supplied.

**Dependencies and story role:** M04–M06. Move from one accepted output to the task performed over many invocations.

**Conceptual connection:** A zero-capacity theorem must rule out arbitrary allowed block codes, not just one decoder or input ensemble.

**Source pointers:** Wilde §§23.1–23.2 and §§24.1–24.3; [communication consequences, §1](../science/operational_consequences.md#1-what-zero-capacity-means).

### M08 — Information cannot improve by receiver processing

**Phase:** Background/preliminaries.

**Central question:** Why does the ability to simulate an output impose a communication bound?

**Understanding target:** Use data processing to compare mutual and coherent information before and after a channel. Distinguish a calculation for one input from a comparison that holds for every input and every block length.

**Dependencies and story role:** M06–M07. Supply the information-theoretic implication of a deterministic simulation.

**Conceptual connection:** Both the controller-domination result and the environment's simulation of the receiver use this direction of processing.

**Source pointers:** Wilde §§11.5–11.6, 11.9 and §§13.5–13.6; [ideal boundary, §7.1](../science/ideal_boundary.md#71-quantum-and-private-capacity-vanish).

### M09 — Antidegradability and its stable consequences

**Phase:** Background/preliminaries.

**Central question:** What follows when the environment can reproduce the complete receiver output?

**Understanding target:** Define antidegradability, explain its preservation by tensor products and receiver postprocessing, and infer zero unassisted quantum and standard private capacity. Keep failure of this sufficient obstruction separate from a proof of positive capacity.

**Dependencies and story role:** M06–M08. Identify the property that the project classifies exactly.

**Conceptual connection:** The conclusion survives arbitrary coding because the environmental simulation survives the whole encoded block.

**Source pointers:** Wilde §§13.5–13.6 and §§24.2–24.3; [ideal boundary, §§2 and 7](../science/ideal_boundary.md#2-why-a-symmetric-choi-extension-is-the-right-criterion).

### M10 — Two receivers and symmetric extension

**Phase:** Background/preliminaries.

**Central question:** How can antidegradability be tested without guessing an explicit environmental channel?

**Understanding target:** Relate an antidegrading map to a joint channel with two equal receiver marginals, and then to a symmetric Choi extension. Distinguish invariance under exchanging outputs from support only in the symmetric subspace.

**Dependencies and story role:** M03, M06, M09. Translate an operational property into a positive-operator construction problem.

**Conceptual connection:** The copied receiver includes both target and flag; omitting the flag changes the extension problem.

**Source pointers:** Wilde §5.2 for dilation foundations; the equivalence and its primary attribution are supplied in [ideal boundary, §2](../science/ideal_boundary.md#2-why-a-symmetric-choi-extension-is-the-right-criterion).

### M11 — Isotropic states and Bell overlap

**Phase:** Background/preliminaries.

**Central question:** When can symmetry reduce an entire pair marginal to a single overlap?

**Understanding target:** Recognize an isotropic state as a mixture of the maximally entangled projector and its orthogonal complement. Explain how unitary covariance, normalization, and Bell overlap determine that marginal, with subnormalized weights kept separate.

**Dependencies and story role:** M01, M03, M10. Introduce the compact coordinates used to verify the extension marginals.

**Conceptual connection:** This symmetry simplifies marginal identification; the constraint on two competing Bell overlaps still needs the later geometric argument.

**Source pointers:** Wilde §§3.6, 4.3 for bipartite-state foundations; local isotropic definitions and primary sources in [ideal boundary, §§3 and 5.1](../science/ideal_boundary.md#51-cross-flag-state).

### M12 — A complete operational comparison

**Phase:** Background/preliminaries.

**Central question:** What information is needed before two transmission claims can be compared?

**Understanding target:** Specify the input, all receiver outputs, environment access, allowed assistance, block coding, and rate denominator together. Use the erasure-channel example to understand why an ideal conditional output alone does not determine an unassisted rate, while recognizing that the cyclic bad branch is a different channel.

**Dependencies and story role:** M04–M11. Synthesize the foundations into a framework for reading the cyclic-order claim.

**Conceptual connection:** Counting unsuccessful invocations and underlying slots keeps fidelity, heralded yield, and capacity in their proper tasks.

**Source pointers:** Wilde §24.7.1; [communication consequences, §§4–5](../science/operational_consequences.md#4-heralding-and-classical-feedback).

## Narrative and innovation

### M13 — The cyclic device and its independent preparation

**Phase:** Narrative/innovation.

**Central question:** Which coherent-order communication resource is actually being studied?

**Understanding target:** Specify the $`N`$ cyclic permutations of $`N`$ independent depolarizing slots on a target of dimension $`d`$. Explain the factorization of the controller and retained preparation ancilla from the complete encoded target/reference input, and charge $`N`$ raw calls per invocation.

**Dependencies and story role:** M02, M06, M12. Begin the project from its physical architecture and admissible resources.

**Conceptual connection:** A message-bearing controller, a target bypass, or interleaved target operations changes the channel rather than furnishing a counterexample inside this model.

**Source pointers:** Wilde §§4.4, 5.2 as foundations; [channel model, §1](../science/channel_model.md#1-registers-independence-and-resource-accounting).

### M14 — What survives between distinct cyclic orders

**Phase:** Narrative/innovation.

**Central question:** How does coherence between orders retain input dependence when each definite order depolarizes completely?

**Understanding target:** Follow the matrix-unit Kraus contractions that give the depolarizing map in a diagonal control block and $`X/d^2`$ in every off-diagonal cyclic block. Explain why the resulting identity applies to arbitrary target operators and retained references.

**Dependencies and story role:** M02–M03, M13. Identify the mechanism before compressing its outputs.

**Conceptual connection:** Dependence only on equality of order labels later makes a controller simulation possible across entire blocks.

**Source pointers:** Wilde §4.4 for Kraus maps; [channel model, §2 and its direct derivation](../science/channel_model.md#direct-kraus-derivation).

### M15 — Lossless flags and the two Choi weights

**Phase:** Narrative/innovation.

**Central question:** Why can an output controller of dimension $`N`$ be replaced by two flags without losing useful information?

**Understanding target:** Construct both the flag measurement and its receiver-side reconstruction for uniform control. Read the branch probabilities from subnormalized Choi traces, and identify the good branch's Bell weight $`1/d^2`$ and the bad branch's zero Bell weight.

**Dependencies and story role:** M03–M04, M11, M14. Reduce the exact device to the fixed output structure used by the proofs.

**Conceptual connection:** This is a reversible conversion between complete output channels; selecting only the good flag is an additional operation.

**Source pointers:** Wilde §§4.4, 5.3 for channel/instrument foundations; [channel model, §3](../science/channel_model.md#3-uniform-control-and-lossless-binary-flags).

### M16 — Why uniform control suffices for one device

**Phase:** Narrative/innovation.

**Central question:** Could another independent controller preparation evade the uniform-control bound?

**Understanding target:** Explain how the cyclic-shift Kraus construction turns the uniform-controller output into the output of any fixed preparation, including a retained entangled ancilla. Check the trace-preserving normalization and the two required images of the controller states.

**Dependencies and story role:** M02, M08–M09, M13–M15. Extend a calculation for one preparation to an operational dominance statement.

**Conceptual connection:** The simulation is a deterministic receiver channel, so antidegradability and its capacity consequences pass to every allowed preparation.

**Source pointers:** Wilde §§4.4, 13.5 for channels and antidegradability; [channel model, Proposition 1 in §4](../science/channel_model.md#4-uniform-control-dominates-every-independent-preparation).

### M17 — Correlations across prepared controllers

**Phase:** Narrative/innovation.

**Central question:** Why does the dominance result survive joint controller preparations across many devices?

**Understanding target:** Use simultaneous shifts of the order-label strings to construct a single receiver map for an arbitrary correlated preparation. Distinguish entanglement among preparation registers from correlations with the encoded target/reference input or among physical noise environments.

**Dependencies and story role:** M07–M09, M14, M16. Close the gap between a single-device result and the full allowed block model.

**Conceptual connection:** Equality of linear maps on entangled payloads is stronger than checking a product input or tensoring a single-preparation argument without proof.

**Source pointers:** Wilde §§4.4, 24.1 for channels and block transmission; [channel model, Proposition 2 in §5](../science/channel_model.md#5-correlated-controllers-across-a-block).

### M18 — Competing Bell correlations

**Phase:** Narrative/innovation.

**Central question:** How much Bell overlap can one receiver have if the other receiver has none?

**Understanding target:** Derive the overlap identities for the two Bell projectors and distinguish the unrestricted symmetric overlap bound from the constrained bound $`1-d^{-2}`$. Explain why the latter is at least the former for every $`d\ge2`$.

**Dependencies and story role:** M10–M11, M15. Isolate the geometric ingredient needed for a witness covering every allocation of flags.

**Conceptual connection:** The project applies established isotropic-compatibility geometry to its particular good and bad Choi weights.

**Source pointers:** Wilde §§3.6, 4.3 for entangled-state foundations; the calculation and research attribution are in [ideal boundary, §3](../science/ideal_boundary.md#3-two-bell-projectors).

### M19 — The witness for every flagged extension

**Phase:** Narrative/innovation.

**Central question:** How can a necessary bound cover all possible extensions rather than one chosen construction?

**Understanding target:** Dephase the two output flags without altering their marginals, use positivity to enforce the zero-Bell support of the bad sector, and combine the sector bounds. Obtain the inequality $`1/d^2\le(1-d^{-2})p_0`$ without assuming the eventual sufficiency construction.

**Dependencies and story role:** M10, M15, M18. Turn the Bell geometry into a universal obstruction.

**Conceptual connection:** Substituting the actual good-flag probability yields the necessary ideal boundary $`N\le(d^2-1)^2`$.

**Source pointers:** Wilde §4.4 for positive-operator foundations; [ideal boundary, §4](../science/ideal_boundary.md#4-necessity-a-witness-for-every-flagged-extension).

### M20 — A positive extension at the endpoint

**Phase:** Narrative/innovation.

**Central question:** What construction saturates the ideal witness with the correct quantum marginals?

**Understanding target:** Explain the cross-flag state built from a compressed Bell projector and the both-bad state built from the common kernel. Check positivity, normalization, swap symmetry, and both flagged marginals when their weights are assembled at $`N=(d^2-1)^2`$.

**Dependencies and story role:** M10–M11, M18–M19. Supply attainability to complement the necessary witness.

**Conceptual connection:** The extension allocates good outcomes between the two receiver copies; it does not clone the accepted quantum state at both outputs.

**Source pointers:** Wilde §§4.3–4.4 for states and channels; [ideal boundary, §5](../science/ideal_boundary.md#5-sufficiency-explicit-extension-at-the-endpoint).

### M21 — Interpolation and the exact ideal classification

**Phase:** Narrative/innovation.

**Central question:** Why does the endpoint construction establish every smaller integer order count?

**Understanding target:** Use the affine dependence on $`1/N`$ to interpolate between the one-slot channel and the endpoint extension. Combine this positive construction with the universal witness to state the exact antidegradability classification of uniform control.

**Dependencies and story role:** M09, M15, M19–M20. Join the ideal proof's necessary and sufficient directions.

**Conceptual connection:** The uniform channel is non-antidegradable above the boundary, while other preparations and positive capacity require their own claims.

**Source pointers:** Wilde §§4.4, 13.5 as channel foundations; [ideal boundary, §§1 and 6](../science/ideal_boundary.md#6-explicit-extension-for-every-smaller-integer).

### M22 — The gain from retaining both flags in the proof

**Phase:** Narrative/innovation.

**Central question:** What does the complete-channel argument establish beyond testing the conditional branches separately?

**Understanding target:** Compare the sufficient bound $`(d+1)^2`$ from separate branches with the exact boundary $`(d^2-1)^2`$. Explain their coincidence for qubits and their separation for larger dimensions, together with the endpoint's accepted fidelity, success probability, and raw-slot cost.

**Dependencies and story role:** M05, M12, M15, M21. Interpret the ideal theorem quantitatively rather than only algebraically.

**Conceptual connection:** A faithful accepted branch can coexist with a shareable complete output, and increasing fidelity can entail rarer acceptance and more underlying calls.

**Source pointers:** Wilde §§9.5, 24.1 for fidelity and rate concepts; [ideal boundary, §§7.2–7.3](../science/ideal_boundary.md#72-accuracy-of-the-successful-branch-at-the-endpoint) and [communication consequences, §2](../science/operational_consequences.md#2-exact-boundary-and-a-useful-baseline).

### M23 — Physical dephasing and an inaccessible record

**Phase:** Narrative/innovation.

**Central question:** Which loss of order coherence is strong enough to support the noise theorem?

**Understanding target:** Specify the channel $`\mathcal D_v=v\,\mathrm{id}+(1-v)\Delta_C`$, its location, and the inaccessibility of its environment. Explain the example in which a retained phase label permits correction despite a low-visibility reduced controller state.

**Dependencies and story role:** M06, M12–M14, M17. Introduce the noisy model while keeping operationally different kinds of lost coherence separate.

**Conceptual connection:** A channel acting before traversal can be moved after traversal here because the controlled Kraus operators commute with the relevant diagonal phases.

**Source pointers:** Wilde §§4.7, 5.2 for noise and environments; [unobserved dephasing, §1](../science/unobserved_dephasing.md#1-physical-channel-and-noise-placement).

### M24 — A limit on a fixed output space

**Phase:** Narrative/innovation.

**Central question:** How can increasing the order-register dimension yield a well-defined limiting channel?

**Understanding target:** Compress the noisy uniform-controller output to the same two flags for every $`N`$. Derive its affine relation to the limiting channel and the one-slot flagged depolarizer, and interpret the diamond-norm bound $`2/N`$ without postulating a finite-cost infinite-order device.

**Dependencies and story role:** M03–M04, M15, M23. Set up a limit that can prove exact statements about finite devices.

**Conceptual connection:** The limit has a pure good Choi block, which changes the extension argument from the ideal finite-order case.

**Source pointers:** Wilde §§4.4, 9.5 for channels and their comparison; [unobserved dephasing, §§2–3](../science/unobserved_dephasing.md#3-fixed-dimensional-limit-and-affine-identity).

### M25 — Purity fixes the noisy extension's cross sectors

**Phase:** Narrative/innovation.

**Central question:** Why does a pure successful marginal force a residual-positivity test?

**Understanding target:** Use rank-one marginal factorization to exclude simultaneous good outputs and fix the two cross sectors after covariance averaging. Subtract their contribution from the bad marginal and derive $`v\le d^2/(d^2+1)`$ from the residual's Bell-direction eigenvalue.

**Dependencies and story role:** M01, M10–M11, M20, M24. Establish the necessary noisy limiting threshold.

**Conceptual connection:** The inherited pure-marginal mechanism restricts the extension, but its quantum residual still requires a sufficiency proof.

**Source pointers:** Wilde §§4.3, 5.1 for marginal and purification foundations; [unobserved dephasing, §4, necessity](../science/unobserved_dephasing.md#necessity-a-pure-successful-marginal-fixes-the-cross-sectors).

### M26 — Sharing the residual completes the noisy proof

**Phase:** Narrative/innovation.

**Central question:** Why is the necessary residual condition also sufficient in this model?

**Understanding target:** Decompose the residual into nonnegative multiples of a product state and a separable isotropic state. Extend the latter through its product-state representation and combine the residual with the fixed cross sectors to recover both full marginals.

**Dependencies and story role:** M10–M11, M25. Complete the exact limiting antidegradability equivalence.

**Conceptual connection:** Positivity alone does not generally prove shareability; the supplied separable decomposition is the additional step for this quantum bad branch.

**Source pointers:** Wilde §§3.6, 4.3 for entanglement foundations; [unobserved dephasing, §4, sufficiency](../science/unobserved_dephasing.md#sufficiency-the-residual-is-separable-and-can-be-shared).

### M27 — Transfer to every finite device and allowed preparation

**Phase:** Narrative/innovation.

**Central question:** How does a theorem about the limiting uniform channel constrain every finite device?

**Understanding target:** Combine convexity of symmetric-extension feasibility with the exact affine identity. Explain the completely positive flag-conditioned controller map and its tensorization for arbitrary fixed joint preparations independent of the payload, with independent physical dephasing environments.

**Dependencies and story role:** M09–M10, M16–M17, M24, M26. Transfer the limiting obstruction to the full noisy communication model.

**Conceptual connection:** Every finite $`N`$ is antidegradable below the visibility ceiling. Above it, closedness and convergence imply eventual non-antidegradability, not a positive-capacity theorem or a full finite-$`N`$ boundary.

**Source pointers:** Wilde §§4.4, 13.5 for channels and antidegradability; [unobserved dephasing, §§5–6](../science/unobserved_dephasing.md#5-every-finite-number-of-orders-below-the-same-visibility).

### M28 — Accurate qubit transmission with zero unassisted rate

**Phase:** Narrative/innovation.

**Central question:** What happens when the accepted branch improves at a fixed nonzero dephasing level?

**Understanding target:** Derive the acceptance probability and both accepted fidelities, and evaluate the qubit example at $`v=4/5`$ and $`N=1000`$. Explain why their fixed-dimension limit requires $`v>0`$, and why a nonzero limiting acceptance probability does not give a constant accepted yield per raw slot.

**Dependencies and story role:** M05, M12, M24, M27. Connect the exact proof to a concrete performance comparison.

**Conceptual connection:** High accepted entanglement fidelity and $`Q=P=0`$ describe different aspects of the same complete channel, with all unsuccessful invocations counted.

**Source pointers:** Wilde §§9.5.2, 23.1, 24.1; [unobserved dephasing, §8](../science/unobserved_dephasing.md#8-high-accepted-fidelity-at-nonvanishing-success-probability) and [communication consequences, §§3 and 5](../science/operational_consequences.md#3-fixed-dimension-accuracy-with-zero-capacity).

### M29 — Arbitrary coding, privacy, and assistance

**Phase:** Narrative/innovation.

**Central question:** Which communication conclusions survive the most general coding allowed here?

**Understanding target:** Apply the environmental simulation to arbitrary block encodings and joint receiver decoders, including the allowed controller correlations. Explain why standard private capacity gives Eve the complete complement, and why feedback-assisted or trusted-noise tasks require different statements.

**Dependencies and story role:** M06–M09, M12, M17, M21, M27–M28. Integrate both antidegradability results into their operational consequences.

**Conceptual connection:** The original heralded and two-way-assisted cyclic-order results remain compatible with the zero-unassisted-capacity regimes proved here.

**Source pointers:** Wilde §§13.5–13.6, 23.1–23.2, 24.1–24.3; [unobserved dephasing, §7](../science/unobserved_dephasing.md#7-environment-simulation-and-the-capacity-consequence) and [communication consequences, §§1 and 4](../science/operational_consequences.md#4-heralding-and-classical-feedback).

### M30 — The complete contribution and its boundaries

**Phase:** Narrative/innovation.

**Central question:** What has been established, how is it supported, and what remains outside the result?

**Understanding target:** Connect the physical cyclic model, lossless flags, controller dominance, ideal boundary, and specified dephasing obstruction in one account. Identify inherited channel and Bell-geometry ingredients, distinguish analytic proofs from finite numerical checks, and preserve the unresolved capacity question above the antidegradable regimes.

**Dependencies and story role:** M13–M29. Complete the local-to-global narrative by explaining the scientific consequence together with its assumptions and costs.

**Conceptual connection:** The contribution is an operational classification of this cyclic architecture; it neither determines arbitrary coherent-order channels nor claims a hardware advantage or a new general monogamy principle.

**Source pointers:** Wilde §§23.1–23.2 and §§24.1–24.3 for the capacity tasks; [communication consequences](../science/operational_consequences.md), [related work](../references/RELATED_WORK.md), and [verification guide](../verification/README.md).

## Read the proofs directly

The map points into four authoritative scientific pages: [the channel and controller model](../science/channel_model.md), [the exact ideal boundary](../science/ideal_boundary.md), [unobserved dephasing](../science/unobserved_dephasing.md), and [communication consequences and resources](../science/operational_consequences.md). The [anchor and bridge](ANCHOR_AND_BRIDGE.md) connects the selected source to these pages. The [repository entrypoint](../README.md) supplies the result overview and reproduction route.
