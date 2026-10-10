---
layout: default
last_modified_at: 2026-10-10
date: 2026-10-09
title: "Numerical Series: Convergence Tests and 10 Solved Exercises"
description: "Learn comparison, ratio, root, condensation and alternating-series tests with complete theory and ten solved numerical-series exercises, including parameters."
permalink: /mathematics/calculus/numerical-series/
background_image: "/images/serie.png"
area: mathematics
topic: calculus
subtopic: numerical-series
level: university
content_type: solved-exercises
author: "Antonino De Martino and Luana Manfredini"
---


<div class="content-box">

**Exercise editors and source:** **Antonino De Martino and Luana Manfredini**, *Eserciziario 2.1*. The original exercises and source theory are presented here in English for Logic & Motion. Any editorial corrections are marked explicitly.

</div>

<div class="content-box">

# Numerical Series: Convergence Tests and Solved Exercises

This page translates the complete theoretical introduction to numerical series and the first ten worked exercises in *Eserciziario 2.1*, by Antonino De Martino and Luana Manfredini. The English adaptation corrects indexing and positivity slips explicitly noted below and adds a check for absolute convergence in Exercise 10.

Numerical series concern sums of real numbers. For pointwise and uniform convergence of functions, see [Sequences and Series of Functions]({{ "/mathematics/calculus/series/" | relative_url }}).

</div>

<div class="content-box">

## Complete Theoretical Recall

The concept of a series extends addition to infinitely many terms of a given sequence. The following definitions and properties are fundamental.

### Definition and Necessary Condition

For a real sequence aₙ, the series converges if its sequence of partial sums converges:

$$
s_k=\sum_{n=0}^{k}a_n,
\qquad \lim_{k\to\infty}s_k=S\in\mathbb R.
$$

The value S is the sum of the series. A necessary condition is:

$$
\sum_{n=0}^{\infty}a_n\text{ converges}
\quad\Longrightarrow\quad
\lim_{n\to\infty}a_n=0.
$$

**Warning from the source:** This condition is only necessary. When it holds, the series may converge or diverge; a convergence test is still required. When the terms do not tend to zero, the series cannot converge.

### Geometric Series

$$
\sum_{n=0}^{\infty}q^n=\frac1{1-q},\qquad -1<q<1.
$$

For q ≥ 1 the partial sums tend to +∞. For q ≤ −1 the partial sums have no limit, even in the extended real sense.

### Generalized Harmonic Series

$$
\sum_{n=1}^{\infty}\frac1{n^\alpha}
\begin{cases}
\text{converges},&\alpha>1,\\
\text{diverges to }+\infty,&\alpha\le1.
\end{cases}
$$

### Logarithmic Series

$$
\sum_{n=2}^{\infty}\frac1{n(\log n)^\beta}
\begin{cases}
\text{diverges to }+\infty,&\beta\le1,\\
\text{converges},&\beta>1.
\end{cases}
$$

**Editorial correction:** The source starts this sum at n = 0. Its terms are undefined at n = 0 and n = 1; the correct starting index is n = 2.

### Linearity

If both series below converge and c is real, their sum and scalar multiple also converge:

$$
\sum_{n=0}^{\infty}(a_n+b_n)
=\sum_{n=0}^{\infty}a_n+\sum_{n=0}^{\infty}b_n.
$$

$$
\sum_{n=0}^{\infty}ca_n=c\sum_{n=0}^{\infty}a_n.
$$

### Comparison Test

For nonnegative sequences with aₙ ≤ bₙ, convergence of the series of bₙ implies convergence of the series of aₙ. Divergence of the series of aₙ implies divergence of the series of bₙ. Eventual inequalities suffice because changing finitely many terms does not change convergence.

### Limit Comparison: All Three Cases

For positive terms:

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=\ell\in(0,\infty)
\quad\Longrightarrow\quad
\sum a_n\text{ and }\sum b_n\text{ have the same behavior}.
$$

If the ratio tends to zero and the series of bₙ converges, the series of aₙ converges. If the ratio tends to +∞ and the series of bₙ diverges, the series of aₙ diverges.

### Condensation Test

For a nonnegative, eventually nonincreasing sequence:

$$
\sum_{n=1}^{\infty}a_n\text{ converges}
\quad\Longleftrightarrow\quad
\sum_{n=1}^{\infty}2^n a_{2^n}\text{ converges}.
$$

### Ratio Test

For eventually positive aₙ, suppose the limit exists:

$$
\ell=\lim_{n\to\infty}\frac{a_{n+1}}{a_n}.
$$

The series converges for ℓ < 1, diverges for ℓ > 1, and the test is inconclusive for ℓ = 1.

