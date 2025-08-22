---
layout: default
title: "Equilibrium & Spontaneity — ΔG°, K, Temperature"
meta-description: "From ΔH° and ΔS° to ΔG° and K: compute Kp at 298 K, decide the reaction direction from standard conditions, and discuss temperature effects."
permalink: /university/physics/thermodynamics/equilibrium-and-spontaneity/
nav_order: 25
background_image: /images/termodinamica.png
---

# Equilibrium & Spontaneity — $\Delta G^\circ$, $K$, Temperature

<div class="content-box">

## Theoretical background (quick recall)

- Standard Gibbs criterion: $\,\Delta G_r^\circ = \Delta H_r^\circ - T\Delta S_r^\circ$.  
- Link to equilibrium: $\,\Delta G_r^\circ = -RT\ln K \;\Rightarrow\; K=\exp\!\big[-\Delta G_r^\circ/(RT)\big]$.  
- For gas-phase reactions, the pressure-based constant (with $p_0=1\,\text{bar}$) is
  $$
  K_p=\frac{\left(\dfrac{p_{\text{NO}_2}}{p_0}\right)^2}{\left(\dfrac{p_{\text{NO}}}{p_0}\right)^2\left(\dfrac{p_{\text{O}_2}}{p_0}\right)}.
  $$
  Equivalently, $K_p=K_c\,(RT)^{\Delta n_\text{gas}}$ with $\Delta n_\text{gas}=\sum\nu_\text{products}-\sum\nu_\text{reactants}$.  
- Direction from standard conditions: if $\Delta G_r^\circ<0$ at $T$, the reaction is spontaneous toward products; if $K\gg1$, products strongly prevail at equilibrium.  
- Temperature effect (van ’t Hoff): $\dfrac{d\ln K}{dT}=\dfrac{\Delta H_r^\circ}{RT^2}$. For exothermic reactions $(\Delta H_r^\circ<0)$, $K$ decreases as $T$ increases.

</div>

<div class="content-box">

## Exercise — Oxidation of NO: $K_p$ and direction of spontaneity

For
$$
2\,\mathrm{NO}(g)+\mathrm{O}_2(g)\;\rightleftharpoons\;2\,\mathrm{NO}_2(g)
$$
at $T=298.15\,\text{K}$, use  
$\Delta H_f^\circ(\mathrm{NO})=+90.2\,\text{kJ mol}^{-1}$,  
$\Delta H_f^\circ(\mathrm{NO}_2)=+33.2\,\text{kJ mol}^{-1}$, and  
$\Delta S_r^\circ=-145.0\,\text{J mol}^{-1}\,\text{K}^{-1}$  

to evaluate $\Delta G_r^\circ$, then $K_p$. State the spontaneous direction from standard conditions and discuss the effect of increasing temperature.

</div>

<div class="content-box">

## Step-by-step solution (with explanations)

**1) Write $K_p$ (definition).**  
Using partial pressures normalized by $p_0=1\,\text{bar}$:
$$
K_p=\frac{\left(\dfrac{p_{\text{NO}_2}}{p_0}\right)^2}{\left(\dfrac{p_{\text{NO}}}{p_0}\right)^2\!\left(\dfrac{p_{\text{O}_2}}{p_0}\right)}.
$$
Here $\Delta n_\text{gas}=2-(2+1)=-1$, so $K_p=K_c\,(RT)^{-1}$.

---

**2) Compute $\Delta H_r^\circ$ from formation enthalpies.**  
Remember $\Delta H_f^\circ(\mathrm{O}_2,g)=0$:
$$
\Delta H_r^\circ=2\,\Delta H_f^\circ(\mathrm{NO}_2)-\big[2\,\Delta H_f^\circ(\mathrm{NO})+1\cdot\Delta H_f^\circ(\mathrm{O}_2)\big]
=2(33.2)-2(90.2)= -114.0\,\text{kJ mol}^{-1}.
$$

---

**3) Compute $\Delta G_r^\circ$ at $298.15\,\text{K}$.**  
Use $\Delta S_r^\circ=-145.0\,\text{J mol}^{-1}\,\text{K}^{-1}=-0.145\,\text{kJ mol}^{-1}\,\text{K}^{-1}$:
$$
\Delta G_r^\circ=\Delta H_r^\circ-T\Delta S_r^\circ
= -114.0 - (298.15)(-0.145)
\approx -70.8\,\text{kJ mol}^{-1}.
$$

---

**4) Convert $\Delta G_r^\circ$ into $K_p$.**  
With $R=8.314\,\text{J mol}^{-1}\text{K}^{-1}$:
$$
K_p=\exp\!\left[-\frac{\Delta G_r^\circ}{RT}\right]
=\exp\!\left(\frac{70.8\times10^3}{(8.314)(298.15)}\right)
=\exp(28.56)\approx 2.5\times10^{12}.
$$

---

**5) Direction from standard conditions.**  
Because $\Delta G_r^\circ<0$ and $K_p\gg1$, the reaction is spontaneous toward **products** from standard-state reactants; equilibrium lies far to the side of $\mathrm{NO}_2$.

---

**6) Temperature effect (sign analysis).**  
Here $\Delta H_r^\circ<0$ (exothermic) and $\Delta S_r^\circ<0$ (gas moles decrease: $3\to2$).  
Increasing $T$ makes $-T\Delta S_r^\circ$ more **positive**, so $\Delta G_r^\circ$ becomes **less negative** (eventually positive at high $T$): the reaction is **less favorable** as temperature increases, and $K_p$ decreases with $T$ (consistent with van ’t Hoff and Le Châtelier).

</div>

<div class="content-box">

## Conceptual notes

- Why $\Delta S_r^\circ<0$ here? Gas-phase stoichiometry gives $\Delta n_\text{gas}=-1$: fewer gas moles at products generally implies lower entropy of the system.  
- Standard formation data reminder: $\Delta H_f^\circ(\mathrm{O}_2,g)=0$ by convention; only $\mathrm{NO}$ and $\mathrm{NO_2}$ contribute to $\Delta H_r^\circ$.  
- Large $K_p$ ($\sim10^{12}$ at $298\,\text{K}$) means that, at equilibrium, $p_{\text{NO}_2}$ dominates compared to $p_{\text{NO}}$ and $p_{\text{O}_2}$ under standard-state scaling.  
- For different $T$, you may estimate $K_p(T)$ using the van ’t Hoff equation with (piecewise) constant $\Delta H_r^\circ$ in the temperature range of interest.

</div>

---

### Related topics
- [Ideal-Gas Processes — Work, ΔU and ΔS](/university/physics/thermodynamics/ideal-gas-processes/)  
- [Reaction Energetics — Internal Energy and Enthalpy](/university/physics/thermodynamics/reaction-energetics/)  
- [Entropy in Adiabatic Transformations](/university/physics/thermodynamics/entropy-adiabatic/)  
- [Colligative Properties — Freezing Point Depression](/university/physics/thermodynamics/colligative-freezing/)  
- [Gibbs Free Energy for Incompressible Substances](/university/physics/thermodynamics/gibbs-incompressible/)  
- [Phase Transitions — Heating Curve and Enthalpy Changes](/university/physics/thermodynamics/phase-transitions/)  

