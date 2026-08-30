---
layout: default
title: "Equilibrium & Spontaneity — ΔG°, K, Temperature"
meta-description: "From ΔH° and ΔS° to ΔG° and K: compute Kp at 298 K, decide the reaction direction from standard conditions, and discuss temperature effects."
permalink: /physics/thermodynamics/equilibrium-and-spontaneity/
redirect_from:
  - /university/physics/thermodynamics/equilibrium-and-spontaneity/
nav_order: 25
background_image: /images/termodinamica.png
---

# Equilibrium & Spontaneity — $\Delta G^\circ$, $K$, Temperature

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

- For gas-phase reactions, the pressure-based constant (with $p_0=1\,\text{bar}$) is
  $$
  K_p=\frac{\left(\dfrac{p_{\text{NO}_2}}{p_0}\right)^2}{\left(\dfrac{p_{\text{NO}}}{p_0}\right)^2\left(\dfrac{p_{\text{O}_2}}{p_0}\right)}.
  $$
  Because each pressure is divided by the standard pressure, this definition of $K_p$ is dimensionless.

- For a system with reaction quotient $Q$,
  $
  \Delta G_r=\Delta G_r^\circ+RT\ln Q.
  $
  Thus, $\Delta G_r^\circ<0$ implies spontaneous progress toward products when $Q=1$; it does not determine the direction for every possible composition. If $K\gg1$, equilibrium is strongly product-favored.  

- Temperature effect (van ’t Hoff):  
  $$
  \frac{d\ln K}{dT}=\frac{\Delta H_r^\circ}{RT^2}
  $$
  For exothermic reactions $(\Delta H_r^\circ<0)$, $K$ decreases as $T$ increases.

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
Since every partial pressure is divided by $p_0$, the value of $K_p$ obtained from this expression is dimensionless.

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
> Since standard-state conditions correspond to $Q=1$, the negative value of $\Delta G_r^\circ$ indicates spontaneous progress toward products from that composition.

---

**4) Convert $\Delta G_r^\circ$ into $K_p$.**  
With $R=8.314\,\text{J mol}^{-1}\text{K}^{-1}$:
$$
K_p=\exp\!\left[-\frac{\Delta G_r^\circ}{RT}\right]
=\exp\!\left(\frac{70.8\times10^3}{(8.314)(298.15)}\right)
=\exp(28.56)\approx 2.5\times10^{12}.
$$
> Such a large $K_p$ means that equilibrium is strongly product-favored. The individual equilibrium partial pressures still depend on the initial composition and the total pressure.

---

**5) Direction from standard conditions.**  
Because $\Delta G_r^\circ<0$, the forward reaction is spontaneous when $Q=1$. Since $K_p\gg1$, equilibrium is strongly shifted toward $\mathrm{NO}_2$.

---

**6) Temperature effect (sign analysis).**  
Here $\Delta H_r^\circ<0$ (exothermic) and $\Delta S_r^\circ<0$ (gas moles decrease: $3\to2$).  
Increasing $T$ makes $-T\Delta S_r^\circ$ more **positive**, so $\Delta G_r^\circ$ becomes less negative. If $\Delta H_r^\circ$ and $\Delta S_r^\circ$ are treated as approximately constant, it becomes positive above about $786\,\text{K}$. The decrease of $K_p$ with temperature is consistent with the van ’t Hoff equation.

</div>

<div class="content-box">

## Conceptual notes

- The negative value of $\Delta S_r^\circ$ is consistent with the decrease from three to two moles of gas. The change in gas-mole count is a useful qualitative guide, while the numerical value comes from standard molar entropies.  
- Standard formation data reminder: $\Delta H_f^\circ(\mathrm{O}_2,g)=0$ by convention; only $\mathrm{NO}$ and $\mathrm{NO_2}$ contribute to $\Delta H_r^\circ$.  
- The value $K_p\sim10^{12}$ at $298\,\text{K}$ shows that equilibrium is strongly product-favored; it does not by itself determine each equilibrium partial pressure.  
- For different $T$, you may estimate $K_p(T)$ using the van ’t Hoff equation with (piecewise) constant $\Delta H_r^\circ$ in the temperature range of interest.  
- A complete interpretation uses both numerical values ($\Delta G^\circ$, $K$) and the signs of $\Delta H^\circ$ and $\Delta S^\circ$, while distinguishing standard-state spontaneity from the direction at an arbitrary composition.

</div>

---

### Related topics
- [Ideal-Gas Processes — Work, ΔU and ΔS](/physics/thermodynamics/ideal-gas-processes/)  
- [Reaction Energetics — Internal Energy and Enthalpy](/physics/thermodynamics/reaction-energetics/)  
- [Entropy in Adiabatic Transformations](/physics/thermodynamics/entropy-adiabatic/)  
- [Colligative Properties — Freezing Point Depression](/physics/thermodynamics/colligative-freezing/)  
- [Gibbs Free Energy for Incompressible Substances](/physics/thermodynamics/gibbs-free-energy/)  
- [Phase Transitions — Heating Curve and Enthalpy Changes](/physics/thermodynamics/phase-transitions/)  
