---
layout: default
title: "Reaction Energetics — Internal Energy and Enthalpy"
meta-description: "Worked example on the energetics of a chemical reaction: relation between ΔU and ΔH, step-by-step calculations, and key thermodynamic notes."
permalink: /university/physics/thermodynamics/reaction-energetics/
nav_order: 23
background_image: /images/termodinamica.png
---

# Reaction Energetics — Internal Energy and Enthalpy

<div class="content-box">

## Theoretical Background

- **First Law of Thermodynamics:**  
  $$
  \Delta U = q + w
  $$

- **Enthalpy definition:**  
  $$
  H = U + pV \;\Rightarrow\; \Delta H = \Delta U + \Delta(pV)
  $$

- For reactions at constant $(T,p)$:  
  $$
  \Delta H = q_p
  $$

- Connection between $\Delta H$ and $\Delta U$ (ideal gases):  
  $$
  \Delta H = \Delta U + (\Delta n_{\text{gas}})RT
  \qquad \Rightarrow \qquad
  \Delta U = \Delta H - (\Delta n_{\text{gas}})RT
  $$

> **Validity note (ideal-gas assumption).**  
> The identities above use $pV = nRT$; the correction $(\Delta n_{\text{gas}})RT$ applies when the **gas phase behaves ideally**. For real gases, use an appropriate equation of state (the simple $RT\,\Delta n$ term no longer holds exactly).

> **Sign convention used here.**  
> $w>0$ = work **done on** the system (compression); $w<0$ = work **done by** the system (expansion). The First Law is written as $\Delta U = q + w$.
  
where $\Delta n_{\text{gas}}$ is the change in the number of moles of gas.

</div>

<div class="content-box">

## Exercise

Consider the combustion of carbon monoxide:

$$
2\,\mathrm{CO}(g) + \mathrm{O}_2(g) \;\longrightarrow\; 2\,\mathrm{CO}_2(g)
$$

At $T = 298\,\text{K}$ and $p = 1\,\text{bar}$, the standard enthalpy of reaction is:

$$
\Delta H^{\circ} = -566.0\,\text{kJ mol}^{-1}
$$

**Tasks:**

1. Calculate the standard internal energy change $\Delta U^{\circ}$.  
2. Explain the relation between $\Delta U$ and $\Delta H$ for reactions involving gases.

</div>

<div class="content-box">

## Step-by-Step Solution

**Step 1. Count moles of gas**  
- Reactants: $n_{\text{gas}} = 2 + 1 = 3$  
- Products: $n_{\text{gas}} = 2$  

So:
$$
\Delta n_{\text{gas}} = n_{\text{prod}} - n_{\text{reag}} = 2 - 3 = -1
$$

---

**Step 2. Relation between $\Delta H$ and $\Delta U$**  
For ideal gases:
$$
\Delta U = \Delta H - (\Delta n_{\text{gas}})RT
$$

---

**Step 3. Insert data**  
With $T = 298\,\text{K}$ and $R = 8.314\,\text{J mol}^{-1}\text{K}^{-1}$:
$$
(\Delta n_{\text{gas}})RT = (-1)(8.314)(298) = -2.48 \times 10^{3}\,\text{J} = -2.48\,\text{kJ}
$$

---

**Step 4. Final value**  
$$
\Delta U^{\circ} = (-566.0)\,\text{kJ mol}^{-1} - (-2.48)\,\text{kJ mol}^{-1}
= -563.5\,\text{kJ mol}^{-1}.
$$

---

**Answer:**  
$$
\Delta U^{\circ} = -563.5\,\text{kJ mol}^{-1}
$$

</div>

<div class="content-box">

## Notes

- The difference between $\Delta U$ and $\Delta H$ is small here because only **1 mol of gas disappears**.  
- If $\Delta n_{\text{gas}} = 0$, then $\Delta H = \Delta U$.  
- The correction $(\Delta n_{\text{gas}})RT$ grows with $T$ and with large changes in gas moles.  
- **Pedagogical point:** $\Delta H$ is often tabulated (easy to measure at constant $p$), while $\Delta U$ is the central state function in the First Law.  
- **Real-gas reminder:** for non‑ideal gases the simple $RT\,\Delta n$ correction is only approximate; use the appropriate equation of state if accuracy is required.

</div>

---

### Related topics  
- [Ideal-Gas Processes — Work, ΔU and ΔS](/university/physics/thermodynamics/ideal-gas-processes/)  
- [Entropy in Adiabatic Transformations](/university/physics/thermodynamics/entropy-adiabatic/)  
- [Equilibrium & Spontaneity — ΔG°, K, Temperature](/university/physics/thermodynamics/equilibrium-and-spontaneity/)  
- [Colligative Properties — Freezing Point Depression](/university/physics/thermodynamics/colligative-freezing/)  
- [Gibbs Free Energy for Incompressible Substances](/university/physics/thermodynamics/gibbs-incompressible/)  
- [Phase Transitions — Heating Curve and Enthalpy Changes](/university/physics/thermodynamics/phase-transitions/)  
