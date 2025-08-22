---
layout: default
title: "Reaction Energetics — Internal Energy and Enthalpy"
meta-description: "Worked example on the energetics of a chemical reaction: relation between ΔU and ΔH, step-by-step calculations, and key thermodynamic notes."
permalink: /university/physics/thermodynamics/reaction-energetics/
nav_order: 23
background_image: /images/termodinamica.png
---

# Reaction Energetics — Internal Energy and Enthalpy

<div class="content-box">

## Theoretical Background

- **First Law of Thermodynamics:**  
  $$
  \\Delta U = q + w
  $$

- **Enthalpy definition:**  
  $$
  H = U + pV \\quad \\Rightarrow \\quad \\Delta H = \\Delta U + \\Delta(pV)
  $$

- For reactions at constant $T$ and $p$:  
  $$
  \\Delta H = q_p
  $$

- Connection between $\\Delta H$ and $\\Delta U$ (ideal gases):  
  $$
  \\Delta H = \\Delta U + \\Delta n_{gas} RT
  $$

where $\\Delta n_{gas}$ is the change in the number of moles of gas.

</div>

<div class="content-box">

## Exercise

Consider the combustion of carbon monoxide:

$$
2\\,CO(g) + O_2(g) \\;\\longrightarrow\\; 2\\,CO_2(g)
$$

At $T = 298\\,K$ and $p = 1\\,\\text{bar}$, the standard enthalpy of reaction is:

$$
\\Delta H^\\circ = -566.0\\,\\text{kJ mol}^{-1}
$$

**Tasks:**

1. Calculate the standard internal energy change $\\Delta U^\\circ$.  
2. Explain the relation between $\\Delta U$ and $\\Delta H$ for reactions involving gases.

</div>

<div class="content-box">

## Step-by-Step Solution

**Step 1. Count moles of gas**  
- Reactants: $n_{gas} = 2 + 1 = 3$  
- Products: $n_{gas} = 2$  
So:
$$
\\Delta n_{gas} = n_{prod} - n_{reag} = 2 - 3 = -1
$$

---

**Step 2. Relation between $\\Delta H$ and $\\Delta U$**  
For ideal gases:
$$
\\Delta H = \\Delta U + \\Delta n_{gas}RT
$$
Rearrange:
$$
\\Delta U = \\Delta H - \\Delta n_{gas}RT
$$

---

**Step 3. Insert data**  
With $T=298\\,\\text{K}$ and $R=8.314\\,\\text{J mol}^{-1}\\text{K}^{-1}$:
$$
\\Delta n_{gas}RT = (-1)(8.314)(298) = -2.48 \\times 10^3\\,\\text{J} = -2.48\\,\\text{kJ}
$$

---

**Step 4. Final value**  
$$
\\Delta U^\\circ = (-566.0\\,\\text{kJ}) - (-2.48\\,\\text{kJ}) = -563.5\\,\\text{kJ}
$$

---

**Answer:**  
$\\Delta U^\\circ = -563.5\\,\\text{kJ mol}^{-1}$

</div>

<div class="content-box">

## Notes

- The difference between $\\Delta U$ and $\\Delta H$ is small because only **1 mol of gas disappears**.  
- If $\\Delta n_{gas} = 0$, then $\\Delta H = \\Delta U$.  
- This correction ($\\Delta n RT$) becomes important at high $T$ or when many gas moles change.  
- **Pedagogical point:** Remember that $\\Delta H$ is often tabulated (easy to measure at $p$ constant), but $\\Delta U$ is more fundamental in the First Law.

</div>
