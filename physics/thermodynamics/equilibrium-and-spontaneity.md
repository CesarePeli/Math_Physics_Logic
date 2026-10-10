---
layout: default
title: "Chemical Equilibrium — Gibbs Energy, Temperature and Chemical Potentials"
author: Marco Ruzzi
description: "Worked NO oxidation and copper carbonate equilibrium exercises: reaction Gibbs energy, equilibrium constants, temperature effects and chemical potentials."
permalink: /physics/thermodynamics/equilibrium-and-spontaneity/
redirect_from:
  - /university/physics/thermodynamics/equilibrium-and-spontaneity/
nav_order: 25
background_image: /images/termodinamica.png
last_modified_at: 2026-10-10
---

# Chemical Equilibrium — Gibbs Energy, Temperature and Chemical Potentials

<div class="content-box">

*By Prof. Marco Ruzzi.*

## Theoretical background

At fixed temperature and pressure, the sign of the reaction Gibbs energy determines the direction of thermodynamic progress:

$$
\Delta_rG=\Delta_rG^\circ+RT\ln Q.
$$

$$
\Delta_rG^\circ=\Delta_rH^\circ-T\Delta_rS^\circ.
$$

At equilibrium Q=K and Δ<sub>r</sub>G=0, hence:

$$
\Delta_rG^\circ=-RT\ln K.
$$

$$
K=\exp\left(-\frac{\Delta_rG^\circ}{RT}\right).
$$

</div>

<div class="content-box">

## Exercise 6 — Exothermic oxidation and temperature

Discuss how temperature affects the spontaneity, from standard conditions, of the following exothermic reaction:

$$
2\mathrm{NO}(g)+\mathrm{O}_2(g)\rightleftharpoons2\mathrm{NO}_2(g).
$$

### Solution

We compare the reaction under standard conditions, where Q=1. Δ<sub>r</sub>H°<0 because the reaction is exothermic. Δ<sub>r</sub>S°<0 for this reaction, consistently with the reduction from three moles of gaseous reactants to two moles of gaseous products.

**High temperatures.** In the constant-ΔH°, constant-ΔS° approximation, sufficiently high T makes the positive contribution −TΔ<sub>r</sub>S° dominate:

$$
\Delta_rG^\circ\simeq-T\Delta_rS^\circ>0.
$$

The forward reaction is then unfavorable from standard conditions; raising T makes it less favorable.

**Low temperatures.** At sufficiently low T the negative enthalpic contribution dominates:

$$
\Delta_rG^\circ\simeq\Delta_rH^\circ<0.
$$

The forward reaction is favorable from standard conditions when the magnitude of the negative enthalpy contribution exceeds the opposing entropy term:

$$
|\Delta_rH^\circ|>|T\Delta_rS^\circ|.
$$

Within this approximation, that inequality is more marked at lower temperature.

### Observations

If oxygen were liquid, the sign of the reaction entropy could not be inferred merely from the phases indicated in the reaction equation. To calculate Δ<sub>r</sub>S° and establish its sign, the standard molar entropies of **all** participating substances would be required: NO(g), NO₂(g) and O₂(l).

Likewise, if the exercise did not state that the reaction is exothermic, its enthalpy change would have to be calculated from the formation enthalpies of NO(g) and NO₂(g). For O₂(g) in its elemental standard reference state, the standard formation enthalpy is zero.

</div>

<div class="content-box">

## Exercise 7 — Copper carbonate and chemical potentials

The reaction:

$$
\mathrm{CuCO}_3(s)\rightleftharpoons\mathrm{CuO}(s)+\mathrm{CO}_2(g)
$$

has K<sub>p</sub>=50. A reaction mixture has a CO₂ pressure of 50 bar. Determine whether it is at equilibrium and write the resulting relation between the chemical potentials of its components.

Define the chemical-potential difference:

$$
D=\mu_{\mathrm{CuO}(s)}+\mu_{\mathrm{CO}_2(g)}-\mu_{\mathrm{CuCO}_3(s)}.
$$

### Solution

For pure solid phases, their activities are one. Using the pressure-based ideal-gas expression, with p°=1 bar:

$$
Q_p=\frac{p_{\mathrm{CO}_2}}{p^\circ}=50=K_p.
$$

The mixture is therefore at equilibrium. In general, the equilibrium condition on chemical potentials is:

