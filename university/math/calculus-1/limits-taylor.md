---
layout: default
date: 2025-08-30
title: "Solved Exercises — Limits with Taylor Expansion"
meta-description: "Worked examples on limits using Taylor expansion: expansions of exponential, logarithmic and trigonometric functions, with detailed author notes."
permalink: "/university/math/calculus-1/limits-taylor/"
background_image: "/images/limiti.png"

---

<div class="content-box">

## Theoretical Recall

Taylor expansion of a function $f$ at $x_0$:

$$
f(x) = f(x_0) + \frac{f'(x_0)}{1!}(x-x_0) + \frac{f''(x_0)}{2!}(x-x_0)^2 + \dots +
\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n + o((x-x_0)^n).
$$

If $x_0=0$ we obtain the **Maclaurin expansion**.

**Rules for $o$-notation:**

- $o(x^m)+o(x^m) = o(x^m)$  
- $o(x^m)\cdot o(x^n) = o(x^{m+n})$  
- $o(x^n)+o(x^m) = o(x^{\min\{m,n\}})$  
- $x^n \cdot o(x^m) = o(x^{n+m})$  
- $o(x^n + o(x^n)) = o(x^n)$  

**Maclaurin series (up to relevant order):**

- $(1+x)^\alpha = 1+\alpha x+\tfrac{\alpha(\alpha-1)}{2!}x^2 + \dots + o(x^n)$  
- $e^x = 1+x+\tfrac{x^2}{2!}+\tfrac{x^3}{3!}+o(x^3)$  
- $\log(1+x)=x-\tfrac{x^2}{2}+\tfrac{x^3}{3}-\tfrac{x^4}{4}+o(x^4)$  
- $\sin x = x-\tfrac{x^3}{3!}+\tfrac{x^5}{5!}+o(x^5)$  
- $\cos x = 1-\tfrac{x^2}{2}+\tfrac{x^4}{4!}+o(x^4)$  
- $\tan x = x+\tfrac{x^3}{3}+\tfrac{2}{15}x^5+o(x^5)$  

**Author’s note:**  
The expansions must be truncated only after ensuring the approximation order is sufficient to determine the limit. A common mistake is cutting the series too early.

</div>

<div class="content-box">

## Exercises

### Exercise 1
$$
\lim_{x\to0} \frac{e^x-1-x}{x^2}
$$

**Solution:**  
$e^x = 1+x+\tfrac{x^2}{2}+o(x^2)$.  
Numerator $=\tfrac{x^2}{2}+o(x^2)$.  

**Final Result:**
$$
\frac{1}{2}
$$

---

### Exercise 2
$$
\lim_{x\to0} \frac{\log(1+x)-x}{x^2}
$$

**Solution:**  
$\log(1+x)=x-\tfrac{x^2}{2}+o(x^2)$.  
Numerator $=-\tfrac{x^2}{2}+o(x^2)$.  

**Final Result:**
$$
-\frac{1}{2}
$$

---

### Exercise 3
$$
\lim_{x\to0} \frac{\sin x - x}{x^3}
$$

**Solution:**  
$\sin x = x-\tfrac{x^3}{6}+o(x^3)$.  
Numerator $=-\tfrac{x^3}{6}+o(x^3)$.  

**Final Result:**
$$
-\frac{1}{6}
$$

---

### Exercise 4
$$
\lim_{x\to0} \frac{1-\cos x}{x^2}
$$

**Solution:**  
$\cos x=1-\tfrac{x^2}{2}+o(x^2)$.  
Numerator $=\tfrac{x^2}{2}+o(x^2)$.  

**Final Result:**
$$
\frac{1}{2}
$$

---

### Exercise 5
$$
\lim_{x\to0} \frac{e^{2x}-1-2x}{x^2}
$$

**Solution:**  
$e^{2x}=1+2x+2x^2+o(x^2)$.  
Numerator $=2x^2+o(x^2)$.  

**Final Result:**
$$
2
$$

---

### Exercise 6
$$
\lim_{x\to0} \frac{\tan x - x}{x^3}
$$

**Solution:**  
$\tan x = x+\tfrac{x^3}{3}+o(x^3)$.  
Numerator $=\tfrac{x^3}{3}+o(x^3)$.  

**Final Result:**
$$
\frac{1}{3}
$$

---

### Exercise 7
$$
\lim_{x\to0} \frac{\log(1+x)-\sin x}{x^3}
$$

**Solution:**  
$\log(1+x)=x-\tfrac{x^2}{2}+\tfrac{x^3}{3}+o(x^3)$,  
$\sin x = x-\tfrac{x^3}{6}+o(x^3)$.  

Difference $=-\tfrac{x^2}{2}+\tfrac{x^3}{2}+o(x^3)$.  
Dividing by $x^3$: $\sim -\tfrac{1}{2}\cdot \tfrac{1}{x}+\tfrac{1}{2}+o(1)$.  

Thus, as $x\to0^+$, limit $\to -\infty$; as $x\to0^-$, limit $\to +\infty$.  

**Final Result:**  
The two-sided limit **does not exist**.

---

### Exercise 8
$$
\lim_{x\to0} \frac{e^x-\cos x}{x}
$$

**Solution:**  
$e^x=1+x+\tfrac{x^2}{2}+o(x^2)$,  
$\cos x=1-\tfrac{x^2}{2}+o(x^2)$.  

Numerator $=x+x^2+o(x^2)$. Divide by $x$: $1+x+o(x)$.  

**Final Result:**
$$
1
$$

---

### Exercise 9
$$
\lim_{x\to0} \frac{\sin x - \tan x}{x^3}
$$

**Solution:**  
$\sin x=x-\tfrac{x^3}{6}+o(x^3)$,  
$\tan x=x+\tfrac{x^3}{3}+o(x^3)$.  

Difference $=-\tfrac{x^3}{2}+o(x^3)$.  

**Final Result:**
$$
-\frac{1}{2}
$$

---

### Exercise 10
$$
\lim_{x\to0} \frac{e^x-\sin x-1}{x}
$$

**Solution:**  
$e^x=1+x+\tfrac{x^2}{2}+o(x^2)$,  
$\sin x=x-\tfrac{x^3}{6}+o(x^3)$.  

Numerator $=\tfrac{x^2}{2}+\tfrac{x^3}{6}+o(x^2)$.  
Divided by $x$: $\tfrac{x}{2}+o(x)\to0$.  

**Final Result:**
$$
0
$$

</div>

<div class="content-box">

## Related Pages in *Calculus I*

- [Complex Numbers](/university/math/calculus-1/complex-numbers/)  
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
- [Limits with L’Hôpital’s Rule](/university/math/calculus-1/limits-hopital/)  
- [Sequences](/university/math/calculus-1/sequences/)  
- [Series](/university/math/calculus-1/series/)  
- [Continuity](/university/math/calculus-1/continuity/)  
- [Differentiability](/university/math/calculus-1/differentiability/)  
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-by-substitution/)  
- [Ordinary Differential Equations](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems](/university/math/calculus-1/odes-cauchy/)  

</div>
