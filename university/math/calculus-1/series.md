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