$$
\begin{aligned}
\Delta_rG={}&\sum_{\mathrm{products}}\nu_i\mu_i\\
&-\sum_{\mathrm{reactants}}\nu_i\mu_i=0.
\end{aligned}
$$

For this reaction:

$$
\mu_{\mathrm{CuO}(s)}+\mu_{\mathrm{CO}_2(g)}-\mu_{\mathrm{CuCO}_3(s)}=0.
$$

</div>

<div class="content-box">

## Problem — NO oxidation and its equilibrium constant

Consider:

$$
2\mathrm{NO}(g)+\mathrm{O}_2(g)\rightleftharpoons2\mathrm{NO}_2(g).
$$

At T=298.15 K, the formation enthalpies are +90.2 kJ mol⁻¹ for NO(g) and +33.2 kJ mol⁻¹ for NO₂(g). The standard reaction entropy is −145.0 J mol⁻¹ K⁻¹.

1. Write the expression for K<sub>p</sub>.
2. Calculate the equilibrium constant at 298.15 K.
3. Starting from standard conditions, determine the direction in which the reaction moves toward equilibrium.
4. What is Δ<sub>r</sub>G at equilibrium?
5. Describe the effect of increasing temperature on the equilibrium.

### 1. Reaction quotient and equilibrium constant

For ideal gases, normalize each partial pressure by p°=1 bar:

$$
Q=\frac{(p_{\mathrm{NO}_2}/p^\circ)^2}{(p_{\mathrm{NO}}/p^\circ)^2(p_{\mathrm{O}_2}/p^\circ)}.
$$

Equivalently:

$$
Q=\frac{p_{\mathrm{NO}_2}^2p^\circ}{p_{\mathrm{NO}}^2p_{\mathrm{O}_2}}.
$$

At equilibrium the partial pressures no longer change and K<sub>p</sub>=Q evaluated at those pressures. The constant is dimensionless.

### 2. Numerical value of the equilibrium constant

At equilibrium:

$$
0=\Delta_rG^\circ+RT\ln K_p.
$$

Thus Δ<sub>r</sub>G°=−RT ln K<sub>p</sub>, and calculating K<sub>p</sub> requires the standard reaction Gibbs energy.

First calculate the enthalpy from the formation data:

$$
\begin{aligned}
\Delta_rH^\circ={}&2\Delta_fH^\circ(\mathrm{NO}_2)\\
&-2\Delta_fH^\circ(\mathrm{NO})\\
&-\Delta_fH^\circ(\mathrm{O}_2).
\end{aligned}
$$

$$
\Delta_rH^\circ=2(33.2)-2(90.2)-0=-114\ \mathrm{kJ\,mol^{-1}}.
$$

The entropy is supplied directly: −145.0 J mol⁻¹ K⁻¹, or −0.1450 kJ mol⁻¹ K⁻¹. Hence:

$$
\Delta_rG^\circ=-114-(298.15)(-0.1450)\ \mathrm{kJ\,mol^{-1}}.
$$

$$
\Delta_rG^\circ\simeq-70.8\ \mathrm{kJ\,mol^{-1}}.
$$

Using R=8.314 J mol⁻¹ K⁻¹ and the rounded Gibbs energy:

$$
-\frac{\Delta_rG^\circ}{RT}\simeq\frac{70.8\times10^3}{(8.314)(298.15)}\simeq28.56.
$$

$$
K_p=e^{28.56}\simeq2.5\times10^{12}.
$$

### 3. Direction from standard conditions

The standard conditions give Q=1. Since Δ<sub>r</sub>G°≈−70.8 kJ mol⁻¹, the reaction proceeds toward the products.

### 4. Gibbs energy at equilibrium

The **reaction** Gibbs energy vanishes at equilibrium:

$$
\Delta_rG=0.
$$

### 5. Effect of temperature

Here Δ<sub>r</sub>H°=−114 kJ mol⁻¹ and Δ<sub>r</sub>S°=−145.0 J mol⁻¹ K⁻¹. The term TΔ<sub>r</sub>S° is negative; its magnitude grows with temperature, so its contribution **−TΔ<sub>r</sub>S°** to the Gibbs energy is increasingly positive. Raising the temperature favors the reactants in this exothermic equilibrium.

</div>

[← Thermodynamics worked problems]({{ '/physics/thermodynamics/' | relative_url }})
