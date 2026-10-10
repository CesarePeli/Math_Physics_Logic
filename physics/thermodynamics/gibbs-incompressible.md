---
layout: default
title: "Gibbs Free Energy — Pressure and Incompressible Water"
author: Marco Ruzzi
description: "Use the fundamental thermodynamic equation to calculate the Gibbs-energy change of 2 kg of incompressible water when pressure increases from 1 to 3 atm."
permalink: /physics/thermodynamics/gibbs-free-energy/
redirect_from:
  - /university/physics/thermodynamics/gibbs-incompressible/
nav_order: 27
background_image: /images/termodinamica.png
last_modified_at: 2026-10-10
---

# Gibbs Free Energy — Pressure and Incompressible Water

<div class="content-box">

*By Prof. Marco Ruzzi.*

## Theoretical background

The fundamental equation for Gibbs energy is:

$$
dG=V\,dp-S\,dT+\sum_i\mu_i\,dn_i.
$$

For a closed system with constant composition undergoing an isothermal change, dT=0 and dn<sub>i</sub>=0. Therefore dG=Vdp.

</div>

<div class="content-box">

## Exercise 10 — Increasing the pressure on liquid water

The pressure on a 2 kg sample of water increases from 1.00 to 3.00 atm at constant temperature. Assume a constant liquid volume (incompressible water), with density 1 kg L⁻¹. Use 1 L atm=101.325 J.

**Hint:** use the fundamental thermodynamic equation.

Calculate the Gibbs-energy change.

### 1. Reduce the fundamental equation

The system is closed and its composition is constant. For water alone:

$$
dG=V\,dp-S\,dT+\mu_{\mathrm{H_2O}}\,dn_{\mathrm{H_2O}}.
$$

Since dT=0 and dn<sub>H₂O</sub>=0:

$$
dG=V\,dp.
$$

### 2. Integrate at constant volume

$$
\Delta G=V(p_f-p_i)=\frac{m}{\rho}(p_f-p_i).
$$

$$
V=\frac{2\ \mathrm{kg}}{1\ \mathrm{kg\,L^{-1}}}=2\ \mathrm{L}.
$$

$$
\Delta G=(2\ \mathrm{L})(2\ \mathrm{atm})=4\ \mathrm{L\,atm}.
$$

$$
\Delta G=4(101.325)\ \mathrm{J}=+405.3\ \mathrm{J}.
$$



</div>

[← Thermodynamics worked problems]({{ '/physics/thermodynamics/' | relative_url }})
