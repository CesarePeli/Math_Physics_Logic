---
layout: default
title: "Phase Transitions — Heating Curve and Enthalpy Changes"
meta-description: "Worked example on phase transitions: enthalpy changes during heating and melting of ice. Includes theoretical recalls, calculations, and explanatory notes."
permalink: /physics/thermodynamics/phase-transitions/
redirect_from:
  - /university/physics/thermodynamics/phase-transitions/
nav_order: 28
background_image: /images/termodinamica.png
---

# Phase Transitions — Heating Curve and Enthalpy Changes

<div class="content-box">

## Theoretical Background

- **Heat required for temperature change:**
  $$
  q = m c \Delta T
  $$

- **Heat absorbed in a phase transition at constant pressure:**
  $$
  q = n \Delta H_{\text{trans}}
  $$

- During an equilibrium phase transition of a pure substance at fixed pressure, the temperature remains constant while heat changes the phase and reorganizes intermolecular interactions.  
- Under these conditions, a heating curve combines *sloped segments* within a single phase and *plateaus* during phase changes.

</div>

<div class="content-box">

## Exercise

Calculate the total heat required to bring **50.0 g of ice** from **–10.0 °C** to liquid water at **25.0 °C**.  

Given data:  
- $c_{\text{ice}} = 2.09 \, J\,g^{-1}\,K^{-1}$  
- $c_{\text{water}} = 4.18 \, J\,g^{-1}\,K^{-1}$  
- $\Delta H_{\text{fus}} = 6.01 \, kJ\,mol^{-1}$  
- Molar mass of $H_2O = 18.0 \, g\,mol^{-1}$  

</div>

<div class="content-box">

## Step-by-Step Solution

**Step 1. Heating ice from –10 °C to 0 °C**  
$$
q_1 = m c_{\text{ice}} \Delta T = (50.0)(2.09)(10.0) = 1045 \, J
$$

---

**Step 2. Melting ice at 0 °C**  
Moles of water:
$$
n = \frac{50.0}{18.0} = 2.78 \, mol
$$

$$
q_2 = n \Delta H_{\text{fus}}
= (2.78\,\mathrm{mol})(6.01\,\mathrm{kJ\,mol^{-1}})
= 16.7\,\mathrm{kJ}
$$

---

**Step 3. Heating liquid water from 0 °C to 25 °C**  
$$
q_3 = m c_{\text{water}} \Delta T = (50.0)(4.18)(25.0) = 5225 \, J
$$

---

**Step 4. Total heat**  
$$
q_{\text{tot}} = q_1 + q_2 + q_3
$$

Convert to consistent units (kJ):  
- $q_1 = 1.05 \, kJ$  
- $q_2 = 16.7 \, kJ$  
- $q_3 = 5.23 \, kJ$

$$
q_{\text{tot}} = 1.05 + 16.7 + 5.23 = 23.0 \, kJ
$$

---

**Answer:**  
$$
q_{\text{tot}} = 23.0 \, kJ
$$

</div>

<div class="content-box">

## Notes

- Over the temperature interval considered, the heating curve has three regions: heating the solid, the melting plateau, and heating the liquid.  
- The largest energy contribution comes from the **phase transition** (fusion), which requires far more heat than simply raising the temperature.  
- This illustrates the difference between:  
  - **specific heat** (energy per unit mass per degree, linked to temperature changes),  
  - **latent heat** (energy associated with structural reorganization of matter).  
- At constant pressure, the supplied heat equals the enthalpy change, so a heating curve represents how enthalpy is added within and between phases.

</div>

---

### Related topics  
- [Ideal-Gas Processes — Work, ΔU and ΔS](/physics/thermodynamics/ideal-gas-processes/)  
- [Reaction Energetics — Internal Energy and Enthalpy](/physics/thermodynamics/reaction-energetics/)  
- [Entropy in Adiabatic Transformations](/physics/thermodynamics/entropy-adiabatic/)  
- [Equilibrium & Spontaneity — ΔG°, K, Temperature](/physics/thermodynamics/equilibrium-and-spontaneity/)  
- [Colligative Properties — Freezing Point Depression](/physics/thermodynamics/colligative-freezing/)  
- [Gibbs Free Energy for Incompressible Substances](/physics/thermodynamics/gibbs-free-energy/)  
