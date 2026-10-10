---
layout: default
area: mathematics
topic: calculus
level: university
content_type: solved-exercises
background_image: "/images/limiti.png"
permalink: /mathematics/calculus/improper-integrals/
title: "Improper Integrals: Original Convergence and Evaluation Exercises"
description: "Eight improper-integral problems with endpoint and interior singularities, absolute comparison, asymptotic comparison and infinite bounds."
date: 2026-10-10
last_modified_at: 2026-10-10
---


<div class="content-box">

# Improper Integrals: Original Convergence and Evaluation Exercises

*Exercise editors and source: Prof. Antonino De Martino and Dr. Luana Manfredini, Eserciziario 2.1. The original exercises and source theory are presented here in English for Logic & Motion.*

</div>


<div class="content-box">

## Improper Integrals: All Three Source Cases

An endpoint singularity or an infinite interval requires a limit of proper integrals. At an interior singularity, both one-sided improper integrals must converge separately; cancellation in a symmetric limit does not establish convergence.

For α > 0:

$$
\int_0^\alpha\frac{dx}{x^p}\quad
\begin{cases}\text{converges},&p<1,\\\text{diverges},&p\ge1.\end{cases}
$$

$$
\int_\alpha^\infty\frac{dx}{x^p}\quad
\begin{cases}\text{converges},&p>1,\\\text{diverges},&p\le1.\end{cases}
$$

For α > 1:

$$
\int_1^\alpha\frac{dx}{(\log x)^p}\quad
\begin{cases}\text{converges},&p<1,\\\text{diverges},&p\ge1.\end{cases}
$$

Absolute comparison and comparison by a finite positive ratio reduce the following original exercises to these cases. Strict inequalities at p = 1 matter.

</div>

<div class="content-box">

## Original Convergence and Evaluation Problems

</div>

<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5839. -->

Prove convergence and evaluate the integral:

$$
\int_{\frac{1}{e}}^e \frac{\log (|\log x|)}{x} \, dx.
$$


**Solution.**

The integrand has an interior logarithmic singularity at x = 1. Split there:
$$
I=\int_{1/e}^1\frac{\log(-\log x)}x\,dx
+\int_1^e\frac{\log(\log x)}x\,dx.
$$
In the first part use t = −log x and dt = −dx/x; in the second use t = log x and dt = dx/x. Both become the same convergent improper integral:
$$
\int_{1/e}^1\frac{\log(-\log x)}x\,dx
=-\int_1^0\log t\,dt=\int_0^1\log t\,dt.
$$
$$
\int_1^e\frac{\log(\log x)}x\,dx=\int_0^1\log t\,dt.
$$
$$
I=2\lim_{a\to0^+}\left[t\log t-t\right]_a^1
=2\lim_{a\to0^+}(-1-a\log a+a).
$$

**Final result**

$$
-2
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6227. -->

Determine whether the following function is improperly integrable on [1,+∞):

$$
f(x)=\frac{\sin x}{x\sqrt{x+1}}.
$$


**Solution.**

Use absolute comparison, as in the source:
$$
0\le\left|\frac{\sin x}{x\sqrt{x+1}}\right|
\le\frac1{x\sqrt{x+1}}\le\frac1{x^{3/2}},\qquad x\ge1.
$$
The last inequality uses √(x+1) ≥ √x. The comparison integral converges because 3/2 > 1. Therefore the original function is integrable in the improper sense, in fact absolutely.


**Final result**

$$
\int_1^\infty\left|\frac{\sin x}{x\sqrt{x+1}}\right|dx<\infty.
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6236. -->

Determine whether the following function is improperly integrable on [0,1]:

$$
f(x)=\frac1{\sqrt{1-x^3}}.
$$


**Solution.**

Factor the radicand:
$$
1-x^3=(1-x)(1+x+x^2).
$$
For 0 ≤ x < 1:
$$
0\le\frac1{\sqrt{1-x^3}}
=\frac1{\sqrt{1-x}\sqrt{1+x+x^2}}
\le\frac1{\sqrt{1-x}}.
$$
The inequality uses √(1+x+x²) ≥ 1. The comparison integral at the endpoint converges since 1/2 < 1.


**Final result**

$$
\int_0^1\frac{dx}{\sqrt{1-x^3}}<\infty.
$$

</div>

<div class="content-box">

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6261. -->

Prove convergence and evaluate the integral:

$$
\int_{2}^{+\infty} \frac{1}{x \sqrt{x^{2}-1}} \,dx.
$$


**Solution.**

