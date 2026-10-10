---
layout: default
area: mathematics
topic: calculus
level: university
content_type: solved-exercises
background_image: "/images/limiti.png"
permalink: /mathematics/calculus/rational-integrals/
title: "Rational Integrals and Partial Fractions: Original Exercises"
description: "Original solved rational integrals using polynomial division and Hermite partial fractions, including repeated poles and irreducible quadratics."
date: 2026-10-10
last_modified_at: 2026-10-10
---

# Rational Integrals and Partial Fractions: Original Exercises


<div class="content-box">

The theory and selected worked exercises are adapted into English from *Eserciziario 2.1* by Antonino De Martino and Luana Manfredini. Original exercise statements and parameter cases are retained. Mathematical corrections are identified explicitly.

</div>

<div class="content-box">

## Polynomial Division and Hermite Decomposition

These three original exercises cover proper and improper rational functions, distinct linear factors, irreducible quadratic factors and repeated poles. Factor the denominator, divide first if needed, and match numerator coefficients. Primitives are valid separately on each interval avoiding the poles.

</div>

<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5961. -->

Evaluate the integral:

$$
\int \frac{1}{x^{3}-1} \, dx.
$$



**Solution.**

Factor the denominator and use the source's Hermite decomposition:
$$
x^3-1=(x-1)(x^2+x+1).
$$
$$
\frac1{x^3-1}=\frac A{x-1}+\frac{Bx+C}{x^2+x+1}.
$$
Matching the numerator coefficients gives:
$$
A+B=0,\quad A-B+C=0,\quad A-C=1.
$$
$$
A=\frac13,\quad B=-\frac13,\quad C=-\frac23.
$$
$$
I=\frac13\int\frac{dx}{x-1}-\frac13\int\frac{x+2}{x^2+x+1}\,dx.
$$
Separate a logarithmic derivative:
$$
\frac13\int\frac{x+2}{x^2+x+1}\,dx
=\frac16\int\frac{2x+1}{x^2+x+1}\,dx
+\frac12\int\frac{dx}{x^2+x+1}.
$$
Complete the square, or use the complex conjugate factors as in the source:
$$
x^2+x+1=(x+1/2)^2+3/4
=(x+1/2-i\sqrt3/2)(x+1/2+i\sqrt3/2).
$$
$$
\frac12\int\frac{dx}{x^2+x+1}
=\frac1{\sqrt3}\arctan\left(\frac{2x+1}{\sqrt3}\right)+C.
$$

**Final result**

$$
\frac13\log|x-1|-\frac16\log(x^2+x+1)-\frac1{\sqrt3}\arctan\left(\frac{2x+1}{\sqrt3}\right)+C
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6000. -->

Evaluate the integral:

$$
\int \frac{x^{3}}{x^{2}-5x+6}\, dx.
$$



**Solution.**

Start with polynomial division:
$$
\frac{x^3}{x^2-5x+6}=x+5+\frac{19x-30}{(x-2)(x-3)}.
$$
The first two terms integrate to x²/2 + 5x. For the remainder:
$$
\frac{19x-30}{(x-2)(x-3)}=\frac A{x-2}+\frac B{x-3}.
$$
$$
A+B=19,\quad3A+2B=30,
\qquad A=-8,\quad B=27.
$$
$$
\int\frac{19x-30}{(x-2)(x-3)}\,dx
=-8\log|x-2|+27\log|x-3|+C.
$$

**Final result**

$$
\frac{x^2}{2}+5x-8\log|x-2|+27\log|x-3|+C
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6027. -->

Evaluate the integral:

$$
\int \frac{x^{2}+1}{x^{3}-4x^{2}+5x-2}\, dx.
$$



**Solution.**

The denominator factors as:
$$
x^3-4x^2+5x-2=(x-1)^2(x-2).
$$
**Author's observation:** one strategy is to find the most immediate root of the cubic and then solve the remaining quadratic equation. The repeated factor requires a second-order term. Use the source's derivative form:
$$
\frac{x^2+1}{(x-1)^2(x-2)}
=\frac A{x-1}+\frac B{x-2}+\frac d{dx}\left(\frac C{x-1}\right).
$$
The combined numerator is:
$$
(A+B)x^2-(3A+2B+C)x+(2A+B+2C).
$$
$$
A+B=1,\quad3A+2B+C=0,\quad2A+B+2C=1.
$$
$$
A=-4,\quad B=5,\quad C=2.
$$
Integrate the logarithmic terms and the exact derivative separately.

**Final result**

$$
-4\log|x-1|+5\log|x-2|+\frac2{x-1}+C
$$

</div>


<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
