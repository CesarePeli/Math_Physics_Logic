---
layout: default
title: "Reaction Energetics — ΔU from ΔH"
meta-description: "Compute the internal‑energy change from enthalpy data: ΔU = ΔH − RT·Δn for ideal gases. Worked example for 2 NO(g) + O2(g) → 2 NO2(g)."
permalink: /university/physics/thermodynamics/reaction-energetics/
nav_order: 23
background_image: /images/termodinamica.png
---


# Reaction Energetics — $\Delta U$ from $\Delta H$


<div class="content-box">


### Theoretical Background
For ideal gases: $H = U + nRT$. For a reaction at constant $T$:
$$
\Delta U = \Delta H - RT\,\Delta n,\qquad \Delta n = n_{\text{gas,prod}} - n_{\text{gas,react}}.
$$


</div>


<div class="content-box">


## Exercise — Internal energy change of NO oxidation (298.15 K)
For $2\,\mathrm{NO}(g) + \mathrm{O}_2(g) \to 2\,\mathrm{NO}_2(g)$, use $\Delta H_f^\circ(\mathrm{NO})=+90.2\,\text{kJ mol}^{-1}$ and $\Delta H_f^\circ(\mathrm{NO}_2)=+33.2\,\text{kJ mol}^{-1}$ to compute $\Delta U^\circ$.


**Solution.**
$$
\Delta H^\circ = 2\,\Delta H_f^\circ(\mathrm{NO}_2) - [2\,\Delta H_f^\circ(\mathrm{NO}) + \Delta H_f^\circ(\mathrm{O}_2)] = 2(33.2) - 2(90.2) = -114\,\text{kJ mol}^{-1}.
$$
Gas moles change: $\Delta n = 2 - 3 = -1$. Thus
$$
\Delta U^\circ = \Delta H^\circ - RT\,\Delta n \approx -114\,\text{kJ mol}^{-1} - (8.314\times10^{-3}\,\text{kJ K}^{-1}\text{mol}^{-1})(298.15\,\text{K})(-1) \approx -111.5\,\text{kJ mol}^{-1}.
$$


</div>