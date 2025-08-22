---
layout: default
title: "Colligative Properties — Freezing Point Depression"
meta-description: "Worked example on freezing point depression as a colligative property. Includes theoretical recalls, full calculation, and explanatory notes."
permalink: /university/physics/thermodynamics/colligative-freezing/
nav_order: 26
background_image: /images/termodinamica.png
---

# Colligative Properties — Freezing Point Depression

<div class="content-box">

## Theoretical Background

- **Colligative properties** depend only on the **number of solute particles**, not on their nature.  
- For freezing point depression:  
  $$
  \Delta T_f = K_f \, m
  $$
  where:  
  - $\Delta T_f$ = freezing point lowering  
  - $K_f$ = cryoscopic constant of solvent  
  - $m$ = molality of solute  

- **Molality**:  
  $$
  m = \frac{n_{\text{solute}}}{m_{\text{solvent}}(kg)}
  $$

</div>

<div class="content-box">

## Exercise

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
NaCl dissociates into 2 ions ($Na^+, Cl^-$), so:  
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

- The assumption of **complete dissociation** is an idealization; in reality the van ’t Hoff factor $i$ is slightly less than 2 due to ion pairing.  
- Colligative properties are a key tool to estimate **molar masses** or **degree of dissociation** experimentally.  
- This simple case illustrates how adding salt lowers the freezing point of water — the basis of antifreeze and de-icing processes.

</div>

---

### Related topics  
- [Ideal-Gas Processes — Work, ΔU and ΔS](/university/physics/thermodynamics/ideal-gas-processes/)  
- [Reaction Energetics — Internal Energy and Enthalpy](/university/physics/thermodynamics/reaction-energetics/)  
- [Entropy in Adiabatic Transformations](/university/physics/thermodynamics/entropy-adiabatic/)  
- [Equilibrium & Spontaneity — ΔG°, K, Temperature](/university/physics/thermodynamics/equilibrium-and-spontaneity/)  
