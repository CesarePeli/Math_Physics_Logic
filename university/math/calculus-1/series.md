---
layout: default
date: 2025-08-29
title: "Solved Exercises — Series"
meta-description: "Solved exercises on numerical series with detailed solutions and original author’s remarks: geometric, harmonic, p-series, alternating, absolute, telescoping, integral, ratio, root, and power series."
permalink: "/university/math/calculus-1/series/"
background_image: "/images/serie.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

Given a sequence $(a_n)$, a **series** is the formal sum
$$
\sum_{n=1}^{\infty} a_n, \qquad S_N=\sum_{n=1}^{N} a_n.
$$
If $(S_N)$ converges to $S$, we say the series **converges** and write $\sum a_n=S$; otherwise it **diverges**.

- **Necessary condition (Cauchy criterion):**  
  A series $\sum a_n$ converges iff its partial sums $(S_N)$ form a Cauchy sequence:  
  $$
  \forall \varepsilon>0,\ \exists N:\ m>n\geq N \implies \left|\sum_{k=n+1}^m a_k\right| < \varepsilon.
  $$
  In particular, convergence implies $a_n \to 0$.

---

### Main convergence tests

- **Comparison test:** if $0\le a_n\le b_n$ and $\sum b_n$ converges, then $\sum a_n$ converges.  
- **Limit comparison test:** if $\lim\frac{a_n}{b_n}=c\in(0,\infty)$, then $\sum a_n$ and $\sum b_n$ share the same nature.  
- **Ratio test (d’Alembert):**  
  $$
  \rho=\limsup\left|\frac{a_{n+1}}{a_n}\right|
  $$
  $\rho<1\Rightarrow$ convergent, $\rho>1\Rightarrow$ divergent.  
- **Root test:**  
  $$
  r=\limsup\sqrt[n]{|a_n|}
  $$
  $r<1\Rightarrow$ convergent, $r>1\Rightarrow$ divergent.  
- **Integral test:** for decreasing $f(x)\ge0$, $\sum f(n)$ converges iff $\int f(x)dx$ converges.  
- **Alternating series test (Leibniz):** if $b_n\downarrow0$, then $\sum (-1)^{n+1}b_n$ converges.  
- **Telescoping series:** $\sum (b_n-b_{n+1})$ telescopes to $b_1-\lim b_n$.

---

### Reference families

- **Geometric:** $\sum ar^n$ converges iff $|r|<1$, sum $=\frac{a}{1-r}$.  
- **$p$-series:** $\sum \frac{1}{n^p}$ converges iff $p>1$.

</div>

<div class="content-box">

## Exercises

### Exercise 1 — Geometric series
$\displaystyle \sum_{n=0}^{\infty}\left(\frac{1}{2}\right)^n$  

**Solution:**  
Geometric with $r=\tfrac12<1$, sum $2$.  

Observation: The simplest convergent series; it shows how a geometric decay ensures finite total.  

**Final Result:**  
$$
\sum_{n=0}^{\infty}\left(\tfrac{1}{2}\right)^n=2
$$

---

### Exercise 2 — Harmonic series
$\displaystyle \sum_{n=1}^{\infty}\frac{1}{n}$  

**Solution:**  
$p=1$, diverges (by integral test $\int 1/x$).  

Observation: Terms vanish but too slowly; a fundamental counterexample reminding that $a_n\to0$ is not sufficient.  

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{1}{n}=\text{diverges}
$$

---

### Exercise 3 — Convergent $p$-series
$\displaystyle \sum_{n=1}^{\infty}\frac{1}{n^2}$  

**Solution:**  
$p=2>1$, converges.  

Observation: A classical result due to Euler: the exact sum equals $\pi^2/6$, but convergence follows directly from $p>1$.  

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{1}{n^2}\ \text{converges}
$$

---

### Exercise 4 — Alternating harmonic (Leibniz test)
$\displaystyle \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}$  

