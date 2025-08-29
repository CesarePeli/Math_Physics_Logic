---
layout: default
date: 2025-08-29
title: "Solved Exercises — Limits with Taylor Expansions"
meta-description: "Step-by-step limits solved via Taylor polynomials: systematic expansions for exponential, logarithmic and trigonometric functions, with precise order tracking."
permalink: "/university/math/calculus-1/limits-taylor/"
background_image: "/images/limiti.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

**Taylor polynomial at 0 (Maclaurin).** If $f$ is sufficiently smooth near $0$:

$$
T_n f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots + \frac{f^{(n)}(0)}{n!}x^n,
$$

and

$$
f(x) = T_n f(x) + o(x^n) \quad (x\to 0).
$$

**Big-O / little-o.** We write $f(x)=O(x^k)$ if $|f(x)|\le C|x|^k$ near 0; and $f(x)=o(x^k)$ if $\lim_{x\to 0} f(x)/x^k = 0$.

**Classical expansions** (as $x\to 0$):

$$
\begin{aligned}
e^{x} &= 1 + x + \tfrac{x^2}{2} + \tfrac{x^3}{6} + O(x^4),\\
\log(1+x) &= x - \tfrac{x^2}{2} + \tfrac{x^3}{3} - \tfrac{x^4}{4} + O(x^5),\\
\sin x &= x - \tfrac{x^3}{6} + \tfrac{x^5}{120} + O(x^7),\\
\cos x &= 1 - \tfrac{x^2}{2} + \tfrac{x^4}{24} + O(x^6),\\
\tan x &= x + \tfrac{x^3}{3} + \tfrac{2x^5}{15} + O(x^7),\\
\arctan x &= x - \tfrac{x^3}{3} + \tfrac{x^5}{5} + O(x^7).
\end{aligned}
$$

**Method.** Match the **lowest non-zero order** in numerator and denominator; keep terms up to that order; simplify and pass to the limit.

</div>

<div class="content-box">

## Exercises

### Exercise 1
$$
\lim_{x\to 0} \frac{\sin x - x + \tfrac{x^3}{6}}{x^5}
$$

**Solution:**

Use $\sin x = x - \tfrac{x^3}{6} + \tfrac{x^5}{120} + O(x^7)$. Then

$$
\sin x - x + \tfrac{x^3}{6} = \tfrac{x^5}{120} + O(x^7).
$$

Hence

$$
\frac{\sin x - x + \tfrac{x^3}{6}}{x^5} = \tfrac{1}{120} + O(x^2) \to \tfrac{1}{120}.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{\sin x - x + \tfrac{x^3}{6}}{x^5} = \tfrac{1}{120}
$$

---

### Exercise 2
$$
\lim_{x\to 0} \frac{1 - \cos x - \tfrac{x^2}{2}}{x^4}
$$

**Solution:**

With $\cos x = 1 - \tfrac{x^2}{2} + \tfrac{x^4}{24} + O(x^6)$:

$$
1 - \cos x - \tfrac{x^2}{2} = -\tfrac{x^4}{24} + O(x^6).
$$

Therefore

$$
\frac{1 - \cos x - \tfrac{x^2}{2}}{x^4} \to -\tfrac{1}{24}.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{1 - \cos x - \tfrac{x^2}{2}}{x^4} = -\tfrac{1}{24}
$$

---

### Exercise 3
$$
\lim_{x\to 0} \frac{e^{x} - 1 - x - \tfrac{x^2}{2}}{x^3}
$$

**Solution:**

Using $e^x = 1 + x + \tfrac{x^2}{2} + \tfrac{x^3}{6} + O(x^4)$:

$$
\frac{e^{x} - 1 - x - \tfrac{x^2}{2}}{x^3} = \frac{\tfrac{x^3}{6} + O(x^4)}{x^3} \to \tfrac{1}{6}.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{e^{x} - 1 - x - \tfrac{x^2}{2}}{x^3} = \tfrac{1}{6}
$$

---

### Exercise 4
$$
\lim_{x\to 0} \frac{\log(1+x) - x + \tfrac{x^2}{2}}{x^3}
$$

**Solution:**

With $\log(1+x) = x - \tfrac{x^2}{2} + \tfrac{x^3}{3} + O(x^4)$:

$$
\frac{\log(1+x) - x + \tfrac{x^2}{2}}{x^3} = \frac{\tfrac{x^3}{3} + O(x^4)}{x^3} \to \tfrac{1}{3}.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{\log(1+x) - x + \tfrac{x^2}{2}}{x^3} = \tfrac{1}{3}
$$

---

### Exercise 5
$$
\lim_{x\to 0} \frac{\tan x - x - \tfrac{x^3}{3}}{x^5}
$$

**Solution:**

Use $\tan x = x + \tfrac{x^3}{3} + \tfrac{2x^5}{15} + O(x^7)$:

