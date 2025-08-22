---
layout: default
title: "Ideal‑Gas Processes — Work, ΔU and ΔS"
meta-description: "Compare work, internal energy, and entropy for compressions of an ideal gas along different reversible paths. State vs path functions with a fully worked example."
permalink: /university/physics/thermodynamics/ideal-gas-processes/
nav_order: 22
background_image: /images/termodinamica.png
---


# Ideal‑Gas Processes — Work, $\Delta U$ and $\Delta S$


<div class="content-box">


### Theoretical Background
For an ideal gas, $U=U(T)$. Along an isothermal transformation $\Delta U=0$. A reversible isothermal entropy change is $\Delta S = nR\,\ln(V_2/V_1)$.


</div>


<div class="content-box">


## Exercise — Same endpoints, different reversible paths
A sample of $n=100\,\text{mol}$ ideal hydrogen at $T=300\,\text{K}$ is compressed from $V_1=4\,\text{m}^3$ to $V_2=2\,\text{m}^3$.


Compute the total work **on** the gas for three reversible paths: (a) isobaric then isochoric; (b) single isothermal step; (c) isochoric then isobaric. Then find $\Delta U$ and $\Delta S$, and discuss.


**Solution.** With $p_1=nRT/V_1$, $p_2=nRT/V_2=2p_1$, and $nRT=2.4942\times10^5\,\text{J}$:
- (a) $w_a = p_1(V_2-V_1)= nRT[(V_2/V_1)-1] = +1.247\times10^5\,\text{J}$.
- (b) Isothermal: $w_b = nRT\ln(V_2/V_1) = nRT\ln(1/2) = +1.729\times10^5\,\text{J}$.
- (c) $w_c = p_2(V_2-V_1)=2p_1(V_2-V_1)=2w_a=+2.494\times10^5\,\text{J}$.


Isothermal $\Rightarrow \Delta U=0$ (ideal gas). Entropy change (reversible reference):
$$
\Delta S = nR\ln\!\left(\tfrac{V_2}{V_1}\right) = 100\,(8.314)\,\ln(1/2) = -5.763\times10^2\,\text{J K}^{-1}.
$$


**Discussion.** $U$ and $S$ are state functions (same values for all paths), while work depends on the path: $w_a < w_b < w_c$.


</div>