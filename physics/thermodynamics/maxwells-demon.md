---
title: "Maxwell's Demon"
author: Cesare Peli
description: "Maxwell’s demon explained through everyday irreversibility, statistical entropy, information and the thermodynamic cost of memory erasure."
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


# Maxwell’s Demon

<div class="content-box">

*By Cesare Peli.*

## Why doesn’t a cooked pizza become raw again?

Why doesn’t a can of green paint separate back into yellow and blue?

Why doesn’t the bathwater, after giving heat to the air and the tiles, start warming itself again?

These questions lead to the **Second Law of Thermodynamics**: in the processes we observe, heat redistributes, differences fade, and the energy available to do work decreases.  
Kelvin phrased it as the impossibility of a cyclic engine producing work when interacting with a single thermal reservoir.  
Clausius expressed it more succinctly: *heat does not spontaneously flow from a colder body to a hotter one*.  
But why?

</div>

<div class="content-box">

## From molecules to statistics: Maxwell’s insight

In *Illustration of the Dynamical Theory of Gases* (1860), **James Clerk Maxwell** described a gas as a huge ensemble of particles whose velocities follow a statistical law.  
Temperature does not describe a single molecule. For a classical ideal gas, it is proportional to the *mean translational kinetic energy* of its particles.

This leads to his famous 1871 thought experiment (*Theory of Heat*).  
Imagine two identical chambers, **A** and **B**, connected by a tiny door.  
A perfect observer — the *demon* — can measure the velocity of each molecule and applies a rule:

- let fast molecules from A pass to B;  
- let slow molecules from B pass to A.

For the gas in this model, since temperature depends on mean translational kinetic energy, region **B** heats up and **A** cools down — seemingly creating a temperature difference without work.  
The experiment illustrates that **the macroscopic arrow of time is not in the time-reversible mechanical equations of this model**, but in the *collective behavior* of many particles.

</div>

<div class="content-box">

## Boltzmann: order, multiplicity, and entropy

**Ludwig Boltzmann** made the “collective” explicit.  
Each measurable state — a *macrostate* with a given pressure, volume, temperature — corresponds to countless *microstates* of positions and velocities.  
Entropy measures the size of this multiplicity:

$$
S = k_B \ln W
$$

where *W* is the number of microstates compatible with the macrostate.

States representing **mixing, diffusion, and thermal equilibrium** occupy enormous regions of phase space;  
states representing **separation and reconstruction** occupy tiny ones.  
For a gas prepared away from equilibrium, evolution toward the larger regions of its possibilities is overwhelmingly more probable than the reverse.  

This explains why a gas spreads through an available volume and why heat dispersed into a room almost never reconcentrates spontaneously.

Cooking and the mixing of real paints also involve changes in chemical composition and material structure. They illustrate macroscopic irreversibility, but cannot be explained by simply counting “cooked” and “raw” microstates.

</div>

<div class="content-box">

## Gibbs and the probability of states

**Josiah Willard Gibbs** connected entropy with probabilities:

$$
S = -k_B \sum_i P_i \ln P_i
$$

If all microstates are equally likely (*Pₖ = 1/W*), the formula reduces to Boltzmann’s.  
This clarifies a key point: when differences fade, energy has not disappeared — it is merely **redistributed** among configurations that, for the vast majority, **cannot yield usable work** under the current conditions.

</div>

<div class="content-box">

## The demon meets information theory

At first glance, Maxwell’s demon seems to escape the Second Law by continuously selecting rare microstates.  
But to operate, the demon must *measure*, *decide*, and *store* information.  
Replacing it with a robot clarifies the cost:  
each “open/close” decision requires sensing, classification, and memory.

Here enters **Claude Shannon**.  
The informational entropy of a discrete source sets the minimum average number of bits per outcome approached by lossless coding of long sequences:

$$
H = -\sum_i P_i \log_2 P_i
$$

If the demon’s gate decisions are independent and binary, with probabilities p and 1−p, their entropy per decision is:

