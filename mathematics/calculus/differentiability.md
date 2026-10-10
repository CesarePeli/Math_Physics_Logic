---
layout: default
last_modified_at: 2026-10-10
date: 2026-10-10
original_date: 2025-08-29
title: "Differentiability: Original Exercises and Parameter Cases"
permalink: /mathematics/calculus/differentiability/
redirect_from:
  - /university/math/calculus-1/differentiability/
background_image: "/images/grafi.png"
description: "Original university exercises on difference quotients, piecewise functions, parameters and Ck regularity, preserving the exercise-book difficulty."
area: mathematics
topic: calculus
subtopic: differentiability
level: university
content_type: solved-exercises
---


<div class="content-box">

**Exercise editors and source:** **Antonino De Martino and Luana Manfredini**, *Eserciziario 2.1*. The original exercises and source theory are presented here in English for Logic & Motion.

</div>

# Differentiability: Original Exercises and Parameter Cases


<div class="content-box">

## Difference Quotients and Differentiability

Let f map an open interval (a,b) to ℝ and let x₀ belong to that interval. The difference quotient at x₀ is the function:

$$
\theta:(a,b)\setminus\{x_0\}\longrightarrow\mathbb R,
\qquad \theta(x)=\frac{f(x)-f(x_0)}{x-x_0}.
$$

The function f is differentiable at x₀ if this quotient has a finite limit:

$$
f'(x_0)=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}\in\mathbb R.
$$

Differentiability implies continuity. Before studying a derivative at a joining point, check continuity there.

### Corners

For a continuous function, a corner occurs when the one-sided difference quotients tend to two distinct finite numbers:

$$
f'_-(x_0)=c_1\in\mathbb R,\qquad f'_+(x_0)=c_2\in\mathbb R,
\qquad c_1\ne c_2.
$$

### Cusps: Both Sign Configurations

The one-sided difference quotients are infinite with opposite signs:

$$
f'_-(x_0)=-\infty,\qquad f'_+(x_0)=+\infty,
$$

or:

$$
f'_-(x_0)=+\infty,\qquad f'_+(x_0)=-\infty.
$$

### Vertical Tangents: Both Sign Configurations

The one-sided difference quotients may instead be infinite with the same sign:

$$
f'_-(x_0)=f'_+(x_0)=+\infty,
$$

or:

$$
f'_-(x_0)=f'_+(x_0)=-\infty.
$$

The source calls this case an inflection point with a vertical tangent. A vertical tangent follows from these limits; an inflection additionally requires a change of concavity and must be checked separately.

### Piecewise Functions and Higher Regularity

At a joining point, calculate the one-sided difference quotients using the actual assigned function value. The class Cᵏ requires existence and continuity of all derivatives through order k; matching only the function values establishes C⁰, not higher regularity.

</div>

<div class="content-box">

## Original Worked Exercises

</div>

<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4683. -->

Study continuity and differentiability, including all parameter cases:

$$
f(x)=
	\begin{cases}
		\frac{\log(1+x^{3})-x^{3}}{\sqrt{x}} \qquad x >0 \\
		x^{3}+2x^{4} \qquad x \leq 0.
	\end{cases}
$$


**Solution.**

Away from zero both branches are smooth. On the left:
$$
\lim_{x\to0^-}(x^3+2x^4)=0.
$$
On the right use the logarithm expansion:
$$
\log(1+x^3)=x^3-\frac{x^6}{2}+o(x^6).
$$
$$
\frac{\log(1+x^3)-x^3}{\sqrt x}
=x^{11/2}\left(-\frac12+\frac{o(x^6)}{x^6}\right)\longrightarrow0.
$$
Thus f is continuous at zero. For differentiability:
$$
\lim_{x\to0^-}\frac{x^3+2x^4}x=0.
$$
Reuse the previous expansion on the right:
$$
\frac{\log(1+x^3)-x^3}{x\sqrt x}
=x^{9/2}\left(-\frac12+\frac{o(x^6)}{x^6}\right)\longrightarrow0.
$$

**Final result**

$$
f\text{ is continuous and differentiable on }\mathbb R;\quad f'(0)=0.
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4705. -->

Study continuity and differentiability, including all parameter cases:

