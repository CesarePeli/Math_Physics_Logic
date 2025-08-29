---
layout: default
date: 2025-04-21
title: "Solved Exercises — Limits with L’Hôpital’s Rule"
meta-description: "Step-by-step worked examples using L’Hôpital’s rule: indeterminate forms 0/0 and ∞/∞, repeated applications, logarithmic tricks, and mixed exponential–trigonometric cases."
permalink: "/university/math/calculus-1/limits-hopital/"
background_image: "/images/limiti.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

**L’Hôpital’s Rule (basic form).** Let $I$ be an open interval containing $a$ (possibly $\pm\infty$). Suppose $f$ and $g$ are differentiable on $I \setminus \{a\}$, and

$$
\lim_{x\to a} f(x) = \lim_{x\to a} g(x) = 0 \quad \text{or} \quad |f(x)|, |g(x)| \to +\infty.
$$

If $g'(x) \neq 0$ near $a$ and the limit $\displaystyle \lim_{x\to a} \frac{f'(x)}{g'(x)}$ exists (finite or infinite), then

$$
\lim_{x\to a} \frac{f(x)}{g(x)} = \lim_{x\to a} \frac{f'(x)}{g'(x)}.
$$

**Notes and cautions**
- The rule applies **only** to $0/0$ or $\infty/\infty$.
- It may be applied **repeatedly**, provided the hypotheses remain valid at each step.
- Other indeterminate forms ($0\cdot\infty$, $\infty-\infty$, $1^{\infty}$, $0^0$, $\infty^0$) must be **algebraically transformed** into a quotient first.
- Prefer simpler tools (factoring, rationalization, notable limits, Taylor) when they provide a shorter proof.

</div>

<div class="content-box">

## Exercises

### Exercise 1 — Triple application at 0
$$
\lim_{x\to 0} \frac{\sin x - x}{x^3}
$$

**Solution:**

Indeterminate form $0/0$. Apply L’Hôpital repeatedly:

$$
\frac{\sin x - x}{x^3}
\xrightarrow{(1)} \frac{\cos x - 1}{3x^2}
\xrightarrow{(2)} \frac{-\sin x}{6x}
\xrightarrow{(3)} \frac{-\cos x}{6}\Big|_{x=0} = -\frac{1}{6}.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{\sin x - x}{x^3} = -\tfrac{1}{6}
$$

---

### Exercise 2 — Twice at 0 (exponential)
$$
\lim_{x\to 0} \frac{e^x - 1 - x}{x^2}
$$

**Solution:**

Form $0/0$. Differentiate numerator and denominator twice:

$$
\xrightarrow{(1)} \frac{e^x - 1}{2x}
\xrightarrow{(2)} \frac{e^x}{2}\Big|_{x=0} = \frac{1}{2}.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{e^x - 1 - x}{x^2} = \tfrac{1}{2}
$$

---

### Exercise 3 — Growth comparison at $+\infty$
$$
\lim_{x\to +\infty} \frac{\log x}{\sqrt{x}}
$$

**Solution:**

Indeterminate $\infty/\infty$. One application suffices:

$$
\frac{\log x}{\sqrt{x}} \xrightarrow{(1)} \frac{1/x}{\tfrac{1}{2}x^{-1/2}} = \frac{2}{\sqrt{x}} \to 0.
$$

**Final Result:**

$$
\lim_{x\to +\infty} \frac{\log x}{\sqrt{x}} = 0
$$

---

### Exercise 4 — Tangent vs. identity
$$
\lim_{x\to 0} \frac{\tan x - x}{x^3}
$$

**Solution:**

Form $0/0$. Differentiate three times:

$$
\xrightarrow{(1)} \frac{\sec^2 x - 1}{3x^2} = \frac{\tan^2 x}{3x^2}
\xrightarrow{(2)} \frac{2\tan x\,\sec^2 x}{6x} = \frac{\tan x\,\sec^2 x}{3x}
\xrightarrow{(3)} \frac{\sec^4 x + 2\tan^2 x\,\sec^2 x}{3}\Big|_{x=0} = \frac{1}{3}.
$$

**Final Result:**

$$
\lim_{x\to 0} \frac{\tan x - x}{x^3} = \tfrac{1}{3}
$$

---

### Exercise 5 — Product $0\cdot\infty$ turned into a quotient
$$
\lim_{x\to 0^+} x\,\log\big((1+x)^{1/x}\big)
$$

**Solution:**

First evaluate the bounded factor:

$$
\log\big((1+x)^{1/x}\big) = \frac{\log(1+x)}{x} \to 1.
$$

Hence the product behaves like $x\cdot 1$ and tends to 0. (No L’Hôpital needed after the algebraic insight.)

**Final Result:**

$$
\lim_{x\to 0^+} x\,\log\big((1+x)^{1/x}\big) = 0
$$

---

### Exercise 6 — Logarithmic trick for $1^{\infty}$
$$
\lim_{x\to 0^+} \big(1+3x\big)^{\,2/x}
$$

**Solution:**

Set $y(x) = (1+3x)^{2/x}$. Work with logs:

$$
\log y(x) = \frac{2}{x}\,\log(1+3x).
$$

Indeterminate $0/0$. Apply L’Hôpital:

$$
\lim_{x\to 0^+} \frac{2\,\log(1+3x)}{x}
= \lim_{x\to 0^+} 2\,\frac{\tfrac{3}{1+3x}}{1} = 6.
$$

Therefore $\log y(x) \to 6$ and

**Final Result:**

$$
\lim_{x\to 0^+} (1+3x)^{2/x} = e^6
$$

---

### Exercise 7 — Classic $0\cdot\infty$ example
$$
\lim_{x\to 0^+} x\,\log x
$$

**Solution:**

Rewrite as a quotient:

$$
\frac{\log x}{1/x} \quad (x\to 0^+).
$$

Form $-\infty/\infty$. L’Hôpital gives

$$
\lim_{x\to 0^+} \frac{1/x}{-1/x^2} = \lim_{x\to 0^+} -x = 0.
$$

**Final Result:**

$$
\lim_{x\to 0^+} x\,\log x = 0
$$

---

### Exercise 8 — $\infty-\infty$ reduced by rationalization
$$
\lim_{x\to +\infty} \big(\sqrt{x^2+x} - x\big)
$$

**Solution:**

Multiply and divide by the conjugate:

$$
\sqrt{x^2+x} - x = \frac{x}{\sqrt{x^2+x}+x}.
$$

Now the limit is of type $\infty/\infty$. Apply L’Hôpital (or divide numerator/denominator by $x$):

$$
\lim_{x\to +\infty} \frac{x}{\sqrt{x^2+x}+x} = \lim_{x\to +\infty} \frac{1}{\sqrt{1+\tfrac{1}{x}}+1} = \tfrac{1}{2}.
$$

**Final Result:**

$$
\lim_{x\to +\infty} (\sqrt{x^2+x} - x) = \tfrac{1}{2}
$$

---

### Exercise 9 — Exponential vs. polynomial at $+\infty$
$$
\lim_{x\to +\infty} \frac{x^3}{e^{x}}
$$

**Solution:**

Form $\infty/\infty$. Apply L’Hôpital three times:

$$
\frac{x^3}{e^x} \xrightarrow{(1)} \frac{3x^2}{e^x} \xrightarrow{(2)} \frac{6x}{e^x} \xrightarrow{(3)} \frac{6}{e^x} \to 0.
$$

**Final Result:**

$$
\lim_{x\to +\infty} \frac{x^3}{e^x} = 0
$$

---

### Exercise 10 — Mixed exponent $1^{\infty}$ with trigonometric factor
$$
\lim_{x\to +\infty} \Big(1+\tfrac{1}{x}\Big)^{\,x\,\sin(1/x)}
$$

**Solution:**

Let $y(x) = (1+1/x)^{x\sin(1/x)}$. Then

$$
\log y(x) = x\sin(1/x)\,\log\Big(1+\tfrac{1}{x}\Big).
$$

Use the expansions as $x\to+\infty$: $\sin(1/x)\sim 1/x$, $\log(1+1/x)\sim 1/x$. Hence

$$
\log y(x) \sim x\cdot \tfrac{1}{x}\cdot \tfrac{1}{x} = \tfrac{1}{x} \to 0.
$$

Therefore $\log y(x)\to 0$ and

**Final Result:**

$$
\lim_{x\to +\infty} \Big(1+\tfrac{1}{x}\Big)^{x\sin(1/x)} = 1
$$

</div>

---
layout: default
date: 2025-08-29
title: "Solved Exercises — Series"
meta-description: "Solved exercises on series: convergence tests (comparison, ratio, root, integral, alternating), absolute vs conditional convergence, telescoping sums, geometric and p-series, with step-by-step solutions."
permalink: "/university/math/calculus-1/series/"
background_image: "/images/euclide.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

Given a sequence $(a_n)$, a (numerical) **series** is the formal sum
$$
\sum_{n=1}^{\infty} a_n, \qquad S_N=\sum_{n=1}^{N} a_n.
$$
If $(S_N)$ converges to $S$, we say the series **converges** and write $\sum a_n=S$; otherwise it **diverges**.

- **Necessary condition:** if $\sum a_n$ converges, then $a_n \to 0$.
- **Absolute vs conditional convergence:**  
  The series is **absolutely convergent** if $\sum |a_n|$ converges; it is **conditionally convergent** if $\sum a_n$ converges but $\sum |a_n|$ diverges.

**Classical tests (toolbox):**
- **Comparison / Limit comparison**  
- **Ratio test (d’Alembert)**  
- **Root test (Cauchy)**  
- **Integral test**  
- **Alternating series test (Leibniz)**  
- **Telescoping series**

**Reference families:**
- **Geometric:** $\sum ar^{n}$ converges iff $|r|<1$ and equals $\frac{a}{1-r}$ (starting at $n=0$).  
- **$p$-series:** $\sum \frac{1}{n^p}$ converges iff $p>1$.

</div>

<div class="content-box">

## Exercises

### Exercise 1 — Geometric baseline
Study $\displaystyle \sum_{n=0}^{\infty}\left(\frac{1}{2}\right)^n$.

**Solution:**  
Geometric with $r=\tfrac12$, convergent with sum $\frac{1}{1-\tfrac12}=2$.

**Final Result:**  
$$
\sum_{n=0}^{\infty}\left(\tfrac{1}{2}\right)^n = 2
$$

---

### Exercise 2 — Harmonic series
Study $\displaystyle \sum_{n=1}^{\infty}\frac{1}{n}$.

**Solution:**  
$p$-series with $p=1$: diverges.

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{1}{n}=\text{diverges}
$$

---

### Exercise 3 — A convergent $p$-series
Study $\displaystyle \sum_{n=1}^{\infty}\frac{1}{n^2}$.

**Solution:**  
$p=2>1$ $\Rightarrow$ converges (equals $\frac{\pi^2}{6}$).

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{1}{n^2}\ \text{converges}
$$

---

### Exercise 4 — Alternating harmonic
Study $\displaystyle \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}$.

