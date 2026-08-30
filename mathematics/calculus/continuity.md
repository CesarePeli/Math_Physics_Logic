---
layout: default
date: 2026-08-24
original_date: 2025-08-29
title: "Solved Exercises — Continuity"
permalink: /mathematics/calculus/continuity/
redirect_from:
  - /university/math/calculus-1/continuity/
background_image: "/images/grafi.png"
description: "Solved exercises on continuity, removable, jump, infinite and oscillatory discontinuities, piecewise functions, domains, and the epsilon-delta definition."
area: mathematics
topic: calculus
subtopic: continuity
level: university
content_type: solved-exercises
---

<div class="content-box">

# Continuity — Theory and Solved Exercises

## Theoretical Recall

A function f is **continuous at x₀** if it is defined at x₀ and:

$$
\lim_{x\to x_0}f(x)=f(x_0).
$$

Equivalently, continuity at x₀ requires:

$$
\lim_{x\to x_0^-}f(x)
=
\lim_{x\to x_0^+}f(x)
=
f(x_0).
$$

### Epsilon–Delta Definition

A function f is continuous at x₀ if, for every ε > 0, there exists δ > 0 such that:

$$
|x-x_0|<\delta
\quad\Longrightarrow\quad
|f(x)-f(x_0)|<\varepsilon.
$$

### Types of Discontinuities

- **Removable discontinuity:** the limit exists and is finite, but f(x₀) is either undefined or different from the limit.
- **Jump discontinuity:** the left-hand and right-hand limits exist and are finite, but they are different.
- **Infinite discontinuity:** at least one of the one-sided limits is +∞ or −∞.
- **Oscillatory discontinuity:** the limit does not exist because the function oscillates indefinitely near the point.

### Basic Continuity Properties

Polynomials are continuous on ℝ.

Rational functions are continuous wherever their denominators are nonzero.

The functions sin x, cos x and eˣ are continuous on ℝ.

The logarithmic function log x is continuous on its domain:

$$
(0,+\infty).
$$

If f and g are continuous at x₀, then their sum, difference and product are continuous at x₀.

If additionally g(x₀) ≠ 0, their quotient is also continuous at x₀.

Compositions of continuous functions are continuous wherever the composition is defined.

</div>


<div class="content-box">

## Exercises

</div>

<div class="content-box">

### Exercise 1 — Removable Discontinuity

Consider:

$$
f(x)=\frac{x^2-1}{x-1},
\qquad x\ne1,
$$

with:

$$
f(1)=c.
$$

Determine c so that f is continuous at x = 1.

**Solution.**

For x ≠ 1, factor the numerator:

$$
x^2-1=(x-1)(x+1).
$$

Therefore:

$$
f(x)=x+1.
$$

Hence:

$$
\lim_{x\to1}f(x)
=
\lim_{x\to1}(x+1)
=
2.
$$

For continuity we require:

$$
f(1)
=
\lim_{x\to1}f(x).
$$

Since f(1) = c:

$$
c=2.
$$

**Final Result**

$$
c=2
$$


</div>

<div class="content-box">

### Exercise 2 — Jump Discontinuity

Classify the discontinuity of sgn(x) at x = 0.

**Solution.**

The left-hand limit is:

$$
\lim_{x\to0^-}\operatorname{sgn}(x)=-1.
$$

The right-hand limit is:

$$
\lim_{x\to0^+}\operatorname{sgn}(x)=1.
$$

Since the two one-sided limits are finite but different:

$$
-1\ne1.
$$

Therefore the two-sided limit does not exist and the function has a jump discontinuity.

**Final Result**

$$
\text{Jump discontinuity at }x=0
$$


</div>

<div class="content-box">

### Exercise 3 — Infinite Discontinuity

Study:

$$
f(x)=\frac1x
$$

at x = 0.

**Solution.**

Consider the one-sided limits:

$$
\lim_{x\to0^+}\frac1x=+\infty,
$$

while:

$$
\lim_{x\to0^-}\frac1x=-\infty.
$$

Thus the function has an infinite discontinuity at x = 0.

The vertical line x = 0 is also a vertical asymptote.

**Final Result**

$$
\text{Infinite discontinuity at }x=0
$$


</div>

<div class="content-box">

### Exercise 4 — Extending a Function Continuously

Consider:

$$
f(x)=\frac{\sin x}{x},
\qquad x\ne0,
$$

with:

$$
f(0)=1.
$$

Study the continuity of f at x = 0.

**Solution.**

The fundamental trigonometric limit gives:

$$
\lim_{x\to0}\frac{\sin x}{x}=1.
$$

By definition:

$$
f(0)=1.
$$

Therefore:

$$
\lim_{x\to0}f(x)=f(0).
$$

Hence f is continuous at x = 0.

For x ≠ 0, the quotient is continuous because both sin x and x are continuous and the denominator is nonzero.

Therefore f is continuous on all of ℝ.

**Final Result**

$$
f\text{ is continuous on }\mathbb{R}
$$


</div>

<div class="content-box">

### Exercise 5 — Continuity by the Squeeze Theorem

Consider:

$$
f(x)=|x|\sin\left(\frac1x\right),
\qquad x\ne0,
$$

with:

$$
f(0)=0.
$$

Study continuity at x = 0.

**Solution.**

Since:

$$
-1\le
\sin\left(\frac1x\right)
\le1,
$$

we obtain:

$$
\left|
|x|\sin\left(\frac1x\right)
\right|
\le|x|.
$$

As x → 0:

$$
|x|\to0.
$$

