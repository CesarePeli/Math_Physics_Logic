---
layout: default
title: "Ideal-Gas Processes — Work, ΔU and ΔS"
author: Marco Ruzzi
description: "Compare work, internal energy, and entropy for compressions of an ideal gas along different reversible paths. Includes theoretical recalls and full solution with notes."
permalink: /physics/thermodynamics/ideal-gas-processes/
redirect_from:
  - /university/physics/thermodynamics/ideal-gas-processes/
nav_order: 22
background_image: /images/termodinamica.png
last_modified_at: 2026-10-10
---

# Ideal-Gas Processes — Work, ΔU and ΔS

*By Prof. Marco Ruzzi.*

<div class="content-box">

## Theoretical Background

- **Equation of state:** pV=nRT
- **Internal energy of an ideal gas:** U=U(T), so ΔU depends only on the temperature change.
- **Isothermal process:** ΔU=0
- **Work done on the gas in a reversible isothermal process:**
  

$$
w_{\mathrm{on}}
  =-nRT\,\ln\!\left(\frac{V_2}{V_1}\right)
  =nRT\,\ln\!\left(\frac{V_1}{V_2}\right)
$$


- **Entropy change between ideal-gas states at the same temperature:**
  $$
  \Delta S=nR\,\ln\!\left(\frac{V_2}{V_1}\right)
  $$
- **State vs path functions:** ΔU and ΔS depend only on initial and final states, while w and q depend on the path.

> **Sign convention reminder.** Here wₒₙ>0 denotes work done on the gas, so compression gives positive work. Texts that define work as work done by the gas use the opposite sign.

> **Validity conditions.** The equation of state and internal-energy statement assume an ideal gas. The stated work formula requires a reversible isothermal path. The entropy formula requires equal initial and final temperatures; because entropy is a state function, that value also applies to an irreversible path with the same endpoints. For unequal endpoint temperatures, a thermal contribution must be included:

$$
\Delta S=n\int_{T_1}^{T_2}\frac{C_{V,m}(T)}{T}\,dT+nR\ln\!\left(\frac{V_2}{V_1}\right).
$$

</div>

<div class="content-box">

## Exercise

A sample of n=100 mol of ideal hydrogen is compressed between two equilibrium states, both at T=300 K, from V₁=4.0 m³ to V₂=2.0 m³.

Calculate the work **on** the gas along three different reversible paths:

1. **(a)** Isobaric compression (at p₁) followed by isochoric heating to the final state.  
2. **(b)** Direct isothermal compression from V₁ to V₂.  
3. **(c)** Isochoric heating to p₂, followed by isobaric compression at p₂.

Then evaluate ΔU and ΔS, and compare results.

</div>

<div class="content-box">

## Step-by-Step Solution

**Step 1. Calculate initial and final pressures**  
From pV=nRT:
$$
p_1=\frac{nRT}{V_1},\qquad p_2=\frac{nRT}{V_2}.
$$
With nRT=2.494×10⁵ J, we have p₂=2p₁.

---

**Step 2. Work for each path**

- **(a) Isobaric (at p₁):**
  $$
  w_a=-p_1(V_2-V_1)=p_1(V_1-V_2)
  =nRT\!\left(1-\frac{V_2}{V_1}\right)
  $$
  Numerically: wₐ=1.247×10⁵ J.

- **(b) Isothermal:**
  $$
  w_b=-nRT\,\ln\!\left(\frac{V_2}{V_1}\right)
       =nRT\,\ln\!\left(\frac{V_1}{V_2}\right)
       =2.494\times10^5\,\ln 2
  $$
  w<sub>b</sub>=1.729×10⁵ J.

- **(c) Isobaric (at p₂):**
  $$
  w_c=-p_2(V_2-V_1)=p_2(V_1-V_2)=2w_a
  $$
  w<sub>c</sub>=2.494×10⁵ J.

---

**Step 3. Internal energy change**  
Since T is the same at initial and final state:
$$
\Delta U=0.
$$

---

**Step 4. Entropy change**  
Use the isothermal reference (reversible):
$$
\Delta S=nR\,\ln\!\left(\frac{V_2}{V_1}\right).
$$
Numerically:
$$
\Delta S=100(8.314)\,\ln(0.5)=-5.76\times10^2\,\text{J K}^{-1}.
$$

</div>

<div class="content-box">

## Notes and Discussion

- The **work** depends on the path: wₐ<w<sub>b</sub><w<sub>c</sub>. This illustrates that work is **path-dependent**.
- The **internal energy** change is zero for all cases because U of an ideal gas depends only on T.
- The **entropy** decreases because the gas reaches the same temperature in a smaller volume. Entropy is a **state function**, so the same value is obtained for all three paths.
- **Important remark:** Here ΔU=0 because the initial and final temperatures are equal and the gas is ideal. Only path (b) is isothermal throughout; paths (a) and (c) pass through intermediate temperatures.

</div>

---

### Related topics
- [Reaction Energetics — Internal Energy and Enthalpy](/physics/thermodynamics/reaction-energetics/)  
- [Entropy in Adiabatic Transformations](/physics/thermodynamics/entropy-adiabatic/)  
- [Equilibrium & Spontaneity — ΔG°, K, Temperature](/physics/thermodynamics/equilibrium-and-spontaneity/)  
- [Colligative Properties — Freezing Point Depression](/physics/thermodynamics/colligative-freezing/)  
- [Gibbs Free Energy for Incompressible Substances](/physics/thermodynamics/gibbs-free-energy/)  
- [Phase Transitions — Heating Curve and Enthalpy Changes](/physics/thermodynamics/phase-transitions/)
