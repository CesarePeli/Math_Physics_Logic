---
layout: default
last_modified_at: 2026-10-10
date: 2026-10-10
original_date: 2025-08-29
title: "Continuity: Original Piecewise and Discontinuity Exercises"
permalink: /mathematics/calculus/continuity/
redirect_from:
  - /university/math/calculus-1/continuity/
background_image: "/images/grafi.png"
description: "Original university exercises on continuity, removable holes, jumps, infinite discontinuities and domains, with full solutions."
area: mathematics
topic: calculus
subtopic: continuity
level: university
content_type: solved-exercises
---


<div class="content-box">

# Continuity: Original Piecewise and Discontinuity Exercises

*Exercise editors and source: Prof. Antonino De Martino and Dr. Luana Manfredini, Eserciziario 2.1. The original exercises and source theory are presented here in English for Logic & Motion.*

</div>


<div class="content-box">

## Continuity and Discontinuities

The familiar picture of continuity is drawing a graph without lifting the pencil. The mathematical definition is more precise. At a point x₀ belonging to the domain and accumulating the domain, f is continuous if:

$$
\lim_{x\to x_0}f(x)=f(x_0).
$$

### First-Kind or Jump Discontinuity

Both one-sided limits exist and are finite, but they differ:

$$
\lim_{x\to x_0^-}f(x)\ne\lim_{x\to x_0^+}f(x).
$$

### Second-Kind Discontinuity

At least one one-sided limit is infinite or does not exist. Infinite and oscillatory behavior are both included.

### Removable Discontinuity

The one-sided limits agree, but their common value differs from the assigned value of the function. If no value is assigned, the same finite limit identifies a removable hole and the value needed for a continuous extension.

$$
\lim_{x\to x_0^-}f(x)=\lim_{x\to x_0^+}f(x)=L\ne f(x_0).
$$

Continuity at a point requires that it belong to the domain. At an excluded point, we classify the limiting behavior or ask whether the function admits a continuous extension.

</div>

<div class="content-box">

## Worked Exercises

</div>

<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4879. -->

Study continuity and classify every exceptional point:

$$
f(x)=
	\begin{cases}
		\frac{2}{3}-x \qquad x<0\\
		0 \qquad x=0\\
		\frac{\sin 2x}{\sin 3x} \qquad 0<x<\frac{\pi}{6}\\
		\cos x \qquad \frac{\pi}{6}< x \leq \frac{\pi}{2}\\
		1 \qquad x> \frac{\pi}{2}
	\end{cases}
$$


**Solution.**

Each branch is continuous away from the joining points. The possible exceptional points are:
$$
A=\left\{0,\frac\pi6,\frac\pi2\right\}.
$$
At zero:
$$
\lim_{x\to0^-}\left(\frac23-x\right)=\frac23.
$$
$$
\lim_{x\to0^+}\frac{\sin2x}{\sin3x}
=\lim_{x\to0^+}\frac{2x}{3x}\frac{\sin2x/(2x)}{\sin3x/(3x)}=\frac23.
$$
Since f(0) = 0, this is removable. At π/6:
$$
\lim_{x\to(\pi/6)^-}\frac{\sin2x}{\sin3x}=\frac{\sqrt3}{2}.
$$
$$
\lim_{x\to(\pi/6)^+}\cos x=\frac{\sqrt3}{2}.
$$
The statement assigns no value at π/6. Thus this point is a removable hole; assigning √3/2 makes the extension continuous. At π/2:
$$
\lim_{x\to(\pi/2)^-}\cos x=0,\qquad
\lim_{x\to(\pi/2)^+}1=1.
$$
This is a jump.


**Final result**

$$
0,\ \pi/6:\ \text{removable};\qquad\pi/2:\ \text{jump}.
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4910. -->

Study continuity and classify every exceptional point:

$$
f(x)=
	\begin{cases}
		\frac{1}{\sqrt{|x|}}-\sqrt{1-\frac{1}{x}} \qquad x<0\\
		1 \qquad x=0\\
		\frac{\sin x \log(1+x)}{x^{2}} \qquad x>0
	\end{cases}
$$


**Solution.**

The function is continuous away from zero. From the right, use the fundamental limits:
$$
\lim_{x\to0^+}\frac{\sin x\log(1+x)}{x^2}
=\lim_{x\to0^+}\frac{\sin x}{x}\frac{\log(1+x)}x=1.
$$
From the left the original difference has the indeterminate form ∞ − ∞. Rewrite it as:
$$
\frac1{\sqrt{-x}}-\sqrt{1-\frac1x}
=\frac{1-\sqrt{1-x}}{\sqrt{-x}}.
$$
L'Hôpital's rule gives:
$$
\lim_{x\to0^-}\frac{1-\sqrt{1-x}}{\sqrt{-x}}
=\lim_{x\to0^-}\frac{1/(2\sqrt{1-x})}{-1/(2\sqrt{-x})}
=-\lim_{x\to0^-}\sqrt{\frac{-x}{1-x}}=0.
$$
The finite one-sided limits differ.

**Final result**

$$
\text{Jump at }x=0:\quad f(0^-)=0,\quad f(0^+)=1.
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5010. -->

Study continuity and classify every exceptional point:

$$
f(x)=\frac{1}{2-e^{\frac{1}{x}}}.
$$


**Solution.**

