---
layout: default
date: 2026-08-29
original_date: 2025-08-31
title: "Ordinary Differential Equations — Theory and Solved Exercises"
description: "Learn how to find general solutions of ordinary differential equations through theory and 10 solved ODE exercises using trial solutions and variation of parameters."
permalink: /mathematics/calculus/ordinary-differential-equations/
redirect_from:
  - /university/math/calculus-1/odes-general/
background_image: "/images/grafi.png"
featured: true
area: mathematics
topic: calculus
subtopic: ordinary-differential-equations
level: university
content_type: solved-exercises
---

<div class="content-box">

# Ordinary Differential Equations: Theory and Solved Exercises

## ODE Topics and General Solution Methods

This page explains how to find general solutions of ordinary differential equations and includes 10 solved ODE exercises. The methods covered include first-order linear equations, constant-coefficient equations, trial solutions, separable equations, and variation of parameters.

Differential equations are a fundamental tool for modeling real phenomena.

A simple example is **Malthus’ model**: suppose the birth–death rate per unit time is constant.

If a population at time t₀ has size x₀, its growth is modeled by the Cauchy problem

$$
\begin{cases}
y'(t)=a y(t),\\
y(t_0)=x_0.
\end{cases}
$$

with a ∈ ℝ.

The solution is

$$
y(t)=x_0 e^{a(t-t_0)}.
$$

For a = 0.02, this model matches the growth of the human population between 1700 and 1961.

</div>

<div class="content-box">

## How to Solve Linear First-Order ODEs

A linear first-order differential equation has the form

$$
y'(t)+a(t)y(t)=g(t),
$$

with a(t) and g(t) continuous.

The general solution is

$$
y(t)
=
e^{-A(t)}
\left(
c+\int g(t)e^{A(t)}\,dt
\right),
$$

where c ∈ ℝ and

$$
A(t)=\int a(t)\,dt.
$$

For a Cauchy problem

$$
\begin{cases}
y'(t)+a(t)y(t)=g(t),\\
y(t_0)=y_0,
\end{cases}
$$

the solution becomes

$$
y(t)
=
e^{-A(t)}
\left(
y_0+\int_{t_0}^{t}g(s)e^{A(s)}\,ds
\right),
$$

where

$$
A(t)=\int_{t_0}^{t}a(s)\,ds.
$$

</div>

<div class="content-box">

## Linear ODEs of Order k with Constant Coefficients

Consider the homogeneous equation

$$
y^{(k)}(t)
+
a_{k-1}y^{(k-1)}(t)
+
\dots
+
a_1y'(t)
+
a_0y(t)
=
0.
$$

Its characteristic polynomial is

$$
P(\lambda)
=
\lambda^k
+
a_{k-1}\lambda^{k-1}
+
\dots
+
a_1\lambda
+
a_0.
$$

If λⱼ is a real root with multiplicity mⱼ, then the fundamental solutions include

$$
e^{\lambda_j t},
\quad
t e^{\lambda_j t},
\quad
\dots,
\quad
t^{m_j-1}e^{\lambda_j t}.
$$

If

$$
\lambda_j=\sigma+ip
$$

and

$$
\overline{\lambda_j}=\sigma-ip
$$

are complex conjugate roots of multiplicity mⱼ, the real fundamental set includes

$$
e^{\sigma t}\cos(pt),
\quad
t e^{\sigma t}\cos(pt),
\quad
\dots,
\quad
t^{m_j-1}e^{\sigma t}\cos(pt),
$$

and

$$
e^{\sigma t}\sin(pt),
\quad
t e^{\sigma t}\sin(pt),
\quad
\dots,
\quad
t^{m_j-1}e^{\sigma t}\sin(pt).
$$

</div>

<div class="content-box">

## Non-Homogeneous Linear ODEs

Equations of the form

$$
y^{(k)}(t)
+
a_{k-1}y^{(k-1)}(t)
+
\dots
+
a_1y'(t)
+
a_0y(t)
=
g(t)
$$

can be solved by two main methods:

- **method of undetermined coefficients (similarity)**;
- **variation of parameters**.

### Method of Undetermined Coefficients (Trial Solution Method)

#### 1. Polynomial forcing term

If g(t) is a polynomial of degree m:

- If P(0) ≠ 0, try

$$
y_p(t)
=
A_0+A_1t+\dots+A_mt^m.
$$

