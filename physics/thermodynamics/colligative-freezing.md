---
layout: default
date: 2026-08-29
title: "Freezing Point Depression — Formula and Solved Example"
description: "Freezing point depression explained with ΔTf = iKfm: meaning of Kf, molality and the van ’t Hoff factor, validity conditions, and a solved NaCl example."
permalink: /physics/thermodynamics/colligative-freezing/
redirect_from:
  - /university/physics/thermodynamics/colligative-freezing/
nav_order: 26
background_image: /images/termodinamica.png
area: physics
topic: thermodynamics
content_type: solved-exercises
---

# Freezing Point Depression: Formula and Solved Example

<div class="content-box">

## What Is Freezing Point Depression?

Freezing point depression is the decrease in a solvent's freezing temperature when a solute is dissolved in it. It is a **colligative property** because, for a dilute ideal solution, the effect depends on the number of dissolved particles rather than on their chemical identity.

Dissolved particles lower the chemical potential of the liquid solvent. Equilibrium between the liquid and solid phases is therefore reached at a lower temperature.

Other colligative properties include vapor-pressure lowering, boiling-point elevation, and osmotic pressure.

### Freezing Point Depression Formula

The magnitude of the freezing point depression is

$$
\Delta T_f = i K_f \, m
$$

where:

- $\Delta T_f$ is the decrease in freezing temperature;
- $i$ is the van ’t Hoff factor, representing the effective number of dissolved particles produced by each solute unit;
- $K_f$ is the cryoscopic or molal freezing-point-depression constant of the solvent;
- $m$ is the molality of the solute.

For water,

$$
K_f = 1.86\,\mathrm{K\,kg\,mol^{-1}}.
$$

Molality is defined as

$$
m = \frac{n_{\text{solute}}}{m_{\text{solvent}}(\mathrm{kg})}.
$$

### When Does the Formula Apply?

The relation $\Delta T_f=iK_fm$ is a dilute-solution approximation. It applies when:

- the solute is effectively nonvolatile;
- the solution is sufficiently dilute and behaves approximately ideally;
- solvent and solute do not undergo a chemical reaction that changes the species present;
- $K_f$ is the constant for the chosen solvent;
- the factor $i$ represents the effective number of dissolved particles, including dissociation or association.

</div>

<div class="content-box">

## How to Calculate Freezing Point Depression: Solved Example

A solution is prepared by dissolving **10.0 g of NaCl** in **200 g of water**.  

1. Calculate the freezing point depression $\Delta T_f$.  
2. Assume complete dissociation of NaCl.  
3. Use $K_f(\text{H}_2O) = 1.86\, K\,kg\,mol^{-1}$.

</div>

<div class="content-box">

## Step-by-Step Solution

**Step 1. Moles of solute**  
Molar mass NaCl = $58.44\, g\,mol^{-1}$  
$$
n = \frac{10.0}{58.44} = 0.171\, mol
$$

---

**Step 2. Molality**  
Mass of solvent = $200 g = 0.200 kg$  
$$
m = \frac{0.171}{0.200} = 0.855\, mol\,kg^{-1}
$$

---

**Step 3. van ’t Hoff factor**  
NaCl dissociates ideally into 2 ions ($Na^+, Cl^-$), so:  
$$
i = 2
$$

Effective molality:  
$$
m_{\text{eff}} = i m = 2 \times 0.855 = 1.71\, mol\,kg^{-1}
$$

---

**Step 4. Freezing point depression**  
$$
\Delta T_f = K_f m_{\text{eff}} = (1.86)(1.71) = 3.18\, K
$$

So the new freezing point is:  
$$
T_f = 273.15 - 3.18 = 269.97\,K \;\approx -3.2^\circ C
$$

</div>

<div class="content-box">

## Notes

- The assumption of **complete dissociation** is an idealization; in real solutions the van ’t Hoff factor $i$ is slightly less than 2 due to **ion pairing**.  
- Colligative properties provide a powerful experimental tool to determine **molar masses** of solutes or to estimate their **degree of dissociation**.  
- This case illustrates why adding salt lowers the freezing point of water — the scientific basis of **road de-icing** in winter and of **antifreeze mixtures** in car engines.  

</div>

---

### Related topics  
- [Ideal-Gas Processes — Work, ΔU and ΔS](/physics/thermodynamics/ideal-gas-processes/)  
- [Reaction Energetics — Internal Energy and Enthalpy](/physics/thermodynamics/reaction-energetics/)  
- [Entropy in Adiabatic Transformations](/physics/thermodynamics/entropy-adiabatic/)  
- [Equilibrium & Spontaneity — ΔG°, K, Temperature](/physics/thermodynamics/equilibrium-and-spontaneity/)  
- [Phase Transitions — Heating Curve and Enthalpy Changes](/physics/thermodynamics/phase-transitions/)  
- [Gibbs Free Energy for Incompressible Substances](/physics/thermodynamics/gibbs-free-energy/)  

[**← Back to Thermodynamics**]({{ "/physics/thermodynamics/" | relative_url }})
