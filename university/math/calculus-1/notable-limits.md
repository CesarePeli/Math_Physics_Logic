---
layout: default
date: 2025-04-21
title: "Solved Exercises — Notable Limits"
meta-description: "Solved exercises on notable limits: fundamental indeterminate forms, exponential and trigonometric limits, and classical remarkable results."
permalink: "/university/math/calculus-1/notable-limits/"
background_image: "/images/limiti.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

The main notable limits in calculus are:

$$
\lim_{x\to 0}\frac{\sin x}{x}=1, \quad
\lim_{x\to \infty}\frac{\sin x}{x}=0,
$$

$$
\lim_{x\to 0}\frac{\log(1+x)}{x}=1, \quad
\lim_{x\to 0}\frac{1-\cos x}{x^{2}}=\tfrac{1}{2},
$$

$$
\lim_{x\to +\infty}\left(1+\tfrac{1}{x}\right)^{x}=e, \quad
\lim_{x\to -\infty}\left(1+\tfrac{1}{x}\right)^{x}=e,
$$

$$
\lim_{x\to 0}(1+x)^{1/x}=e, \quad
\lim_{x\to 0}\frac{e^{x}-1}{x}=1,
$$

$$
\lim_{x\to 0}\frac{\tan x}{x}=1, \quad
\lim_{x\to 0}\frac{\arcsin x}{x}=1, \quad
\lim_{x\to 0}\frac{\arctan x}{x}=1.
$$

### Key Theorems

**Theorem (Non-existence via sequences).**  
If there exist two sequences $a_{n},b_{n}\to c$ such that
$$
\lim_{n\to\infty}f(a_{n}) \ne \lim_{n\to\infty}f(b_{n}),
$$
then $\lim_{x\to c}f(x)$ does not exist.

**Theorem (Squeeze Theorem).**  
If $f(x)\le g(x)\le h(x)$ and
$$
\lim_{x\to c}f(x)=\lim_{x\to c}h(x)=L,
$$
then
$$
\lim_{x\to c}g(x)=L.
$$

</div>

---

<div class="content-box">

### Exercise 1  
$$
\lim_{x\to +\infty}\Big(\sqrt{x^{2}+x+1}-\sqrt{x^{2}-x+1}\Big).
$$

**Solution:**  
Rationalize the numerator:
$$
\frac{(\sqrt{x^{2}+x+1}-\sqrt{x^{2}-x+1})(\sqrt{x^{2}+x+1}+\sqrt{x^{2}-x+1})}{\sqrt{x^{2}+x+1}+\sqrt{x^{2}-x+1}}.
$$

Simplify:
$$
\frac{2x}{x\left(\sqrt{1+\tfrac{1}{x}+\tfrac{1}{x^{2}}}+\sqrt{1-\tfrac{1}{x}+\tfrac{1}{x^{2}}}\right)} \to 1.
$$

**Final Result:**  
$$1$$

</div>

---

<div class="content-box">

### Exercise 2  
$$
\lim_{x\to \infty}x\log\!\Big(\tfrac{x+4}{x+5}\Big).
$$

**Solution:**  
Rewrite:
$$
x\log\!\Big(1-\tfrac{1}{x+5}\Big).
$$

Let $t=-\tfrac{1}{x+5}$, so $x=\tfrac{-1-5t}{t}$. Then:
$$
\lim_{t\to 0}\frac{-1-5t}{t}\log(1+t)=-1.
$$

**Final Result:**  
$$-1$$

</div>

---

<div class="content-box">

### Exercise 3  
$$
\lim_{x\to +\infty}\left(\tfrac{2x+9}{2x+1}\right)^{x}.
$$

**Solution:**  
Rewrite:
$$
\Big(1+\tfrac{8}{2x+1}\Big)^{x}.
$$

Let $t=\tfrac{8}{2x+1}$, then $x=\tfrac{4}{t}-\tfrac{1}{2}$. So:
$$
\lim_{t\to 0}(1+t)^{4/t-1/2}=\frac{(1+t)^{4/t}}{(1+t)^{1/2}}\to e^{4}.
$$

**Final Result:**  
$$e^{4}$$

</div>

---

<div class="content-box">

### Exercise 4  
$$
\lim_{x\to +\infty}x\log\Big(\tfrac{x^{2}+1}{x^{2}+x}\Big).
$$

