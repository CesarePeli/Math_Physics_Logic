---
layout: default
title: "Reaction Energetics — Internal Energy and Enthalpy"
meta-description: "Worked example on the energetics of a chemical reaction: relation between ΔU and ΔH, step-by-step calculations, and key thermodynamic notes."
permalink: /physics/thermodynamics/reaction-energetics/
redirect_from:
  - /university/physics/thermodynamics/reaction-energetics/
nav_order: 23
background_image: /images/termodinamica.png
---

# Reaction Energetics — Internal Energy and Enthalpy

<div class="content-box">

## Theoretical Background

- **First Law of Thermodynamics:**  
  $$
  \Delta U = q + w
  $$

- **Enthalpy definition:**  
  $$
  H = U + pV \;\Rightarrow\; \Delta H = \Delta U + \Delta(pV)
  $$

- At constant pressure, when the only mechanical work is pressure–volume work:
  $
  \Delta H=q_p.
  $

- For an ideal-gas reaction at a fixed temperature:
  $
  \Delta_r H^\circ
  =\Delta_r U^\circ+\Delta\nu_{\text{gas}}RT,
  \qquad
  \Delta_r U^\circ
  =\Delta_r H^\circ-\Delta\nu_{\text{gas}}RT,
  $
  where $\Delta\nu_{\text{gas}}$ is the sum of the gaseous stoichiometric coefficients of the products minus that of the reactants.

> **Validity note.**  
> The relation containing $\Delta\nu_{\text{gas}}RT$ follows from the ideal-gas equation for the gaseous species. It is exact for the all-gas ideal reaction considered below. Real gases require an appropriate equation of state.

> **Sign convention used here.**  
> $w>0$ denotes work done on the system, while $w<0$ denotes work done by the system. With this convention, the First Law is $\Delta U=q+w$.

</div>

<div class="content-box">

## Exercise

Consider the combustion of carbon monoxide:

$$
2\,\mathrm{CO}(g) + \mathrm{O}_2(g) \;\longrightarrow\; 2\,\mathrm{CO}_2(g)
$$

At $T = 298\,\text{K}$ and $p = 1\,\text{bar}$, the standard enthalpy of reaction is:

$$
\Delta_r H^{\circ} = -566.0\,\text{kJ mol}^{-1}
$$

**Tasks:**

1. Calculate the standard molar internal-energy change $\Delta_r U^{\circ}$.  
2. Explain the relation between $\Delta U$ and $\Delta H$ for reactions involving gases.

</div>

<div class="content-box">

## Step-by-Step Solution

**Step 1. Count moles of gas**  
- Reactants: $n_{\text{gas}} = 2 + 1 = 3$  
- Products: $n_{\text{gas}} = 2$  

So:
$$
\Delta\nu_{\text{gas}}
= \sum\nu_{\text{products}}-\sum\nu_{\text{reactants}}
=2-(2+1)=-1
$$

---

**Step 2. Relation between $\Delta H$ and $\Delta U$**  
For ideal gases:
$$
\Delta_r U^\circ
=\Delta_r H^\circ-\Delta\nu_{\text{gas}}RT
$$

---

**Step 3. Insert data**  
With $T = 298\,\text{K}$ and $R = 8.314\,\text{J mol}^{-1}\text{K}^{-1}$:
$$
\Delta\nu_{\text{gas}}RT
=(-1)(8.314)(298)
=-2.48 \times 10^{3}\,\text{J mol}^{-1}
=-2.48\,\text{kJ mol}^{-1}
$$

---

**Step 4. Final value**  
$$
\Delta_r U^{\circ}
=(-566.0)\,\text{kJ mol}^{-1}
-(-2.48)\,\text{kJ mol}^{-1}
=-563.5\,\text{kJ mol}^{-1}.
$$

---

**Answer:**  
$$
\Delta_r U^{\circ} = -563.5\,\text{kJ mol}^{-1}
$$

</div>

<div class="content-box">

## Notes

- The difference between $\Delta_r U^\circ$ and $\Delta_r H^\circ$ is small here because $\Delta\nu_{\text{gas}}=-1$.  
- If $\Delta\nu_{\text{gas}}=0$ for an ideal-gas reaction, then $\Delta_r H^\circ=\Delta_r U^\circ$.  
- The magnitude of the correction $\Delta\nu_{\text{gas}}RT$ grows with temperature and with the change in gaseous stoichiometric coefficients.  
- Standard reaction enthalpies are commonly tabulated, while the First Law is written directly in terms of internal energy.  
- For non-ideal gases, the simple $RT\Delta\nu_{\text{gas}}$ correction is only approximate.

</div>

---

### Related topics  
- [Ideal-Gas Processes — Work, ΔU and ΔS](/physics/thermodynamics/ideal-gas-processes/)  
- [Entropy in Adiabatic Transformations](/physics/thermodynamics/entropy-adiabatic/)  
- [Equilibrium & Spontaneity — ΔG°, K, Temperature](/physics/thermodynamics/equilibrium-and-spontaneity/)  
- [Colligative Properties — Freezing Point Depression](/physics/thermodynamics/colligative-freezing/)  
- [Gibbs Free Energy for Incompressible Substances](/physics/thermodynamics/gibbs-free-energy/)  
- [Phase Transitions — Heating Curve and Enthalpy Changes](/physics/thermodynamics/phase-transitions/)  
