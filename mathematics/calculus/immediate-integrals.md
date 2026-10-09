---
layout: default
date: 2026-10-09
title: "Immediate Integrals: Formulas and Worked Examples"
permalink: /mathematics/calculus/immediate-integrals/
description: "Review basic antiderivatives, the power rule and logarithmic integrals through worked examples. Download the immediate-integrals formula sheet."
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

## Continue Studying Integration

- [Integration by substitution]({{ "/mathematics/calculus/integration-by-substitution/" | relative_url }}) — recognize an inner function and its derivative.
- [Integration by parts]({{ "/mathematics/calculus/integration-by-parts/" | relative_url }}) — integrate products using the product rule in reverse.
- [Back to Calculus]({{ "/mathematics/calculus/" | relative_url }})
