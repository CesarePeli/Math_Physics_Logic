---
layout: default
title: "Equilibrium & Spontaneity — ΔG°, K, Temperature"
author: Marco Ruzzi
description: "From ΔH° and ΔS° to ΔG° and K: compute Kp at 298 K, decide the reaction direction from standard conditions, and discuss temperature effects."
permalink: /physics/thermodynamics/equilibrium-and-spontaneity/
redirect_from:
  - /university/physics/thermodynamics/equilibrium-and-spontaneity/
nav_order: 25
background_image: /images/termodinamica.png
last_modified_at: 2026-10-10
---

# Equilibrium & Spontaneity — ΔG°, K, Temperature

*By Prof. Marco Ruzzi.*

<div class="content-box">

## Theoretical background (quick recall)

- Standard Gibbs criterion:  
  $$
  \Delta G_r^\circ = \Delta H_r^\circ - T\Delta S_r^\circ
  $$

- Link to equilibrium:  
  $$
  \Delta G_r^\circ = -RT\ln K \;\;\Rightarrow\;\; K=\exp\!\left[-\frac{\Delta G_r^\circ}{RT}\right]
  $$

- For gas-phase reactions, the pressure-based constant (with p₀=1 bar) is
  $$
  K_p=\frac{\left(\dfrac{p_{\text{NO}_2}}{p_0}\right)^2}{\left(\dfrac{p_{\text{NO}}}{p_0}\right)^2\left(\dfrac{p_{\text{O}_2}}{p_0}\right)}.
  $$
  Because each pressure is divided by the standard pressure, this definition of K<sub>p</sub> is dimensionless.

- For a system with reaction quotient Q,
  

$$
\Delta G_r=\Delta G_r^\circ+RT\ln Q.
$$


  Thus, ΔG<sub>r</sub>°<0 implies spontaneous progress toward products when Q=1; it does not determine the direction for every possible composition. If K≫1, equilibrium is strongly product-favored.  

- Temperature effect (van ’t Hoff):  
  $$
  \frac{d\ln K}{dT}=\frac{\Delta H_r^\circ}{RT^2}
  $$
  For exothermic reactions (ΔH<sub>r</sub>°<0), K decreases as T increases.

</div>

<div class="content-box">

## Exercise — Oxidation of NO: K<sub>p</sub> and direction of spontaneity

For
$$
2\,\mathrm{NO}(g)+\mathrm{O}_2(g)\;\rightleftharpoons\;2\,\mathrm{NO}_2(g)
$$
at T=298.15 K, use  
ΔH<sub>f</sub>°(NO)=+90.2 kJ mol⁻¹,  
ΔH<sub>f</sub>°(NO₂)=+33.2 kJ mol⁻¹, and  
ΔS<sub>r</sub>°=-145.0 J mol⁻¹ K⁻¹  

to evaluate ΔG<sub>r</sub>°, then K<sub>p</sub>. State the spontaneous direction from standard conditions and discuss the effect of increasing temperature.

</div>

<div class="content-box">

## Step-by-step solution (with explanations)

**1) Write K<sub>p</sub> (definition).**  
Using partial pressures normalized by p₀=1 bar:
$$
K_p=\frac{\left(\dfrac{p_{\text{NO}_2}}{p_0}\right)^2}{\left(\dfrac{p_{\text{NO}}}{p_0}\right)^2\!\left(\dfrac{p_{\text{O}_2}}{p_0}\right)}.
$$
Since every partial pressure is divided by p₀, the value of K<sub>p</sub> obtained from this expression is dimensionless.

---

**2) Compute ΔH<sub>r</sub>° from formation enthalpies.**  
Remember ΔH<sub>f</sub>°(O₂,g)=0:
$$
\Delta H_r^\circ=2\,\Delta H_f^\circ(\mathrm{NO}_2)-\big[2\,\Delta H_f^\circ(\mathrm{NO})+1\cdot\Delta H_f^\circ(\mathrm{O}_2)\big]
=2(33.2)-2(90.2)= -114.0\,\text{kJ mol}^{-1}.
$$

---

**3) Compute ΔG<sub>r</sub>° at 298.15 K.**  
Use ΔS<sub>r</sub>°=-145.0 J mol⁻¹ K⁻¹=-0.145 kJ mol⁻¹ K⁻¹:
$$
\Delta G_r^\circ=\Delta H_r^\circ-T\Delta S_r^\circ
= -114.0 - (298.15)(-0.145)
\approx -70.8\,\text{kJ mol}^{-1}.
$$
> Since standard-state conditions correspond to Q=1, the negative value of ΔG<sub>r</sub>° indicates spontaneous progress toward products from that composition.

---

**4) Convert ΔG<sub>r</sub>° into K<sub>p</sub>.**  
With R=8.314 J mol⁻¹K⁻¹:
$$
K_p=\exp\!\left[-\frac{\Delta G_r^\circ}{RT}\right]
=\exp\!\left(\frac{70.8\times10^3}{(8.314)(298.15)}\right)
=\exp(28.56)\approx 2.5\times10^{12}.
$$
> Such a large K<sub>p</sub> means that equilibrium is strongly product-favored. The individual equilibrium partial pressures still depend on the initial composition and the total pressure.

---

**5) Direction from standard conditions.**  
Because ΔG<sub>r</sub>°<0, the forward reaction is spontaneous when Q=1. Since K<sub>p</sub>≫1, equilibrium is strongly shifted toward NO₂.

---

**6) Temperature effect (sign analysis).**  
Here ΔH<sub>r</sub>°<0 (exothermic) and ΔS<sub>r</sub>°<0 (gas moles decrease: 3→2).  
Increasing T makes -TΔS<sub>r</sub>° more **positive**, so ΔG<sub>r</sub>° becomes less negative. If ΔH<sub>r</sub>° and ΔS<sub>r</sub>° are treated as approximately constant, assuming constant ΔH° and ΔS°, it becomes positive above about 786 K. The decrease of K<sub>p</sub> with temperature is consistent with the van ’t Hoff equation.

</div>

<div class="content-box">

## Conceptual notes

- The negative value of ΔS<sub>r</sub>° is consistent with the decrease from three to two moles of gas. The change in gas-mole count is a useful qualitative guide, while the numerical value comes from standard molar entropies.  
- Standard formation data reminder: ΔH<sub>f</sub>°(O₂,g)=0 by convention; only NO and NO₂ contribute to ΔH<sub>r</sub>°.  
- The value K<sub>p</sub>∼10¹² at 298 K shows that equilibrium is strongly product-favored; it does not by itself determine each equilibrium partial pressure.  
- For different T, you may estimate K<sub>p</sub>(T) using the van ’t Hoff equation with (piecewise) constant ΔH<sub>r</sub>° in the temperature range of interest.  
- A complete interpretation uses both numerical values (ΔG°, K) and the signs of ΔH° and ΔS°, while distinguishing standard-state spontaneity from the direction at an arbitrary composition.

</div>

---

### Related topics
- [Ideal-Gas Processes — Work, ΔU and ΔS](/physics/thermodynamics/ideal-gas-processes/)  
- [Reaction Energetics — Internal Energy and Enthalpy](/physics/thermodynamics/reaction-energetics/)  
- [Entropy in Adiabatic Transformations](/physics/thermodynamics/entropy-adiabatic/)  
- [Colligative Properties — Freezing Point Depression](/physics/thermodynamics/colligative-freezing/)  
- [Gibbs Free Energy for Incompressible Substances](/physics/thermodynamics/gibbs-free-energy/)  
- [Phase Transitions — Heating Curve and Enthalpy Changes](/physics/thermodynamics/phase-transitions/)  
