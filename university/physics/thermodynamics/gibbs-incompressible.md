---
layout: default
title: "Gibbs Free Energy for Incompressible Substances"
meta-description: "Worked example on the dependence of Gibbs free energy on pressure for incompressible substances. Includes theoretical recalls, full derivation, and explanatory notes."
permalink: /university/physics/thermodynamics/gibbs-incompressible/
nav_order: 27
background_image: /images/termodinamica.png
---

# Gibbs Free Energy for Incompressible Substances

<div class="content-box">

## Theoretical Background

- **Definition of Gibbs free energy:**
  $$
  G = H - TS
  $$

- Differential form:
  $$
  dG = V\,dp - S\,dT
  $$

- For **isothermal processes** ($dT = 0$):
  $$
  dG = V\,dp
  $$

- If the substance is **incompressible**, $V$ is constant:
  $$
  \Delta G = V\,(p_2 - p_1)
  $$

</div>

<div class="content-box">

## Exercise

For **1.00 L of liquid water** at $25^\circ C$, calculate the change in Gibbs free energy when pressure increases from **1 bar to 100 bar**, assuming water is incompressible with molar volume $V_m = 18.0 \times 10^{-6}\, m^3 mol^{-1}$.

</div>

<div class="content-box">

## Step-by-Step Solution

**Step 1. Number of moles**  
$$
n = \frac{V}{V_m} = \frac{1.00 \times 10^{-3}\, m^3}{18.0 \times 10^{-6}\, m^3 mol^{-1}} = 55.6\, mol
$$

---

**Step 2. Pressure change**  
$$
\Delta p = p_2 - p_1 = (100 - 1)\, bar = 99\, bar
$$

Convert: $1\, bar = 10^5\, Pa$  
$$
\Delta p = 99 \times 10^5 = 9.9 \times 10^6\, Pa
$$

---

**Step 3. Gibbs free energy change**  
$$
\Delta G = n V_m \Delta p
$$

Insert values:  
$$
\Delta G = (55.6)(18.0 \times 10^{-6})(9.9 \times 10^6)\, J
$$

$$
\Delta G = 9900\, J = 9.9\, kJ
$$

---

**Answer:**  
$$
\Delta G \approx 9.9\, kJ
$$

</div>

<div class="content-box">

## Notes

- The result shows that $\Delta G$ for liquids and solids is **linear in pressure**, since they are almost incompressible.  
- For gases, the relation is logarithmic instead:
  $$
  G = G^\circ + RT \ln \frac{p}{p^\circ}
  $$
- This distinction is crucial in chemical thermodynamics: pressure effects on liquids are usually negligible compared to gases.  

</div>

---

### Related topics  
- [Ideal-Gas Processes — Work, ΔU and ΔS](/university/physics/thermodynamics/ideal-gas-processes/)  
- [Reaction Energetics — Internal Energy and Enthalpy](/university/physics/thermodynamics/reaction-energetics/)  
- [Entropy in Adiabatic Transformations](/university/physics/thermodynamics/entropy-adiabatic/)  
- [Equilibrium & Spontaneity — ΔG°, K, Temperature](/university/physics/thermodynamics/equilibrium-and-spontaneity/)  
- [Colligative Properties — Freezing Point Depression](/university/physics/thermodynamics/colligative-freezing/)  
