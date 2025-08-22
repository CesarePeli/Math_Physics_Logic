---
layout: default
title: "Entropy in Adiabatic Transformations"
meta-description: "Worked example on entropy change in adiabatic processes, with theoretical recalls and full step-by-step solution."
permalink: /university/physics/thermodynamics/entropy-adiabatic/
nav_order: 24
background_image: /images/termodinamica.png
---

# Entropy in Adiabatic Transformations

<div class="content-box">

## Theoretical Background

- **Adiabatic process:** $q = 0$  
- **First Law:** $\\Delta U = q + w \\; \\Rightarrow \\; \\Delta U = w$  
- For an **ideal gas**: $U = U(T)$  
- **Reversible adiabatic:** $\\Delta S = 0$  
- **Irreversible adiabatic:** $\\Delta S > 0$  
- **Entropy change of the universe:**  
  $$
  \\Delta S_{univ} = \\Delta S_{sys} + \\Delta S_{surr}
  $$

</div>

<div class="content-box">

## Exercise

A sample of **1 mol of ideal gas** expands adiabatically from $V_1 = 10.0\\,L$ to $V_2 = 20.0\\,L$.  

1. Evaluate the entropy change of the system in the case of a **reversible adiabatic** expansion.  
2. Repeat for an **irreversible adiabatic** free expansion against vacuum.  
3. Discuss the entropy change of the universe in both cases.

</div>

<div class="content-box">

## Step-by-Step Solution

**Case 1 — Reversible adiabatic expansion**  
- By definition, $q_{rev} = 0$  
- Entropy change of system:
  $$
  \\Delta S_{sys} = \\int \\frac{dq_{rev}}{T} = 0
  $$
- So: $\\Delta S_{sys} = 0$  

Entropy of the surroundings:  
$$
\\Delta S_{surr} = 0
$$

Therefore:  
$$
\\Delta S_{univ} = 0
$$

---

**Case 2 — Irreversible adiabatic free expansion**  
- Still $q = 0$, so $\\Delta U = 0$ (no work done, no heat exchanged).  
- For the **system entropy** we must compare initial and final equilibrium states.  

For 1 mol ideal gas:
$$
\\Delta S_{sys} = R \\ln\\!\\left( \\frac{V_2}{V_1} \\right) = 8.314 \\ln 2 = 5.76\\, J K^{-1}
$$

Surroundings are vacuum, so:
$$
\\Delta S_{surr} = 0
$$

Therefore:  
$$
\\Delta S_{univ} = +5.76\\, J K^{-1}
$$

---

**Case 3 — Discussion**  
- Reversible adiabatic: entropy does not change (system and universe).  
- Irreversible free expansion: entropy of the system increases, and so does that of the universe.  

This illustrates the **Second Law**:  
$$
\\Delta S_{univ} \\ge 0
$$

</div>

<div class="content-box">

## Notes

- In a reversible adiabatic expansion, the gas cools as it expands, but the process is perfectly balanced: entropy remains constant.  
- In the free expansion, the gas ends up occupying a larger volume at the same temperature, increasing disorder → entropy rises.  
- This is a textbook example that entropy is a **state function**, independent of path, but the *entropy production* distinguishes reversible vs irreversible paths.

</div>
