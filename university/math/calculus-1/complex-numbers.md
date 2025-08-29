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
