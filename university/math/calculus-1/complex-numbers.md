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

$$
z = a + ib, \quad i^2 = -1 .
$$

- **Conjugate and modulus**:  

$$
\overline{z} = a - ib, \quad |z| = \sqrt{a^2+b^2} .
$$

- **Polar and exponential form**:  

$$
z = r(\cos \theta + i\sin \theta) = re^{i\theta}, \quad r = |z|, \ \theta = \arg(z) .
$$

- **De Moivre’s formula**:  

$$
(re^{i\theta})^n = r^n e^{in\theta} .
$$

- **n-th roots of unity**:  

$$
z_k = e^{\tfrac{2k\pi i}{n}}, \quad k=0,1,\dots,n-1 .
$$

- Useful relations:  

$$
|zw| = |z|\,|w|, \quad \overline{zw} = \overline{z}\,\overline{w} .
$$

</div>

---

<div class="content-box">

## Theoretical recalls

The idea of complex numbers began to emerge around the 16th century, when Italian algebraists attempted to solve algebraic equations.  
The term *imaginary number* was introduced by Bombelli (1572), while a more rigorous foundation was given by Gauss in the early 19th century.  
One of the most important theorems based on complex numbers is the **Fundamental Theorem of Algebra**.

Given z = x + i y ∈ ℂ, the most important formulas are:

- **Modulus**  

$$
|z| = \sqrt{x^{2}+y^{2}} .
$$

- **Trigonometric form**  

$$
z = |z|(\cos \theta + i\sin \theta) .
$$

- **Euler’s formula**  

$$
e^{i\theta} = \cos\theta + i\sin\theta .
$$

- **Exponential form**  

$$
z = |z|e^{i\theta} .
$$

- **De Moivre’s formula**  

$$
z^{n} = \rho^{n}(\cos(n\theta)+i\sin(n\theta)) .
$$

- **n-th roots of a complex number**  

$$
w_{k} = \sqrt[n]{\rho}\Bigl[\cos\!\Bigl(\tfrac{\theta+2k\pi}{n}\Bigr)
+ i\sin\!\Bigl(\tfrac{\theta+2k\pi}{n}\Bigr)\Bigr],
\quad k=0,1,\dots,n-1 .
$$

</div>

---

<div class="content-box">

## Exercises

**Ex 1.** Sixth roots of −1.  

**Solution.** Since |−1|=1 and arg(−1)=π, by the n-th roots formula:  

$$
w_k=\sqrt[6]{1}\Bigl[\cos\!\Bigl(\tfrac{\pi+2k\pi}{6}\Bigr)+i\sin\!\Bigl(\tfrac{\pi+2k\pi}{6}\Bigr)\Bigr],\quad k=0,\dots,5 .
$$

Thus  

$$
\frac{\sqrt{3}}{2}+\frac{i}{2},\quad i,\quad -\frac{\sqrt{3}}{2}+\frac{i}{2},\quad -\frac{\sqrt{3}}{2}-\frac{i}{2},\quad -i,\quad \frac{\sqrt{3}}{2}-\frac{i}{2}.
$$

**Final result**  

$$
w=\Bigl\{\tfrac{\sqrt{3}}{2}\pm\tfrac{i}{2},\ \pm i,\ -\tfrac{\sqrt{3}}{2}\pm\tfrac{i}{2}\Bigr\}.
$$

---

**Ex 2.** Solve |z| z̄ = 2i.  

**Solution.** Taking moduli:  

$$
||z|\,\overline{z}|=|2i| \ \Rightarrow\ |z|^2=2 \ \Rightarrow\ |z|=\sqrt{2} .
$$

Back to the equation:  

$$
\sqrt{2}\,z̄=2i \ \Rightarrow\ z̄=2i/\sqrt{2} \ \Rightarrow\ z=-\sqrt{2}\,i .
$$

**Final result**  

$$
z=-\sqrt{2}\,i .
$$

---

**Ex 3.** Solve the system  

$$
\begin{cases}
z^{2}+w^{4}=0 \\[6pt]
z^{3}\,\overline{w}^{\,5}=1
\end{cases}
$$

