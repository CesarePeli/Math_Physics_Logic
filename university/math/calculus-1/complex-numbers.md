---
layout: default
date: 2025-04-20
title: "Solved Exercises — Complex Numbers"
meta-description: "A curated selection of solved exercises on complex numbers: algebraic form, trigonometric form, exponential representation, and basic properties."
permalink: /university/math/calculus-1/complex-numbers/
background_image: /images/complessi.png
featured: true
---

<div class="content-box">

## Theoretical Recall

A **complex number** can be represented in different forms:

- **Algebraic form:** $z = a + ib$, with $a, b \in \mathbb{R}$.
- **Trigonometric (polar) form:** $z = r(\cos \theta + i \sin \theta)$, where  

$$
r = |z| = \sqrt{a^2+b^2}, \qquad \theta = \arg(z).
$$

- **Exponential form (Euler):** $z = re^{i\theta}$.

**Key properties:**
- Conjugate: $\overline{z} = a - ib$.
- Modulus: $|z| = \sqrt{z\,\overline{z}}$.
- **De Moivre’s theorem:**

$$
(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta).
$$

- **Roots of unity:** solutions of $z^n=1$ are equally spaced on the unit circle.

</div>

<div class="content-box">

## Exercises

### Exercise 1
Express the complex number $z = 1 + i$ in polar and exponential form.

**Solution:**  
We compute modulus and argument:

$$
|z| = \sqrt{1^2+1^2} = \sqrt{2}, \qquad \arg(z)=\arctan(1/1)=\tfrac{\pi}{4}.
$$

Therefore

$$
z = \sqrt{2}\,(\cos \tfrac{\pi}{4} + i\sin \tfrac{\pi}{4}) = \sqrt{2}\,e^{i\pi/4}.
$$

**Final Result:**

$$
z = \sqrt{2}\,e^{i\pi/4}
$$

---

### Exercise 2
Compute $(1+i)^4$.

**Solution:**  
Write in exponential form:

$$
1+i=\sqrt{2}\,e^{i\pi/4}.
$$

Then

$$
(1+i)^4 = (\sqrt{2})^4 e^{i\pi} = 4(-1) = -4.
$$

**Final Result:**

$$
(1+i)^4 = -4
$$

---

### Exercise 3
Find all solutions of $z^3=1$.

**Solution:**  
Equation:

$$
z_k=e^{i2k\pi/3}, \quad k=0,1,2.
$$

Thus

$$
z_0=1,\quad z_1=-\tfrac{1}{2}+ i\tfrac{\sqrt{3}}{2},\quad z_2=-\tfrac{1}{2}- i\tfrac{\sqrt{3}}{2}.
$$

**Final Result:**

$$
\{\,1,\;-1/2+i\sqrt{3}/2,\;-1/2-i\sqrt{3}/2\,\}
$$

---

### Exercise 4
Find all solutions of $z^4=-16$.

**Solution:**  
Rewrite RHS: $-16=16 e^{i\pi}$.

$$
z = 2 e^{i(\pi+2k\pi)/4}, \quad k=0,1,2,3.
$$

That is

$$
z=2e^{i\pi/4},\;2e^{i3\pi/4},\;2e^{i5\pi/4},\;2e^{i7\pi/4}.
$$

**Final Result:**

$$
\{\,2e^{i\pi/4},\;2e^{i3\pi/4},\;2e^{i5\pi/4},\;2e^{i7\pi/4}\,\}
$$

---

### Exercise 5
Compute $|(2+i)(3-4i)|$.

**Solution:**  
Expand first:

$$
(2+i)(3-4i)=6-8i+3i-4i^2=10-5i.
$$

Then modulus:

$$
|10-5i|=\sqrt{100+25}=\sqrt{125}=5\sqrt{5}.
$$

**Final Result:**

$$
|(2+i)(3-4i)| = 5\sqrt{5}
$$

---

### Exercise 6
Solve the equation $z^2+(1+i)z+1=0$.

**Solution:**  
Quadratic formula:

$$
z=\frac{-(1+i)\pm\sqrt{(1+i)^2-4}}{2}.
$$

Compute discriminant:

$$
(1+i)^2-4=1+2i-1-4=-4+2i.
$$

Thus

$$
z=\frac{-(1+i)\pm\sqrt{-4+2i}}{2}.
$$

**Note:** To simplify $\sqrt{-4+2i}$, express it in polar form and then use De Moivre.

**Final Result:**

$$
z=\frac{-(1+i)\pm\sqrt{-4+2i}}{2}
$$

---

### Exercise 7
Find the cube roots of $-8$.

**Solution:**  
Write RHS: $-8=8e^{i\pi}$.

$$
z=2e^{i(\pi+2k\pi)/3},\quad k=0,1,2.
$$

Explicitly:

$$
2e^{i\pi/3}=1+i\sqrt{3},\quad 2e^{i\pi}=-2,\quad 2e^{i5\pi/3}=1-i\sqrt{3}.
$$

**Final Result:**

$$
\{\,1+i\sqrt{3},\;-2,\;1-i\sqrt{3}\,\}
$$

---

### Exercise 8
Compute the product of all solutions of $z^5=1$.

**Solution:**  
The roots are $e^{i2k\pi/5}, k=0,1,2,3,4$.  
By Vieta’s theorem, the product of roots of $z^5-1=0$ equals $(-1)^5(-1)=1$.

**Final Result:**

$$
\prod_{k=0}^4 e^{i2k\pi/5} = 1
$$

---

### Exercise 9
Express in trigonometric form $z=-1+i\sqrt{3}$.

**Solution:**  
Compute modulus and argument:

$$
|z|=\sqrt{(-1)^2+( \sqrt{3})^2}=2,\quad \theta=\tfrac{2\pi}{3}.
$$

So:

$$
z=2(\cos\tfrac{2\pi}{3}+i\sin\tfrac{2\pi}{3}).
$$

**Final Result:**

$$
z=2(\cos\tfrac{2\pi}{3}+i\sin\tfrac{2\pi}{3})
$$

---

### Exercise 10
Find all solutions of $z^6=64$.

**Solution:**  
Note $64=2^6$. Then

$$
z=2e^{i2k\pi/6},\quad k=0,1,2,3,4,5.
$$

Explicitly:

$$
z=\{\,2,\;2e^{i\pi/3},\;2e^{i2\pi/3},\;2e^{i\pi},\;2e^{i4\pi/3},\;2e^{i5\pi/3}\,\}.
$$

**Final Result:**

$$
\{\,2,\;2e^{i\pi/3},\;2e^{i2\pi/3},\;2e^{i\pi},\;2e^{i4\pi/3},\;2e^{i5\pi/3}\,\}
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


- [Notable Limits](/university/math/calculus-1/notable-limits/)  
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