### Root Test

For positive terms, suppose the limit exists:

$$
\ell=\lim_{n\to\infty}\sqrt[n]{a_n}.
$$

The series converges for ℓ < 1, diverges for ℓ > 1, and the test is inconclusive for ℓ = 1.

### Absolute Convergence

A series is absolutely convergent when:

$$
\sum_{n=1}^{\infty}|a_n|<\infty.
$$

Absolute convergence implies convergence of the original series. The converse is false.

### Leibniz's Alternating-Series Test

For the alternating series:

$$
\sum_{n=0}^{\infty}(-1)^n a_n,
$$

assume that aₙ tends to zero, is nonnegative, and is eventually nonincreasing:

$$
\lim_{n\to\infty}a_n=0,
\qquad a_n\ge0,
\qquad a_{n+1}\le a_n\quad(n\ge n_0).
$$

Then the alternating series converges. This test alone does not establish absolute convergence.

</div>

<div class="content-box">

## Choosing a Test

| Structure | Useful first test |
| --- | --- |
| Rational expressions or small-angle terms | Limit comparison with a p-series |
| Factorials or exponentials | Ratio test |
| Terms raised to the n-th power | Root test |
| Alternating signs | Leibniz, then a separate absolute-convergence check |
| A fixed quantity raised to n | Geometric series |

**Source note:** In the worked examples, the necessary condition is understood to hold unless its failure is explicitly identified. Unless indicated otherwise, the series have nonnegative terms. Here the wording includes zero terms at the starting index.

</div>

<div class="content-box">

### Exercise 1 — Limit comparison with a p-series

Study the convergence of:

$$
\sum_{n=1}^{\infty}\frac{n-1}{3n^3+n-1}.
$$

**Solution.**

The terms are nonnegative. Compare with bₙ = 1/n², whose series converges.

$$
\lim_{n\to\infty}\frac{(n-1)/(3n^3+n-1)}{1/n^2}
=\lim_{n\to\infty}\frac{n^3-n^2}{3n^3+n-1}=\frac13>0.
$$

Both series have the same behavior.

**Final Result**

$$
\text{Converges}.
$$

</div>

<div class="content-box">

### Exercise 2 — A difference that does not telescope

Study the convergence of:

$$
\sum_{n=1}^{\infty}\left(\frac1{\sqrt n}-\frac1{\sqrt n+1}\right).
$$

**Solution.**

Combine the fractions:

$$
a_n=\frac1{\sqrt n(\sqrt n+1)}=\frac1{n+\sqrt n}>0.
$$

Compare with the divergent harmonic series:

$$
\lim_{n\to\infty}\frac{1/(n+\sqrt n)}{1/n}
=\lim_{n\to\infty}\frac n{n+\sqrt n}=1.
$$

**Final Result**

$$
\text{Diverges to }+\infty.
$$

</div>

<div class="content-box">

### Exercise 3 — Using a notable limit

Study the convergence of:

$$
\sum_{n=1}^{\infty}\frac1n\sin\frac1n.
$$

**Solution.**

Since 0 < 1/n ≤ 1 < π/2, all terms are positive. Compare with 1/n²:

$$
\lim_{n\to\infty}\frac{(1/n)\sin(1/n)}{1/n^2}
=\lim_{n\to\infty}\frac{\sin(1/n)}{1/n}=1.
$$

The comparison series converges.

**Final Result**

$$
\text{Converges}.
$$

</div>

<div class="content-box">

### Exercise 4 — Ratio test with a radical

Study the convergence of:

$$
\sum_{n=0}^{\infty}\sqrt{ne^{-n}}.
$$

**Solution.**

The term at n = 0 is zero; the remaining terms are positive. For n ≥ 1:

$$
\lim_{n\to\infty}\frac{a_{n+1}}{a_n}
=\lim_{n\to\infty}\sqrt{\frac{n+1}{n}e^{-1}}
=\frac1{\sqrt e}<1.
$$

The ratio test proves convergence.

**Final Result**

$$
\text{Converges}.
$$

</div>

<div class="content-box">

### Exercise 5 — Absolute convergence

Study the convergence of:

$$
\sum_{n=0}^{\infty}\frac{\cos n}{n^2+1}.
$$

**Solution.**

Study absolute values:

$$
\left|\frac{\cos n}{n^2+1}\right|\le\frac1{n^2+1}\le\frac1{n^2},\qquad n\ge1.
$$

The p-series with exponent 2 converges. The finite term at n = 0 does not affect convergence. Comparison proves absolute convergence and hence convergence.

**Final Result**

