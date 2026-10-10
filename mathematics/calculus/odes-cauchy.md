---
layout: default
date: 2026-10-10
original_date: 2025-08-29
title: "Cauchy Problems: Original Worked Exercises"
permalink: /mathematics/calculus/cauchy-problems/
redirect_from:
  - /university/math/calculus-1/odes-cauchy/
background_image: "/images/grafi.png"
description: "Original initial-value problems of first, second, third and fourth order, with detailed solutions and maximal intervals."
area: mathematics
topic: calculus
subtopic: ordinary-differential-equations
content_type: solved-exercises
level: university
last_modified_at: 2026-10-10
---

# Cauchy Problems: Original Worked Exercises


<div class="content-box">

The theory and selected worked exercises are adapted into English from *Eserciziario 2.1* by Antonino De Martino and Luana Manfredini. Original exercise statements and parameter cases are retained. Mathematical corrections are identified explicitly.

</div>


<div class="content-box">


## Theoretical Recall

A **Cauchy problem**, also called an **initial-value problem**, consists of an ordinary differential equation together with one or more initial conditions.

For a first-order equation:

$$
\begin{cases}
y'(x)=F(x,y),\\
y(x_0)=y_0.
\end{cases}
$$

The differential equation determines a family of possible solutions, while the initial condition selects the solution passing through the prescribed point.

For a second-order linear equation, a Cauchy problem typically has the form:

$$
\begin{cases}
y''+ay'+by=0,\\
y(x_0)=y_0,\\
y'(x_0)=y_1.
\end{cases}
$$

More generally, an ordinary differential equation of order k requires k independent initial conditions to determine a particular solution from the general solution.

### Picard–Lindelöf Theorem

**Theorem (Picard–Lindelöf, simplified).**

If F(x,y) is continuous and satisfies a Lipschitz condition with respect to y in a suitable neighborhood of the initial point, then the Cauchy problem

$$
\begin{cases}
y'(x)=F(x,y),\\
y(x_0)=y_0
\end{cases}
$$

has a **unique local solution**.

**Author’s note:** Solving consists of two steps: find the general solution of the ODE, then use the initial conditions to fix the constants.

</div>


<div class="content-box">

## Exercises

</div>


<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 8172. -->

Solve the following initial-value problem:

$$
\begin{cases}
		y''(x)-y(x)= e^{x}+ \cos x\\
		y(0)=0\\
		y'(0)=1.
	\end{cases}
$$



**Solution.**

The characteristic equation is λ²−1=0, so the complementary solution is c₁eˣ+c₂e⁻ˣ. The exponential forcing is resonant: substitute Axeˣ; its second derivative minus itself is 2Aeˣ, hence A=1/2. For the cosine forcing, B cos x gives −2B cos x, hence B=−1/2.
$$
y=c_1e^x+c_2e^{-x}+\frac{x e^x}{2}-\frac{\cos x}{2}.
$$
The initial data give c₁+c₂=1/2 and c₁−c₂=1/2. Thus c₁=1/2 and c₂=0.

**Final result**

$$
y(x)=\frac{(1+x)e^x-\cos x}{2}
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 8280. -->

Solve the following initial-value problem:

$$
\begin{cases}
		y'(x)= \frac{e^{x}}{y(x)}\\
		y(0)=1
	\end{cases}
$$



**Solution.**

Separate the variables on an interval where y is nonzero:
$$
y\,dy=e^x\,dx,\qquad \frac{y^2}{2}=e^x+C.
$$
At x=0, y=1 gives C=−1/2. The initial value selects the positive square root. The radicand is positive exactly when x>−log 2. At the left endpoint y vanishes and the differential equation is undefined.

**Editorial correction.** The source unnecessarily excludes x=0 from the solution interval, although the initial condition is prescribed there. The interval above includes it.

**Final result**

$$
y(x)=\sqrt{2e^x-1},\qquad x\in(-\log2,+\infty)
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 8337. -->

Solve the following initial-value problem:

