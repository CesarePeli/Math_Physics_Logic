---
layout: default
title: "Equilibrium and Spontaneity — Gibbs Free Energy"
meta-description: "Worked example on spontaneity and equilibrium conditions using Gibbs free energy. Full solution with theoretical recalls and explanatory notes."
permalink: /university/physics/thermodynamics/equilibrium-and-spontaneity/
nav_order: 25
background_image: /images/termodinamica.png
---

# Equilibrium and Spontaneity — Gibbs Free Energy

<div class="content-box">

## Theoretical Background

- **Second Law of Thermodynamics (constant T, p):**
  $$
  \\Delta G = \\Delta H - T \\Delta S
  $$

- **Spontaneity criterion:**
  - If $\\Delta G < 0 \\; \\Rightarrow$ spontaneous  
  - If $\\Delta G > 0 \\; \\Rightarrow$ non-spontaneous  
  - If $\\Delta G = 0 \\; \\Rightarrow$ equilibrium

- **At equilibrium:**
  $$
  \\Delta G = 0 \\quad \\text{and} \\quad \\Delta S_{univ} = 0
  $$

- Relationship with the equilibrium constant:
  $$
  \\Delta G^\\circ = -RT \\ln K
  $$

</div>

<div class="content-box">

## Exercise

For the reaction:

$$
N_2O_4(g) \\; \\rightleftharpoons \\; 2 NO_2(g)
$$

at $T = 298\\,K$, the standard enthalpy and entropy changes are:

- $\\Delta H^\\circ = +57.2\\,kJ mol^{-1}$  
- $\\Delta S^\\circ = +175.8\\,J mol^{-1}K^{-1}$  

**Tasks:**

1. Evaluate $\\Delta G^\\circ$ at 298 K.  
2. Discuss spontaneity and equilibrium position.  
3. Estimate the equilibrium constant $K$ at this temperature.

</div>

<div class="content-box">

## Step-by-Step Solution

**Step 1. Gibbs free energy change**  

Convert $\\Delta S^\\circ$:  
$$
\\Delta S^\\circ = 175.8\\, J mol^{-1}K^{-1} = 0.1758\\,kJ mol^{-1}K^{-1}
$$

Now:
$$
\\Delta G^\\circ = \\Delta H^\\circ - T \\Delta S^\\circ
$$

Insert values:
$$
\\Delta G^\\circ = 57.2 - (298)(0.1758) = 57.2 - 52.4 = +4.8\\,kJ mol^{-1}
$$

---

**Step 2. Spontaneity**  

Since $\\Delta G^\\circ > 0$, the forward reaction is **non-spontaneous at 298 K**.  
The equilibrium lies to the **left** (towards $N_2O_4$).

---

**Step 3. Equilibrium constant**  

Use:
$$
\\Delta G^\\circ = -RT \\ln K
$$

Rearrange:
$$
K = e^{-\\Delta G^\\circ / RT}
$$

Insert values:  
$R = 8.314\\,J mol^{-1}K^{-1} = 0.008314\\,kJ mol^{-1}K^{-1}$  
$RT = (0.008314)(298) = 2.48\\,kJ mol^{-1}$

So:
$$
K = e^{-4.8/2.48} = e^{-1.94} = 0.14
$$

</div>

<div class="content-box">

## Notes

- At 298 K the reaction is **not strongly spontaneous**, but $K$ is not extremely small either: there will be some dissociation of $N_2O_4$.  
- At higher $T$, the $T \\Delta S$ term becomes more important, and $\\Delta G$ may turn negative → dissociation favored.  
- This example illustrates how **enthalpy and entropy compete** in determining spontaneity.  
- The connection to the equilibrium constant provides a quantitative link between thermodynamics and chemical composition at equilibrium.

</div>