**Solution.** Equivalent system:  

$$
\begin{cases}
z^{2}=-w^{4} \\[6pt]
z^{6}\,\overline{w}^{\,10}=1
\end{cases}
$$

From the first: z⁶=−w¹². Substitute:  

$$
w^{12}\,\overline{w}^{\,10}=-1 \ \Rightarrow\ w^{2}|w|^{20}=-1 .
$$

Taking moduli: |w|²²=1 ⇒ |w|=1. Then w²=−1 ⇒ w=±i. From z²=−1 ⇒ z=±i.  
Valid solutions: (i,−i) and (−i,i).  

**Final result**  

$$
(z,w)\in\{(i,-i),\ (-i,i)\} .
$$

---

**Ex 4.** Solve z²+(i−1)z−i=0.  

**Solution.** Discriminant:  

$$
\Delta=(i-1)^{2}+4i=1+2i+i^{2}=(1+i)^{2} .
$$

Thus z₁=1, z₂=−i.  
Factorization check: (z−1)(z+i)=0.  

**Final result**  

$$
z\in\{1,\ -i\}.
$$

---

**Ex 5.** Solve z⁴ = z̄³.  

**Solution.** Multiply by z³:  

$$
z^{7}=|z|^{6} .
$$

Taking moduli: |z|⁴=|z|³ ⇒ z=0 or |z|=1.  
If |z|=1, then z⁷=1 ⇒ z are 7th roots of unity.  

**Final result**  

$$
z=0 \quad \text{or} \quad z=e^{2\pi i k/7},\ k=0,\dots,6 .
$$

---

**Ex 6.** Solve z²+z z̄ = 1+i.  

**Solution.** Let z=x+iy:  

$$
(x+iy)^{2}+(x+iy)(x-iy)=1+i
$$

$$
2x^{2}+2ixy=1+i .
$$

So x²=½, xy=½ ⇒ x=±√2/2, y=±√2/2 with same sign.  

**Final result**  

$$
z\in\Bigl\{\tfrac{\sqrt{2}}{2}\pm i\tfrac{\sqrt{2}}{2}\Bigr\}.
$$

---

**Ex 7.** Solve Re(z²)=z+i.  

**Solution.** Re(z²)=x²−y². Equation:  

$$
x^{2}-y^{2}=x+i(y+1) .
$$

So y=−1 and x²−(−1)²=x ⇒ x²−1=x ⇒ x=(1±√5)/2.  

**Final result**  

$$
z=\tfrac{1\pm\sqrt{5}}{2}-i .
$$

---

**Ex 8.** Solve i (z+1)³ = i.  

**Solution.** Divide by i: (z+1)³=1. Let ω=z+1 ⇒ ω³=1 ⇒ ω∈{1, −½±i√3/2}.  
So z∈{0, −3/2±i√3/2}.  

**Final result**  

$$
z\in\Bigl\{0,\ -\tfrac{3}{2}\pm i\tfrac{\sqrt{3}}{2}\Bigr\}.
$$

---

**Ex 9.** Solve (z⁵ z̄² − 1)(z²+z+2)=0.  

**Solution.** Case 1: |z|=1 ⇒ z³=1 ⇒ z∈{1, −½±i√3/2}.  
Case 2: z²+z+2=0 ⇒ z=(−1±i√7)/2.  

**Final result**  

$$
z\in\Bigl\{1,\ -\tfrac{1}{2}\pm i\tfrac{\sqrt{3}}{2},\ \tfrac{-1\pm i\sqrt{7}}{2}\Bigr\}.
$$

---

**Ex 10.** Solve (2z−1)²(2z̄+1)=4z(2z−1).  

**Solution.** Either 2z−1=0 ⇒ z=½, or:  

$$
(2z-1)(2z̄+1)=4z .
$$

Let z=x+iy:  

$$
x^{2}+y^{2}-x=\tfrac{1}{4} .
$$

That is circle centered at (½,0), radius √2/2, including z=½.  

**Final result**  

$$
z=\tfrac{1}{2}\ \ \text{or}\ \ x^{2}+y^{2}-x=\tfrac{1}{4}.
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