The domain excludes zero and the zero of the denominator:
$$
D=\mathbb R\setminus\left\{0,\frac1{\log2}\right\}.
$$
At zero:
$$
\lim_{x\to0^-}\frac1{2-e^{1/x}}=\frac12,
\qquad\lim_{x\to0^+}\frac1{2-e^{1/x}}=0.
$$
This is jump-type limiting behavior. Put c = 1/log 2. When x approaches c from the left, e¹ᐟˣ > 2; from the right it is less than 2. Therefore:
$$
\lim_{x\to c^-}f(x)=-\infty,\qquad
\lim_{x\to c^+}f(x)=+\infty.
$$
The second excluded point is an infinite discontinuity.

**Final result**

$$
0:\ \text{jump};\qquad 1/\log2:\ \text{infinite}.
$$

</div>

<div class="content-box">

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5060. -->

Study continuity and classify every exceptional point:

$$
f(x)= \frac{\log(x^{2})-1}{\log(x^{2})+1}.
$$


**Solution.**

The logarithm requires x ≠ 0. The denominator vanishes when log(x²) = −1:
$$
D=\mathbb R\setminus\left\{0,-\frac1{\sqrt e},\frac1{\sqrt e}\right\}.
$$
At zero divide numerator and denominator by log(x²):
$$
\lim_{x\to0}\frac{\log(x^2)-1}{\log(x^2)+1}
=\lim_{x\to0}\frac{1-1/\log(x^2)}{1+1/\log(x^2)}=1.
$$
Zero is a removable hole. At the positive excluded point:
$$
\lim_{x\to(1/\sqrt e)^-}f(x)=+\infty,
\qquad\lim_{x\to(1/\sqrt e)^+}f(x)=-\infty.
$$
The function is even, so the negative excluded point is also an infinite discontinuity, with the one-sided signs reversed.

**Final result**

$$
0:\ \text{removable};\qquad\pm1/\sqrt e:\ \text{infinite}.
$$

</div>


<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4859. -->

Solve the following exercise:

$$
f(x)=
	\begin{cases}
		\frac{\log x}{x-1} \qquad x \neq 1\\
		1 \qquad x=1
	\end{cases}
$$


**Solution.**

The logarithm requires x>0; x=1 is assigned separately. Away from 1, continuity follows from composition and division. At 1 the notable logarithm limit gives
$$\lim_{x\to1}\frac{\log x}{x-1}=1=f(1).$$
For completeness, set h=x−1 and expand the original difference quotient:
$$\frac{f(1+h)-f(1)}h=\frac{\log(1+h)-h}{h^2}\longrightarrow-\frac12.$$
Thus the assigned value removes the apparent singularity and the function is differentiable there.

**Final result**

$$
D=(0,\infty),\quad f\text{ continuous on }D,\quad f'(1)=-\frac12
$$

</div>

<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 4952. -->

Determine the real parameters for continuity and differentiability at zero:

$$
f(x)=
	\begin{cases}
		a \sin 2x -4 \qquad x<0\\
		b(x-1)+e^{x} \qquad x \geq 0
	\end{cases}
$$


**Solution.**

The left limit at zero is −4; the assigned right-hand value is 1−b. Continuity requires −4=1−b, so b=5. Under this condition, the one-sided difference quotients are
$$f'_-(0)=\lim_{x\to0^-}\frac{a\sin2x}{x}=2a,\qquad f'_+(0)=b+1=6.$$
They agree if a=3. When b=5 but a≠3 the function remains continuous and has a corner; when b≠5 it is discontinuous.

**Final result**

$$
\text{Continuous iff }b=5;\quad\text{differentiable iff }(a,b)=(3,5)
$$

</div>

<div class="content-box">

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5031. -->

Determine the domain and classify discontinuities:

$$
f(x)=
	\begin{cases}
		\frac{\sqrt{2-\sqrt{x+1}}}{1-x}+2^{-\frac{1}{x^{2}}} \qquad x \neq 0\\
		1 \qquad x=0
	\end{cases}
$$


**Solution.**

The nested square roots require x+1≥0 and √(x+1)≤2; thus −1≤x≤3. The denominator excludes x=1; x=0 is defined by its separate branch. Therefore
$$D=[-1,1)\cup(1,3].$$
As x→0, the radical quotient tends to 1 and 2⁻¹⁄ˣ² tends to 0, giving f(0)=1. At x=1 the numerator tends to √(2−√2)>0, so the limits are +∞ from the left and −∞ from the right. Elsewhere the function is continuous, including relative continuity at the endpoints −1 and 3.


**Final result**

$$
f\text{ is continuous on }D;\quad x=1\text{ is an infinite singularity}
$$

</div>

<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5088. -->

Find all real parameter cases for continuity and differentiability:

$$
f(x)=
		\begin{cases}
			(1-x^{2}) \log(1-x) \qquad x<1 \\
			(2x+b)(ax-1) \qquad x \geq 1.
		\end{cases}
$$


**Solution.**

As x→1 from the left, (1−x²)log(1−x)=(1+x)(1−x)log(1−x) tends to zero. From the right, and at the assigned value, the limit is (2+b)(a−1). Hence continuity requires a=1 or b=−2. Under either continuity condition, f(1)=0 and the left difference quotient is
$$\frac{(1-x^2)\log(1-x)}{x-1}=-(1+x)\log(1-x)\longrightarrow+\infty.$$
The right branch is a polynomial and has finite derivative 4a+ab−2 at 1. The one-sided values therefore cannot agree as finite derivatives for any parameters.

**Final result**

$$
\text{Continuous iff }a=1\text{ or }b=-2;\quad\text{never differentiable at }1
$$

</div>
<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
