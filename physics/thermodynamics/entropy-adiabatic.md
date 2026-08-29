---
layout: default
date: 2026-08-29
title: "Is Entropy Constant in an Adiabatic Process?"
author: Cesare Peli
permalink: /physics/thermodynamics/entropy-adiabatic/
redirect_from:
  - /university/physics/thermodynamics/entropy-adiabatic/
background_image: "/images/termodinamica.png"
description: "Entropy is constant only in a reversible adiabatic process. Learn why irreversible adiabatic processes increase entropy, with a worked ideal-gas example."
area: physics
topic: thermodynamics
content_type: solved-exercise
---

# Is Entropy Constant in an Adiabatic Process?

An adiabatic process has $q=0$, but this does not necessarily imply that $\Delta S=0$.

Entropy remains constant only when the adiabatic process is **reversible**. In an irreversible adiabatic process, entropy is produced and the entropy of an isolated system increases.

<div class="content-box">

## Entropy in Reversible and Irreversible Adiabatic Processes

An **adiabatic process** is a transformation in which no heat is exchanged with the surroundings:

$$
q=0.
$$

From the First Law of Thermodynamics,

$$
\Delta U=q+w,
$$

and therefore, for an adiabatic process,

$$
\Delta U=w.
$$

The absence of heat exchange does not by itself determine the entropy change:

- **Reversible adiabatic process:** $\Delta S_{\text{sys}}=0$.
- **Irreversible adiabatic process:** $\Delta S_{\text{sys}}>0$ for an isolated system.
- **Entropy change of the universe:**

  $$
  \Delta S_{\text{univ}}
  =
  \Delta S_{\text{sys}}
  +
  \Delta S_{\text{surr}}.
  $$

For a reversible process,

$$
\Delta S_{\text{univ}}=0,
$$

whereas an irreversible process produces entropy:

$$
\Delta S_{\text{univ}}>0.
$$

> **Important distinction.**  
> The entropy change of the system is calculated by comparing its initial and final equilibrium states, even when the actual transformation is irreversible. The entropy change of the universe indicates whether the transformation is reversible or irreversible.

</div>

<div class="content-box">

## Worked Example

One mole of ideal gas expands adiabatically from

$$
V_1=10.0\,\text{L}
$$

to

$$
V_2=20.0\,\text{L}.
$$

We will determine:

1. the entropy change in a **reversible adiabatic expansion**;
2. the entropy change in an **irreversible adiabatic free expansion**;
3. the entropy change of the universe in both cases.

</div>

<div class="content-box">

## Reversible Adiabatic Expansion

For a reversible transformation, the entropy change is defined by

$$
\Delta S_{\text{sys}}
=
\int\frac{\delta q_{\text{rev}}}{T}.
$$

Since the process is both reversible and adiabatic,

$$
\delta q_{\text{rev}}=0,
$$

and therefore

$$
\Delta S_{\text{sys}}=0.
$$

No heat is transferred to the surroundings, so

$$
\Delta S_{\text{surr}}=0.
$$

Consequently,

$$
\Delta S_{\text{univ}}=0.
$$

A reversible adiabatic process is therefore also called an **isentropic process**.

</div>

<div class="content-box">

## Irreversible Adiabatic Free Expansion

Suppose that the gas expands freely into a vacuum.

The process is adiabatic:

$$
q=0.
$$

Since the gas expands against zero external pressure, no work is performed:

$$
w=0.
$$

It follows that

$$
\Delta U=0.
$$

For an ideal gas, internal energy depends only on temperature. Therefore,

$$
\Delta T=0.
$$

The entropy change of one mole of ideal gas between the initial and final equilibrium states is

$$
\Delta S_{\text{sys}}
=
R\ln\left(\frac{V_2}{V_1}\right).
$$

Substituting the given volumes,

$$
\Delta S_{\text{sys}}
=
8.314\ln\left(\frac{20.0}{10.0}\right)
=
8.314\ln 2.
$$

Thus,

$$
\Delta S_{\text{sys}}
=
5.76\,\text{J K}^{-1}.
$$

No heat is exchanged with the surroundings, so

$$
\Delta S_{\text{surr}}=0.
$$

Therefore,

$$
\Delta S_{\text{univ}}
=
5.76\,\text{J K}^{-1}.
$$

The transformation is adiabatic, but its entropy increases because the process is irreversible.

</div>

<div class="content-box">

## Why Can Entropy Increase When $q=0$?

The relation

$$
dS=\frac{\delta q_{\text{rev}}}{T}
$$

refers to a **reversible path** connecting two equilibrium states.

In a reversible adiabatic process, the actual path is reversible and $\delta q_{\text{rev}}=0$, so the entropy remains constant.

During an irreversible free expansion, the actual process cannot be used directly in the integral that defines entropy change. A hypothetical reversible path must be considered between the same initial and final equilibrium states. Along that path, the entropy change is

$$
\Delta S_{\text{sys}}
=
R\ln\left(\frac{V_2}{V_1}\right)>0.
$$

Thus, $q=0$ does not imply $\Delta S=0$. It implies constant entropy only when the adiabatic transformation is also reversible.

</div>

<div class="content-box">

## Results

For the reversible adiabatic expansion,

$$
\Delta S_{\text{sys}}
=
\Delta S_{\text{surr}}
=
\Delta S_{\text{univ}}
=
0.
$$

For the irreversible adiabatic free expansion,

$$
\Delta S_{\text{sys}}
=
\Delta S_{\text{univ}}
=
5.76\,\text{J K}^{-1},
$$

while

$$
\Delta S_{\text{surr}}=0.
$$

This example illustrates the Second Law of Thermodynamics:

$$
\Delta S_{\text{univ}}\geq 0.
$$

Equality holds for a reversible process; a strict inequality characterizes an irreversible process.

</div>

---

### Related Topics

- [Ideal-Gas Processes — Work, $\Delta U$ and $\Delta S$]({{ "/university/physics/thermodynamics/ideal-gas-processes/" | relative_url }})
- [Reaction Energetics — Internal Energy and Enthalpy]({{ "/university/physics/thermodynamics/reaction-energetics/" | relative_url }})
- [Equilibrium and Spontaneity — $\Delta G^\circ$, $K$ and Temperature]({{ "/university/physics/thermodynamics/equilibrium-and-spontaneity/" | relative_url }})
- [Colligative Properties — Freezing-Point Depression]({{ "/university/physics/thermodynamics/colligative-freezing/" | relative_url }})
- [Gibbs Free Energy for Incompressible Substances]({{ "/university/physics/thermodynamics/gibbs-incompressible/" | relative_url }})
- [Phase Transitions — Heating Curve and Enthalpy Changes]({{ "/university/physics/thermodynamics/phase-transitions/" | relative_url }})