- If P(0) = 0 with multiplicity h, try

$$
y_p(t)
=
t^h
\left(
A_0+A_1t+\dots+A_mt^m
\right).
$$

#### 2. Polynomial times exponential

If

$$
g(t)=p(t)e^{\lambda t},
$$

with p(t) a polynomial of degree m:

- If P(λ) ≠ 0, try

$$
y_p(t)
=
\left(
A_0+A_1t+\dots+A_mt^m
\right)e^{\lambda t}.
$$

- If P(λ) = 0 with multiplicity h, try

$$
y_p(t)
=
t^h
\left(
A_0+A_1t+\dots+A_mt^m
\right)e^{\lambda t}.
$$

#### 3. Trigonometric forcing term

If

$$
g(t)
=
\alpha\cos(\lambda t)
+
\beta\sin(\lambda t),
$$

then:

- If P(iλ) ≠ 0, try

$$
y_p(t)
=
A\cos(\lambda t)
+
B\sin(\lambda t).
$$

- If P(iλ) = 0 with multiplicity h, try

$$
y_p(t)
=
t^h
\left(
A\cos(\lambda t)
+
B\sin(\lambda t)
\right).
$$

#### 4. Exponential-trigonometric forcing term

If

$$
g(t)
=
e^{\mu t}
\left(
\alpha\cos(\lambda t)
+
\beta\sin(\lambda t)
\right),
$$

then:

- If P(μ + iλ) ≠ 0, try

$$
y_p(t)
=
e^{\mu t}
\left(
A\cos(\lambda t)
+
B\sin(\lambda t)
\right).
$$

- If P(μ + iλ) = 0 with multiplicity h, try

$$
y_p(t)
=
t^h e^{\mu t}
\left(
A\cos(\lambda t)
+
B\sin(\lambda t)
\right).
$$

#### 5. Sum of forcing terms

If

$$
g(t)=g_1(t)+g_2(t),
$$

solve separately for each part and sum the particular solutions.

</div>

<div class="content-box">

## Variation of Parameters

Consider a second-order linear equation

$$
y''(x)
+
a(x)y'(x)
+
b(x)y(x)
=
f(x),
$$

with a, b, and f continuous.

Let y₁ and y₂ be two linearly independent solutions of the corresponding homogeneous equation.

Define z₁ and z₂ so that their derivatives solve

$$
\begin{cases}
z_1'(x)y_1(x)+z_2'(x)y_2(x)=0,\\
z_1'(x)y_1'(x)+z_2'(x)y_2'(x)=f(x).
\end{cases}
$$

Then a particular solution is

$$
y_p(x)
=
z_1(x)y_1(x)
+
z_2(x)y_2(x).
$$

</div>

<div class="content-box">

## ODE Exercises with Solutions

> **Scope note.** This page excludes Cauchy problems, or initial-value problems. Those are treated separately.

<div class="content-box exercise-box" markdown="1">

### Exercise 1

Solve

$$
y'''(x)+3y''(x)=9x.
$$

**Solution**

The characteristic polynomial of the homogeneous equation is

$$
P(\lambda)
=
\lambda^3+3\lambda^2
=
\lambda^2(\lambda+3).
$$

Therefore λ = 0 is a double root and λ = −3 is a simple root.

Hence

$$
y_h
=
c_1+c_2x+c_3e^{-3x}.
$$

The right-hand side is a polynomial of degree 1. Since λ = 0 is a root of multiplicity 2, we try

$$
y_p
=
x^2(Ax+B).
$$

Thus

$$
y_p
=
Ax^3+Bx^2.
$$

Differentiating,

$$
y_p'
=
3Ax^2+2Bx,
$$

$$
y_p''
=
6Ax+2B,
$$

$$
y_p'''
=
6A.
$$

Substituting into the differential equation gives

$$
6A+3(6Ax+2B)=9x.
$$

Therefore

$$
18Ax+6A+6B=9x.
$$

Comparing coefficients,

$$
18A=9,
$$

so

$$
A=\frac12.
$$

Moreover,

$$
6A+6B=0,
$$

hence

$$
B=-\frac12.
$$

Therefore

$$
y_p
=
\frac12x^3-\frac12x^2.
$$

**Final Result**

$$
y(x)
=
c_1+c_2x+c_3e^{-3x}
+\frac12x^3-\frac12x^2.
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 2

Solve