$$
\text{Converges absolutely}.
$$

</div>

<div class="content-box">

### Exercise 6 — A parameter in the denominator

Study the convergence of:

$$
\sum_{n=0}^{\infty}\frac n{x^{2n}},\qquad x\in\mathbb R\setminus\{0\}.
$$

**Solution.**

The terms are nonnegative. For n ≥ 1 the root test gives:

$$
\lim_{n\to\infty}\sqrt[n]{\frac n{x^{2n}}}
=\lim_{n\to\infty}\frac{\sqrt[n]n}{x^2}=\frac1{x^2}.
$$

If ∣x∣ > 1, the limit is less than 1 and the series converges. If 0 < ∣x∣ < 1, it is greater than 1 and the series diverges. For x = ±1, substitution gives the divergent series with terms n.

**Final Result**

$$
\text{Converges exactly when }|x|>1.
$$

</div>

<div class="content-box">

### Exercise 7 — A logarithmic geometric series

Study the convergence of:

$$
\sum_{n=0}^{\infty}[\log(1+x)]^n,\qquad x>-1.
$$

**Solution.**

The common ratio is log(1+x). Convergence requires:

$$
|\log(1+x)|<1
\quad\Longleftrightarrow\quad
-1<\log(1+x)<1
$$

$$
\quad\Longleftrightarrow\quad
\log(1/e)<\log(1+x)<\log e
\quad\Longleftrightarrow\quad
e^{-1}-1<x<e-1.
$$

For x ≥ e−1, the ratio is at least 1 and the partial sums tend to +∞. For −1 < x ≤ e⁻¹−1, the ratio is at most −1 and the partial sums have no limit.

**Final Result**

$$
\text{Converges exactly when }e^{-1}-1<x<e-1.
$$

</div>

<div class="content-box">

### Exercise 8 — An arctangent tail

Study the convergence of:

$$
\sum_{n=0}^{\infty}\left(\frac\pi2-\arctan n\right).
$$

**Solution.**

For n ≥ 1, 0 < arctan n < π/2, so the terms are positive; the initial term is π/2. Compare with 1/n. L'Hôpital's rule on the corresponding real-variable quotient gives:

$$
\lim_{x\to\infty}\frac{\pi/2-\arctan x}{1/x}
=\lim_{x\to\infty}\frac{-1/(1+x^2)}{-1/x^2}
=\lim_{x\to\infty}\frac{x^2}{1+x^2}=1.
$$

Limit comparison with the harmonic series proves divergence.

**Final Result**

$$
\text{Diverges to }+\infty.
$$

</div>

<div class="content-box">

### Exercise 9 — A root test and the exponential limit

Study the convergence of:

$$
\sum_{n=1}^{\infty}\left(1-\frac1{\sqrt n}\right)^{n\sqrt n}.
$$

**Solution.**

The first term is zero and subsequent terms are positive. Apply the root test:

$$
\lim_{n\to\infty}\sqrt[n]{a_n}
=\lim_{n\to\infty}\left(1-\frac1{\sqrt n}\right)^{\sqrt n}
=e^{-1}<1.
$$

The standard exponential limit proves convergence.

**Final Result**

$$
\text{Converges}.
$$

</div>

<div class="content-box">

### Exercise 10 — Leibniz and conditional convergence

Study the convergence of:

$$
\sum_{n=1}^{\infty}\frac{(-1)^n}{n-\log n}.
$$

**Solution.**

Set aₙ = 1/(n−log n). Since log n < n for n ≥ 1, aₙ is positive. Moreover:

$$
\lim_{n\to\infty}\frac1{n-\log n}
=\lim_{n\to\infty}\frac1{n(1-(\log n)/n)}=0.
$$

To verify monotonicity, consider f(x) = x−log x:

$$
f'(x)=1-\frac1x\ge0,\qquad x\ge1.
$$

Thus the denominators increase and aₙ is nonincreasing. Leibniz proves convergence.

**Additional check:** The absolute-value series diverges by comparison with the harmonic series:

$$
\lim_{n\to\infty}\frac{1/(n-\log n)}{1/n}
=\lim_{n\to\infty}\frac1{1-(\log n)/n}=1.
$$

**Final Result**

$$
\text{Converges conditionally, not absolutely}.
$$

</div>

<div class="content-box">

## Continue Exploring Calculus

- [Sequences and Series of Functions]({{ "/mathematics/calculus/series/" | relative_url }})
- [Notable Limits]({{ "/mathematics/calculus/limits/fundamental-limits-examples/" | relative_url }})
- [Back to Calculus]({{ "/mathematics/calculus/" | relative_url }})

</div>
