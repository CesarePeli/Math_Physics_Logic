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

## Theoretical recalls

- **Complex numbers** are defined as ordered pairs of real numbers, with algebraic form  
  $$ z = a + ib, \quad i^2 = -1. $$
- **Conjugate and modulus**:  
  $$ \overline{z} = a - ib, \quad |z| = \sqrt{a^2+b^2}. $$
- **Polar and exponential form**:  
  $$ z = r(\cos \theta + i\sin \theta) = re^{i\theta}, \quad r = |z|, \ \theta = \arg(z). $$
- **De Moivre’s formula**:  
  $$ (re^{i\theta})^n = r^n e^{in\theta}. $$
- **n-th roots of unity**:  
  $$ z_k = e^{\frac{2k\pi i}{n}}, \quad k=0,1,\dots,n-1. $$
- Useful relations:  
  $$ |zw| = |z|\,|w|, \quad \overline{zw} = \overline{z}\,\overline{w}. $$

</div>

---

---
date: 2025-08-30
layout: default
title: Complex Numbers — Worked Exercises
permalink: /university/math/calculus-1/complex-numbers/
nav_exclude: false
description: "Worked exercises on complex numbers with theory recalls and faithful solutions based on the original exercise set."
---

<div class="content-box">

## Theoretical recalls

The idea of complex numbers began to emerge around the 16th century, when Italian algebraists attempted to solve algebraic equations.  
The term *imaginary number* was introduced by Bombelli (1572), while a more rigorous foundation was given by Gauss in the early 19th century.  
One of the most important theorems based on complex numbers is the **Fundamental Theorem of Algebra**.

Given \( z = x + iy \in \mathbb{C} \), the most important formulas are:

- **Modulus**  
  $$ |z| = \sqrt{x^{2}+y^{2}}. $$

- **Trigonometric form**  
  $$ z = |z|(\cos \theta + i\sin \theta). $$

- **Euler’s formula**  
  $$ e^{i\theta} = \cos\theta + i\sin\theta. $$

- **Exponential form**  
  $$ z = |z|e^{i\theta}. $$

- **De Moivre’s formula**  
  $$ z^{n} = \rho^{n}(\cos(n\theta)+i\sin(n\theta)). $$

- **n-th roots of a complex number**  
  $$
  w_{k} = \sqrt[n]{\rho}\left[\cos\!\left(\frac{\theta+2k\pi}{n}\right)
  + i\sin\!\left(\frac{\theta+2k\pi}{n}\right)\right],
  \quad k=0,1,\dots,n-1.
  $$

</div>


---

<div class="content-box">

### Exercise 1 — Sixth roots of \(-1\)
Find the sixth roots of \(-1\).

**Solution.** Since \(|-1|=1\) and \(\arg(-1)=\pi\), by the n-th roots formula:
$$
w_k=\sqrt[6]{1}\left[\cos\!\left(\frac{\pi+2k\pi}{6}\right)+i\sin\!\left(\frac{\pi+2k\pi}{6}\right)\right],\quad k=0,\dots,5.
$$
Thus
\[
\frac{\sqrt{3}}{2}+\frac{i}{2},\ i,\ -\frac{\sqrt{3}}{2}+\frac{i}{2},\ -\frac{\sqrt{3}}{2}-\frac{i}{2},\ -i,\ \frac{\sqrt{3}}{2}-\frac{i}{2}.
\]

**Final result**  
$$ w=\left\{\tfrac{\sqrt{3}}{2}\pm\tfrac{i}{2},\ \pm i,\ -\tfrac{\sqrt{3}}{2}\pm\tfrac{i}{2}\right\}. $$

</div>

---

<div class="content-box">

### Exercise 2 — Solve \( |z|\,\overline{z}=2i \)
**Solution.** Take moduli on both sides:
\[
||z|\,\overline{z}|=|2i|\ \Rightarrow\ |z|\cdot|z|=2\ \Rightarrow\ |z|=\sqrt{2}.
\]
Back to the equation:
\[
\sqrt{2}\,\overline{z}=2i\ \Rightarrow\ \overline{z}=\frac{2i}{\sqrt{2}}\ \Rightarrow\ z=-\frac{2i}{\sqrt{2}}.
\]

