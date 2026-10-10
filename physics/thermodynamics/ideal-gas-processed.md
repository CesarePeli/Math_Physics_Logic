---
layout: default
title: "Ideal-Gas Processes — Work, Heat and State Functions"
author: Marco Ruzzi
description: "Isothermal expansion, pressure-volume work and compression along three paths: worked ideal-gas exercises with internal-energy and entropy calculations."
permalink: /physics/thermodynamics/ideal-gas-processes/
redirect_from:
  - /university/physics/thermodynamics/ideal-gas-processes/
nav_order: 22
background_image: /images/termodinamica.png
last_modified_at: 2026-10-10
---

# Ideal-Gas Processes — Work, Heat and State Functions

<div class="content-box">

*By Prof. Marco Ruzzi.*

## Theoretical background

The sign convention is ΔU=q+w: heat absorbed and work done on the system are positive. For an ideal gas, pV=nRT and U depends only on temperature. An isothermal change therefore gives ΔU=0.

At constant external pressure:

$$
w=-p_0(V_f-V_i).
$$

For a reversible isothermal ideal-gas process:

$$
w=-nRT\ln\left(\frac{V_f}{V_i}\right).
$$

Between ideal-gas states at the same temperature:

$$
\Delta S=nR\ln\left(\frac{V_f}{V_i}\right).
$$

</div>

<div class="content-box">

## Exercise 1 — Irreversible isothermal expansion

Determine the relation between pressure–volume work, absorbed heat and internal-energy change during an irreversible isothermal expansion of an ideal gas. Compare it with the reversible case.

### Solution

Work is not a state function. It depends on the path, that is, on how the transformation is performed.

For an ideal gas U depends only on temperature. During an isothermal expansion both T and U remain constant. The First Law also applies to irreversible transformations:

$$
\Delta U=q+w=0.
$$

$$
w=-q.
$$

The change in internal energy is zero, whereas expansion against a nonzero opposing pressure involves negative work and positive absorbed heat.

### Observations

For the ideal-gas model, U is a function of T alone, so an isothermal transformation leaves it unchanged. The decrease in internal energy that expansion work would produce by itself is compensated by the increase due to heat absorption:

$$
\Delta U=q+w=0.
$$

In particular, for a **reversible** isothermal expansion:

$$
w=-q=-nRT\ln\left(\frac{V_f}{V_i}\right),\qquad V_f>V_i.
$$

The work is negative because the system does work on its surroundings. Without heat absorption, that work would reduce its internal energy. The heat is positive because it is absorbed: without the work done by the system, it would increase its internal energy. The logarithmic work expression must not be used for an arbitrary irreversible path.

</div>

<div class="content-box">

## Exercise 3 — Work at constant external pressure

Discuss pressure–volume work for a real gas expanding against constant external pressure, the heat–work balance in an isothermal ideal-gas expansion, and the conditions needed to write the expansion work of a gas produced by a reaction as w=−nRT.

### Solution

Deriving the work expression at constant external pressure does not require reversibility:

$$
w=-\int_{V_i}^{V_f}p_0\,dV=-p_0\Delta V.
$$

For an isothermal ideal-gas expansion, U=U(T); constant T therefore gives ΔU=0 and q+w=0.

To derive w=−nRT, consider expansion against constant p₀, with the initial gas volume negligible and the final gas pressure equal to p₀, the derivation is:

$$
w=-p_0(V_f-V_i)\simeq-p_0V_f.
$$

Using the **ideal-gas** equation p<sub>f</sub>V<sub>f</sub>=nRT:

$$
w\simeq-p_0\frac{nRT}{p_f}=-nRT.
$$

The ideal equation of state is essential to that last substitution. It cannot be applied as stated to a real gas.

</div>

<div class="content-box">

## Problem — Compression along three paths

A compression takes 100 mol of H₂, treated as an ideal gas, from (p₁, 4 m³, 300 K) to (p₂, 2 m³, 300 K).

1. Determine the total work done **on** the gas for: **(a)** an isobaric process followed by an isochoric process; **(b)** an isothermal process; **(c)** an isochoric process followed by an isobaric process.
2. Determine ΔU and ΔS in each case.
3. Discuss the results in terms of state functions.

### 1. Work along the paths

The three paths are shown in the p–V diagram. They are treated as reversible paths for the work calculations.

<a href="{{ '/images/ruzzi/compression-paths.png' | relative_url }}"><img src="{{ '/images/ruzzi/compression-paths.png' | relative_url }}" alt="Pressure-volume diagram of three compression paths: isobaric then isochoric, isothermal, and isochoric then isobaric" style="display:block;width:100%;max-width:420px;height:auto;margin:1.2rem auto;background:#fff;padding:12px;box-sizing:border-box;"></a>

[View the diagram at full size]({{ '/images/ruzzi/compression-paths.png' | relative_url }}).

V₁=2V₂ and V₂<V₁. All three processes are compressions, so positive work is expected: it is done on the system.

$$
p_1=\frac{nRT}{V_1}.
$$

$$
p_2=\frac{nRT}{V_2}=\frac{2nRT}{V_1}=2p_1.
$$

$$
nRT=(100)(8.314)(300)=249.420\times10^3\ \mathrm{J}.
$$

**Path (a).** The isochoric stage contributes no work:

$$
w_a=-p_1(V_2-V_1)+0.
$$

$$
w_a=-nRT\left(\frac{V_2}{V_1}-1\right).
$$

$$
w_a=+124.71\times10^3\ \mathrm{J}.
$$

**Path (b).** For the reversible isothermal compression:

$$
w_b=-nRT\ln\left(\frac{V_2}{V_1}\right).
$$

$$
w_b=-(249.420\times10^3)\ln(1/2)\ \mathrm{J}.
$$

$$
w_b\simeq+172.885\times10^3\ \mathrm{J}.
$$

**Path (c).** The first, isochoric stage contributes no work; the compression takes place at p₂:

$$
w_c=0-p_2(V_2-V_1)=2w_a.
$$

$$
w_c=+249.42\times10^3\ \mathrm{J}.
$$

### 2. Internal energy and entropy

U and S are state functions, so their changes are the same for all three paths. They can be evaluated along the isothermal path:

$$
\Delta U=0.
$$

$$
\Delta S=nR\ln\left(\frac{V_2}{V_1}\right).
$$

$$
\Delta S=(100)(8.314)\ln(1/2)\ \mathrm{J\,K^{-1}}.
$$

$$
\Delta S\simeq-576.28\ \mathrm{J\,K^{-1}}.
$$

### 3. State functions and path dependence

ΔU and ΔS can be calculated without knowing the actual path, because the endpoints determine them:

$$
\Delta U_a=\Delta U_b=\Delta U_c.
$$

$$
\Delta S_a=\Delta S_b=\Delta S_c.
$$

Work is not a state function: wₐ, w<sub>b</sub> and w<sub>c</sub> differ. For reversible processes its magnitude is the area under the p(V) curve. The diagram therefore gives:

$$
w_a<w_b<w_c.
$$

</div>

[← Thermodynamics worked problems]({{ '/physics/thermodynamics/' | relative_url }})
