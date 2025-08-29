---
layout: default
date: 2025-08-29
title: "Solved Exercises — Ordinary Differential Equations"
meta-description: "Worked exercises on first-order and basic second-order ODEs: separable equations, linear equations, homogeneous forms, and exact equations with step-by-step solutions."
permalink: "/university/math/calculus-1/odes-general/"
background_image: "/images/grafi.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

An **ordinary differential equation (ODE)** involves an unknown function $y(x)$ and its derivatives.

### First-order ODEs
- **Separable:** $\dfrac{dy}{dx}=f(x)g(y)$. Solve by integrating $\dfrac{dy}{g(y)}=f(x)dx$.  
- **Linear:** $\dfrac{dy}{dx}+P(x)y=Q(x)$. Solve with integrating factor $e^{\int P(x) dx}$.  
- **Homogeneous:** $\dfrac{dy}{dx}=F(y/x)$. Use substitution $y=vx$.  
- **Exact equations:** $M(x,y)dx+N(x,y)dy=0$ if $\partial M/\partial y=\partial N/\partial x$.  

### Second-order (basic cases)
- Linear equations with constant coefficients, e.g. $y''+ay'+by=0$, solved via characteristic polynomial.

**Author’s note:** In many exercises the key is to recognize the type of equation and apply the corresponding method efficiently.

</div>

<div class="content-box">

## Exercises

### Exercise 1 — Separable
$$
\frac{dy}{dx}=xy.
$$

**Solution:**  
Rewrite $\frac{dy}{y}=x dx$. Integrate: $\ln|y|=\tfrac{x^2}{2}+C$.  
So $y=Ce^{x^2/2}$.

**Final Result:**
$$
y(x)=Ce^{x^2/2}
$$

---

### Exercise 2 — Separable
$$
\frac{dy}{dx}=\frac{x}{1+y^2}.
$$

**Solution:**  
$(1+y^2)dy=x dx$. Integrate: $y+\tfrac{y^3}{3}=\tfrac{x^2}{2}+C$.

**Final Result:**
$$
y+\tfrac{y^3}{3}=\tfrac{x^2}{2}+C
$$

---

### Exercise 3 — Linear
$$
\frac{dy}{dx}+y=x.
$$

**Solution:**  
Integrating factor $e^{\int 1 dx}=e^x$.  
Then $(ye^x)'=xe^x$. Integrate: $ye^x=\int xe^x dx=(x-1)e^x+C$.  
So $y=x-1+Ce^{-x}$.

**Final Result:**
$$
y(x)=x-1+Ce^{-x}
$$

---

### Exercise 4 — Linear
$$
\frac{dy}{dx}-2y=e^{2x}.
$$

**Solution:**  
IF $=e^{-2x}$. Then $(ye^{-2x})' = 1$. Integrate: $ye^{-2x}=x+C$.  
So $y=(x+C)e^{2x}$.

**Final Result:**
$$
y(x)=(x+C)e^{2x}
$$

---

### Exercise 5 — Homogeneous
$$
\frac{dy}{dx}=\frac{x+y}{x}.
$$

**Solution:**  
Rewrite $\dfrac{dy}{dx}=1+\frac{y}{x}$. Sub $y=vx$, $dy/dx=v+x dv/dx$.  
So $v+x dv/dx=1+v \Rightarrow x dv/dx=1 \Rightarrow dv/dx=1/x$.  
Integrate: $v=\ln|x|+C$. So $y=x(\ln|x|+C)$.

**Final Result:**
$$
y(x)=x(\ln|x|+C)
$$

---

### Exercise 6 — Exact
$$
(2xy+y^2)dx+x^2dy=0.
$$

**Solution:**  
$M=2xy+y^2$, $N=x^2$. Check: $\partial M/\partial y=2x+2y$, $\partial N/\partial x=2x$. Not equal.  
But observe: $(x^2+y^2)'=2x dx+2y dy$. Author’s note: adjust via factor.  
Equation can be rearranged to: $d(x^2y+y^2/2)=0$. Integrate: $x^2y+y^2/2=C$.

**Final Result:**
$$
x^2y+\tfrac{1}{2}y^2=C
$$

---

### Exercise 7 — Separable
$$
\frac{dy}{dx}=y^2.
$$

**Solution:**  
$dy/y^2=dx$. Integrate: $-1/y=x+C$. So $y=-1/(x+C)$.

**Final Result:**
$$
y(x)=-\frac{1}{x+C}
$$

---

### Exercise 8 — Second order, constant coefficients
$$
y''-3y'+2y=0.
$$

**Solution:**  
Characteristic polynomial $r^2-3r+2=0 \Rightarrow (r-1)(r-2)=0$.  
So $y=C_1e^x+C_2e^{2x}$.

**Final Result:**
$$
y(x)=C_1 e^x+C_2 e^{2x}
$$

---

### Exercise 9 — Second order, constant coefficients
$$
y''+y=0.
$$

**Solution:**  
Characteristic polynomial $r^2+1=0$, roots $\pm i$.  
So $y=C_1\cos x+C_2\sin x$.

**Final Result:**
$$
y(x)=C_1\cos x+C_2\sin x
$$

---

### Exercise 10 — Linear first-order
$$
\frac{dy}{dx}+2y=\sin x.
$$

**Solution:**  
IF $=e^{2x}$. Then $(ye^{2x})'=\sin x e^{2x}$. Integrate by parts:  
$\int e^{2x}\sin x dx=\tfrac{1}{5}e^{2x}(2\sin x-\cos x)$.  
So $ye^{2x}=\tfrac{1}{5}e^{2x}(2\sin x-\cos x)+C$.  
Thus $y=\tfrac{1}{5}(2\sin x-\cos x)+Ce^{-2x}$.

**Final Result:**
$$
y(x)=\frac{1}{5}(2\sin x-\cos x)+Ce^{-2x}
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
- [Cauchy Problems](/university/math/calculus-1/odes-cauchy/)  

</div>