**Solution:**  
$b_n=1/n$ decreases to $0$, so by Leibniz the series converges. Not absolutely, since $\sum 1/n$ diverges.  

Observation: Canonical example of conditional convergence; sign alternation “slows down” divergence.  

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\ \text{converges conditionally}
$$

---

### Exercise 5 — Absolute convergence
$\displaystyle \sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}$  

**Solution:**  
Since $\sum 1/n^2$ converges, the alternating series converges absolutely.  

Observation: When absolute convergence holds, conditional/alternating arguments are unnecessary.  

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{(-1)^n}{n^2}\ \text{converges absolutely}
$$

---

### Exercise 6 — Telescoping series
$\displaystyle \sum_{n=1}^{\infty}\frac{1}{n(n+1)}$  

**Solution:**  
$\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}$. The partial sums collapse: $S_N=1-\tfrac{1}{N+1}\to1$.  

Observation: Telescoping structure is powerful; often the hardest step is spotting the decomposition.  

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{1}{n(n+1)}=1
$$

---

### Exercise 7 — Integral test
$\displaystyle \sum_{n=2}^{\infty}\frac{1}{n\ln n}$  

**Solution:**  
Compare with $\int \frac{dx}{x\ln x}$ from $2$ to $\infty$: diverges ($\ln(\ln x)$).  

Observation: This is the borderline case “slower than harmonic”: terms vanish but divergence persists.  

**Final Result:**  
$$
\sum_{n=2}^{\infty}\frac{1}{n\ln n}=\text{diverges}
$$

---

### Exercise 8 — Ratio test
$\displaystyle \sum_{n=1}^{\infty}\frac{n}{2^n}$  

**Solution:**  
$\lim \frac{a_{n+1}}{a_n}=\tfrac12<1$, converges. In fact $\sum \frac{n}{2^n}=2$.  

Observation: Ratio test is decisive when factorials or exponentials dominate.  

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{n}{2^n}=2
$$

---

### Exercise 9 — Root test
$\displaystyle \sum_{n=1}^{\infty}\frac{n^3}{3^n}$  

**Solution:**  
$\sqrt[n]{n^3/3^n}\to 1/3<1$, converges.  

Observation: Root test is well-suited for terms with $n$-th powers and exponentials.  

**Final Result:**  
$$
\sum_{n=1}^{\infty}\frac{n^3}{3^n}\ \text{converges}
$$

---

### Exercise 10 — Power series
$\displaystyle \sum_{n=1}^{\infty}\frac{x^n}{n}$  

**Solution:**  
Radius $R=1$ by ratio/root. At $x=1$: harmonic $\Rightarrow$ diverges. At $x=-1$: alternating harmonic $\Rightarrow$ converges conditionally.  

Observation: Power series demand careful boundary checks; the interior is automatic.  

**Final Result:**  
$$
R=1,\quad \text{converges for }|x|<1,\ \text{diverges at }x=1,\ \text{converges at }x=-1
$$

</div>

---

<div class="content-box">

## Explore more topics in Calculus 1

- [Complex Numbers]({{ "/university/math/calculus-1/complex-numbers/" | relative_url }})  
- [Notable Limits](/university/math/calculus-1/notable-limits/)  
- [Limits with L’Hôpital’s Rule](/university/math/calculus-1/limits-hopital/)  
- [Limits with Taylor Expansions](/university/math/calculus-1/limits-taylor/)  
- [Sequences](/university/math/calculus-1/sequences/)  
- [Continuity](/university/math/calculus-1/continuity/)  
- [Differentiability](/university/math/calculus-1/differentiability/)  
- [Integration by Parts](/university/math/calculus-1/integration-by-parts/)  
- [Integration by Substitution](/university/math/calculus-1/integration-substitution/)  
- [General ODEs](/university/math/calculus-1/odes-general/)  
- [Cauchy Problems for ODEs](/university/math/calculus-1/odes-cauchy/)  

</div>
