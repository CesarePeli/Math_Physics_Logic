---
layout: default
date: 2025-08-29
title: "Solved Exercises — Cauchy Problems"
meta-description: "Worked exercises on Cauchy problems: first- and second-order ODEs with initial conditions, solved step by step, including remarks from the original Italian text."
permalink: "/university/math/calculus-1/odes-cauchy/"
background_image: "/images/grafi.png"

---

<div class="content-box">

## Theoretical Recall

A **Cauchy problem** is an ODE together with **initial conditions**:

$$
\begin{cases}
y'(x) = F(x,y), \\
y(x_0) = y_0.
\end{cases}
$$

For higher order:
$$
\begin{cases}
y''+ay'+by=0, \\
y(x_0)=y_0,\; y'(x_0)=y_1.
\end{cases}
$$

**Theorem (Picard–Lindelöf, simplified):**  
If $F(x,y)$ is continuous and satisfies a Lipschitz condition in $y$, then the Cauchy problem has a **unique local solution**.

**Author’s note:** Solving consists of two steps: find the general solution of the ODE, then use the initial conditions to fix the constants.

</div>

<div class="content-box">

## Exercises

### Exercise 1
$$
\begin{cases}
y' = y, \\
y(0)=1.
\end{cases}
$$

**Solution:**  
General solution: $y=Ce^x$. Condition: $1=C e^0 \Rightarrow C=1$.  

**Final Result:**
$$
y(x)=e^x
$$

---

### Exercise 2
$$
\begin{cases}
y' = -2y, \\
y(0)=3.
\end{cases}
$$

**Solution:**  
General: $y=Ce^{-2x}$. Condition: $3=C$.  

**Final Result:**
$$
y(x)=3e^{-2x}
$$

---

### Exercise 3
$$
\begin{cases}
y' = x, \\
y(0)=0.
\end{cases}
$$

**Solution:**  
Integrate: $y=\tfrac{x^2}{2}+C$. Condition: $0=C$.  

**Final Result:**
$$
y(x)=\tfrac{x^2}{2}
$$

---

### Exercise 4
$$
\begin{cases}
y''-y=0, \\
y(0)=1,\; y'(0)=0.
\end{cases}
$$

**Solution:**  
Characteristic: $r^2-1=0$, roots $\pm1$. General $y=C_1e^x+C_2e^{-x}$.  
Conditions: $y(0)=C_1+C_2=1$, $y'(x)=C_1e^x-C_2e^{-x}$, so $y'(0)=C_1-C_2=0$.  
Thus $C_1=C_2=1/2$.  

**Final Result:**
$$
y(x)=\cosh x
$$

---

### Exercise 5
$$
\begin{cases}
y''+y=0, \\
y(0)=0,\; y'(0)=1.
\end{cases}
$$

**Solution:**  
General $y=C_1\cos x+C_2\sin x$. Conditions: $y(0)=C_1=0$, $y'(x)=-C_1\sin x+C_2\cos x$, so $y'(0)=C_2=1$.  

**Final Result:**
$$
y(x)=\sin x
$$

---

### Exercise 6
$$
\begin{cases}
y' - y = e^x, \\
y(0)=0.
\end{cases}
$$

**Solution:**  
Linear ODE. IF $=e^{-x}$. Then $(ye^{-x})' =1$. Integrate: $ye^{-x}=x+C$. So $y=(x+C)e^x$.  
Condition: $0=(0+C)e^0 \Rightarrow C=0$.  

**Final Result:**
$$
y(x)=x e^x
$$

---

### Exercise 7
$$
\begin{cases}
y''+4y=0, \\
y(0)=2,\; y'(0)=0.
\end{cases}
$$

**Solution:**  
Characteristic: $r^2+4=0$, roots $\pm2i$. General $y=C_1\cos(2x)+C_2\sin(2x)$.  
Conditions: $y(0)=C_1=2$, $y'(x)=-2C_1\sin(2x)+2C_2\cos(2x)$, $y'(0)=2C_2=0\Rightarrow C_2=0$.  

**Final Result:**
$$
y(x)=2\cos(2x)
$$

---

### Exercise 8
$$
\begin{cases}
y''-3y'+2y=0, \\
y(0)=1,\; y'(0)=1.
\end{cases}
$$

**Solution:**  
Characteristic $(r-1)(r-2)=0$, roots $1,2$. General $y=C_1e^x+C_2e^{2x}$.  
Conditions: $y(0)=C_1+C_2=1$, $y'(x)=C_1e^x+2C_2e^{2x}$, so $y'(0)=C_1+2C_2=1$.  
Subtract: $(C_1+2C_2)-(C_1+C_2)=C_2=0$. So $C_1=1$.  

**Final Result:**
$$
y(x)=e^x
$$

---

### Exercise 9
$$
\begin{cases}
y''+y' = 0, \\
y(0)=0,\; y'(0)=1.
\end{cases}
$$

**Solution:**  
Characteristic $r^2+r=0\Rightarrow r(r+1)=0$. Roots $0,-1$.  
General $y=C_1+C_2e^{-x}$.  
Derivative: $y'=-C_2e^{-x}$.  
Conditions: $y(0)=C_1+C_2=0$, $y'(0)=-C_2=1\Rightarrow C_2=-1$, $C_1=1$.  

**Final Result:**
$$
y(x)=1-e^{-x}
$$

---

### Exercise 10
$$
\begin{cases}
y' = y\cos x, \\
y(0)=1.
\end{cases}
$$

**Solution:**  
Equation separable: $dy/y=\cos x dx$. Integrate: $\ln y=\sin x+C$.  
So $y=Ce^{\sin x}$. Condition $y(0)=1 \Rightarrow C=1$.  

**Final Result:**
$$
y(x)=e^{\sin x}
$$

</div>

<div class="content-box">

## Related Pages in *Calculus I*

- [Complex Numbers](/university/math/calculus-1/complex-numbers/)  
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
- [Limits with L’Hôpital’s Rule](/university/math/calculus-1/limits-hopital/)  
- [Limits with Taylor Expansion](/university/math/calculus-1/limits-taylor/)  
- [Sequences](/university/math/calculus-1/sequences/)  
- [Series](/university/math/calculus-1/series/)  
- [Continuity](/university/math/calculus-1/continuity/)  
- [Differentiability](/university/math/calculus-1/differentiability/)  
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-by-substitution/)  
- [Ordinary Differential Equations](/university/math/calculus-1/odes-general/)  

</div>