**Solution:**  
Let $t=1/x$, so $x=1/t$. Then:
$$
\lim_{t\to 0}\frac{1}{t}\log\Big(\tfrac{1+t^{2}}{1+t}\Big).
$$

This equals:
$$
\lim_{t\to 0}\frac{\log(1+t^{2})}{t}-\frac{\log(1+t)}{t}=-1.
$$

**Final Result:**  
$$-1$$

</div>

---

<div class="content-box">

### Exercise 5  
$$
\lim_{x\to +\infty}\frac{\log(x^{3}+1)}{x}.
$$

**Solution:**  
Rewrite:
$$
\frac{3\log x+\log(1+\tfrac{1}{x^{3}})}{x}.
$$

As $x\to\infty$, numerator grows like $\log x$, denominator like $x$. Limit is 0.

**Final Result:**  
$$0$$

</div>

---

<div class="content-box">

### Exercise 6  
$$
\lim_{x\to +\infty}\frac{\sin x -x}{\cos x+\sqrt{1+x^{2}}}.
$$

**Solution:**  
Divide numerator and denominator by $x$:
$$
\frac{\tfrac{\sin x}{x}-1}{\tfrac{\cos x}{x}+\sqrt{1+\tfrac{1}{x^{2}}}}.
$$

As $x\to\infty$, $\tfrac{\sin x}{x}\to 0$, $\tfrac{\cos x}{x}\to 0$. So limit is $-1$.

**Final Result:**  
$$-1$$

</div>

---

<div class="content-box">

### Exercise 7  
$$
\lim_{x\to +\infty}\left(\frac{x+3}{x-1}\right)^{x+1}.
$$

**Solution:**  
Rewrite:
$$
\left(1+\tfrac{4}{x-1}\right)^{x+1}.
$$

Let $y=\tfrac{4}{x-1}$, so $x=\tfrac{4+y}{y}$. Then:
$$
\lim_{y\to 0}(1+y)^{4/y}(1+y)=e^{4}.
$$

**Final Result:**  
$$e^{4}$$

</div>

---

<div class="content-box">

### Exercise 8  
$$
\lim_{x\to 0^{+}}x^{1/\log(3x)}.
$$

**Solution:**  
Let $y=1/\log(3x)$, so $x=e^{1/y}/3$. Then:
$$
\lim_{y\to 0^{+}}\left(\tfrac{e^{y}}{3}\right)^{y}=\lim_{y\to 0^{+}}\tfrac{e}{3^{y}}=e.
$$

**Final Result:**  
$$e$$

</div>

---

<div class="content-box">

### Exercise 9  
$$
\lim_{x\to 0}\frac{e^{x}-e^{-x}}{x}.
$$

**Solution:**  
Rewrite:
$$
\frac{e^{x}-1}{x}+\frac{e^{-x}-1}{-x}.
$$

Each tends to 1 as $x\to 0$. Sum is 2.

**Final Result:**  
$$2$$

</div>

---

<div class="content-box">

### Exercise 10  
$$
\lim_{x\to 1}\frac{\cos\!\left(\tfrac{\pi}{2}x\right)}{x-1}.
$$

**Solution:**  
Let $y=x-1$, $x=y+1$. Then:
$$
\lim_{y\to 0}\frac{\cos(\tfrac{\pi}{2}y+\tfrac{\pi}{2})}{y}
=\lim_{y\to 0}-\frac{\sin(\tfrac{\pi}{2}y)}{y}.
$$

So:
$$
-\frac{\pi}{2}.
$$

**Final Result:**  
$$-\tfrac{\pi}{2}$$

</div>

---

<div class="content-box">

## Explore more topics in Calculus 1

- [Complex Numbers]({{ "/university/math/calculus-1/complex-numbers/" | relative_url }})  
- [Limits with L’Hôpital’s Rule](/university/math/calculus-1/limits-hopital/)  
- [Limits with Taylor Expansions](/university/math/calculus-1/limits-taylor/)  
- [Sequences](/university/math/calculus-1/sequences/)  
- [Series](/university/math/calculus-1/series/)  
- [Continuity](/university/math/calculus-1/continuity/)  
- [Differentiability](/university/math/calculus-1/differentiability/)  
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-substitution/)  
- [General ODEs](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems for ODEs](/university/math/calculus-1/odes-cauchy/)  

</div>