$$
\frac{\tan x - x - \tfrac{x^3}{3}}{x^5} = \frac{\tfrac{2x^5}{15} + O(x^7)}{x^5} \to \tfrac{2}{15}.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{\tan x - x - \tfrac{x^3}{3}}{x^5} = \tfrac{2}{15}
$$

---

### Exercise 6
$$
\lim_{x\to 0} \frac{\arctan x - x + \tfrac{x^3}{3}}{x^5}
$$

**Solution:**

With $\arctan x = x - \tfrac{x^3}{3} + \tfrac{x^5}{5} + O(x^7)$:

$$
\frac{\arctan x - x + \tfrac{x^3}{3}}{x^5} = \frac{\tfrac{x^5}{5} + O(x^7)}{x^5} \to \tfrac{1}{5}.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{\arctan x - x + \tfrac{x^3}{3}}{x^5} = \tfrac{1}{5}
$$

---

### Exercise 7
$$
\lim_{x\to 0} \frac{(1+ax)^b - 1 - abx}{x^2} \quad (a,b\in\mathbb{R})
$$

**Solution:**

Use the generalized binomial expansion:

$$
(1+ax)^b = 1 + abx + \tfrac{b(b-1)}{2}a^2x^2 + O(x^3).
$$

Hence

$$
\frac{(1+ax)^b - 1 - abx}{x^2} \to \tfrac{b(b-1)}{2}a^2.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{(1+ax)^b - 1 - abx}{x^2} = \tfrac{b(b-1)}{2}a^2
$$

---

### Exercise 8
$$
\lim_{x\to 0} \frac{(1+x)^{1/x} - e}{x}
$$

**Solution:**

Let $y(x)=(1+x)^{1/x}=\exp\!\big(\tfrac{\log(1+x)}{x}\big)$. Then

$$
\frac{\log(1+x)}{x} = 1 - \tfrac{x}{2} + \tfrac{x^2}{3} + O(x^3).
$$

Thus

$$
(1+x)^{1/x} = e\,\exp\!\Big(-\tfrac{x}{2} + \tfrac{x^2}{3} + O(x^3)\Big)
= e\Big(1 - \tfrac{x}{2} + \tfrac{11}{24}x^2 + O(x^3)\Big).
$$

Therefore

$$
\frac{(1+x)^{1/x} - e}{x} = e\Big(-\tfrac{1}{2} + \tfrac{11}{24}x + O(x^2)\Big) \to -\tfrac{e}{2}.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{(1+x)^{1/x} - e}{x} = -\tfrac{e}{2}
$$

---

### Exercise 9
$$
\lim_{x\to 0} \frac{\log(1+\sin x)}{x}
$$

**Solution:**

Use $\sin x = x - \tfrac{x^3}{6} + O(x^5)$ and then $\log(1+u)=u-\tfrac{u^2}{2}+O(u^3)$:

$$
\log(1+\sin x) = \big(x - \tfrac{x^3}{6}\big) - \tfrac{1}{2}x^2 + O(x^3) = x + O(x^2).
$$

Hence

$$
\frac{\log(1+\sin x)}{x} = 1 + O(x) \to 1.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{\log(1+\sin x)}{x} = 1
$$

---

### Exercise 10
$$
\lim_{x\to 0} \left(\frac{\sin x}{x}\right)^{\!1/x^2}
$$

**Solution:**

Take logs: let $y(x)=\big(\tfrac{\sin x}{x}\big)^{1/x^2}$. Then

$$
\log y(x) = \frac{\log\big(\sin x / x\big)}{x^2}.
$$

Use $\sin x / x = 1 - \tfrac{x^2}{6} + O(x^4)$ and $\log(1+u) = u - \tfrac{u^2}{2} + O(u^3)$:

$$
\log\Big(\tfrac{\sin x}{x}\Big) = -\tfrac{x^2}{6} + O(x^4).
$$

Therefore

$$
\log y(x) = -\tfrac{1}{6} + O(x^2) \to -\tfrac{1}{6},
$$

so $y(x) \to e^{-1/6}$.

**Final Result:**

$$
\lim_{x\to 0} \left(\frac{\sin x}{x}\right)^{1/x^2} = e^{-1/6}
$$

</div>


---

<div class="content-box">

## Explore more topics in Calculus 1

- [Complex Numbers]({{ "/university/math/calculus-1/complex-numbers/" | relative_url }})  
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
- [Limits with L’Hôpital’s Rule](/university/math/calculus-1/limits-hopital/)   
- [Sequences](/university/math/calculus-1/sequences/)  
- [Series](/university/math/calculus-1/series/)  
- [Continuity](/university/math/calculus-1/continuity/)  
- [Differentiability](/university/math/calculus-1/differentiability/)  
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-substitution/)  
- [General ODEs](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems for ODEs](/university/math/calculus-1/odes-cauchy/)  

</div>

