---
layout: default
title: "Gibbs Free Energy for Incompressible Substances"
author: Marco Ruzzi
description: "Worked example on the dependence of Gibbs free energy on pressure for incompressible substances. Includes theoretical recalls, full derivation, and explanatory notes."
permalink: /physics/thermodynamics/gibbs-free-energy/
redirect_from:
  - /university/physics/thermodynamics/gibbs-incompressible/
nav_order: 27
background_image: /images/termodinamica.png
last_modified_at: 2026-10-10
---

# Gibbs Free Energy for Incompressible Substances

*By Prof. Marco Ruzzi.*

<div class="content-box">

## Theoretical Background

- **Definition of Gibbs free energy:**
  $$
  G = H - TS
  $$

- Differential form for a simple compressible closed system of fixed composition, with pressure–volume work as the only work mode:
  $$
  dG = V\,dp - S\,dT
  $$

- For an **isothermal process** (dT = 0):
  $$
  dG = V\,dp
  $$

- For a fixed amount of an **incompressible** substance (constant total volume V):
  $$
  \Delta G = V\,(p_2 - p_1)
  $$

For a fixed amount of an incompressible substance at constant temperature, the Gibbs free-energy change is therefore proportional to the pressure change.

</div>

<div class="content-box">

## Exercise

For **1.00 L of liquid water** at 25° C, calculate the change in Gibbs free energy when pressure increases from **1 bar to 100 bar**, assuming water is incompressible with molar volume V<sub>m</sub> = 18.0 × 10⁻⁶  m³ mol⁻¹.

</div>

<div class="content-box">

## Step-by-Step Solution

**Step 1. Number of moles**  
From the total volume and the molar volume:
$$
n = \frac{V}{V_m} = \frac{1.00 \times 10^{-3}\, m^3}{18.0 \times 10^{-6}\, m^3 mol^{-1}} = 55.6\, mol
$$

---

**Step 2. Pressure change**  
$$
\Delta p = p_2 - p_1 = (100 - 1)\, bar = 99\, bar
$$

Convert to SI units:  
$$
1\, bar = 10^5\, Pa \quad \Rightarrow \quad \Delta p = 99 \times 10^5 = 9.9 \times 10^6\, Pa
$$

---

**Step 3. Gibbs free energy change**  
Use ΔG = n V<sub>m</sub> Δ p:  
$$
\Delta G
= (55.6\,\mathrm{mol})
  (18.0 \times 10^{-6}\,\mathrm{m^3\,mol^{-1}})
  (9.9 \times 10^6\,\mathrm{Pa})
$$

$$
\Delta G = 9900\, J \;\approx 9.9\, kJ
$$

---

**Final Answer:**  
$$
\Delta G \approx 9.9\, kJ
$$

</div>

<div class="content-box">

## Notes

- The calculation shows that for liquids, ΔG is proportional to the pressure change.  
- Increasing the pressure from 1 bar to 100 bar changes G by about 9.9 kJ for one litre of water; the change per mole is only about 0.18 kJ mol⁻¹ because the molar volume is small.  
- For a pure ideal gas, the molar Gibbs free energy, or chemical potential, is
  

$$
\mu(T,p)=\mu^\circ(T)+RT\ln\!\left(\frac{p}{p^\circ}\right).
$$


  Its pressure dependence is logarithmic.  
- Pressure enters gas chemical potentials explicitly. For liquids and solids, the pressure contribution is usually much smaller because their molar volumes are small.  

</div>

---

### Related topics  
- [Ideal-Gas Processes — Work, ΔU and ΔS](/physics/thermodynamics/ideal-gas-processes/)  
- [Reaction Energetics — Internal Energy and Enthalpy](/physics/thermodynamics/reaction-energetics/)  
- [Entropy in Adiabatic Transformations](/physics/thermodynamics/entropy-adiabatic/)  
- [Equilibrium & Spontaneity — ΔG°, K, Temperature](/physics/thermodynamics/equilibrium-and-spontaneity/)  
- [Colligative Properties — Freezing Point Depression](/physics/thermodynamics/colligative-freezing/)  
- [Phase Transitions — Heating Curve and Enthalpy Changes](/physics/thermodynamics/phase-transitions/)  
