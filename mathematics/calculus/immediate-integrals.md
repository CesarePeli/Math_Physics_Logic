---
layout: default
last_modified_at: 2026-10-09
date: 2026-10-09
title: "Immediate Integrals: Formulas and Worked Examples"
permalink: /mathematics/calculus/immediate-integrals/
description: "Immediate-integral formulas and six worked examples, with the complete integration recall and three additional exercises from Eserciziario 2.1."
background_image: "/images/integrali.png"
area: mathematics
topic: calculus
content_type: solved-exercises
---

# Immediate Integrals: Formulas and Worked Examples

An immediate integral is evaluated by recognizing a derivative in reverse. This page introduces a few basic patterns and shows how to check the result by differentiation.

[**Download the immediate-integrals formula sheet (PDF)**]({{ "/downloads/immediate_integrals.pdf" | relative_url }})

<div class="content-box">

## Basic Antiderivatives

An indefinite integral describes a family of antiderivatives. The constant C is arbitrary on each interval of the domain. For a real exponent α other than −1, on intervals where the power is real and differentiable:

$$
\int x^\alpha\,dx=\frac{x^{\alpha+1}}{\alpha+1}+C,
\qquad \alpha\ne-1.
$$

The exceptional exponent −1 gives a logarithm, on an interval excluding zero:

$$
\int\frac{1}{x}\,dx=\ln|x|+C.
$$

Other useful patterns are:

$$
\int e^x\,dx=e^x+C.
$$

$$
\int\cos x\,dx=\sin x+C.
$$

$$
\int\sin x\,dx=-\cos x+C.
$$

Integration is linear: integrate sums term by term and take constant factors outside the integral. Products generally require a different method.

</div>

<div class="content-box">

## Example 1: A Polynomial

Evaluate:

$$
\int(3x^2-4x+2)\,dx.
$$

Apply linearity and the power rule to each term:

$$
3\frac{x^3}{3}-4\frac{x^2}{2}+2x+C.
$$

Differentiating gives back the original polynomial.

$$
x^3-2x^2+2x+C
$$

</div>

<div class="content-box">

## Example 2: The Exceptional Power

For x ≠ 0, evaluate:

$$
\int\frac{2}{x}\,dx.
$$

The power rule above does not apply because its denominator would be zero. Use the logarithmic pattern, then multiply by two. The answer is valid separately on each interval not containing zero.

$$
2\ln|x|+C
$$

</div>

<div class="content-box">

## Example 3: Check the Inner Derivative

Evaluate:

$$
\int\cos(3x)\,dx.
$$

The derivative of sin(3x) is 3 cos(3x), so the antiderivative needs a factor of one third:

$$
\frac{d}{dx}\left(\frac{\sin(3x)}{3}\right)=\cos(3x).
$$

$$
\frac{\sin(3x)}{3}+C
$$

</div>


<div class="content-box">

## Complete Integration Recall from the Exercise Book

The following recall preserves all formulas, methods and improper-integral cases in the source introduction. Constants and domain restrictions omitted in the source are made explicit. Here C is arbitrary on each interval where the integrand is defined.

$$
\int k\,dx=kx+C.
$$

$$
\int x^\alpha\,dx=\frac{x^{\alpha+1}}{\alpha+1}+C,\qquad\alpha\ne-1.
$$

$$
\int\frac1x\,dx=\log|x|+C.
$$

$$
\int a^{kx}\,dx=\frac{a^{kx}}{k\log a}+C,\qquad a>0,\ a\ne1,\ k\ne0.
$$

$$
\int(f(x))^\alpha f\prime(x)\,dx=\frac{(f(x))^{\alpha+1}}{\alpha+1}+C,\qquad\alpha\ne-1.
$$

$$
\int\frac{f\prime(x)}{f(x)}\,dx=\log|f(x)|+C,\qquad f(x)\ne0.
$$

$$
\int a^{f(x)}f\prime(x)\,dx=\frac{a^{f(x)}}{\log a}+C,\qquad a>0,\ a\ne1.
$$

$$
\int\cos x\,dx=\sin x+C.
$$

$$
\int\sin x\,dx=-\cos x+C.
$$

$$
\int f\prime(x)\cos(f(x))\,dx=\sin(f(x))+C.
$$

$$
\int f\prime(x)\sin(f(x))\,dx=-\cos(f(x))+C.
$$

$$
\int\frac1{\cos^2x}\,dx=\int(1+\tan^2x)\,dx=\tan x+C.
$$

$$
\int\frac1{\sin^2x}\,dx=\int(1+\cot^2x)\,dx=-\cot x+C.
$$

$$
\int\frac1{\sqrt{1-x^2}}\,dx=\arcsin x+C=-\arccos x+C,\qquad |x|<1.
$$

$$
\int\frac1{1+x^2}\,dx=\arctan x+C.
$$

$$
\int\frac{f\prime(x)}{1+(f(x))^2}\,dx=\arctan(f(x))+C.
$$