Therefore, by the Squeeze Theorem:

$$
\lim_{x\to0}
|x|\sin\left(\frac1x\right)
=
0.
$$

Since:

$$
f(0)=0,
$$

we have:

$$
\lim_{x\to0}f(x)=f(0).
$$

**Final Result**

$$
f\text{ is continuous at }x=0
$$


</div>

<div class="content-box">

### Exercise 6 — Continuity of a Piecewise Function

Consider:

$$
f(x)=
\begin{cases}
ax+b, & x<2,\\
x^2, & x\ge2.
\end{cases}
$$

Determine a and b so that f is continuous at x = 2.

**Solution.**

The left-hand limit is:

$$
\lim_{x\to2^-}f(x)=2a+b.
$$

Since the second branch applies at x = 2:

$$
f(2)=2^2=4.
$$

The right-hand limit is:

$$
\lim_{x\to2^+}f(x)=4.
$$

Continuity requires:

$$
2a+b=4.
$$

Thus there are infinitely many pairs (a,b) satisfying the condition.

Equivalently:

$$
b=4-2a.
$$

**Final Result**

$$
2a+b=4
$$


</div>

<div class="content-box">

### Exercise 7 — Continuity and Domain

Study the continuity of:

$$
f(x)=\log(x^2-4).
$$

**Solution.**

The logarithm requires a strictly positive argument:

$$
x^2-4>0.
$$

Factorizing:

$$
(x-2)(x+2)>0.
$$

Therefore:

$$
x<-2
$$

or:

$$
x>2.
$$

Hence the domain is:

$$
(-\infty,-2)\cup(2,+\infty).
$$

The polynomial x² − 4 is continuous on ℝ, and the logarithm is continuous for positive arguments.

Therefore their composition is continuous throughout its domain.

**Final Result**

$$
f\text{ is continuous on }
(-\infty,-2)\cup(2,+\infty)
$$


</div>

<div class="content-box">

### Exercise 8 — Oscillatory Discontinuity

Consider:

$$
f(x)=
\begin{cases}
\sin\left(\frac1x\right), & x\ne0,\\
0, & x=0.
\end{cases}
$$

Check continuity at x = 0.

**Solution.**

As x approaches zero, 1/x becomes arbitrarily large in absolute value and:

$$
\sin\left(\frac1x\right)
$$

oscillates between −1 and 1.

For example, consider the sequences:

$$
x_n=
\frac{1}{\frac{\pi}{2}+2\pi n}.
$$

Then:

$$
x_n\to0
$$

and:

$$
\sin\left(\frac1{x_n}\right)=1.
$$

Now consider:

$$
y_n=
\frac{1}{\frac{3\pi}{2}+2\pi n}.
$$

Then:

$$
y_n\to0
$$

and:

$$
\sin\left(\frac1{y_n}\right)=-1.
$$

The function therefore approaches different values along two sequences converging to zero.

Hence:

$$
\lim_{x\to0}\sin\left(\frac1x\right)
$$

does not exist.

Thus f is not continuous at zero.

**Final Result**

$$
\text{Oscillatory discontinuity at }x=0
$$


</div>

<div class="content-box">

### Exercise 9 — Piecewise Jump Discontinuity

Consider:

$$
f(x)=
\begin{cases}
x^2, & x\le0,\\
1, & x>0.
\end{cases}
$$

Check continuity at x = 0.

**Solution.**

The left-hand limit is:

$$
\lim_{x\to0^-}x^2=0.
$$

The right-hand limit is:

$$
\lim_{x\to0^+}1=1.
$$

Thus:

$$
\lim_{x\to0^-}f(x)
\ne
\lim_{x\to0^+}f(x).
$$

The two-sided limit does not exist.

Moreover:

$$
f(0)=0.
$$

The value at zero agrees with the left-hand limit, but this does not restore continuity because the right-hand limit is different.

**Final Result**

$$
\text{Jump discontinuity at }x=0
$$


</div>

<div class="content-box">

### Exercise 10 — Parameters in a Piecewise Function

Consider:

$$
f(x)=
\begin{cases}
\cos x, & x<0,\\
a+bx, & x\ge0.
\end{cases}
$$

Determine a and b so that f is continuous at x = 0.

**Solution.**

The left-hand limit is:

$$
\lim_{x\to0^-}\cos x=1.
$$

For the second branch:

$$
f(0)=a.
$$

The right-hand limit is:

$$
\lim_{x\to0^+}(a+bx)=a.
$$

Continuity therefore requires:

$$
a=1.
$$

The term bx tends to zero independently of the value of b, so continuity imposes no restriction on b.

Thus:

$$
b\in\mathbb{R}.
$$

**Final Result**

$$
a=1,
\qquad
b\in\mathbb{R}
$$


</div>


<div class="content-box">

## Explore More Topics in Calculus

- [Limits]({{ "/mathematics/calculus/limits/" | relative_url }})
- [Sequences]({{ "/mathematics/calculus/sequences/" | relative_url }})
- [Series]({{ "/mathematics/calculus/series/" | relative_url }})
- [Differentiability]({{ "/mathematics/calculus/differentiability/" | relative_url }})
- [Integration by Parts]({{ "/mathematics/calculus/integration-by-parts/" | relative_url }})
- [Integration by Substitution]({{ "/mathematics/calculus/integration-by-substitution/" | relative_url }})
- [Ordinary Differential Equations]({{ "/mathematics/calculus/odes-general/" | relative_url }})
- [Cauchy Problems]({{ "/mathematics/calculus/odes-cauchy/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>