$$
\begin{cases}
		y'''(x)-3y'(x)-2y(x)=x^{3}+2\\
		y(0)= \frac{61}{8}\\
		y'(0)=- \frac{27}{4}\\
		y''(0)= \frac{9}{2}
	\end{cases}
$$



**Solution.**

The characteristic polynomial factors as
$$
\lambda^3-3\lambda-2=(\lambda+1)^2(\lambda-2).
$$
Consequently the complementary solution is (c₁+c₂x)e⁻ˣ+c₃e²ˣ. For a cubic particular solution p=Ax³+Bx²+Cx+D, equate coefficients in p‴−3p′−2p=x³+2:
$$
-2A=1,\quad-9A-2B=0,\quad-6B-2C=0,\quad6A-3C-2D=2.
$$
This yields A=−1/2, B=9/4, C=−27/4, D=61/8. Its values p(0), p′(0), p″(0) already equal the three initial data. The complementary constants therefore satisfy
$$
c_1+c_3=0,\quad-c_1+c_2+2c_3=0,\quad c_1-2c_2+4c_3=0,
$$
whose only solution is c₁=c₂=c₃=0.

**Final result**

$$
y(x)=-\frac{x^3}{2}+\frac{9x^2}{4}-\frac{27x}{4}+\frac{61}{8}
$$

</div>

<div class="content-box">

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 8513. -->

Solve the following initial-value problem:

$$
\begin{cases}
		y^{IV}(x)-y(x)=e^{x}( \cos x+ \sin x)\\
		y(0)=0\\
		y'(0)=0\\
		y''(0)=0\\
		y'''(0)=0
	\end{cases}
$$



**Solution.**

The characteristic roots are 1, −1, i, −i. The complementary solution is c₁eˣ+c₂e⁻ˣ+c₃ sin x+c₄ cos x. Substitution of eˣ(A cos x+B sin x) into y⁽⁴⁾−y multiplies this expression by −5, so A=B=−1/5.
$$
y_p=-\frac{e^x(\sin x+\cos x)}5,
\quad y_p'=-\frac{2e^x\cos x}5,
\quad y_p''=\frac{2e^x(\sin x-\cos x)}5,
\quad y_p^{(3)}=\frac{4e^x\sin x}5.
$$
The four zero initial conditions become
$$
\begin{cases}c_1+c_2+c_4=1/5,\\c_1-c_2+c_3=2/5,\\c_1+c_2-c_4=2/5,\\c_1-c_2-c_3=0.\end{cases}
$$
Solving gives c₁=1/4, c₂=1/20, c₃=1/5, c₄=−1/10.

**Final result**

$$
y(x)=\frac{e^x}{4}+\frac{e^{-x}}{20}+\frac{\sin x}{5}-\frac{\cos x}{10}-\frac{e^x(\sin x+\cos x)}5
$$

</div>

<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 8606. -->

Solve the following initial-value problem:

$$
\begin{cases}
		y''(x)+y(x)= \frac{2}{ \sin^{3} x}\\
		y \bigl( \frac{\pi}{2} \bigl)=0\\
		y' \bigl( \frac{\pi}{2} \bigl)=1
	\end{cases}
$$



**Solution.**

Use sin x and cos x as a fundamental pair and vary their coefficients. The equations for their derivatives are
$$
\begin{cases}u'\sin x+v'\cos x=0,\\u'\cos x-v'\sin x=2/\sin^3x.\end{cases}
$$
Thus u′=2 cos x/sin³x and v′=−2/sin²x. Integrating gives u=−1/sin²x and v=2 cot x, so a particular solution is cos(2x)/sin x. The general solution is
$$
y=c_1\sin x+c_2\cos x+\frac{\cos2x}{\sin x}.
$$
At π/2 the particular solution is −1 and its derivative is 0. The initial conditions imply c₁=1 and c₂=−1. Combining sin x with cos(2x)/sin x gives cos²x/sin x. The maximal interval containing π/2 is (0,π), since the forcing is singular at both endpoints.

**Final result**

$$
y(x)=-\cos x+\frac{\cos^2x}{\sin x},\qquad0<x<\pi
$$

</div>


<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