$$
y'''(x)+y(x)=xe^{-x}.
$$

**Solution**

The characteristic polynomial is

$$
P(\lambda)
=
\lambda^3+1.
$$

Factorizing,

$$
P(\lambda)
=
(\lambda+1)(\lambda^2-\lambda+1).
$$

The roots are

$$
\lambda_1=-1,
$$

and

$$
\lambda_{2,3}
=
\frac12
\pm
i\frac{\sqrt3}{2}.
$$

Therefore

$$
y_h
=
c_1e^{-x}
+
c_2e^{x/2}
\cos\left(\frac{\sqrt3}{2}x\right)
+
c_3e^{x/2}
\sin\left(\frac{\sqrt3}{2}x\right).
$$

The forcing term is

$$
xe^{-x}.
$$

Since λ = −1 is a simple root of the characteristic polynomial, resonance occurs. We therefore try

$$
y_p
=
x(Ax+B)e^{-x}.
$$

Substitution into the differential equation gives

$$
A=\frac16,
\qquad
B=\frac13.
$$

Hence

$$
y_p
=
x
\left(
\frac{x}{6}+\frac13
\right)e^{-x}.
$$

**Final Result**

$$
y(x)
=
c_1e^{-x}
+
c_2e^{x/2}
\cos\left(\frac{\sqrt3}{2}x\right)
+
c_3e^{x/2}
\sin\left(\frac{\sqrt3}{2}x\right)
+
x
\left(
\frac{x}{6}+\frac13
\right)e^{-x}.
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 3

Solve

$$
2y''(x)-5y'(x)+3y(x)=\sin(2x).
$$

**Solution**

The characteristic polynomial is

$$
P(\lambda)
=
2\lambda^2-5\lambda+3.
$$

Factorizing,

$$
P(\lambda)
=
(2\lambda-3)(\lambda-1).
$$

The roots are

$$
\lambda_1=1,
\qquad
\lambda_2=\frac32.
$$

Therefore

$$
y_h
=
c_1e^x+c_2e^{3x/2}.
$$

Since there is no resonance with the forcing term, we try

$$
y_p
=
A\cos(2x)+B\sin(2x).
$$

Then

$$
y_p'
=
-2A\sin(2x)+2B\cos(2x),
$$

and

$$
y_p''
=
-4A\cos(2x)-4B\sin(2x).
$$

Substituting,

$$
2y_p''-5y_p'+3y_p
=
\sin(2x).
$$

The coefficient of cos(2x) is

$$
-8A-10B+3A
=
-5A-10B.
$$

The coefficient of sin(2x) is

$$
-8B+10A+3B
=
10A-5B.
$$

Therefore

$$
\begin{cases}
-5A-10B=0,\\
10A-5B=1.
\end{cases}
$$

From the first equation,

$$
A=-2B.
$$

Substituting into the second,

$$
-20B-5B=1.
$$

Thus

$$
B=-\frac{1}{25},
$$

and

$$
A=\frac{2}{25}.
$$

Therefore

$$
y_p
=
\frac{2}{25}\cos(2x)
-
\frac{1}{25}\sin(2x).
$$

**Final Result**

$$
y(x)
=
c_1e^x
+
c_2e^{3x/2}
+
\frac{2}{25}\cos(2x)
-
\frac{1}{25}\sin(2x).
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 4

Solve

$$
y''(x)-2y'(x)+2y(x)
=
e^x+x\cos x.
$$

**Solution**

The characteristic polynomial is

$$
P(\lambda)
=
\lambda^2-2\lambda+2.
$$

Its roots are

$$
\lambda=1\pm i.
$$

Therefore

$$
y_h
=
c_1e^x\cos x
+
c_2e^x\sin x.
$$

We split the forcing term into two parts.

For

$$
g_1(x)=e^x,
$$

we have P(1) ≠ 0, so we try

$$
y_{p1}=Ae^x.
$$

Substitution gives

$$
A=1.
$$

Hence

$$
y_{p1}=e^x.
$$

For

$$
g_2(x)=x\cos x,
$$

there is no resonance, so we try

$$
y_{p2}
=
(Bx+C)\cos x
+
(Dx+E)\sin x.
$$

Substitution and comparison of coefficients give

$$
B=\frac15,
\qquad
C=\frac{2}{25},
$$

$$
D=-\frac25,
\qquad
E=-\frac{14}{25}.
$$

Therefore

$$
y_{p2}
=
\frac15
\left[
\left(x+\frac25\right)\cos x
-
\left(2x+\frac{14}{5}\right)\sin x
\right].
$$

**Final Result**

$$
y(x)
=
c_1e^x\cos x
+
c_2e^x\sin x
+
e^x
+
\frac15
\left[
\left(x+\frac25\right)\cos x
-
\left(2x+\frac{14}{5}\right)\sin x
\right].
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 5

Solve

$$
y'(x)=e^{x+y(x)}.
$$

**Solution**

The equation is separable:

$$
e^{-y}y'=e^x.
$$

Therefore

$$
\int e^{-y}\,dy
=
\int e^x\,dx.
$$

Integrating,

$$
-e^{-y}
=
e^x+C.
$$

Equivalently, writing the arbitrary constant as c,

$$
e^{-y}
=
c-e^x.
$$

Taking the logarithm,

$$
-y
=
\log(c-e^x).
$$

Hence

$$
y(x)
=
-\log(c-e^x).
$$

For a real-valued solution we require

$$
c-e^x>0.
$$

Thus c > 0 and

$$
x<\log c.
$$

**Final Result**

$$
y(x)
=
-\log(c-e^x),
\qquad
c>0,
\qquad
x<\log c.
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 6

Solve

$$
y'''(x)-y''(x)-y'(x)+y(x)=e^x.
$$