**Final result**  
$$ z=-\frac{2i}{\sqrt{2}}=-\sqrt{2}\,i. $$

</div>

---

<div class="content-box">

### Exercise 3 — Solve the system
\[
\begin{cases}
z^{2}+w^{4}=0\\
z^{3}\,\overline{w}^{\,5}=1
\end{cases}
\]

**Solution.** Consider the equivalent system
\[
\begin{cases}
z^{2}=-w^{4}\\
z^{6}\,\overline{w}^{\,10}=1
\end{cases}
\]
From the first equation: \(z^{6}=(z^{2})^{3}=-w^{12}\). Substitute into the second:
\[
w^{12}\,\overline{w}^{\,10}=-1\ \Rightarrow\ w^{2}\cdot w^{10}\overline{w}^{\,10}=-1\ \Rightarrow\ w^{2}|w|^{20}=-1.
\]
Take moduli:
\[
|w^{2}|\,|w|^{20}=1 \Rightarrow |w|^{22}=1 \Rightarrow |w|=1.
\]
Back to \(w^{2}|w|^{20}=-1\) gives \(w^{2}=-1\), hence \(w=\pm i\). Using \(z^{2}=-w^{4}=-1\) we get \(z=\pm i\).

Checking the original system, the valid pairs are \((z,w)=(i,-i)\) and \((-i,i)\).

**Final result**  
$$ (z,w)\in\{(i,-i),\ (-i,i)\}. $$

</div>

---

<div class="content-box">

### Exercise 4 — Solve \( z^{2}+(i-1)z-i=0 \)
**Solution (method 1).** Discriminant:
\[
\Delta=(i-1)^{2}+4i=1+2i+i^{2}= (1+i)^{2}.
\]
Thus \(z_{1}=1,\ z_{2}=-i\).

**Solution (method 2).** Partial factorization:
\[
z^{2}+(i-1)z-i=z^{2}+iz-z-i=(z-1)(z+i)=0,
\]
so \(z=1\) or \(z=-i\).

**Final result**  
$$ z\in\{1,\ -i\}. $$

</div>

---

<div class="content-box">

### Exercise 5 — Solve \( z^{4}=\overline{z}^{\,3} \)
**Solution.** Multiply both sides by \(z^{3}\):
\[
z^{7}=\overline{z}^{\,3}z^{3}=|z|^{6}.
\]
Taking moduli on the original equation:
\[
|z|^{4}=|z|^{3}\ \Rightarrow\ |z|^{3}(|z|-1)=0\ \Rightarrow\ z=0\ \text{ or }\ |z|=1.
\]
If \(|z|=1\), then \(z^{7}=1\), so \(z\) are the seventh roots of unity.

**Final result**  
$$ z=0\quad \text{or}\quad z=e^{2\pi i k/7},\ k=0,\dots,6. $$

</div>

---

<div class="content-box">

### Exercise 6 — Solve \( z^{2}+z\overline{z}=1+i \)
**Solution.** Let \(z=x+iy\). Then
\[
(x+iy)^{2}+(x+iy)(x-iy)=1+i
\]
\[
x^{2}-y^{2}+2ixy+x^{2}+y^{2}=1+i \Rightarrow 2x^{2}+2ixy=1+i.
\]
Equate real and imaginary parts:
\[
\begin{cases}
2x^{2}=1\\
2xy=1
\end{cases}
\Rightarrow
\begin{cases}
x=\pm \frac{\sqrt{2}}{2}\\
y=\pm \frac{\sqrt{2}}{2}
\end{cases}
\ \text{with matching signs}.
\]
So
\[
z_{1}=\frac{\sqrt{2}}{2}+i\frac{\sqrt{2}}{2},\quad
z_{2}=-\frac{\sqrt{2}}{2}-i\frac{\sqrt{2}}{2}.
\]