First check convergence by comparing with 1/x²:
$$
\lim_{x\to\infty}\frac{1/(x\sqrt{x^2-1})}{1/x^2}
=\lim_{x\to\infty}\sqrt{\frac{x^2}{x^2-1}}=1.
$$
Keep the source's Euler substitution:
$$
\sqrt{x^2-1}=x+t,\qquad x=-\frac{t^2+1}{2t}.
$$
$$
dx=-\frac{t^2-1}{2t^2}\,dt,
\qquad\sqrt{x^2-1}=\frac{t^2-1}{2t}.
$$
Substitute the displayed expressions for x, the square root, and dx. The negative sign in x cancels the negative sign in dx, while the factors t²−1 and 2t cancel algebraically:
$$
\int\frac{dx}{x\sqrt{x^2-1}}=2\int\frac{dt}{1+t^2}=2\arctan t+C.
$$
The lower endpoint is t = √3 − 2. At the upper endpoint:
$$
t=\sqrt{b^2-1}-b=-\frac1{\sqrt{b^2-1}+b}\longrightarrow0^-.
$$
Thus:
$$
I=2\lim_{b\to\infty}\left[\arctan t\right]_{\sqrt3-2}^{\sqrt{b^2-1}-b}
=-2\arctan(\sqrt3-2).
$$
Since √3 − 2 = −tan(π/12), the result is π/6.


**Final result**

$$
\frac\pi6
$$

</div>

<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6348. -->

Prove convergence:

$$
\int_{0}^{1} \frac{\log(1+\sqrt[4]{x})}{e^{x}-1} \, dx
$$


**Solution.**

Compare with x⁻³ᐟ⁴ at zero. The ratio factors into two fundamental limits:
$$
\lim_{x\to0^+}\frac{\log(1+x^{1/4})/(e^x-1)}{x^{-3/4}}
=\lim_{x\to0^+}\frac{x}{e^x-1}\frac{\log(1+x^{1/4})}{x^{1/4}}=1.
$$
The integrand is continuous away from zero. The comparison integral at zero converges because 3/4 < 1.

**Final result**

$$
\int_0^1\frac{\log(1+\sqrt[4]x)}{e^x-1}\,dx<\infty.
$$

</div>

<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6607. -->

Prove convergence and evaluate the integral:

$$
\int_{3}^{+ \infty} \frac{x+1}{(x-1)^{2}(x-2)} \, dx.
$$


**Solution.**

The integrand is continuous for x ≥ 3. Compute the primitive by Hermite decomposition:
$$
\frac{x+1}{(x-1)^2(x-2)}
=-\frac3{x-1}+\frac3{x-2}-\frac2{(x-1)^2}.
$$
Equivalently, write the last term as the derivative of 2/(x−1). Matching coefficients gives A = −3, B = 3 and C = 2 in the source's notation. Hence:
$$
F(x)=3\log\frac{|x-2|}{|x-1|}+\frac2{x-1}.
$$
Keep the infinite upper endpoint:
$$
I=\lim_{b\to\infty}[F(x)]_3^b
=\lim_{b\to\infty}\left(3\log\frac{b-2}{b-1}+\frac2{b-1}+3\log2-1\right).
$$
The first two terms tend to zero.

**Final result**

$$
\log8-1
$$

</div>


<div class="content-box">

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6647. -->

Solve the following exercise:

$$
\int_{1}^{+\infty} \frac{1}{(x+1)(x+2)x^{2}} \, dx.
$$


**Solution.**

The integrand is continuous and positive on [1,∞) and behaves as x⁻⁴ at infinity, so comparison establishes convergence. Its partial fractions are
$$\frac1{x^2(x+1)(x+2)}=-\frac3{4x}+\frac1{2x^2}+\frac1{x+1}-\frac1{4(x+2)}.$$
An antiderivative is
$$F(x)=-\frac34\log x-\frac1{2x}+\log(x+1)-\frac14\log(x+2).$$
The logarithmic leading terms cancel at infinity, so F(∞)=0. At 1 it is −1/2+log 2−(log 3)/4. Subtract this endpoint value.

**Final result**

$$
\frac12-\log2+\frac14\log3
$$

</div>

<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6375. -->

Solve the following exercise:

$$
\int_{-1}^{1} \frac{1}{(x-4) \sqrt{|x|}} \, dx.
$$


**Solution.**

The only interior singularity is zero and behaves as a constant times |x|⁻¹ᐟ², so both one-sided integrals converge. Put t=√x on (0,1] and t=√(−x) on [−1,0). Each half becomes
$$I_+=2\int_0^1\frac{dt}{t^2-4},\qquad I_-=-2\int_0^1\frac{dt}{t^2+4}.$$
Integrate with partial fractions and the arctangent:
$$I_+=\frac12\left[\log\left|\frac{t-2}{t+2}\right|\right]_0^1=-\frac12\log3,\qquad I_-=-[\arctan(t/2)]_0^1.$$
Add the convergent contributions.

**Final result**

$$
-\frac12\log3-\arctan\frac12
$$

</div>


<div class="content-box">

[**← Back to Integrals**]({{ "/mathematics/calculus/integrals/" | relative_url }})

</div>
