---
title: "Maxwell's Demon"
description: "From cooked pizzas to information entropy: Maxwell’s demon and the deep link between thermodynamics, probability, and the arrow of time."
permalink: /odd/maxwells-demon/
date: 2025-11-07
keywords: [Maxwell's demon, entropy, second law of thermodynamics, information theory, statistical mechanics, Boltzmann, Gibbs, Shannon, Landauer, irreversibility, physics paradox, thermodynamics thought experiment]
section: "Odd"
background: /images/demon.png
image_alt: "Illustration of Maxwell's demon observing gas molecules through a tiny door"
---



<div class="content-box">

### Why doesn’t a cooked pizza become raw again?
Why doesn’t a can of green paint separate back into yellow and blue?  
Why doesn’t the bathwater, after giving heat to the air and the tiles, start warming itself again?

These questions lead to the **Second Law of Thermodynamics**: in the processes we observe, heat redistributes, differences fade, and the energy available to do work decreases.  
Kelvin phrased it as the impossibility of a cyclic engine producing work when interacting with a single thermal reservoir.  
Clausius expressed it more succinctly: *heat does not spontaneously flow from a colder body to a hotter one*.  
But why?

---

### From molecules to statistics: Maxwell’s insight

In *Illustration of the Dynamical Theory of Gases* (1860), **James Clerk Maxwell** described a gas as a huge ensemble of particles whose velocities follow a statistical law.  
Temperature does not describe a single molecule; it represents the *average kinetic energy* of all particles.

This leads to his famous 1871 thought experiment (*Theory of Heat*).  
Imagine two identical chambers, **A** and **B**, connected by a tiny door.  
A perfect observer — the *demon* — can measure the velocity of each molecule and applies a rule:

- let fast molecules from A pass to B;  
- let slow molecules from B pass to A.

Since temperature depends on average kinetic energy, region **B** heats up and **A** cools down — seemingly creating a temperature difference without work.  
The experiment illustrates that **the arrow of time is not in the mechanical equations**, but in the *collective behavior* of many particles.

---

### Boltzmann: order, multiplicity, and entropy

**Ludwig Boltzmann** made the “collective” explicit.  
Each measurable state — a *macrostate* with a given pressure, volume, temperature — corresponds to countless *microstates* of positions and velocities.  
Entropy measures the size of this multiplicity:

$$
S = k_B \ln W
$$

where *W* is the number of microstates compatible with the macrostate.

States representing **mixing, diffusion, and thermal equilibrium** occupy enormous regions of phase space;  
states representing **separation and reconstruction** occupy tiny ones.  
A system evolves naturally toward the larger regions of its possibilities.  

That’s why:
- the “cooked pizza” macrostate vastly outnumbers the “raw pizza” one;  
- mixed paint corresponds to more microstates than separated pigments;  
- heat dispersed into the room almost never reconcentrates spontaneously.

---

### Gibbs and the probability of states

**Josiah Willard Gibbs** connected entropy with probabilities:

$$
S = -k_B \sum_i P_i \ln P_i
$$

If all microstates are equally likely (*Pₖ = 1/W*), the formula reduces to Boltzmann’s.  
This clarifies a key point: when differences fade, energy has not disappeared — it is merely **redistributed** among configurations that, for the vast majority, **cannot yield usable work** under the current conditions.

---

### The demon meets information theory

At first glance, Maxwell’s demon seems to escape the Second Law by continuously selecting rare microstates.  
But to operate, the demon must *measure*, *decide*, and *store* information.  
Replacing it with a robot clarifies the cost:  
each “open/close” decision requires sensing, classification, and memory.

Here enters **Claude Shannon**.  
The informational entropy of a source measures the average number of bits required to encode its outcomes:

$$
H = -\sum_i P_i \log_2 P_i
$$

If the demon’s gate decisions are binary with probabilities *p* and *1−p*, each decision processes *H(p)* bits on average.  
Over *N* events, at least *N H(p)* bits must eventually be erased to keep the device cyclic.

---

### Landauer’s principle: the cost of erasure

**Rolf Landauer** (1961) established that erasing one bit of information in any physical system has a minimum thermal cost:

$$
Q_{\text{min}} = k_B T \ln 2 \text{ per bit.}
$$

Erasing *N H(p)* bits dissipates at least *k_B T ln 2 × N H(p)* of heat.  
Hence, when the demon resets its memory, the total entropy of the combined system — gas, robot, and environment — **increases**.  

The paradox dissolves not through prohibition, but through **a complete accounting that includes information**.

---

### Classical limits and quantum corrections

Microscopic theory provides two classical results:

- temperature is proportional to the *mean kinetic energy*;  
- the **equipartition theorem** assigns an average energy  
  $$ \bar{ϵ_i} = \tfrac{1}{2} k_B T $$  
  to each active degree of freedom.

However, classical mechanics failed to predict the correct ratio of specific heats,  
$$ \gamma = c_p / c_V, $$
for many gases.  
**Quantum mechanics** resolved this by showing that rotational and vibrational degrees of freedom can be *inactive* at low temperatures.

---

### The complete picture

The **Second Law** describes the direction of processes in systems with many degrees of freedom because *most microstates correspond to mixed and redistributed configurations*.  
Entropy measures the actual breadth of those possibilities.  

Maxwell’s thought experiment shows where reversal might be attempted: *selection*.  
Shannon quantifies the information required to maintain it;  
Landauer ties that information to a **thermal cost**.  

Thus the pizza doesn’t uncook, the paint doesn’t separate, and the bathwater doesn’t heat itself —  
not because the reverse is logically forbidden,  
but because it occupies a microscopic corner of configuration space,  
and the information required to sustain it *is part of the world’s energy bookkeeping*.

---

### Essential References

- **J. C. Maxwell**, *Illustration of the Dynamical Theory of Gases* (1860); *Theory of Heat* (1871).  
- **L. Boltzmann**, *Vorlesungen über Gastheorie* (1896–1898).  
- **J. W. Gibbs**, *Elementary Principles in Statistical Mechanics* (1902).  
- **C. E. Shannon**, “A Mathematical Theory of Communication”, *Bell System Technical Journal* (1948).  
- **R. Landauer**, “Irreversibility and Heat Generation in the Computing Process”, *IBM Journal of Research and Development* (1961).  
- **F. Reif**, *Fundamentals of Statistical and Thermal Physics* (1965/1985).  
- **A. Bettini**, *Meccanica e Termodinamica* (1995).  
- **L. Geymonat (ed.)**, *Storia del pensiero filosofico e scientifico* (1970).  
- **M. Schwartz**, *Statistical Mechanics* (lecture notes, 2019).

</div>