**Solution:**  
$b_n=\tfrac1n$ decreases to $0$ $\Rightarrow$ Leibniz test: convergent, not absolutely.

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\ \text{converges conditionally}
$$

---

### Exercise 5 — Absolute convergence with signs
Study $\displaystyle \sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}$.

**Solution:**  
$\sum |a_n|=\sum \tfrac{1}{n^2}$ converges $\Rightarrow$ absolutely convergent.

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\ \text{converges absolutely}
$$

---

### Exercise 6 — Telescoping
Study $\displaystyle \sum_{n=1}^{\infty}\frac{1}{n(n+1)}$.

**Solution:**  
$\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}$.  
Partial sums: $S_N=1-\frac{1}{N+1}\to 1$.

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{1}{n(n+1)}=1
$$

---

### Exercise 7 — Divergence via logarithmic telescoping
Study $\displaystyle \sum_{n=1}^{\infty}\log\!\left(1+\frac{1}{n}\right)$.

**Solution:**  
$\log(1+\tfrac1n)=\log(n+1)-\log n$.  
$S_N=\log(N+1)\to+\infty$.

**Final Result:**  
$$
\sum_{n=1}^{\infty}\log\!\left(1+\frac{1}{n}\right)=\text{diverges to }+\infty
$$

---

### Exercise 8 — Ratio test
Study $\displaystyle \sum_{n=1}^{\infty}\frac{n}{2^n}$.

