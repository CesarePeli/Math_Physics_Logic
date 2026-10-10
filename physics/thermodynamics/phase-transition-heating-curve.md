---
layout: default
title: "Phase Transitions — Water Heating Curve"
author: Marco Ruzzi
description: "Read a water heating curve: melting and vaporization enthalpies, phase coexistence and the relation between curve slopes and heat capacities."
permalink: /physics/thermodynamics/phase-transitions/
redirect_from:
  - /university/physics/thermodynamics/phase-transitions/
nav_order: 28
background_image: /images/termodinamica.png
last_modified_at: 2026-10-10
---

# Phase Transitions — Water Heating Curve

<div class="content-box">

*By Prof. Marco Ruzzi.*

## Theoretical background

At constant pressure, heating a single phase gives dq=C<sub>p</sub>dT. On a graph of temperature against supplied heat:

$$
\frac{dT}{dq}=\frac{1}{C_p}.
$$

For one mole this becomes 1/C<sub>p,m</sub>. During melting or vaporization of a pure substance at a fixed pressure, the two phases coexist at a constant transition temperature.

</div>

<div class="content-box">

## Exercise 5 — Interpret the heating curve

The graph shows the temperature of a quantity of water as it passes from the solid to the gaseous state. Explain the physical meaning of its five segments. Identify the conditions under which the plateau widths represent standard molar transition enthalpies and the slopes determine molar heat capacities.

<a href="{{ '/images/ruzzi/water-heating-curve.gif' | relative_url }}"><img src="{{ '/images/ruzzi/water-heating-curve.gif' | relative_url }}" alt="Water heating curve: segments 1, 3 and 5 warm ice, liquid water and vapor; segments 2 and 4 are melting and boiling plateaus" style="display:block;width:100%;max-width:780px;height:auto;margin:1.2rem auto;background:#fff;padding:12px;box-sizing:border-box;"></a>

[View the graph at full size]({{ '/images/ruzzi/water-heating-curve.gif' | relative_url }}).

### Solution

**Melting plateau.** For one mole of water at the standard pressure of 1 bar, the heat absorbed during melting is its standard molar enthalpy of fusion. The transition temperatures in this schematic graph are shown approximately as 0 °C and 100 °C.

**Vaporization plateau.** Segment 4 represents the liquid–gas transition: the two phases coexist while the temperature remains constant.

**Slope of segment 1.** Segment 1 describes the **solid**. For one mole its slope is the reciprocal of the molar heat capacity of ice at constant pressure, rather than that of liquid water.

### Observations on melting and vaporization

The system absorbs heat during melting. For one mole at 1 bar, the horizontal width of segment 2 represents Δ<sub>fus</sub>H°. Melting is isothermal at T<sub>fus</sub>: the absorbed energy changes the intermolecular structure of the crystalline solid rather than increasing its temperature. In ice this concerns the hydrogen-bond network.

The same reasoning applies to vaporization. For one mole under standard-pressure conditions, the horizontal width of segment 4 represents Δ<sub>vap</sub>H°, at the constant vaporization temperature T<sub>vap</sub>.

Segments 1, 3 and 5 represent heating of the solid, liquid and vapor, respectively. Their slopes are:

$$
m_1=\frac{1}{C_{p,\mathrm{solid}}}.
$$

$$
m_3=\frac{1}{C_{p,\mathrm{liquid}}}.
$$

$$
m_5=\frac{1}{C_{p,\mathrm{gas}}}.
$$

These heat capacities are molar heat capacities when the amount is one mole. The stated geometrical interpretation of the **standard molar** transition enthalpies requires both one mole of pure substance and a pressure of 1 bar. For another amount, the plateau width represents the total heat required by that amount.

</div>

[← Thermodynamics worked problems]({{ '/physics/thermodynamics/' | relative_url }})
