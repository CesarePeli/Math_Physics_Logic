---
layout: default
date: 2025-04-22
title: "Solved Exercises — Sequences"
meta-description: "Solved exercises on sequences: convergence, divergence, monotonicity, boundedness, and classical limits, with detailed step-by-step solutions."
permalink: "/university/math/calculus-1/sequences/"
background_image: "/images/serie.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

A **sequence** is a function $a:\mathbb{N} \to \mathbb{R}$, usually denoted by $(a_n)_{n\in\mathbb{N}}$.

- **Convergence:**  
  We say that $a_n \to L \in \mathbb{R}$ if  
  $$\forall \varepsilon > 0, \; \exists N \in \mathbb{N}: n > N \implies |a_n - L| < \varepsilon.$$

- **Divergence:**  
  If $a_n$ tends to $+\infty$ (or $-\infty$) we write  
  $$\lim_{n\to\infty} a_n = +\infty \quad (\text{resp. } -\infty).$$

- **Oscillation:**  
  If $a_n$ has no limit (e.g. alternates between two values), the sequence is **divergent by oscillation**.

- **Monotonicity:**  
  A sequence is monotone increasing if $a_{n+1}\ge a_n$ for all $n$; decreasing if $a_{n+1}\le a_n$.

- **Theorem (Monotone Convergence):**  
  Every bounded and monotone sequence converges.

**Classical Examples:**
- $\lim_{n\to\infty}\frac{1}{n}=0$  
- $\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e$  
- $\lim_{n\to\infty}(-1)^n$ does **not** exist (oscillatory divergence)

</div>

<div class="content-box">

## Exercises

### Exercise 1
Study the convergence of $a_n = \frac{1}{n}$.

**Solution:**  
As $n\to\infty$, denominator $\to\infty$, hence $a_n \to 0$.  

**Final Result:**  

$$
\lim_{n\to\infty}\frac{1}{n}=0
$$

---

### Exercise 2
Study $a_n = \left(1+\frac{1}{n}\right)^n$.

**Solution:**  
This is the classical definition of $e$.  

**Final Result:**  

$$
\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n = e
$$

---

### Exercise 3
Study $a_n = (-1)^n$.

**Solution:**  
The sequence alternates between $1$ and $-1$.  
No finite limit exists.  

**Final Result:**  

$$
\lim_{n\to\infty} (-1)^n \; \text{does not exist (oscillation)}
$$

---

### Exercise 4
Study $a_n = \frac{n}{n+1}$.

**Solution:**  
Divide numerator and denominator by $n$:  
$$
\frac{n}{n+1}=\frac{1}{1+\tfrac{1}{n}} \to 1.
$$  

**Final Result:**  

$$
\lim_{n\to\infty}\frac{n}{n+1}=1
$$

---

### Exercise 5
Study $a_n = \frac{2^n}{n!}$.

**Solution:**  
Denominator grows faster than numerator (factorial vs exponential). Hence limit $0$.  

**Final Result:**  

$$
\lim_{n\to\infty}\frac{2^n}{n!}=0
$$

---

### Exercise 6
Study $a_n = \sqrt{n+1}-\sqrt{n}$.

**Solution:**  
Rationalize:  
$$
\sqrt{n+1}-\sqrt{n}=\frac{1}{\sqrt{n+1}+\sqrt{n}} \to 0.
$$  

**Final Result:**  

$$
\lim_{n\to\infty}(\sqrt{n+1}-\sqrt{n})=0
$$

---

### Exercise 7
Study $a_n = \frac{n^2}{2^n}$.

**Solution:**  
Exponential dominates polynomial, so limit $0$.  

**Final Result:**  

$$
\lim_{n\to\infty}\frac{n^2}{2^n}=0
$$

---

### Exercise 8
Study $a_n = \sqrt[n]{n}$.

**Solution:**  
Take $\log$: $\log a_n=\tfrac{1}{n}\log n \to 0$, so $a_n\to e^0=1$.  

**Final Result:**  

$$
\lim_{n\to\infty}\sqrt[n]{n}=1
$$

---

### Exercise 9
Study $a_n = \frac{n}{\log n}$.

**Solution:**  
As $n\to\infty$, $\log n$ grows slower than $n$, hence $a_n\to\infty$.  

**Final Result:**  

$$
\lim_{n\to\infty}\frac{n}{\log n}=+\infty
$$

---

### Exercise 10
Study $a_n = \frac{n!}{n^n}$.

**Solution:**  
Compare with Stirling: $n! \sim \sqrt{2\pi n}\,(n/e)^n$. Then  
$$
\frac{n!}{n^n}\sim \sqrt{2\pi n}\,e^{-n}\to 0.
$$  

**Final Result:**  

$$
\lim_{n\to\infty}\frac{n!}{n^n}=0
$$

</div>