**Solution:**  
Ratio test $\rho=\tfrac12<1$: convergent.  
Also, $\sum_{n=1}^\infty \tfrac{n}{2^n}=2$.

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{n}{2^n}=2
$$

---

### Exercise 9 — Root test
Study $\displaystyle \sum_{n=1}^{\infty}\frac{n^3}{3^n}$.

**Solution:**  
$\sqrt[n]{\tfrac{n^3}{3^n}} \to \tfrac{1}{3}<1$ $\Rightarrow$ convergent.

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{n^3}{3^n}\ \text{converges}
$$

---

### Exercise 10 — Power series radius
Find the radius of convergence of $\displaystyle \sum_{n=1}^{\infty}\frac{x^n}{n}$.

**Solution:**  
Ratio/root test $\Rightarrow R=1$.  
At $x=1$: harmonic $\Rightarrow$ diverges.  
At $x=-1$: alternating harmonic $\Rightarrow$ converges (conditionally).

**Final Result:**  
$$
R=1,\quad \text{converges for }|x|<1,\ \text{diverges at }x=1,\ \text{converges at }x=-1.
$$

</div>

---

<div class="content-box">

## Explore more topics in Calculus 1

- [Complex Numbers]({{ "/university/math/calculus-1/complex-numbers/" | relative_url }})  
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
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

