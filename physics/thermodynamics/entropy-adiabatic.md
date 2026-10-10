---
layout: default
date: 2026-08-29
title: "Entropy in Adiabatic Transformations"
seo_title: "Is Entropy Constant in an Adiabatic Process? Explained"
last_modified_at: 2026-10-10
author: Marco Ruzzi
permalink: /physics/thermodynamics/entropy-adiabatic/
redirect_from:
  - /university/physics/thermodynamics/entropy-adiabatic/
background_image: "/images/termodinamica.png"
description: "Is entropy constant in an adiabatic process? Compare reversible and irreversible transformations using entropy balances and worked thermodynamics examples."
area: physics
topic: thermodynamics
content_type: solved-exercise
---

# Entropy in Adiabatic Transformations

<div class="content-box">

*By Prof. Marco Ruzzi.*

## Theoretical background

The entropy balance for the system and its surroundings is:

$$
\Delta S_{\mathrm{tot}}=\Delta S+\Delta S_{\mathrm{surr}}.
$$

For a reversible transformation ΔS<sub>tot</sub>=0. For an irreversible transformation ΔS<sub>tot</sub>>0. In the adiabatic processes considered here there is no heat exchange with the surroundings; their entropy change is zero.

</div>

<div class="content-box">

## Exercise 4 — Reversible adiabatic process

Determine the entropy change of a system undergoing a reversible adiabatic transformation. Compare it with an irreversible adiabatic transformation and explain why the result is consistent with entropy being a state function.

### Solution

Reversibility gives:

$$
\Delta S_{\mathrm{tot}}=0.
$$

For the adiabatic process, q<sub>surr</sub>=0 and the surroundings are taken at constant volume, so:

$$
\Delta S_{\mathrm{surr}}=0.
$$

Consequently:

$$
\Delta S_{\mathrm{tot}}=\Delta S+0=0.
$$

$$
\Delta S=0.
$$

A reversible adiabatic transformation therefore does not produce a positive entropy change.

### Irreversible adiabatic transformations

For an irreversible adiabatic transformation the surroundings still exchange no heat, and their entropy remains unchanged under the same assumptions. The entropy balance is now:

$$
\Delta S_{\mathrm{tot}}=\Delta S+0>0.
$$

$$
\Delta S>0.
$$

The contrast between ΔS>0 for an irreversible adiabatic process and ΔS=0 for a reversible one might seem inconsistent with S being a state function. There is no contradiction. Starting from the same initial state, the irreversible adiabatic process cannot reach the same final state as a reversible adiabatic process: their entropy changes differ, and therefore their endpoints differ.

</div>

[← Thermodynamics worked problems]({{ '/physics/thermodynamics/' | relative_url }})
