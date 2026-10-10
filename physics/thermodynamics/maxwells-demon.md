---
title: "Maxwell's Demon"
author: Cesare Peli
description: "Maxwell’s demon, statistical entropy and memory erasure: what the second law requires when measurement and feedback are included."
permalink: /physics/thermodynamics/maxwells-demon/
redirect_from:
  - /odd-questions/maxwells-demon/
date: 2025-11-07
keywords: [Maxwell's demon, entropy, second law of thermodynamics, information theory, statistical mechanics, Boltzmann, Gibbs, Shannon, Landauer, irreversibility, physics paradox, thermodynamics thought experiment]
area: physics
topic: thermodynamics
content_type: article
background_image: "/images/demon.png"
image_alt: "Illustration of Maxwell's demon observing gas molecules through a tiny door"
layout: default
last_modified_at: 2026-10-10
---

<div class="content-box">

# Maxwell’s Demon

*By Cesare Peli.*

## A Temperature Difference without Work?

Hot water cools in a colder room. The reverse process is compatible with energy conservation, but it does not occur spontaneously on the macroscopic scale. The second law supplies the additional restriction: the entropy of an isolated system does not decrease in a macroscopic process. In the Clausius formulation, heat cannot pass from a colder body to a hotter one without some accompanying change. A refrigerator does transfer heat in that direction, but requires work.

Maxwell’s thought experiment asks whether molecular information could evade this restriction. Imagine two gas chambers connected by a small door. An observer lets unusually fast molecules pass from A to B and unusually slow molecules pass from B to A. If the sorting worked without any other change, it could produce a temperature difference from an initially equilibrated gas. That difference could then be used to extract work.

Temperature is a property of an equilibrium state, not of an individual molecule. For a classical ideal gas in three dimensions, its relation to mean translational kinetic energy is

$$
\langle K_{\mathrm{trans}}\rangle=\frac32 k_B T.
$$

This relation explains the proposed sorting. It is not a universal definition of temperature for every physical system.

</div>

<div class="content-box">

## Macrostates and Statistical Entropy

A macrostate specifies a limited set of observable quantities. Many microscopic configurations are compatible with it. In a discrete description, Boltzmann’s entropy is

$$
S_B=k_B\ln W,
$$

where W counts compatible microstates with the relevant constraints fixed. For a classical gas, positions and momenta form a continuous phase space; a corresponding coarse-grained phase-space volume replaces a literal finite count.

Consider a gas initially confined to half an insulated container. After the partition is removed, states with molecules distributed throughout the container occupy a much larger part of the accessible phase space than states with all molecules in the original half. Under suitable initial conditions, typical microscopic evolutions therefore lead to the equilibrium macrostate. This statistical explanation concerns macroscopic behavior and allows fluctuations; it does not make every microscopic trajectory irreversible.

The time-reversal symmetry of an isolated classical Hamiltonian model does not imply that a prepared gas will visibly retrace its evolution. Reversing a trajectory would require reversing the appropriate microscopic momenta, not simply waiting.

Chemical changes such as cooking, or the mixing of real paints, require additional information about composition and interactions. Their irreversibility cannot be established by asserting, without a model, that the final material has more microstates.

Gibbs’ ensemble entropy is

$$
S_G=-k_B\sum_i P_i\ln P_i.
$$

For W equally probable discrete states, it equals k_B ln W. The distinction between this probability description and a macrostate description matters: fine-grained Gibbs entropy is conserved by isolated Hamiltonian evolution. Macroscopic entropy increase requires attention to preparation, coarse graining, or interaction with an environment; it does not follow merely by writing the Gibbs formula.

</div>

<div class="content-box">

## Information, Feedback and a Complete Cycle

The observer’s information is correlated with the gas. Selecting molecules on that basis is a form of feedback. A thermodynamic analysis must include the gas, the memory, the mechanism controlling the door, and any reservoirs with which they interact.

Shannon entropy measures uncertainty in a probability distribution:

$$
H=-\sum_i P_i\log_2 P_i.
$$

For independent binary records with outcome probabilities p and 1−p,

$$
H(p)=-p\log_2 p-(1-p)\log_2(1-p).
$$

For long strings of such records, optimal lossless coding approaches H(p) bits per record on average. This is an asymptotic coding statement, not a claim that each physical decision occupies exactly H(p) bits. Correlations and accessible side information can change the amount of information that must be reset.

Measurement need not itself incur a universal dissipation of k_B T ln 2. Bennett showed why measurement can, in principle, be implemented reversibly. Resetting a reusable memory is a distinct operation: after a complete cycle, the memory must return to its original state rather than retain the record of all previous cycles.

</div>

<div class="content-box">

## What Landauer’s Bound Says

In the standard idealized erasure process, an initially equiprobable classical bit is reset to a fixed logical state while coupled to a reservoir at temperature T. If the two logical states have equal free energies, the mean heat delivered to the reservoir obeys

$$
\langle Q_{\mathrm{bath}}\rangle\ge k_B T\ln 2.
$$

The bound can be approached in a reversible limit. It is not a universal heat cost for every measurement, calculation, or manipulation of a bit. Unequal initial probabilities, different logical-state free energies, correlations with other systems, and additional resources require a more general thermodynamic balance.

For N independent binary records, under the same assumptions and with no usable side information, the entropy removed from the memory is N k_B ln 2 H(p). Resetting it requires at least that much entropy to be transferred elsewhere. Feedback may lower the gas entropy, but that decrease cannot be considered separately from the resources and correlations used by the controller. Over a complete cycle, the total entropy production is nonnegative; it need not be strictly positive in an ideal reversible limit.

The conclusion concerns a complete process. A device that has sorted molecules but has not restored its memory and other resources has not completed the proposed cycle.

</div>

<div class="content-box">

## Equipartition and Its Limits

In classical equilibrium statistical mechanics, each independent quadratic term in the energy contributes k_B T/2 to the mean energy. A three-dimensional translational motion has three such terms. A harmonic vibrational mode has both a kinetic and a potential quadratic term and contributes k_B T in the classical limit.

When thermal energy is small relative to the spacing of quantum energy levels, classical equipartition no longer describes that mode. Rotational and vibrational contributions to a gas’s heat capacity can consequently become small at low temperatures. This qualification is needed when relating molecular motion, temperature and the ratio of heat capacities.

## References

- J. C. Maxwell, *Theory of Heat* (1871), chapter XXII.
- J. W. Gibbs, *Elementary Principles in Statistical Mechanics* (1902).
- C. E. Shannon, “A Mathematical Theory of Communication”, *Bell System Technical Journal* 27 (1948), 379–423 and 623–656.
- R. Landauer, [“Irreversibility and Heat Generation in the Computing Process”](https://doi.org/10.1147/rd.53.0183), *IBM Journal of Research and Development* 5 (1961), 183–191.
- C. H. Bennett, [“The Thermodynamics of Computation—a Review”](https://doi.org/10.1007/BF02084158), *International Journal of Theoretical Physics* 21 (1982), 905–940.
- T. Sagawa and M. Ueda, [“Generalized Jarzynski Equality under Nonequilibrium Feedback Control”](https://arxiv.org/abs/0907.4914), *Physical Review Letters* 104 (2010), 090602.
- F. Reif, *Fundamentals of Statistical and Thermal Physics* (1965).

[← Back to Thermodynamics]({{ "/physics/thermodynamics/" | relative_url }})

</div>