**Solution**

The characteristic polynomial is

$$
P(\lambda)
=
\lambda^3-\lambda^2-\lambda+1.
$$

Factorizing,

$$
P(\lambda)
=
(\lambda-1)^2(\lambda+1).
$$

Therefore

$$
y_h
=
c_1e^{-x}
+
c_2e^x
+
c_3xe^x.
$$

The forcing term eˣ corresponds to the root λ = 1, which has multiplicity 2.

Therefore we try

$$
y_p
=
Ax^2e^x.
$$

Substitution gives

$$
4A=1.
$$

Hence

$$
A=\frac14.
$$

Thus

$$
y_p
=
\frac14x^2e^x.
$$

**Final Result**

$$
y(x)
=
c_1e^{-x}
+
c_2e^x
+
c_3xe^x
+
\frac14x^2e^x.
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 7

Solve

$$
y''(x)-2y'(x)+y(x)=\sinh x.
$$

**Solution**

The characteristic polynomial is

$$
P(\lambda)
=
\lambda^2-2\lambda+1
=
(\lambda-1)^2.
$$

Therefore

$$
y_h
=
c_1e^x+c_2xe^x.
$$

We write

$$
\sinh x
=
\frac12
\left(
e^x-e^{-x}
\right).
$$

We solve separately for the two terms.

For

$$
\frac12e^x,
$$

there is resonance of multiplicity 2. Therefore we try

$$
y_{p1}
=
Ax^2e^x.
$$

Substitution gives

$$
A=\frac14.
$$

Thus

$$
y_{p1}
=
\frac14x^2e^x.
$$

For

$$
-\frac12e^{-x},
$$

there is no resonance. We try

$$
y_{p2}
=
Be^{-x}.
$$

Substitution gives

$$
B=-\frac18.
$$

Therefore

$$
y_{p2}
=
-\frac18e^{-x}.
$$

**Final Result**

$$
y(x)
=
c_1e^x
+
c_2xe^x
+
\frac14x^2e^x
-
\frac18e^{-x}.
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 8

Solve

$$
y^{(4)}(x)-y^{(3)}(x)
=
\cos x+\sin(2x).
$$

**Solution**

The characteristic polynomial is

$$
P(\lambda)
=
\lambda^4-\lambda^3
=
\lambda^3(\lambda-1).
$$

Therefore

$$
y_h
=
c_1+c_2x+c_3x^2+c_4e^x.
$$

We split the forcing term.

For cos x, try

$$
y_{p1}
=
A\cos x+B\sin x.
$$

Substitution gives

$$
A=B=\frac12.
$$

Hence

$$
y_{p1}
=
\frac12
\left(
\cos x+\sin x
\right).
$$

For sin(2x), try

$$
y_{p2}
=
C\cos(2x)+D\sin(2x).
$$

Substitution gives

$$
C=-\frac{1}{40},
\qquad
D=\frac{1}{20}.
$$

Hence

$$
y_{p2}
=
-\frac{1}{40}\cos(2x)
+
\frac{1}{20}\sin(2x).
$$

