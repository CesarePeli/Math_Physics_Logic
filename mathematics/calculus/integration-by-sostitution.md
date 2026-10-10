---
layout: default
last_modified_at: 2026-10-10
date: 2026-10-10
original_date: 2025-08-29
title: "Integration by Substitution: Original University Exercises"
permalink: /mathematics/calculus/integration-by-substitution/
redirect_from:
  - /university/math/calculus-1/integration-by-substitution/
background_image: "/images/integrali.png"
description: "Eight original university exercises using Euler and trigonometric substitutions, partial fractions and integration by parts, with original bounds."
area: mathematics
topic: calculus
subtopic: integration-by-substitution
level: university
content_type: solved-exercises
---


<div class="content-box">

# Integration by Substitution: Original University Exercises

*Exercise editors and source: Prof. Antonino De Martino and Dr. Luana Manfredini, Eserciziario 2.1. The original exercises and source theory are presented here in English for Logic & Motion.*

</div>


<div class="content-box">


## Theoretical Recall

Integration by substitution is the integral counterpart of the chain rule.

Suppose that:

$$
x=g(t)
$$

is a differentiable change of variable. Then:

$$
dx=g'(t)\,dt.
$$

Therefore:

$$
\int f(x)\,dx
=
\int f(g(t))g'(t)\,dt.
$$

Another common form begins with:

$$
u=g(x).
$$

Then:

$$
du=g'(x)\,dx.
$$

Whenever an integral contains a composition together with the derivative of the inner function, we can use:

$$
\int f(g(x))g'(x)\,dx
=
\int f(u)\,du.
$$

After evaluating the new integral, the original variable must be restored.

### Common Strategies

A useful substitution often reveals a simpler structure hidden inside the original integrand.

Typical choices include:

- a linear expression raised to a power;
- the argument of a logarithm;
- the denominator of a rational expression;
- the expression inside a radical;
- trigonometric substitutions for quadratic radicals;
- hyperbolic substitutions for expressions involving sums or differences of squares.

For radicals of the form:

$$
\sqrt{1-x^2},
$$

the substitution:

$$
x=\sin t
$$

is often useful because:

$$
1-\sin^2t=\cos^2t.
$$

For expressions involving:

$$
1+x^2,
$$

the substitution:

$$
x=\tan t
$$

can be useful because:

$$
1+\tan^2t=\sec^2t.
$$

Hyperbolic substitutions can similarly exploit:

$$
\cosh^2t-\sinh^2t=1.
$$

**Author’s note:** Always transform both the integrand and the differential consistently. A substitution is not complete until every occurrence of the original variable has been removed from the transformed integral.

</div>


<div class="content-box">

## Exercises

</div>


<div class="content-box">

## Original Worked Exercises

Original bounds and combined methods are retained. The previous indefinite-only version of the improper integral is replaced by the complete problem on the Improper Integrals page.

</div>

<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6062. -->

Evaluate the integral:

$$
\int \frac{1}{\sqrt{x^{2}-2x}} \, dx.
$$


**Solution.**

The real domain is x < 0 or x > 2. Use the source's Euler substitution:
$$
\sqrt{x^2-2x}=x+t.
$$
Squaring and solving for x gives:
$$
x=-\frac{t^2}{2(1+t)},\qquad
dx=-\frac{t^2+2t}{2(1+t)^2}\,dt.
$$
$$
\sqrt{x^2-2x}=\frac{t^2+2t}{2(1+t)}.
$$
Substitute both factors:
$$
\int\frac{dx}{\sqrt{x^2-2x}}
=-\int\frac{2(1+t)}{t^2+2t}\frac{t^2+2t}{2(1+t)^2}\,dt
=-\int\frac{dt}{1+t}.
$$
$$
-\int\frac{dt}{1+t}=-\log|1+t|+C.
$$

**Final result**

$$
-\log|1+\sqrt{x^2-2x}-x|+C
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6130. -->

Evaluate the integral:

$$
\int_{0}^{\frac{\pi}{3}} \frac{2 \cos x}{5-4 \cos^{2} x} \, dx.
$$


**Solution.**

First find a primitive. Set t = sin x, with dt = cos x dx, and use cos²x = 1 − sin²x:
$$
\int\frac{2\cos x}{5-4\cos^2x}\,dx
=2\int\frac{dt}{1+4t^2}
=\arctan(2t)+C.
$$
Restore the variable and evaluate the original bounds:
$$
\left[\arctan(2\sin x)\right]_0^{\pi/3}
=\arctan\sqrt3-\arctan0.
$$

**Final result**

$$
\frac\pi3
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6154. -->

Evaluate the integral:

$$
\int_{\frac{\pi}{4}}^{\frac{\pi}{2}} \frac{\cos x}{\sin^{2} x-2 \sin x} \, dx.
$$


**Solution.**