**Final result**  
$$ z\in\left\{\tfrac{\sqrt{2}}{2}\pm i\,\tfrac{\sqrt{2}}{2}\right\}. $$

</div>

---

<div class="content-box">

### Exercise 7 — Solve \( \operatorname{Re}(z^{2})=z+i \)
**Solution.** Since \(\operatorname{Re}(z^{2})=x^{2}-y^{2}\), the equation becomes
\[
x^{2}-y^{2}=x+iy+i \Rightarrow x^{2}-y^{2}-x-i(y+1)=0.
\]
Equating parts:
\[
\begin{cases}
x^{2}-y^{2}-x=0\\
y=-1
\end{cases}
\Rightarrow
x=\dfrac{1\pm\sqrt{5}}{2},\ y=-1.
\]
Hence
\[
z_{1}=\frac{1+\sqrt{5}}{2}-i,\quad z_{2}=\frac{1-\sqrt{5}}{2}-i.
\]

**Final result**  
$$ z=\frac{1\pm\sqrt{5}}{2}-i. $$

</div>

---

<div class="content-box">

### Exercise 8 — Solve \( i\,(z+1)^{3}=i \)
**Solution.** Divide by \(i\): \((z+1)^{3}=1\). Let \(\omega=z+1\). Then \(\omega^{3}=1\) with roots
\[
\omega\in\left\{1,\ -\tfrac{1}{2}\pm i\,\tfrac{\sqrt{3}}{2}\right\}.
\]
Thus
\[
z\in\left\{0,\ -\tfrac{3}{2}\pm i\,\tfrac{\sqrt{3}}{2}\right\}.
\]

**Final result**  
$$ z\in\left\{0,\ -\tfrac{3}{2}\pm i\,\tfrac{\sqrt{3}}{2}\right\}. $$

</div>

---

<div class="content-box">

### Exercise 9 — Solve \( \big(z^{5}\overline{z}^{\,2}-1\big)\,(z^{2}+z+2)=0 \)
**Solution.** By zero-product:
\[
z^{5}\overline{z}^{\,2}=1\quad \text{or}\quad z^{2}+z+2=0.
\]

First branch. Take moduli:
\[
|z|^{5}|\overline{z}|^{2}=|z|^{7}=1\Rightarrow |z|=1.
\]
Then \(z^{5}\overline{z}^{\,2}=z^{3}|z|^{2}=z^{3}=1\), hence \(z^{3}=1\) and
\[
z\in\left\{1,\ -\tfrac{1}{2}\pm i\,\tfrac{\sqrt{3}}{2}\right\}.
\]

Second branch. Quadratic formula:
\[
z=\frac{-1\pm i\sqrt{7}}{2}.
\]

**Final result**  
$$ z\in\left\{1,\ -\tfrac{1}{2}\pm i\,\tfrac{\sqrt{3}}{2},\ \frac{-1\pm i\sqrt{7}}{2}\right\}. $$

</div>

---

<div class="content-box">

### Exercise 10 — Solve \( (2z-1)^{2}(2\overline{z}+1)=4z(2z-1) \)
**Solution.** Factor:
\[
(2z-1)\,\big[(2z-1)(2\overline{z}+1)-4z\big]=0.
\]
Thus either \(2z-1=0\Rightarrow z=\tfrac{1}{2}\), or
\[
(2z-1)(2\overline{z}+1)=4z.
\]
Let \(z=x+iy\). Expanding and separating yields
\[
4x^{2}+4y^{2}-4x=1\ \Rightarrow\ x^{2}+y^{2}-x=\frac{1}{4}.
\]
Hence the solutions are all points on the circle with center \(\left(\tfrac{1}{2},0\right)\) and radius \(\tfrac{\sqrt{2}}{2}\), together with \(z=\tfrac{1}{2}\) (already on that circle).

**Final result**  
$$ z=\frac{1}{2}\ \ \text{or}\ \ x^{2}+y^{2}-x=\frac{1}{4}\ \ (\text{circle of center }(\tfrac{1}{2},0),\ r=\tfrac{\sqrt{2}}{2}). $$

</div>


</div>

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
