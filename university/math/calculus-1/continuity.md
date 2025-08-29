---
layout: default
date: 2025-08-29
title: "Solved Exercises — Continuity"
meta-description: "Worked exercises on continuity: definition, removable, jump and infinite discontinuities, matching of piecewise functions, and domain analysis. Ten step-by-step solved examples."
permalink: "/university/math/calculus-1/continuity/"
background_image: "/images/grafi.png"

---

<div class="content-box">

## Theoretical Recall

A function $f$ is **continuous at $x_0$** if

$$
\lim_{x \to x_0} f(x) = f(x_0).
$$

Equivalent $\varepsilon$–$\delta$ definition:  
for all $\varepsilon>0$ there exists $\delta>0$ such that  
$|x-x_0|<\delta \implies |f(x)-f(x_0)|<\varepsilon$.

**Types of discontinuities:**
- *Removable:* limit exists, but $f(x_0)$ missing or mismatched.  
- *Jump:* one-sided limits finite but different.  
- *Infinite:* one or both one-sided limits $\pm\infty$.  
- *Oscillatory:* limit does not exist due to oscillation.

Basic facts:  
- Polynomials, rational functions (on their domain), $\sin,\cos,e^x,\log x$ are continuous on their domains.  
- Algebra and composition of continuous functions yield continuous functions.  

</div>

<div class="content-box">

## Exercises

### Exercise 1
Check continuity of
$$
f(x)=\frac{x^2-1}{x-1}, \quad x\ne1, \quad f(1)=c.
$$

**Solution:**  
For $x\ne1$, $f(x)=x+1$. Limit at $1$ is $2$. To be continuous, set $f(1)=c=2$.

**Final Result:**
$$
c=2 \quad \text{makes $f$ continuous at } x=1.
$$

---

### Exercise 2
Classify discontinuity of $\operatorname{sgn}(x)$ at $0$.

**Solution:**  
$\lim_{x\to0^-}=-1$, $\lim_{x\to0^+}=1$. Different finite limits.

**Final Result:**
$$
\text{Jump discontinuity at } x=0.
$$

---

### Exercise 3
Study $f(x)=\frac{1}{x}$ at $x=0$.

**Solution:**  
One-sided limits diverge to $\pm\infty$.

**Final Result:**
$$
\text{Infinite discontinuity at } x=0.
$$

---

### Exercise 4
Study $f(x)=\frac{\sin x}{x}$ for $x\ne0$, with $f(0)=1$.

**Solution:**  
Limit $\lim_{x\to0}\frac{\sin x}{x}=1=f(0)$. Continuous at $0$.

**Final Result:**
$$
f \text{ continuous on } \mathbb{R}.
$$

---

### Exercise 5
$f(x)=|x|\sin(1/x)$ for $x\ne0$, $f(0)=0$. Study continuity at $0$.

**Solution:**  
$|f(x)|\le |x|\to0$, so $\lim_{x\to0}f(x)=0=f(0)$.

**Final Result:**
$$
f \text{ is continuous at } 0.
$$

---

### Exercise 6
$f(x)=
\begin{cases}
ax+b,&x<2,\\
x^2,&x\ge2
\end{cases}$.
Choose $a,b$ for continuity at $2$.

**Solution:**  
$\lim_{x\to2^-}=2a+b$, $f(2)=4$. Condition: $2a+b=4$.

**Final Result:**
$$
\text{Continuity at }2 \iff 2a+b=4.
$$

---

### Exercise 7
Check continuity of $f(x)=\log(x^2-4)$.

**Solution:**  
Domain requires $x^2-4>0 \iff |x|>2$. On domain, composition of continuous functions is continuous.

**Final Result:**
$$
f \text{ continuous on } (-\infty,-2)\cup(2,\infty).
$$

---

### Exercise 8
$f(x)=
\begin{cases}
\sin(1/x),&x\ne0,\\
0,&x=0.
\end{cases}$

Check continuity at $0$.

**Solution:**  
Limit $\lim_{x\to0}\sin(1/x)$ does not exist (oscillations). So discontinuous at $0$.

**Final Result:**
$$
\text{Oscillatory discontinuity at } 0.
$$

---

### Exercise 9
$f(x)=
\begin{cases}
x^2,&x\le0,\\
1,&x>0.
\end{cases}$

Check continuity at $0$.

**Solution:**  
Left limit $0$, right limit $1$. Different.  

**Final Result:**
$$
\text{Jump discontinuity at } 0.
$$

---

### Exercise 10
$f(x)=
\begin{cases}
\cos x,&x<0,\\
a+bx,&x\ge0.
\end{cases}$

Find $a,b$ for continuity at $0$.

**Solution:**  
$\lim_{x\to0^-}\cos x=1$, $f(0)=a$. Continuity $\Rightarrow a=1$. $b$ free.

**Final Result:**
$$
a=1,\; b \in\mathbb{R}.
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
- [Differentiability](/university/math/calculus-1/differentiability/)  
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-by-substitution/)  
- [Ordinary Differential Equations](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems](/university/math/calculus-1/odes-cauchy/)  

</div>
