---
layout: default
title: "Ideal-Gas Processes — Work, ΔU and ΔS"
meta-description: "Compare work, internal energy, and entropy for compressions of an ideal gas along different reversible paths. Includes theoretical recalls and full solution with notes."
permalink: /university/physics/thermodynamics/ideal-gas-processes/
nav_order: 22
background_image: /images/termodinamica.png
---

# Ideal-Gas Processes — Work, $\\Delta U$ and $\\Delta S$

<div class="content-box">

## Theoretical Background

- **Equation of state:** $pV = nRT$.  
- **Internal energy of an ideal gas:** $U = U(T)$, so $\\Delta U$ depends only on the temperature change.  
- **Isothermal process:** $\\Delta U = 0$.  
- **Work in a reversible isothermal:**  
  $$
  w = nRT \\ln\\!\\left( \\frac{V_2}{V_1} \\right).
  $$
- **Entropy change (reversible):**  
  $$
  \\Delta S = nR \\ln\\!\\left( \\frac{V_2}{V_1} \\right).
  $$
- **State vs path functions:** $\\Delta U$ and $\\Delta S$ depend only on initial and final states, while $w$ and $q$ depend on the path.

</div>

<div class="content-box">

## Exercise

A sample of $n = 100\\,\\text{mol}$ of ideal hydrogen at $T = 300\\,\\text{K}$ is compressed from  
$V_1 = 4.0\\,\\text{m}^3$ to $V_2 = 2.0\\,\\text{m}^3$.

Calculate the work **on** the gas along three different reversible paths:  

1. **(a)** Isobaric compression (at $p_1$) followed by isochoric cooling to the final state.  
2. **(b)** Direct isothermal compression from $V_1$ to $V_2$.  
3. **(c)** Isochoric heating to $p_2$, followed by isobaric compression at $p_2$.

Then evaluate $\\Delta U$ and $\\Delta S$, and compare results.

</div>

<div class="content-box">

## Step-by-Step Solution

**Step 1. Calculate initial and final pressures**  
From $pV = nRT$:
$$
p_1 = \\frac{nRT}{V_1}, \\quad p_2 = \\frac{nRT}{V_2}.
$$
With $nRT = 2.4942\\times 10^5\\,\\text{J}$,  
$p_2 = 2p_1$.

---

**Step 2. Work for each path**

- **(a) Isobaric (at $p_1$):**  
  $$
  w_a = p_1(V_2 - V_1) = nRT\\left(\\frac{V_2}{V_1} - 1\\right).
  $$
  Numerically: $w_a = 1.247\\times 10^5\\,\\text{J}$.

- **(b) Isothermal:**  
  $$
  w_b = nRT \\ln\\!\\left( \\frac{V_2}{V_1} \\right) = 2.4942\\times10^5\\, \\ln(0.5).
  $$
  $w_b = 1.729\\times 10^5\\,\\text{J}$.

- **(c) Isobaric (at $p_2$):**  
  $$
  w_c = p_2(V_2 - V_1) = 2p_1(V_2 - V_1) = 2 w_a.
  $$
  $w_c = 2.494\\times 10^5\\,\\text{J}$.

---

**Step 3. Internal energy change**  
Since $T$ is the same at initial and final state:
$$
\\Delta U = 0.
$$

---

**Step 4. Entropy change**  
Use the isothermal reference (reversible):
$$
\\Delta S = nR \\ln\\!\\left( \\frac{V_2}{V_1} \\right).
$$
Numerically:
$$
\\Delta S = 100(8.314)\\ln(0.5) = -5.76\\times 10^2\\,\\text{J K}^{-1}.
$$

</div>

<div class="content-box">

## Notes and Discussion

- The **work** depends on the path:  
  $w_a < w_b < w_c$.  
  This illustrates that work is **path-dependent**.

- The **internal energy** change is zero for all cases because $U$ of an ideal gas depends only on $T$.

- The **entropy** decreases, consistent with the system becoming more ordered upon compression.  
  This is a **state function**, so the same value emerges regardless of path.

- **Important remark (Ruzzi):**  
  Always check whether $\\Delta U=0$ holds:  
  it is true here because the process is isothermal and the gas is ideal. For real gases this statement is **not exact**.

</div>