$$
f(x)=
	\begin{cases}
		x^{2}+x \qquad x \geq 0\\
		\frac{\cos x -\cos 3x}{x} \qquad x<0
	\end{cases}
$$


**Solution.**

Away from zero the branches are smooth. At zero the right-hand limit is zero. For the left-hand limit:
$$
\cos x-\cos3x
=1-\frac{x^2}{2}+o(x^2)-1+\frac92x^2+o(x^2)
=4x^2+o(x^2).
$$
$$
\lim_{x\to0^-}\frac{\cos x-\cos3x}x=0=f(0).
$$
The function is continuous. The derivative limits are:
$$
f'_+(0)=\lim_{x\to0^+}\frac{x^2+x}x=1.
$$
$$
f'_-(0)=\lim_{x\to0^-}\frac{\cos x-\cos3x}{x^2}=4.
$$
The source concludes that zero is a corner.

**Final result**

$$
f\in C^0(\mathbb R),\qquad f\text{ is not differentiable at }0.
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4773. -->

Study continuity and differentiability, including all parameter cases:

$$
f(x)=
	\begin{cases}
		x^{x \log x} \qquad x>0,\\
		1 \qquad x \leq 0
	\end{cases}
$$


**Solution.**

The function is continuous and differentiable away from zero. Rewrite the positive branch:
$$
x^{x\log x}=e^{x(\log x)^2}.
$$
$$
\lim_{x\to0^+}x(\log x)^2=0,
\qquad\lim_{x\to0^+}x^{x\log x}=1=f(0).
$$
The left branch is constantly one, so f is continuous. The left derivative is zero. On the right:
$$
\frac{x^{x\log x}-1}x
=\frac{e^{x(\log x)^2}-1}{x(\log x)^2}(\log x)^2.
$$
The first factor tends to one and the second to +∞:
$$
f'_-(0)=0,\qquad f'_+(0)=+\infty.
$$

**Final result**

$$
f\in C^0(\mathbb R),\qquad f\text{ is not differentiable at }0.
$$

</div>

<div class="content-box">

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4792. -->

Study continuity and differentiability, including all parameter cases:

$$
f(x)=
	\begin{cases}
		e^{x-1}+a \qquad x <1\\
		bx^{2}+1 \qquad x \geq 1.
	\end{cases}
$$


**Solution.**

The only joining point is one. The branch limits are:
$$
\lim_{x\to1^-}(e^{x-1}+a)=1+a,
\qquad\lim_{x\to1^+}(bx^2+1)=1+b=f(1).
$$
Thus continuity holds exactly when a = b. If a ≠ b, differentiability is impossible. Assuming a = b:
$$
f'_-(1)=\lim_{x\to1^-}\frac{e^{x-1}-1}{x-1}=1.
$$
$$
f'_+(1)=\lim_{x\to1^+}\frac{a(x^2-1)}{x-1}
=\lim_{x\to1^+}a(x+1)=2a.
$$
These agree exactly for a = b = 1/2. With a = b ≠ 1/2 the function is continuous but has a corner.

**Final result**

$$
\text{Continuous iff }a=b;\qquad\text{differentiable iff }a=b=\frac12.
$$

</div>

<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4821. -->

Find the greatest integer k ≥ 0 for which f belongs to Cᵏ(ℝ), as the real parameters vary:

$$
f(x)=
	\begin{cases}
		e^{x^{2} \sin 2x} \qquad x>0\\
		1 \qquad x=0\\
		x^{2}+a \qquad x <0\\
	\end{cases}
$$


**Solution.**

The branches are C∞ away from zero. Their limits at zero are a on the left and one on the right, while f(0) = 1. If a ≠ 1 the function is not even C⁰. Assume a = 1. The difference quotients satisfy:
$$
\lim_{x\to0^-}\frac{x^2+1-1}{x}=0.
$$
$$
\lim_{x\to0^+}\frac{e^{x^2\sin2x}-1}x
=\lim_{x\to0^+}\frac{e^{x^2\sin2x}-1}{x^2\sin2x}\,x\sin2x=0.
$$
Hence f′(0) = 0. The complete derivative is:
$$
f'(x)=\begin{cases}
(2x\sin2x+2x^2\cos2x)e^{x^2\sin2x},&x>0,\\
0,&x=0,\\2x,&x<0.
\end{cases}
$$
Both one-sided limits of f′ are zero, so f belongs to C¹. For the second derivative at zero:
$$
\lim_{x\to0^+}\frac{f'(x)-f'(0)}x
=\lim_{x\to0^+}(2\sin2x+2x\cos2x)e^{x^2\sin2x}=0.
$$
$$
\lim_{x\to0^-}\frac{f'(x)-f'(0)}x=\lim_{x\to0^-}\frac{2x}x=2.
$$
The second derivative does not exist.

