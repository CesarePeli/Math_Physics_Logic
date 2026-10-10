---
layout: default
title: "Reaction Energetics — Internal Energy and Enthalpy"
author: Marco Ruzzi
description: "Calculate the standard internal-energy change for oxidation of NO from formation enthalpies and the ideal-gas pressure-volume correction."
permalink: /physics/thermodynamics/reaction-energetics/
redirect_from:
  - /university/physics/thermodynamics/reaction-energetics/
nav_order: 23
background_image: /images/termodinamica.png
last_modified_at: 2026-10-10
---

# Reaction Energetics — Internal Energy and Enthalpy

<div class="content-box">

*By Prof. Marco Ruzzi.*

## Theoretical background

For ideal gases:

$$
H=U+pV=U+nRT.
$$

At fixed temperature, the change in gaseous amount gives:

$$
dH=dU+d(nRT)=dU+RT\,dn.
$$

$$
\Delta H=\Delta U+RT\Delta n.
$$

For molar reaction quantities, use Δν<sub>gas</sub>, the gaseous stoichiometric coefficients of products minus those of reactants:

$$
\Delta_rU^\circ=\Delta_rH^\circ-RT\Delta\nu_{\mathrm{gas}}.
$$

</div>

<div class="content-box">

## Exercise 2 — Oxidation of nitric oxide

Consider the reaction under standard conditions at T=298 K:

$$
2\mathrm{NO}(g)+\mathrm{O}_2(g)\longrightarrow2\mathrm{NO}_2(g).
$$

The standard formation enthalpies are +90.2 kJ mol⁻¹ for NO(g) and +33.2 kJ mol⁻¹ for NO₂(g). Calculate the standard molar internal-energy change of the reaction.

### 1. Change in gaseous amount

$$
\Delta\nu_{\mathrm{gas}}=2-(2+1)=-1.
$$

Thus:

$$
\Delta_rU^\circ=\Delta_rH^\circ+RT.
$$

### 2. Reaction enthalpy

Use formation enthalpies, taking products minus reactants. Oxygen in its standard elemental reference state has zero standard formation enthalpy by convention:

$$
\begin{aligned}
\Delta_rH^\circ={}&2\Delta_fH^\circ(\mathrm{NO}_2)\\
&-2\Delta_fH^\circ(\mathrm{NO})\\
&-\Delta_fH^\circ(\mathrm{O}_2).
\end{aligned}
$$

$$
\Delta_rH^\circ=2(33.2)-2(90.2)-0.
$$

$$
\Delta_rH^\circ=-114\ \mathrm{kJ\,mol^{-1}}.
$$

### 3. Internal-energy change

With R=8.314 J mol⁻¹ K⁻¹:

$$
\Delta_rU^\circ=-114\times10^3+(8.314)(298)\ \mathrm{J\,mol^{-1}}.
$$

$$
\Delta_rU^\circ=-111522.428\ \mathrm{J\,mol^{-1}}.
$$

$$
\Delta_rU^\circ\simeq-111.5\ \mathrm{kJ\,mol^{-1}}.
$$

The enthalpy change must be distinguished from the internal-energy change.

</div>

[← Thermodynamics worked problems]({{ '/physics/thermodynamics/' | relative_url }})