Set t = sin x. First integrate the transformed rational function:
$$
\int\frac{\cos x}{\sin^2x-2\sin x}\,dx
=\int\frac{dt}{t(t-2)}.
$$
Use partial fractions:
$$
\frac1{t(t-2)}=\frac At+\frac B{t-2},
\qquad A+B=0,\quad-2A=1.
$$
$$
A=-\frac12,\quad B=\frac12,
\qquad F(t)=-\frac12\log|t|+\frac12\log|t-2|.
$$
The bounds in t are √2/2 and one:
$$
I=\left[-\frac12\log|\sin x|+\frac12\log|\sin x-2|\right]_{\pi/4}^{\pi/2}.
$$

**Final result**

$$
\frac12\log\left(\frac{\sqrt2}{4-\sqrt2}\right)
$$

</div>

<div class="content-box">

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6203. -->

Evaluate the integral:

$$
\int_{0}^{1} x^{2} e^{x^{\frac{3}{2}}} \,dx.
$$


**Solution.**

Factor x² as x¹ᐟ² x³ᐟ² and put t = x³ᐟ²:
$$
dt=\frac32\sqrt x\,dx,
\qquad I=\frac23\int_0^1te^t\,dt.
$$
Integration by parts gives:
$$
\frac23\int te^t\,dt=\frac23\left(te^t-\int e^t\,dt\right)
=\frac23e^t(t-1)+C.
$$
$$
I=\left[\frac23e^{x^{3/2}}(x^{3/2}-1)\right]_0^1=\frac23.
$$

**Final result**

$$
\frac23
$$

</div>

<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6214. -->

Evaluate the integral:

$$
\int \frac{x^{3}}{\sqrt{1-x^{2}}} \, dx
$$


**Solution.**

For −1 < x < 1 choose x = sin t with −π/2 < t < π/2, so cos t > 0 and dx = cos t dt:
$$
\int\frac{x^3}{\sqrt{1-x^2}}\,dx
=\int\frac{\sin^3t}{\cos t}\cos t\,dt
=\int(1-\cos^2t)\sin t\,dt.
$$
$$
\int\sin t\,dt+\int\cos^2t(-\sin t)\,dt
=-\cos t+\frac{\cos^3t}{3}+C.
$$
$$
-\sqrt{1-x^2}+\frac{(1-x^2)^{3/2}}3+C
=-\frac{(2+x^2)\sqrt{1-x^2}}3+C.
$$


**Final result**

$$
-\frac{(2+x^2)\sqrt{1-x^2}}3+C
$$

</div>

<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6326. -->

Evaluate the integral:

$$
\int_{0}^{\frac{\pi}{2}} \cos x \log(1+\sin x) \, dx.
$$


**Solution.**

First integrate by parts:
$$
I=\left[\sin x\log(1+\sin x)\right]_0^{\pi/2}
-\int_0^{\pi/2}\frac{\sin x\cos x}{1+\sin x}\,dx.
$$
For the remaining primitive put t = sin x:
$$
\int\frac{\sin x\cos x}{1+\sin x}\,dx
=\int\frac t{1+t}\,dt=t-\log|1+t|+C.
$$
$$
I=\left[\sin x\log(1+\sin x)-\sin x+\log(1+\sin x)\right]_0^{\pi/2}.
$$

**Final result**

$$
\log4-1
$$

</div>

<div class="content-box">

[**Complete improper integral from 2 to infinity →**]({{ "/mathematics/calculus/improper-integrals/" | relative_url }})

</div>


<div class="content-box">

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6314. -->

Solve the following exercise:

$$
\int x^{3} (1+x^{2})^{\frac{1}{3}} \, dx.
$$


**Solution.**

Put t=1+x², so dt=2x dx and x³dx=(t−1)dt/2. The transformed integral is
$$\frac12\int(t-1)t^{1/3}\,dt=\frac12\int(t^{4/3}-t^{1/3})\,dt.$$
Integrate the two powers and replace t by 1+x².

**Final result**

$$
\frac3{14}(1+x^2)^{7/3}-\frac38(1+x^2)^{4/3}+C
$$

</div>

<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6095. -->

Solve the following exercise:

$$
\int \frac{1}{x^{4} \sqrt{x^{3}+1}} \, dx.
$$


**Solution.**

Set t=√(x³+1), so 2t dt=3x²dx and x³=t²−1. The integrand transforms to
$$\int\frac{dx}{x^4\sqrt{x^3+1}}=\frac23\int\frac{dt}{(t^2-1)^2}.$$
Resolve the repeated factors:
$$\frac1{(t^2-1)^2}=\frac14\left(\frac1{(t-1)^2}+\frac1{(t+1)^2}-\frac1{t-1}+\frac1{t+1}\right).$$
Integrating yields −t/[3(t²−1)]+(1/6)log|(t+1)/(t−1)|. Substitute t back. The real integrand requires x>−1 and x≠0.

**Final result**

$$
-\frac{\sqrt{x^3+1}}{3x^3}+\frac16\log\left|\frac{\sqrt{x^3+1}+1}{\sqrt{x^3+1}-1}\right|+C
$$

</div>


<div class="content-box">

[**← Back to Integrals**]({{ "/mathematics/calculus/integrals/" | relative_url }})

</div>
