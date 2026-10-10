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


<div class="content-box">

# Rational Integrals and Partial Fractions: Original Exercises

*Exercise editors and source: Prof. Antonino De Martino and Dr. Luana Manfredini, Eserciziario 2.1. The original exercises and source theory are presented here in English for Logic & Motion.*

</div>


<div class="content-box">

## Polynomial Division and Hermite Decomposition

These eight original exercises cover proper and improper rational functions, distinct linear factors, irreducible quadratic factors and repeated poles. Factor the denominator, divide first if needed, and match numerator coefficients. Primitives are valid separately on each interval avoiding the poles.

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

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6052. -->

Solve the following exercise:

$$
\int \frac{\tan^{3} x + \tan x}{\tan x+4} \, dx
$$


**Solution.**

Set t=tan x and dt=(1+tan²x)dx. The numerator tan³x+tan x equals t(1+t²), so
$$\int\frac{\tan^3x+\tan x}{\tan x+4}\,dx=\int\frac{t}{t+4}\,dt.$$
Polynomial division gives t/(t+4)=1−4/(t+4). Integrate and return to x. Work on intervals where tan x exists and tan x≠−4.

**Final result**

$$
\tan x-4\log|\tan x+4|+C
$$

</div>

<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6176. -->

Solve the following exercise:

$$
\int_{4}^{16} \frac{1}{(x-\sqrt{x})^2} \, dx.
$$


**Solution.**

Set t=√x, dx=2t dt. The bounds become 2 and 4, and (x−√x)²=t²(t−1)². Hence
$$I=\int_2^4\frac2{t(t-1)^2}\,dt.$$
Determine the partial fractions:
$$\frac2{t(t-1)^2}=\frac2t-\frac2{t-1}+\frac2{(t-1)^2}.$$
A primitive is 2log t−2log(t−1)−2/(t−1). Its values at 4 and 2 give
$$I=2\log\frac43-\frac23-(2\log2-2).$$

**Final result**

$$
\frac43+2\log\frac23
$$

</div>

<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6636. -->

Solve the following exercise:

$$
\int \frac{2 \tan x+1}{\sin^{2} x +3 \cos^{2} x} \, dx
$$


**Solution.**

Set t=tan x, so dx=dt/(1+t²), sin²x=t²/(1+t²) and cos²x=1/(1+t²). The resulting rational integral is
$$\int\frac{2t+1}{t^2+3}\,dt=\int\frac{2t}{t^2+3}\,dt+\int\frac{dt}{t^2+3}.$$
The first term is a logarithmic derivative; rescale t by √3 in the second to obtain an arctangent. This substitution works on intervals where tan x is defined.

**Final result**

$$
\log(\tan^2x+3)+\frac1{\sqrt3}\arctan\frac{\tan x}{\sqrt3}+C
$$

</div>


<div class="content-box">

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6738. -->

Evaluate the integral:

$$
\int \frac{1}{x^{3}+1} \, dx.
$$


**Solution.**

This original statement appears in the unsolved-exercise list. The following worked solution is supplied for this edition.

Factor x³+1=(x+1)(x²−x+1) and determine coefficients:
$$\frac1{x^3+1}=\frac1{3(x+1)}+\frac{-x+2}{3(x^2-x+1)}.$$
In the quadratic numerator use −x+2=−(2x−1)/2+3/2. The derivative part integrates to −log(x²−x+1)/6. Complete the square x²−x+1=(x−1/2)²+3/4 to integrate the remaining part as an arctangent. The pole x=−1 separates the primitive intervals.

**Final result**

$$
\frac13\log|x+1|-\frac16\log(x^2-x+1)+\frac1{\sqrt3}\arctan\frac{2x-1}{\sqrt3}+C
$$

</div>


<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6736. -->

Evaluate the integral:

$$
\int \frac{x-1}{x^{2}-4x+5} \, dx.
$$


**Solution.**

This original statement appears in the unsolved-exercise list. The following worked solution is supplied for this edition.

Write the denominator as (x−2)²+1, and split x−1=(x−2)+1. Then
$$\int\frac{x-1}{(x-2)^2+1}\,dx=\int\frac{x-2}{(x-2)^2+1}\,dx+\int\frac{dx}{(x-2)^2+1}.$$
The first term is half the logarithmic derivative of the denominator; the second is the derivative of arctan(x−2). The denominator is positive for every real x.

**Final result**

$$
\frac12\log(x^2-4x+5)+\arctan(x-2)+C
$$

</div>

<div class="content-box">

[**← Back to Integrals**]({{ "/mathematics/calculus/integrals/" | relative_url }})

</div>