**Final result**

$$
\begin{cases}\text{No }k\ge0,&a\ne1,\\ k_{\max}=1,&a=1.\end{cases}
$$

</div>

<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4932. -->

Study continuity and differentiability, including all parameter cases:

$$
f(x)=
	\begin{cases}
		\frac{1}{1-x} \qquad x \leq 0\\
		x e^{a x}+b \qquad x>0
	\end{cases}
$$


**Solution.**

The branches are smooth away from zero. Continuity at zero requires:
$$
\lim_{x\to0^-}\frac1{1-x}=1,
\qquad\lim_{x\to0^+}(xe^{ax}+b)=b.
$$
Thus b = 1. With this value, the one-sided difference quotients are:
$$
f'_-(0)=\lim_{x\to0^-}\frac{1/(1-x)-1}x
=\lim_{x\to0^-}\frac1{1-x}=1.
$$
$$
f'_+(0)=\lim_{x\to0^+}\frac{xe^{ax}+1-1}x
=\lim_{x\to0^+}e^{ax}=1.
$$
No restriction on a is necessary.

**Final result**

$$
b=1,\qquad a\in\mathbb R.
$$

</div>

<div class="content-box">

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4973. -->

Find the greatest integer k ≥ 0 for which f belongs to Cᵏ(ℝ), as the real parameters vary:

$$
f(x)=
	\begin{cases}
		\log(1+x) \qquad x>0\\
		0 \qquad x=0\\
		ax^{2}+bx+c \qquad x<0
	\end{cases}
$$


**Solution.**

The branches are smooth away from zero. Their limits agree with f(0) = 0 exactly when c = 0. Under that condition:
$$
f'_+(0)=\lim_{x\to0^+}\frac{\log(1+x)}x=1,
\qquad f'_-(0)=\lim_{x\to0^-}(ax+b)=b.
$$
Thus if b ≠ 1 the largest regularity order is zero. If b = 1, f′(0) = 1 and:
$$
f'(x)=\begin{cases}1/(1+x),&x>0,\\1,&x=0,\\2ax+1,&x<0.\end{cases}
$$
Both limits of f′ are one, so f is C¹. The next one-sided derivatives are:
$$
f''_+(0)=-1,\qquad f''_-(0)=2a.
$$
They agree if a = −1/2. In this case f″ is continuous at zero, but the third derivatives are two on the right and zero on the left.


**Final result**

$$
k_{\max}=\begin{cases}\text{none},&c\ne0,\\0,&c=0,\ b\ne1,\\1,&c=0,\ b=1,\ a\ne-1/2,\\2,&c=0,\ b=1,\ a=-1/2.\end{cases}
$$

</div>


<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4736. -->

Determine whether the function is differentiable at x=1:

$$
f(x)=\sqrt{x^{4}-(x^{2}+x|x|)+\frac{x}{|x|}},
$$


**Solution.**

On the positive half-axis, |x|=x and x/|x|=1, so the radicand becomes x⁴−2x²+1=(x²−1)². Consequently f(x)=|x²−1| near 1 and f(1)=0. The one-sided difference quotients are
$$\lim_{x\to1^-}\frac{1-x^2}{x-1}=\lim_{x\to1^-}-(x+1)=-2,$$
$$\lim_{x\to1^+}\frac{x^2-1}{x-1}=\lim_{x\to1^+}(x+1)=2.$$
They differ, so the function is continuous but has a corner at 1. On the negative half-axis the radicand is x⁴−1, requiring x≤−1. Zero is excluded by x/|x|.

**Final result**

$$
D=(-\infty,-1]\cup(0,\infty);\quad f\text{ is not differentiable at }1
$$

</div>
<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
