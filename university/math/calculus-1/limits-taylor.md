---
layout: default
date: 2025-08-29
title: "Solved Exercises — Limits with Taylor Expansion"
meta-description: "Worked examples on limits using Taylor expansion: expansions of exponential, logarithmic and trigonometric functions, with detailed author notes."
permalink: "/university/math/calculus-1/limits-taylor/"
background_image: "/images/euclide.png"

---

<div class="content-box">

## Theoretical Recall

Taylor expansions near $x=0$ (Maclaurin series):

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + o(x^3),
$$

$$
\log(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} + o(x^3),
$$

$$
\sin x = x - \frac{x^3}{3!} + o(x^3), 
\quad
\cos x = 1 - \frac{x^2}{2} + o(x^2).
$$

General principle:  
to evaluate $\lim_{x\to0} f(x)$, expand numerator and denominator up to the order needed to cancel dominant terms.

**Author’s note:** The expansions must be truncated only after ensuring that the order of approximation is sufficient to determine the limit. A frequent error is to truncate too early.

</div>

<div class="content-box">

## Exercises

### Exercise 1
$$
\lim_{x\to0} \frac{e^x-1-x}{x^2}
$$

**Solution:**  
$e^x=1+x+\tfrac{x^2}{2}+o(x^2)$. Then numerator $= \tfrac{x^2}{2}+o(x^2)$.  

**Final Result:**
$$
\lim_{x\to0} \frac{e^x-1-x}{x^2} = \tfrac{1}{2}
$$

---

### Exercise 2
$$
\lim_{x\to0} \frac{\log(1+x)-x}{x^2}
$$

**Solution:**  
$\log(1+x)=x-\tfrac{x^2}{2}+o(x^2)$. Numerator $=-\tfrac{x^2}{2}+o(x^2)$.  

**Author’s note:** This is a classical limit where the second-order term of the Taylor expansion is essential.  

**Final Result:**
$$
\lim_{x\to0} \frac{\log(1+x)-x}{x^2} = -\tfrac{1}{2}
$$

---

### Exercise 3
$$
\lim_{x\to0} \frac{\sin x - x}{x^3}
$$

**Solution:**  
$\sin x = x-\tfrac{x^3}{6}+o(x^3)$. Numerator $=-\tfrac{x^3}{6}+o(x^3)$.  

**Final Result:**
$$
\lim_{x\to0} \frac{\sin x - x}{x^3} = -\tfrac{1}{6}
$$

---

### Exercise 4
$$
\lim_{x\to0} \frac{1-\cos x}{x^2}
$$

**Solution:**  
$\cos x=1-\tfrac{x^2}{2}+o(x^2)$. Numerator $=\tfrac{x^2}{2}+o(x^2)$.  

**Author’s note:** The Taylor expansion avoids the indeterminate $0/0$ and is often faster than applying L’Hôpital.  

**Final Result:**
$$
\lim_{x\to0} \frac{1-\cos x}{x^2} = \tfrac{1}{2}
$$

---

### Exercise 5
$$
\lim_{x\to0} \frac{e^{2x}-1-2x}{x^2}
$$

**Solution:**  
$e^{2x}=1+2x+2x^2+o(x^2)$. Numerator $=2x^2+o(x^2)$.  

**Final Result:**
$$
\lim_{x\to0} \frac{e^{2x}-1-2x}{x^2} = 2
$$

---

### Exercise 6
$$
\lim_{x\to0} \frac{\tan x - x}{x^3}
$$

**Solution:**  
$\tan x = x+\tfrac{x^3}{3}+o(x^3)$. Numerator $=\tfrac{x^3}{3}+o(x^3)$.  

**Final Result:**
$$
\lim_{x\to0} \frac{\tan x - x}{x^3} = \tfrac{1}{3}
$$

---

### Exercise 7
$$
\lim_{x\to0} \frac{\log(1+x)-\sin x}{x^3}
$$

**Solution:**  
$\log(1+x)=x-\tfrac{x^2}{2}+\tfrac{x^3}{3}+o(x^3)$,  
$\sin x = x-\tfrac{x^3}{6}+o(x^3)$.  
Difference $=-\tfrac{x^2}{2}+\tfrac{x^3}{3}+\tfrac{x^3}{6}+o(x^3)=-\tfrac{x^2}{2}+\tfrac{x^3}{2}+o(x^3)$.  
Dividing by $x^3$ gives divergence to $-\infty$.  

**Author’s note:** The divergence highlights the importance of identifying the dominating term in the expansion.  

**Final Result:**
$$
\lim_{x\to0} \frac{\log(1+x)-\sin x}{x^3} = -\infty
$$

---

### Exercise 8
$$
\lim_{x\to0} \frac{e^x-\cos x}{x}
$$

**Solution:**  
$e^x=1+x+\tfrac{x^2}{2}+o(x^2)$, $\cos x=1-\tfrac{x^2}{2}+o(x^2)$.  
Numerator $=x+x^2+o(x^2)$. Divide by $x$: $1+x+o(x)$.  

**Final Result:**
$$
\lim_{x\to0} \frac{e^x-\cos x}{x} = 1
$$

---

### Exercise 9
$$
\lim_{x\to0} \frac{\sin x - \tan x}{x^3}
$$

**Solution:**  
$\sin x=x-\tfrac{x^3}{6}+o(x^3)$,  
$\tan x=x+\tfrac{x^3}{3}+o(x^3)$.  
Difference $=-\tfrac{x^3}{6}-\tfrac{x^3}{3}+o(x^3)=-\tfrac{x^3}{2}+o(x^3)$.  

**Final Result:**
$$
\lim_{x\to0} \frac{\sin x - \tan x}{x^3} = -\tfrac{1}{2}
$$

---

### Exercise 10
$$
\lim_{x\to0} \frac{e^x-\sin x-1}{x}
$$

**Solution:**  
$e^x=1+x+\tfrac{x^2}{2}+o(x^2)$,  
$\sin x=x-\tfrac{x^3}{6}+o(x^3)$.  
So numerator $=\tfrac{x^2}{2}+\tfrac{x^3}{6}+o(x^2)$. Divided by $x$: $\tfrac{x}{2}+o(x)\to0$.  

**Author’s note:** The function is continuous at 0 with value $0$, the expansion confirms the limit.  

**Final Result:**
$$
\lim_{x\to0} \frac{e^x-\sin x-1}{x} = 0
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
