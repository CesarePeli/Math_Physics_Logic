---
layout: default
date: 2026-08-24
original_date: 2025-08-29
title: "Cauchy Problems for ODEs — Theory and Solved Exercises"
permalink: /mathematics/calculus/cauchy-problems/
redirect_from:
  - /university/math/calculus-1/odes-cauchy/
background_image: "/images/grafi.png"
description: "Solved Cauchy problems for ordinary differential equations, including first- and second-order ODEs, initial conditions, linear equations, and separable equations."
area: mathematics
topic: calculus
subtopic: ordinary-differential-equations
content_type: solved-exercises
level: university
---

<div class="content-box">

# Cauchy Problems for Ordinary Differential Equations

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

---

<div class="content-box">

## Exercises

### Exercise 1

Solve the Cauchy problem:

$$
\begin{cases}
y'=y,\\
y(0)=1.
\end{cases}
$$

**Solution.**

The differential equation is:

$$
y'=y.
$$

Its general solution is:

$$
y(x)=Ce^x.
$$

Apply the initial condition:

$$
y(0)=1.
$$

Therefore:

$$
1=Ce^0.
$$

Since:

$$
e^0=1,
$$

we obtain:

$$
C=1.
$$

**Final Result**

$$
y(x)=e^x
$$

---

### Exercise 2

Solve:

$$
\begin{cases}
y'=-2y,\\
y(0)=3.
\end{cases}
$$

**Solution.**

The general solution of:

$$
y'=-2y
$$

is:

$$
y(x)=Ce^{-2x}.
$$

Using:

$$
y(0)=3,
$$

we obtain:

$$
3=Ce^0.
$$

Hence:

$$
C=3.
$$

**Final Result**

$$
y(x)=3e^{-2x}
$$

---

### Exercise 3

Solve:

$$
\begin{cases}
y'=x,\\
y(0)=0.
\end{cases}
$$

**Solution.**

Integrate both sides:

$$
y' = x.
$$

Therefore:

$$
y(x)=\frac{x^2}{2}+C.
$$

Apply the initial condition:

$$
y(0)=0.
$$

Hence:

$$
0=C.
$$

**Final Result**

$$
y(x)=\frac{x^2}{2}
$$

---

### Exercise 4

Solve:

$$
\begin{cases}
y''-y=0,\\
y(0)=1,\\
y'(0)=0.
\end{cases}
$$

**Solution.**

The characteristic polynomial is:

$$
r^2-1=0.
$$

Factorizing:

$$
(r-1)(r+1)=0.
$$

The roots are:

$$
r_1=1,
$$

and:

$$
r_2=-1.
$$

Therefore the general solution is:

$$
y(x)=C_1e^x+C_2e^{-x}.
$$

Differentiate:

$$
y'(x)
=
C_1e^x-C_2e^{-x}.
$$

Apply:

$$
y(0)=1.
$$

Thus:

$$
C_1+C_2=1.
$$

Now apply:

$$
y'(0)=0.
$$

Hence:

$$
C_1-C_2=0.
$$

Therefore:

$$
C_1=C_2.
$$

Combining the two equations:

$$
2C_1=1.
$$

Thus:

$$
C_1=C_2=\frac12.
$$

Hence:

$$
y(x)
=
\frac12e^x+\frac12e^{-x}.
$$

Using the definition of the hyperbolic cosine:

$$
\cosh x
=
\frac{e^x+e^{-x}}{2}.
$$

**Final Result**

$$
y(x)=\cosh x
$$

---

### Exercise 5

Solve:

$$
\begin{cases}
y''+y=0,\\
y(0)=0,\\
y'(0)=1.
\end{cases}
$$

**Solution.**

The characteristic equation is:

$$
r^2+1=0.
$$

Its roots are:

$$
r=\pm i.
$$

Therefore the general real solution is:

$$
y(x)
=
C_1\cos x
+
C_2\sin x.
$$

Apply:

$$
y(0)=0.
$$

Since:

$$
\cos0=1,
$$

and:

$$
\sin0=0,
$$

we obtain:

$$
C_1=0.
$$

Differentiate:

$$
y'(x)
=
-C_1\sin x
+
C_2\cos x.
$$

Now:

$$
y'(0)=1.
$$

Thus:

$$
C_2=1.
$$

**Final Result**

$$
y(x)=\sin x
$$

---

### Exercise 6

Solve:

$$
\begin{cases}
y'-y=e^x,\\
y(0)=0.
\end{cases}
$$

**Solution.**

This is a linear first-order ODE:

$$
y'-y=e^x.
$$

The integrating factor is:

$$
\mu(x)=e^{-x}.
$$

Multiply the equation by the integrating factor:

$$
e^{-x}y'
-
e^{-x}y
=
1.
$$

The left-hand side is:

$$
\left(
ye^{-x}
\right)'.
$$

Therefore:

$$
\left(
ye^{-x}
\right)'
=
1.
$$

Integrating:

$$
ye^{-x}=x+C.
$$

Multiply by eˣ:

$$
y(x)
=
(x+C)e^x.
$$

Apply:

$$
y(0)=0.
$$

Thus:

$$
0=(0+C)e^0.
$$

Therefore:

$$
C=0.
$$

**Final Result**

$$
y(x)=xe^x
$$

---

### Exercise 7

Solve:

$$
\begin{cases}
y''+4y=0,\\
y(0)=2,\\
y'(0)=0.
\end{cases}
$$

**Solution.**

The characteristic equation is:

$$
r^2+4=0.
$$

Its roots are:

$$
r=\pm2i.
$$

Therefore:

$$
y(x)
=
C_1\cos(2x)
+
C_2\sin(2x).
$$

Apply:

$$
y(0)=2.
$$

Hence:

$$
C_1=2.
$$

Differentiate:

$$
y'(x)
=
-2C_1\sin(2x)
+
2C_2\cos(2x).
$$

Using:

$$
y'(0)=0,
$$

we obtain:

$$
2C_2=0.
$$

Therefore:

$$
C_2=0.
$$

**Final Result**

$$
y(x)=2\cos(2x)
$$

---

### Exercise 8

Solve:

$$
\begin{cases}
y''-3y'+2y=0,\\
y(0)=1,\\
y'(0)=1.
\end{cases}
$$

**Solution.**

The characteristic polynomial is:

$$
r^2-3r+2.
$$

Factorizing:

$$
(r-1)(r-2)=0.
$$

Therefore the roots are:

$$
r_1=1,
$$

and:

$$
r_2=2.
$$

The general solution is:

$$
y(x)
=
C_1e^x
+
C_2e^{2x}.
$$

From:

$$
y(0)=1,
$$

we obtain:

$$
C_1+C_2=1.
$$

Differentiate:

$$
y'(x)
=
C_1e^x
+
2C_2e^{2x}.
$$

Using:

$$
y'(0)=1,
$$

we obtain:

$$
C_1+2C_2=1.
$$

Subtracting:

$$
(C_1+2C_2)
-
(C_1+C_2)
=
0.
$$

Therefore:

$$
C_2=0.
$$

Hence:

$$
C_1=1.
$$

**Final Result**

$$
y(x)=e^x
$$

---

### Exercise 9

Solve:

$$
\begin{cases}
y''+y'=0,\\
y(0)=0,\\
y'(0)=1.
\end{cases}
$$

**Solution.**

The characteristic equation is:

$$
r^2+r=0.
$$

Factorizing:

$$
r(r+1)=0.
$$

Therefore the roots are:

$$
r_1=0,
$$

and:

$$
r_2=-1.
$$

The general solution is:

$$
y(x)
=
C_1+C_2e^{-x}.
$$

Differentiate:

$$
y'(x)
=
-C_2e^{-x}.
$$

Using:

$$
y(0)=0,
$$

we obtain:

$$
C_1+C_2=0.
$$

Using:

$$
y'(0)=1,
$$

we obtain:

$$
-C_2=1.
$$

Therefore:

$$
C_2=-1.
$$

Hence:

$$
C_1=1.
$$

**Final Result**

$$
y(x)=1-e^{-x}
$$

---

### Exercise 10

Solve:

$$
\begin{cases}
y'=y\cos x,\\
y(0)=1.
\end{cases}
$$

**Solution.**

The equation is separable:

$$
y'=y\cos x.
$$

For nonzero y:

$$
\frac{dy}{y}
=
\cos x\,dx.
$$

Integrating:

$$
\log|y|
=
\sin x+C.
$$

Exponentiating:

$$
|y|
=
e^Ce^{\sin x}.
$$

Absorbing the sign and the positive factor into an arbitrary nonzero constant:

$$
y(x)
=
Ce^{\sin x}.
$$

Now apply:

$$
y(0)=1.
$$

Since:

$$
\sin0=0,
$$

we obtain:

$$
1=Ce^0.
$$

Therefore:

$$
C=1.
$$

**Final Result**

$$
y(x)=e^{\sin x}
$$

</div>

---

<div class="content-box">

## Ordinary Differential Equations and Initial Conditions

The examples above illustrate the role of initial conditions in selecting a unique solution from the family produced by a differential equation.

For linear equations, the general solution contains arbitrary constants corresponding to the order of the equation. The initial conditions determine those constants.

For nonlinear equations, existence and uniqueness require additional hypotheses, such as those appearing in the Picard–Lindelöf theorem.

[**Ordinary Differential Equations — Theory and Solved Exercises →**]({{ "/mathematics/calculus/ordinary-differential-equations/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>