$$
\int\cosh x\,dx=\sinh x+C.
$$

$$
\int\sinh x\,dx=\cosh x+C.
$$

For real powers, use intervals where the expressions are real and differentiable. The tangent and cotangent formulas require cos x ≠ 0 and sin x ≠ 0 respectively. The exceptional cases a = 1 or k = 0 in the exponential formula have constant integrand 1.

### Half-Angle Identities

As the source notes, the following formulas are applications of half-angle identities:

$$
\cos^2x=\frac{1+\cos(2x)}2.
$$

$$
\sin^2x=\frac{1-\cos(2x)}2.
$$

### Integration by Parts

$$
\int f(x)g\prime(x)\,dx=f(x)g(x)-\int f\prime(x)g(x)\,dx.
$$

### Integration by Substitution

Setting x = g(t) gives, on an appropriate interval:

$$
\int f(x)\,dx=\int f(g(t))g\prime(t)\,dt.
$$

### Notable Improper Integrals: All Source Cases

For α > 0:

$$
\int_0^\alpha\frac1{x^p}\,dx
\begin{cases}
\text{converges},&p<1,\\
\text{diverges},&p\ge1.
\end{cases}
$$

For α > 0:

$$
\int_\alpha^{+\infty}\frac1{x^p}\,dx
\begin{cases}
\text{converges},&p>1,\\
\text{diverges},&p\le1.
\end{cases}
$$

For α > 1:

$$
\int_1^\alpha\frac1{(\log x)^p}\,dx
\begin{cases}
\text{converges},&p<1,\\
\text{diverges},&p\ge1.
\end{cases}
$$

</div>

<div class="content-box">

## Three Further Integrals from the Exercise Book

These additional exercises and their solutions are translated from *Eserciziario 2.1* by Antonino De Martino and Luana Manfredini. No new exercise statements have been introduced.

</div>

<div class="content-box">

### Source Exercise 1 — Recognizing two trigonometric derivatives

$$
\int\frac1{\sin^2x\cos^2x}\,dx.
$$

**Solution.**

Use the fundamental trigonometric identity:

$$
\int\frac1{\sin^2x\cos^2x}\,dx
=\int\frac{\sin^2x+\cos^2x}{\sin^2x\cos^2x}\,dx.
$$

Separate the two immediate integrals:

$$
\int\frac1{\cos^2x}\,dx+\int\frac1{\sin^2x}\,dx
=\tan x-\cot x+C.
$$

Work on intervals where both sin x and cos x are nonzero.

**Final Result**

$$
\tan x-\cot x+C
$$

</div>

<div class="content-box">

### Source Exercise 2 — An immediate arcsine after rescaling

$$
\int_{-1}^1\frac1{\sqrt{4-x^2}}\,dx.
$$

**Solution.**

Rewrite the radical:

$$
\sqrt{4-x^2}=2\sqrt{1-(x/2)^2}.
$$

**Editorial correction:** The corresponding line in the source omits the square on x/2. The exercise statement and its final result are unchanged.

Set t = x/2, so dx = 2 dt, and use the evenness of the integrand:

$$
\int_{-1}^1\frac1{2\sqrt{1-(x/2)^2}}\,dx
=\int_{-1/2}^{1/2}\frac1{\sqrt{1-t^2}}\,dt
=2\int_0^{1/2}\frac1{\sqrt{1-t^2}}\,dt.
$$

Evaluate the arcsine:

$$
2[\arcsin t]_0^{1/2}=2\frac\pi6=\frac\pi3.
$$

**Final Result**

$$
\frac\pi3
$$

</div>

<div class="content-box">

### Source Exercise 3 — Algebra before integration

$$
\int\frac{x^2}{x^2+2}\,dx.
$$

**Solution.**

Add and subtract 2 in the numerator, as in the source:

$$
\int\frac{x^2+2-2}{x^2+2}\,dx
=\int1\,dx-\int\frac2{x^2+2}\,dx
=x-\int\frac2{x^2+2}\,dx.
$$

For the remaining integral:

$$
\int\frac2{x^2+2}\,dx
=\int\frac1{(x/\sqrt2)^2+1}\,dx.
$$

Set t = x/√2, so dt = dx/√2:

$$
\sqrt2\int\frac1{1+t^2}\,dt=\sqrt2\arctan t+C.
$$

Substitute back into the original integral.

**Editorial correction:** The source's last line accidentally repeats the statement of the preceding definite integral. Its antiderivative belongs to the exercise displayed here.

**Final Result**

$$
x-\sqrt2\arctan\left(\frac x{\sqrt2}\right)+C
$$

</div>

## Continue Studying Integration

- [Integration by substitution]({{ "/mathematics/calculus/integration-by-substitution/" | relative_url }}) — recognize an inner function and its derivative.
- [Integration by parts]({{ "/mathematics/calculus/integration-by-parts/" | relative_url }}) — integrate products using the product rule in reverse.
- [Back to Calculus]({{ "/mathematics/calculus/" | relative_url }})
