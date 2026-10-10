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

# Continuity: Original Piecewise and Discontinuity Exercises


<div class="content-box">

The theory and selected worked exercises are adapted into English from *Eserciziario 2.1* by Antonino De Martino and Luana Manfredini. Original exercise statements and parameter cases are retained. Mathematical corrections are identified explicitly.

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

The source classifies excluded domain points using the language of discontinuities. Strictly, continuity at a point requires that it belong to the domain; at an excluded point we classify the limiting behavior or ask whether the function admits a continuous extension.

</div>

<div class="content-box">

## Original Worked Exercises

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

**Editorial correction.** The source calls the function continuous at π/6 although the statement excludes that point. The original intervals are retained and the missing value is identified as a removable hole.

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

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
