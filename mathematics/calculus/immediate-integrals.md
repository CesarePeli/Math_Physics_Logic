---
layout: default
last_modified_at: 2026-10-10
date: 2026-10-10
title: "Immediate Integrals: Formulas and Worked Examples"
permalink: /mathematics/calculus/immediate-integrals/
description: "Immediate-integral formulas, the complete integration recall and eight original exercises from Eserciziario 2.1."
background_image: "/images/integrali.png"
area: mathematics
topic: calculus
content_type: solved-exercises
---


<div class="content-box">

# Immediate Integrals: Formulas and Worked Examples

*Exercise editors and source: Prof. Antonino De Martino and Dr. Luana Manfredini, Eserciziario 2.1. The original exercises and source theory are presented here in English for Logic & Motion.*

</div>

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

## Complete Integration Recall

Here C is arbitrary on each interval where the integrand is defined.

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

The following formulas are applications of half-angle identities:

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

### Notable Improper Integrals: Convergence Conditions

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

## Worked Exercises

These additional exercises and their solutions are translated from *Eserciziario 2.1* by Antonino De Martino and Luana Manfredini. No new exercise statements have been introduced.

</div>

<div class="content-box">

### Exercise 1 — Recognizing two trigonometric derivatives

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

### Exercise 2 — An immediate arcsine after rescaling

$$
\int_{-1}^1\frac1{\sqrt{4-x^2}}\,dx.
$$

**Solution.**

Rewrite the radical:

$$
\sqrt{4-x^2}=2\sqrt{1-(x/2)^2}.
$$


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

### Exercise 3 — Algebra before integration

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


**Final Result**

$$
x-\sqrt2\arctan\left(\frac x{\sqrt2}\right)+C
$$

</div>

## Continue Studying Integration

- [Integration by substitution]({{ "/mathematics/calculus/integration-by-substitution/" | relative_url }}) — recognize an inner function and its derivative.
- [Integration by parts]({{ "/mathematics/calculus/integration-by-parts/" | relative_url }}) — integrate products using the product rule in reverse.
- [Back to Calculus]({{ "/mathematics/calculus/" | relative_url }})

<div class="content-box">

[**Definite Integrals →**]({{ "/mathematics/calculus/definite-integrals/" | relative_url }})

[**Improper Integrals →**]({{ "/mathematics/calculus/improper-integrals/" | relative_url }})

[**Rational Integrals →**]({{ "/mathematics/calculus/rational-integrals/" | relative_url }})

</div>


<div class="content-box">

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5894. -->

Solve the following exercise:

$$
\int \frac{1}{\sin x}\, dx.
$$


**Solution.**

Multiply numerator and denominator by sin x and use sin²x=1−cos²x:
$$\int\frac{dx}{\sin x}=\int\frac{\sin x}{1-\cos^2x}\,dx.$$
Put t=cos x, dt=−sin x dx. Partial fractions give
$$-\int\frac{dt}{1-t^2}=\frac12\log\left|\frac{1-t}{1+t}\right|+C.$$
Replace t by cos x. This equals log|tan(x/2)|+C on every interval where sin x≠0.

**Final result**

$$
\frac12\log\left|\frac{1-\cos x}{1+\cos x}\right|+C
$$

</div>

<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6140. -->

Solve the following exercise:

$$
\int \frac{1}{1+ \sin x} \, dx.
$$


**Solution.**

Rationalize the integrand:
$$\frac1{1+\sin x}=\frac{1-\sin x}{\cos^2x}=\frac1{\cos^2x}-\frac{\sin x}{\cos^2x}.$$
The first term has primitive tan x. In the second, set u=cos x, du=−sin x dx, giving the primitive 1/cos x before the subtraction. Thus tan x−sec x is a primitive where cos x≠0. Its equivalent expression −cos x/(1+sin x) extends across points with sin x=1; points with sin x=−1 remain excluded.

**Final result**

$$
-\frac{\cos x}{1+\sin x}+C\qquad(\sin x\ne-1)
$$

</div>


<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6733. -->

Evaluate the integral:

$$
\int x e^{4 x^{2}} \, dx.
$$


**Solution.**



Recognize the inner derivative: d(4x²)=8x dx. With u=4x²,
$$\int xe^{4x^2}\,dx=\frac18\int e^u\,du=\frac18e^u+C.$$
Substituting u back gives a primitive whose derivative is xe⁴ˣ².

**Final result**

$$
\frac18e^{4x^2}+C
$$

</div>


<div class="content-box">

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6734. -->

Evaluate the integral:

$$
\int \frac{3^{\tan x}}{1+\cos 2x} \,dx.
$$


**Solution.**



Use 1+cos 2x=2 cos²x and u=tan x, du=sec²x dx:
$$\int\frac{3^{\tan x}}{1+\cos2x}\,dx=\frac12\int3^u\,du.$$
The exponential antiderivative is 3ᵘ/log 3. Work on intervals with cos x≠0.

**Final result**

$$
\frac{3^{\tan x}}{2\log3}+C
$$

</div>


<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6737. -->

Evaluate the integral:

$$
\int \frac{\cos x (1+\sin x)}{\sqrt{\sin x}} \, dx.
$$


**Solution.**



On intervals with sin x>0 put u=sin x, du=cos x dx. Then
$$\int\frac{(1+u)}{\sqrt u}\,du=\int(u^{-1/2}+u^{1/2})\,du=2\sqrt u+\frac23u^{3/2}+C.$$
Return to the original variable.

**Final result**

$$
2\sqrt{\sin x}+\frac23(\sin x)^{3/2}+C
$$

</div>

<div class="content-box">

[**← Back to Integrals**]({{ "/mathematics/calculus/integrals/" | relative_url }})

</div>