**Final Result**

$$
y(x)
=
c_1+c_2x+c_3x^2+c_4e^x
+
\frac12(\sin x+\cos x)
-
\frac{1}{40}\cos(2x)
+
\frac{1}{20}\sin(2x).
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 9

Solve

$$
y^{(4)}(x)-2y^{(3)}(x)+y''(x)=x.
$$

**Solution**

The characteristic polynomial is

$$
P(\lambda)
=
\lambda^4-2\lambda^3+\lambda^2.
$$

Factorizing,

$$
P(\lambda)
=
\lambda^2(\lambda-1)^2.
$$

Therefore

$$
y_h
=
c_1+c_2x+c_3e^x+c_4xe^x.
$$

Since λ = 0 has multiplicity 2 and the forcing term is a polynomial of degree 1, we try

$$
y_p
=
x^2(Ax+B).
$$

Thus

$$
y_p
=
Ax^3+Bx^2.
$$

Differentiating,

$$
y_p''
=
6Ax+2B,
$$

$$
y_p'''
=
6A,
$$

$$
y_p^{(4)}
=
0.
$$

Substituting,

$$
-12A+6Ax+2B=x.
$$

Comparing the coefficients of x,

$$
6A=1,
$$

so

$$
A=\frac16.
$$

For the constant term,

$$
-12A+2B=0.
$$

Hence

$$
B=1.
$$

Therefore

$$
y_p
=
\frac16x^3+x^2.
$$

**Final Result**

$$
y(x)
=
c_1+c_2x+c_3e^x+c_4xe^x
+
\frac16x^3+x^2.
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 10

Solve

$$
y''(x)+y(x)=\sec x.
$$

**Solution**

The homogeneous equation is

$$
y''+y=0.
$$

A fundamental set of solutions is

$$
y_1=\cos x,
\qquad
y_2=\sin x.
$$

Therefore

$$
y_h
=
c_1\cos x+c_2\sin x.
$$

We use variation of parameters.

The Wronskian is

$$
W
=
\begin{vmatrix}
\cos x & \sin x\\
-\sin x & \cos x
\end{vmatrix}
=
1.
$$

Since

$$
g(x)=\sec x,
$$

a particular solution is

$$
y_p
=
-y_1
\int
\frac{y_2g}{W}\,dx
+
y_2
\int
\frac{y_1g}{W}\,dx.
$$

Thus

$$
y_p
=
-\cos x
\int
\sin x\,\sec x\,dx
+
\sin x
\int
\cos x\,\sec x\,dx.
$$

Since

$$
\sin x\,\sec x
=
\tan x,
$$

and

$$
\cos x\,\sec x
=
1,
$$

we obtain

$$
y_p
=
-\cos x
\int\tan x\,dx
+
\sin x
\int1\,dx.
$$

Now

$$
\int\tan x\,dx
=
-\log|\cos x|.
$$

Therefore

$$
y_p
=
\cos x\log|\cos x|
+
x\sin x.
$$

The equation is defined on intervals where

$$
\cos x\neq0.
$$

**Final Result**

$$
y(x)
=
c_1\cos x
+
c_2\sin x
+
\cos x\log|\cos x|
+
x\sin x,
\qquad
\cos x\neq0.
$$


</div>

</div>

<div class="content-box">

## Explore More Topics in Calculus

- [Fundamental and Notable Limits]({{ "/mathematics/calculus/limits/fundamental-limits-examples/" | relative_url }})
- [Limits with L’Hôpital’s Rule]({{ "/mathematics/calculus/limits/limits-hopital/" | relative_url }})
- [Limits with Taylor Expansions]({{ "/mathematics/calculus/limits/limits-taylor/" | relative_url }})
- [Sequences]({{ "/mathematics/calculus/sequences/" | relative_url }})
- [Series]({{ "/mathematics/calculus/series/" | relative_url }})
- [Continuity]({{ "/mathematics/calculus/continuity/" | relative_url }})
- [Differentiability]({{ "/mathematics/calculus/differentiability/" | relative_url }})
- [Integration by Parts]({{ "/mathematics/calculus/integration-by-parts/" | relative_url }})
- [Integration by Substitution]({{ "/mathematics/calculus/integration-by-substitution/" | relative_url }})
- [Cauchy Problems for Ordinary Differential Equations]({{ "/mathematics/calculus/cauchy-problems/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>