$$
\begin{aligned}
H(p)={}&-p\log_2 p\\
&-(1-p)\log_2(1-p).
\end{aligned}
$$

Over N events, the record contains N H(p) bits of information. To keep the device cyclic, its memory must be reset. The erasure cost below assumes that no usable copy of the record or other correlated information remains available.

</div>

<div class="content-box">

## Landauer’s principle: the cost of erasure

**Rolf Landauer** (1961) established the thermodynamic cost of erasure. For an initially equiprobable bit, stored in logical states of equal free energy and reset in contact with a reservoir at temperature T, the minimum heat delivered to the reservoir is:

$$
Q_{\min}=k_B T\ln 2.
$$

For the independent binary record described above, the minimum heat is:

$$
Q_{\min}=N k_B T\ln 2\,H(p).
$$

Measurement itself can, in principle, be reversible, as **Charles Bennett** clarified. The essential distinction is between acquiring a record and resetting the memory so that the device can repeat its cycle.

When the complete cycle includes the gas, robot, memory and environment, their total entropy **does not decrease**. It increases in an irreversible cycle and can remain unchanged in the ideal reversible limit.  

The paradox dissolves not through prohibition, but through **a complete accounting that includes information**.

</div>

<div class="content-box">

## Classical limits and quantum corrections

Microscopic theory connects temperature with molecular energy.

For a classical ideal gas, temperature is proportional to the *mean translational kinetic energy*.

The **equipartition theorem** assigns an average energy to each independent quadratic term in the energy:

$$
\langle E_i\rangle=\frac{1}{2}k_B T.
$$

A translational degree of freedom has one such term. A harmonic vibrational mode has two, one kinetic and one potential.

However, classical mechanics failed to predict the correct ratio of specific heats for many gases:

$$
\gamma=\frac{c_p}{c_V}.
$$
  
**Quantum mechanics** resolved this by showing that rotational and vibrational degrees of freedom can be *inactive* at low temperatures.

</div>

<div class="content-box">

## The complete picture

The **Second Law** describes the direction of processes in systems with many degrees of freedom because *most microstates correspond to mixed and redistributed configurations*.  
Entropy measures the actual breadth of those possibilities.  

Maxwell’s thought experiment shows where reversal might be attempted: *selection*.  
Shannon quantifies the information required to maintain it;  
Landauer ties that information to a **thermal cost**.  

Thus the pizza doesn’t uncook, the paint doesn’t separate, and the bathwater doesn’t heat itself: these are examples of macroscopic irreversibility. For a gas, statistical mechanics explains why a spontaneous return to a specially prepared state is extraordinarily improbable.

The demon asks a further question: can information be used to produce that return? A complete answer includes the memory and its reset. The information required to sustain the operation *is part of the world’s energy bookkeeping*.

</div>

<div class="content-box">

## Essential References

- **J. C. Maxwell**, *Illustration of the Dynamical Theory of Gases* (1860); *Theory of Heat* (1871).  
- **L. Boltzmann**, *Vorlesungen über Gastheorie* (1896–1898).  
- **J. W. Gibbs**, *Elementary Principles in Statistical Mechanics* (1902).  
- **C. E. Shannon**, “A Mathematical Theory of Communication”, *Bell System Technical Journal* (1948).  
- **R. Landauer**, [“Irreversibility and Heat Generation in the Computing Process”](https://doi.org/10.1147/rd.53.0183), *IBM Journal of Research and Development* (1961).
- **C. H. Bennett**, [“The Thermodynamics of Computation—a Review”](https://doi.org/10.1007/BF02084158), *International Journal of Theoretical Physics* 21 (1982), 905–940.  
- **F. Reif**, *Fundamentals of Statistical and Thermal Physics* (1965/1985).  
- **A. Bettini**, *Meccanica e Termodinamica* (1995).  
- **L. Geymonat (ed.)**, *Storia del pensiero filosofico e scientifico* (1970).  
- **M. Schwartz**, *Statistical Mechanics* (lecture notes, 2019).

</div>

[← Back to Thermodynamics]({{ '/physics/thermodynamics/' | relative_url }})

