---
layout: default
date: 2025-04-20
title: "Solved Exercises — Complex Numbers"
meta-description: "A curated selection of solved exercises on complex numbers: algebraic form, trigonometric form, exponential representation, and basic properties."
permalink: /university/math/calculus-1/complex-numbers/
background_image: "/images/euclide.png"
featured: true
---

**Prepared from the original Italian *Eserciziario 2.1*.**

<div class="content-box">

## Theoretical Recall

A **complex number** can be represented in different forms:

- **Algebraic form:** \(z = a + ib\), with \(a, b \in \mathbb{R}\).
- **Trigonometric (polar) form:** \(z = r(\cos \theta + i \sin \theta)\), where \(r = |z| = \sqrt{a^2+b^2}\) and \(\theta = \arg(z)\).
- **Exponential form (Euler):** \(z = re^{i\theta}\).

**Key properties:**
- \(\overline{z} = a - ib\).
- \(|z| = \sqrt{z\overline{z}}\).
- De Moivre’s theorem: \((\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)\).
- Roots of unity: solutions of \(z^n=1\) are equally spaced on the unit circle.

</div>

<div class="content-box">

## Exercises

### Exercise 1
Express the complex number \(z = 1 + i\) in polar and exponential form.

**Solution:**  
We have \(|z| = \sqrt{1^2+1^2} = \sqrt{2}\), and \(\arg(z)=\arctan(1/1)=\pi/4\).  
So:  
\[ z = \sqrt{2}(\cos \tfrac{\pi}{4} + i\sin \tfrac{\pi}{4}) = \sqrt{2}e^{i\pi/4}. \]

---

### Exercise 2
Compute: \((1+i)^4\).

**Solution:**  
Write \(1+i=\sqrt{2}e^{i\pi/4}\). Then:  
\[(1+i)^4 = (\sqrt{2})^4 e^{i\pi} = 4(-1) = -4.\]

---

### Exercise 3
Find all solutions of \(z^3=1\).

**Solution:**  
Equation: \(z=e^{i2k\pi/3},\;k=0,1,2\).  
So roots are:  
\(z_0=1,\; z_1= -\tfrac{1}{2}+ i\tfrac{\sqrt{3}}{2},\; z_2= -\tfrac{1}{2}- i\tfrac{\sqrt{3}}{2}.\)

---

### Exercise 4
Find all solutions of \(z^4=-16\).

**Solution:**  
Write RHS: \(-16=16 e^{i\pi}\). Solutions:  
\[z = 2 e^{i(\pi+2k\pi)/4},\quad k=0,1,2,3.\]  
That is: \(z=2e^{i\pi/4},\;2e^{i3\pi/4},\;2e^{i5\pi/4},\;2e^{i7\pi/4}.\)

---

### Exercise 5
Compute: \(|(2+i)(3-4i)|\).

**Solution:**  
\((2+i)(3-4i)=6-8i+3i-4i^2=10-5i\).  
So \(|10-5i|=\sqrt{100+25}=\sqrt{125}=5\sqrt{5}.\)

---

### Exercise 6
Solve the equation: \(z^2+(1+i)z+1=0\).

**Solution:**  
Quadratic formula:  
\[z=\frac{-(1+i)\pm\sqrt{(1+i)^2-4}}{2}.\]  
Compute discriminant: \((1+i)^2-4=1+2i-1-4= -4+2i.\)  
Thus:  
\(z=\tfrac{-(1+i)\pm\sqrt{-4+2i}}{2}.\) (Further simplification possible by writing square root in polar form.)

---

### Exercise 7
Find the cube roots of \(-8\).

**Solution:**  
\(-8=8e^{i\pi}\). Roots:  
\[z=2e^{i(\pi+2k\pi)/3},\;k=0,1,2.\]  
So: \(2e^{i\pi/3}=1+ i\sqrt{3},\;2e^{i\pi}= -2,\;2e^{i5\pi/3}=1- i\sqrt{3}.\)

---

### Exercise 8
Compute the product of all solutions of \(z^5=1\).

**Solution:**  
The roots are \(e^{i2k\pi/5}, k=0,1,2,3,4.\) The product equals \((-1)^{5-1}=1\) (since product of roots of \(z^5-1=0\) is \((-1)^5(-1)=1\)).

---

### Exercise 9
Express in trigonometric form: \(z= -1+i\sqrt{3}.\)

**Solution:**  
Modulus: \(|z|=\sqrt{1+3}=2\).  
Argument: \(\arctan(\sqrt{3}/-1)= -\pi/3\), but point is in second quadrant ⇒ angle \(2\pi/3\).  
So: \(z=2(\cos \tfrac{2\pi}{3}+i\sin \tfrac{2\pi}{3}).\)

---

### Exercise 10
Find all solutions of \(z^6=64.\)

**Solution:**  
\(64=2^6\). Roots: \(z=2e^{i2k\pi/6}, k=0,...,5.\)  
So: \(z=2,\;2e^{i\pi/3},\;2e^{i2\pi/3},\;2e^{i\pi},\;2e^{i4\pi/3},\;2e^{i5\pi/3}.\)

</div>
