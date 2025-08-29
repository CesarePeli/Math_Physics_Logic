---
layout: default
date: 2025-08-29
title: "Solved Exercises — Integration by Substitution"
meta-description: "Worked exercises on integration by substitution: change of variables, trigonometric substitutions, and rational simplifications with detailed step-by-step solutions."
permalink: "/university/math/calculus-1/integration-by-substitution/"
background_image: "/images/integrali.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

**Substitution rule:**

If $x=g(t)$ is a differentiable substitution, then

$$
\int f(x)\,dx = \int f(g(t)) g'(t)\, dt.
$$

Common strategies:
- Simplify radicals by trigonometric substitution ($x=\sin t$, $x=\tan t$).  
- Linear substitutions to reduce shifts/scaling.  
- Exponential/logarithmic substitutions to handle $\log$, $e^x$, rational forms.  

**Author’s note:** Always transform both the function and the differential $dx$ consistently.

</div>

<div class="content-box">

## Exercises

### Exercise 1
Evaluate
$$
\int (2x+1)^5 \, dx.
$$

**Solution:**  
Let $u=2x+1$, $du=2dx$, $dx=\tfrac{1}{2}du$.  

$$
\int (2x+1)^5 dx = \tfrac{1}{2}\int u^5 du = \tfrac{1}{12}u^6+C.
$$

Back-substitute: $(2x+1)^6/12+C$.

**Final Result:**
$$
\int (2x+1)^5 dx = \frac{(2x+1)^6}{12}+C
$$

---

### Exercise 2
Evaluate
$$
\int \frac{1}{x\log x}\, dx, \quad x>1.
$$

**Solution:**  
Let $u=\log x$, $du=\tfrac{1}{x}dx$.  

$$
\int \frac{1}{x\log x} dx = \int \frac{1}{u} du = \log|u|+C=\log(\log x)+C.
$$

**Final Result:**
$$
\int \frac{1}{x\log x} dx = \log(\log x)+C
$$

---

### Exercise 3
Evaluate
$$
\int \frac{x}{1+x^2}\, dx.
$$

**Solution:**  
Let $u=1+x^2$, $du=2x dx$.  

$$
\int \frac{x}{1+x^2} dx = \tfrac{1}{2}\int \frac{1}{u} du = \tfrac{1}{2}\log(1+x^2)+C.
$$

**Final Result:**
$$
\int \frac{x}{1+x^2} dx = \tfrac{1}{2}\log(1+x^2)+C
$$

---

### Exercise 4
Evaluate
$$
\int \frac{1}{\sqrt{1-x^2}} dx.
$$

**Solution:**  
Substitute $x=\sin t$, $dx=\cos t dt$.  

$$
\int \frac{1}{\sqrt{1-\sin^2 t}} \cos t dt = \int 1 dt = t+C.
$$

Back-substitute: $\arcsin x + C$.

**Final Result:**
$$
\int \frac{1}{\sqrt{1-x^2}} dx = \arcsin x + C
$$

---

### Exercise 5
Evaluate
$$
\int \frac{1}{x^2+1} dx.
$$

**Solution:**  
Let $x=\tan t$, $dx=\sec^2 t dt$, $1+x^2=\sec^2 t$.  

$$
\int \frac{1}{1+\tan^2 t} \sec^2 t dt = \int 1 dt = t+C.
$$

Back-substitute: $\arctan x + C$.

**Final Result:**
$$
\int \frac{1}{x^2+1} dx = \arctan x + C
$$

---

### Exercise 6
Evaluate
$$
\int \frac{1}{\sqrt{x^2+4}} dx.
$$

**Solution:**  
Substitute $x=2\tan t$, $dx=2\sec^2 t dt$.  

$$
\sqrt{x^2+4}=\sqrt{4\tan^2 t+4}=2\sec t.
$$

So integral:  
$$
\int \frac{2\sec^2 t}{2\sec t} dt = \int \sec t dt.
$$

Result: $\log|\sec t+\tan t|+C$. Back-substitute $t=\arctan(x/2)$.

**Final Result:**
$$
\int \frac{1}{\sqrt{x^2+4}} dx = \log\!\left|\frac{x+\sqrt{x^2+4}}{2}\right|+C
$$

---

### Exercise 7
Evaluate
$$
\int \frac{1}{x^2-1} dx.
$$

**Solution:**  
Use partial fraction substitution:  
$$
\frac{1}{x^2-1}=\tfrac{1}{2}\left(\frac{1}{x-1}-\frac{1}{x+1}\right).
$$

Then integrate directly.

**Final Result:**
$$
\int \frac{1}{x^2-1} dx = \tfrac{1}{2}\log\!\left|\frac{x-1}{x+1}\right|+C
$$

---

### Exercise 8
Evaluate
$$
\int \frac{1}{\sqrt{x^2-1}} dx, \quad x>1.
$$

**Solution:**  
Set $x=\cosh t$, $dx=\sinh t dt$, $\sqrt{x^2-1}=\sinh t$.  

$$
\int \frac{1}{\sinh t}\sinh t dt = \int 1 dt = t+C.
$$

Back-substitute $t=\operatorname{arcosh}(x)=\log(x+\sqrt{x^2-1})$.

**Final Result:**
$$
\int \frac{1}{\sqrt{x^2-1}} dx = \log(x+\sqrt{x^2-1})+C
$$

---

### Exercise 9
Evaluate
$$
\int \sqrt{1+x^2}\, dx.
$$

**Solution:**  
Set $x=\sinh t$, $dx=\cosh t dt$.  

$$
\int \sqrt{1+\sinh^2 t}\cosh t dt = \int \cosh^2 t dt.
$$

Use identity $\cosh^2 t=\tfrac{1}{2}(\cosh 2t+1)$.  
Integral $=\tfrac{1}{4}\sinh 2t+\tfrac{1}{2}t+C$.  
Back-substitute $t=\operatorname{arsinh}(x)$.

**Final Result:**
$$
\int \sqrt{1+x^2}\, dx = \tfrac{1}{2}\left(x\sqrt{1+x^2}+\operatorname{arsinh}(x)\right)+C
$$

---

### Exercise 10
Evaluate
$$
\int \frac{1}{x\sqrt{x^2-1}} dx, \quad x>1.
$$

**Solution:**  
Substitute $x=\sec t$, $dx=\sec t\tan t dt$.  

$$
\int \frac{\sec t \tan t}{\sec t \tan t} dt = \int 1 dt = t+C.
$$

Back-substitute: $t=\operatorname{arcsec}(x)$.

**Final Result:**
$$
\int \frac{1}{x\sqrt{x^2-1}} dx = \operatorname{arcsec}(x)+C
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
- [Ordinary Differential Equations](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems](/university/math/calculus-1/odes-cauchy/)  

</div>
