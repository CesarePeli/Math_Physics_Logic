---
layout: default
date: 2025-08-29
title: "Solved Exercises — Integration by Parts"
meta-description: "Worked exercises on integration by parts: step-by-step solutions, polynomial-exponential and trigonometric products, and logarithmic integrals."
permalink: "/university/math/calculus-1/integration-by-parts/"
background_image: "/images/integrali.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

**Integration by parts formula:**

$$
\int f(x)g'(x)\,dx = f(x)g(x) - \int f'(x)g(x)\,dx.
$$

It derives directly from the product rule $(fg)'=f'g+fg'$.  
A common strategy:  
- Choose $f(x)$ to simplify upon differentiation.  
- Choose $g'(x)$ so that its integral $g(x)$ is elementary.  

**Author’s note:** In most cases, the choice is guided by the LIATE rule (Logarithmic, Inverse trigonometric, Algebraic, Trigonometric, Exponential).

</div>

<div class="content-box">

## Exercises

### Exercise 1
Evaluate
$$
\int x e^x \, dx.
$$

**Solution:**  
Take $f(x)=x$, $g'(x)=e^x$. Then $f'(x)=1$, $g(x)=e^x$.  

$$
\int x e^x dx = x e^x - \int e^x dx = x e^x - e^x + C.
$$

**Final Result:**
$$
\int x e^x dx = (x-1)e^x + C
$$

---

### Exercise 2
Evaluate
$$
\int x \cos x \, dx.
$$

**Solution:**  
$f=x$, $g'=\cos x$. Then $f'=1$, $g=\sin x$.  

$$
\int x\cos x dx = x\sin x - \int \sin x dx = x\sin x + \cos x + C.
$$

**Final Result:**
$$
\int x\cos x dx = x\sin x + \cos x + C
$$

---

### Exercise 3
Evaluate
$$
\int x \sin x \, dx.
$$

**Solution:**  
$f=x$, $g'=\sin x$, $f'=1$, $g=-\cos x$.  

$$
\int x\sin x dx = -x\cos x + \int \cos x dx = -x\cos x + \sin x + C.
$$

**Final Result:**
$$
\int x\sin x dx = -x\cos x + \sin x + C
$$

---

### Exercise 4
Evaluate
$$
\int x e^{2x}\,dx.
$$

**Solution:**  
$f=x$, $g'=e^{2x}$, $f'=1$, $g=\tfrac{1}{2}e^{2x}$.  

$$
\int x e^{2x} dx = \tfrac{x}{2}e^{2x} - \int \tfrac{1}{2} e^{2x} dx = \tfrac{x}{2}e^{2x} - \tfrac{1}{4} e^{2x} + C.
$$

**Final Result:**
$$
\int x e^{2x} dx = \tfrac{1}{2}(x-\tfrac{1}{2}) e^{2x} + C
$$

---

### Exercise 5
Evaluate
$$
\int \ln x \, dx.
$$

**Solution:**  
Take $f=\ln x$, $g'=1$. Then $f'=1/x$, $g=x$.  

$$
\int \ln x dx = x\ln x - \int 1 dx = x\ln x - x + C.
$$

**Final Result:**
$$
\int \ln x dx = x\ln x - x + C
$$

---

### Exercise 6
Evaluate
$$
\int x^2 e^x \, dx.
$$

**Solution:**  
First integration by parts: $f=x^2$, $g'=e^x$, then $f'=2x$, $g=e^x$.  

$$
\int x^2 e^x dx = x^2 e^x - \int 2x e^x dx.
$$

Apply integration by parts again on $\int 2x e^x dx$. Final expression:

$$
x^2 e^x - (2x e^x - 2e^x) = (x^2 - 2x + 2) e^x + C.
$$

**Final Result:**
$$
\int x^2 e^x dx = (x^2 - 2x + 2) e^x + C
$$

---

### Exercise 7
Evaluate
$$
\int x \ln x \, dx.
$$

**Solution:**  
$f=\ln x$, $g'=x$, $f'=1/x$, $g=x^2/2$.  

$$
\int x \ln x dx = \tfrac{x^2}{2}\ln x - \int \tfrac{x^2}{2}\cdot \tfrac{1}{x} dx
= \tfrac{x^2}{2}\ln x - \tfrac{1}{2}\int x dx
= \tfrac{x^2}{2}\ln x - \tfrac{x^2}{4} + C.
$$

**Final Result:**
$$
\int x \ln x dx = \tfrac{x^2}{2}\ln x - \tfrac{x^2}{4} + C
$$

---

### Exercise 8
Evaluate
$$
\int e^x \cos x \, dx.
$$

**Solution:**  
$f=\cos x$, $g'=e^x$, $f'=-\sin x$, $g=e^x$.  

$$
\int e^x \cos x dx = e^x \cos x + \int e^x \sin x dx.
$$

Apply integration by parts again to $\int e^x \sin x dx$. Solving the resulting equation for $I=\int e^x\cos x dx$, we obtain:

$$
I=\frac{e^x}{2}(\sin x + \cos x) + C.
$$

**Final Result:**
$$
\int e^x \cos x dx = \tfrac{1}{2} e^x (\sin x + \cos x) + C
$$

---

### Exercise 9
Evaluate
$$
\int e^x \sin x \, dx.
$$

**Solution:**  
Similar to previous. Final result:

$$
\int e^x \sin x dx = \tfrac{1}{2} e^x (\sin x - \cos x) + C.
$$

**Final Result:**
$$
\int e^x \sin x dx = \tfrac{1}{2} e^x (\sin x - \cos x) + C
$$

---

### Exercise 10
Evaluate
$$
\int x^3 e^x \, dx.
$$

**Solution:**  
Apply parts iteratively. Eventually:

$$
\int x^3 e^x dx = (x^3 - 3x^2 + 6x - 6) e^x + C.
$$

**Final Result:**
$$
\int x^3 e^x dx = (x^3 - 3x^2 + 6x - 6) e^x + C
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
- [Integration by Substitution](/university/math/calculus-1/integration-by-substitution/)  
- [Ordinary Differential Equations](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems](/university/math/calculus-1/odes-cauchy/)  

</div>
