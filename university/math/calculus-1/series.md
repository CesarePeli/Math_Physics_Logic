---
layout: default
date: 2025-08-28
title: "Solved Exercises — Series"
meta-description: "Solved exercises on infinite series: convergence tests, geometric and harmonic series, alternating series, and applications with detailed solutions."
permalink: "/university/math/calculus-1/series/"
background_image: "/images/series.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

A **series** is defined from a sequence $(a_n)$ as the infinite sum

$$
\sum_{n=0}^{\infty} a_n.
$$

We consider the sequence of partial sums:

$$
S_N = \sum_{n=0}^N a_n.
$$

- If $(S_N)$ converges to $S$, we say the series converges and $\sum a_n = S$.
- If $(S_N)$ diverges, the series is divergent.

### Fundamental Series

- **Geometric series:**  
  $$\sum_{n=0}^\infty q^n = \frac{1}{1-q}, \quad |q|<1.$$
- **Harmonic series:**  
  $$\sum_{n=1}^\infty \frac{1}{n} \quad \text{diverges}.$$

### Convergence Criteria

- **Comparison test:** If $0\le a_n\le b_n$ and $\sum b_n$ converges, then $\sum a_n$ converges.
- **Ratio test (d’Alembert):**
  $$
  \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=L.
  $$
  If $L<1$, the series converges; if $L>1$, diverges.
- **Root test (Cauchy):**
  $$
  \lim_{n\to\infty}\sqrt[n]{|a_n|}=L.
  $$
  If $L<1$, converges; if $L>1$, diverges.
- **Alternating series test (Leibniz):** If $a_n\searrow 0$, then $\sum (-1)^n a_n$ converges.

</div>

<div class="content-box">

## Exercises

### Exercise 1
$$
\sum_{n=0}^{\infty} \frac{1}{2^n}
$$

**Solution:**  
Geometric series with $q=\tfrac{1}{2}$. Since $|q|<1$:

$$
\sum_{n=0}^\infty \frac{1}{2^n} = \frac{1}{1-1/2}=2.
$$

**Final Result:**  

$$
\sum_{n=0}^{\infty} \frac{1}{2^n}=2
$$

---

### Exercise 2
$$
\sum_{n=1}^\infty \frac{1}{n}
$$

**Solution:**  
This is the harmonic series, which diverges.  

**Final Result:**  

$$
\sum_{n=1}^\infty \frac{1}{n} = +\infty
$$

---

### Exercise 3
$$
\sum_{n=1}^\infty \frac{1}{n^2}
$$

**Solution:**  
$p$-series with $p=2>1$. Converges. Euler proved that the sum equals $\pi^2/6$.  

**Final Result:**  

$$
\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}
$$

---

### Exercise 4
$$
\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n}
$$

**Solution:**  
Alternating harmonic series. By Leibniz criterion, it converges.  

**Final Result:**  

$$
\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n} = \log 2
$$

---

### Exercise 5
$$
\sum_{n=1}^\infty \frac{n}{2^n}
$$

**Solution:**  
Ratio test:  
$$
\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=\lim \frac{(n+1)/2^{n+1}}{n/2^n}=\frac{1}{2}.
$$  
Converges. In fact,  
$$
\sum_{n=1}^\infty \frac{n}{2^n}=2.
$$

**Final Result:**  

$$
\sum_{n=1}^\infty \frac{n}{2^n}=2
$$

---

### Exercise 6
$$
\sum_{n=1}^\infty \frac{1}{n^p}, \quad p>0
$$

**Solution:**  
Converges if $p>1$, diverges for $0<p\le 1$.  

**Final Result:**  

$$
\sum_{n=1}^\infty \frac{1}{n^p} =
\begin{cases}
\text{converges}, & p>1, \\\\
\text{diverges}, & 0<p\le 1
\end{cases}
$$

---

### Exercise 7
$$
\sum_{n=1}^\infty \frac{n!}{n^n}
$$

**Solution:**  
Root test:  
$$
\sqrt[n]{\frac{n!}{n^n}} \sim \frac{n/e}{n} = e^{-1}<1.
$$  
Hence converges.  

**Final Result:**  

$$
\sum_{n=1}^\infty \frac{n!}{n^n} \;\;\text{converges}
$$

---

### Exercise 8
$$
\sum_{n=1}^\infty \frac{(-1)^n}{\sqrt{n}}
$$

**Solution:**  
Alternating series, terms decrease to $0$, so converges conditionally.  

**Final Result:**  

$$
\sum_{n=1}^\infty \frac{(-1)^n}{\sqrt{n}} \;\;\text{converges conditionally}
$$

---

### Exercise 9
$$
\sum_{n=1}^\infty \frac{1}{n(n+1)}
$$

**Solution:**  
Telescopic:  
$$
\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}.
$$

Partial sums:  
$$
S_N=1-\frac{1}{N+1}\to 1.
$$

**Final Result:**  

$$
\sum_{n=1}^\infty \frac{1}{n(n+1)}=1
$$

---

### Exercise 10
$$
\sum_{n=1}^\infty \frac{2^n}{n!}
$$

**Solution:**  
Ratio test:  
$$
\frac{a_{n+1}}{a_n}=\frac{2^{n+1}/(n+1)!}{2^n/n!}=\frac{2}{n+1}\to 0.
$$  
So converges. In fact,  
$$
\sum_{n=0}^\infty \frac{2^n}{n!}=e^2.
$$

Therefore:  

**Final Result:**  

$$
\sum_{n=1}^\infty \frac{2^n}{n!}=e^2-1
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

