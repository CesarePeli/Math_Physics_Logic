---
layout: default
date: 2026-08-24
original_date: 2025-08-29
title: "Solved Exercises — Differentiability"
permalink: /mathematics/calculus/differentiability/
redirect_from:
  - /university/math/calculus-1/differentiability/
background_image: "/images/grafi.png"
description: "Solved exercises on differentiability, piecewise functions, absolute values, radicals, one-sided derivatives, vertical tangents, and smoothness classes."
area: mathematics
topic: calculus
subtopic: differentiability
level: university
content_type: solved-exercises
---

<div class="content-box">

# Differentiability — Theory and Solved Exercises

## Theoretical Recall

A function f is **differentiable at x₀** if the limit

$$
f'(x_0)
=
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0)}{h}
$$

exists and is finite.

Equivalently, when the corresponding one-sided limits exist, differentiability requires:

$$
f'_-(x_0)=f'_+(x_0).
$$

### Differentiability and Continuity

If f is differentiable at x₀, then f is continuous at x₀.

Therefore:

$$
f\text{ differentiable at }x_0
\quad\Longrightarrow\quad
f\text{ continuous at }x_0.
$$

The converse is false: a function can be continuous without being differentiable.

### Corners and Cusps

A **corner** occurs when the left and right derivatives are finite but different.

For example:

$$
f(x)=|x|
$$

is continuous at zero, but:

$$
f'_-(0)=-1,
$$

while:

$$
f'_+(0)=1.
$$

A **cusp** occurs when the one-sided derivatives become infinite with opposite signs.

### Vertical Tangents

A vertical tangent may occur when the difference quotient tends to +∞ or −∞.

In that case the ordinary derivative is not finite, so the function is not differentiable at that point in the usual sense.

### Piecewise Functions

For a piecewise function to be differentiable at a junction x₀, two conditions are required.

First, continuity:

$$
\lim_{x\to x_0^-}f(x)
=
f(x_0)
=
\lim_{x\to x_0^+}f(x).
$$

Second, equality of the one-sided derivatives:

$$
f'_-(x_0)=f'_+(x_0).
$$

### Higher-Order Smoothness

The notation:

$$
f\in C^k(\mathbb{R})
$$

means that f has derivatives up to order k and that all these derivatives are continuous on ℝ.

The notation:

$$
f\in C^\infty(\mathbb{R})
$$

means that f is infinitely differentiable.

</div>

---

<div class="content-box">

## Exercises

### Exercise 1 — Continuous but Not Differentiable

Consider:

$$
f(x)=
\begin{cases}
x^2, & x\ge0,\\
-x, & x<0.
\end{cases}
$$

Verify continuity and differentiability at x = 0.

**Solution.**

For continuity, consider the left-hand limit:

$$
\lim_{x\to0^-}f(x)
=
\lim_{x\to0^-}(-x)
=
0.
$$

The right-hand limit is:

$$
\lim_{x\to0^+}f(x)
=
\lim_{x\to0^+}x^2
=
0.
$$

Moreover:

$$
f(0)=0.
$$

Therefore:

$$
\lim_{x\to0}f(x)=f(0).
$$

The function is continuous at zero.

Now compute the left derivative:

$$
f'_-(0)
=
\lim_{h\to0^-}
\frac{f(h)-f(0)}{h}.
$$

For h < 0:

$$
f(h)=-h.
$$

Thus:

$$
f'_-(0)
=
\lim_{h\to0^-}
\frac{-h}{h}
=
-1.
$$

For the right derivative:

$$
f'_+(0)
=
\lim_{h\to0^+}
\frac{h^2}{h}.
$$

Therefore:

$$
f'_+(0)
=
\lim_{h\to0^+}h
=
0.
$$

Since:

$$
-1\ne0,
$$

the function is not differentiable at zero.

**Final Result**

$$
f\in C^0(\mathbb{R}),
\qquad
f\notin C^1(\mathbb{R})
$$

---

### Exercise 2 — Absolute Value and Radical

Study the differentiability of:

$$
f(x)=x\sqrt{|x|}.
$$

**Solution.**

For x > 0:

$$
f(x)=x^{3/2}.
$$

Therefore:

$$
f'(x)=\frac32\sqrt{x}.
$$

For x < 0:

$$
f(x)
=
x\sqrt{-x}
=
-(-x)^{3/2}.
$$

Differentiating:

$$
f'(x)
=
\frac32\sqrt{-x}.
$$

At zero:

$$
f(0)=0.
$$

The difference quotient is:

$$
\frac{f(h)-f(0)}{h}
=
\frac{h\sqrt{|h|}}{h}.
$$

For h ≠ 0:

$$
\frac{f(h)}{h}
=
\sqrt{|h|}.
$$

Hence:

$$
f'(0)
=
\lim_{h\to0}\sqrt{|h|}
=
0.
$$

Moreover:

$$
\lim_{x\to0^-}f'(x)=0,
$$

and:

$$
\lim_{x\to0^+}f'(x)=0.
$$

Thus the derivative is continuous at zero.

**Final Result**

$$
f\in C^1(\mathbb{R})
$$

---

### Exercise 3 — A Smooth Absolute-Value Power

Consider:

$$
f(x)=|x|\sqrt{|x|}.
$$

Study differentiability at x = 0.

**Solution.**

We can write:

$$
f(x)=|x|^{3/2}.
$$

For x > 0:

$$
f(x)=x^{3/2},
$$

so:

$$
f'(x)=\frac32\sqrt{x}.
$$

For x < 0:

$$
f(x)=(-x)^{3/2}.
$$

Therefore:

$$
f'(x)
=
-\frac32\sqrt{-x}.
$$

At zero:

$$
\frac{f(h)-f(0)}{h}
=
\frac{|h|^{3/2}}{h}.
$$

For h > 0:

$$
\frac{|h|^{3/2}}{h}
=
\sqrt{h}.
$$

For h < 0:

$$
\frac{|h|^{3/2}}{h}
=
-\sqrt{-h}.
$$

Both expressions tend to zero.

Therefore:

$$
f'(0)=0.
$$

Furthermore:

$$
\lim_{x\to0}f'(x)=0=f'(0).
$$

**Author’s note:** Although the function involves an absolute value and a radical, the exponent 3/2 is greater than 1. This is sufficient for first-order differentiability at the origin, but not for arbitrary smoothness.

**Final Result**

$$
f\in C^1(\mathbb{R})
$$

---

### Exercise 4 — Endpoint and Vertical Tangent

Study:

$$
f(x)=|x|\sqrt{1-x}
$$

at x = 1.

**Solution.**

The square root requires:

$$
1-x\ge0.
$$

Thus the domain is:

$$
(-\infty,1].
$$

At x = 1:

$$
f(1)=0.
$$

Since 1 is an endpoint of the domain, we consider the derivative from within the domain:

$$
\lim_{h\to0^-}
\frac{f(1+h)-f(1)}{h}.
$$

For h sufficiently close to zero from the left:

$$
|1+h|=1+h.
$$

Therefore:

$$
\frac{f(1+h)-f(1)}{h}
=
\frac{(1+h)\sqrt{-h}}{h}.
$$

Since h < 0:

$$
h=-|h|.
$$

Hence:

$$
\frac{(1+h)\sqrt{-h}}{h}
=
-\frac{1+h}{\sqrt{-h}}.
$$

As h → 0⁻:

$$
-\frac{1+h}{\sqrt{-h}}
\to-\infty.
$$

Thus there is a vertical tangent at the endpoint.

The ordinary finite derivative does not exist.

**Final Result**

$$
f\text{ is not differentiable at }x=1
$$

---

### Exercise 5 — Failure of Continuity

Consider:

$$
f(x)=x^x\log x,
\qquad x>0,
$$

and define:

$$
f(0)=0.
$$

Check continuity and differentiability at x = 0.

**Solution.**

For x > 0:

$$
x^x=e^{x\log x}.
$$

We know that:

$$
\lim_{x\to0^+}x\log x=0.
$$

Therefore:

$$
\lim_{x\to0^+}x^x=1.
$$

On the other hand:

$$
\lim_{x\to0^+}\log x=-\infty.
$$

Hence:

$$
x^x\log x\to-\infty.
$$

Therefore:

$$
\lim_{x\to0^+}f(x)\ne f(0).
$$

The extension f(0) = 0 is not continuous at zero.

Since differentiability implies continuity, the function cannot be differentiable there.

**Final Result**

$$
f\text{ is neither continuous nor differentiable at }x=0
$$

---

### Exercise 6 — Differentiability of a Piecewise Function

Consider:

$$
f(x)=
\begin{cases}
ax+b, & x<0,\\
x^2, & x\ge0.
\end{cases}
$$

Find a and b so that f is differentiable at x = 0.

**Solution.**

Differentiability first requires continuity.

The left-hand limit is:

$$
\lim_{x\to0^-}(ax+b)=b.
$$

Since:

$$
f(0)=0,
$$

continuity requires:

$$
b=0.
$$

Now compute the one-sided derivatives.

From the left:

$$
f'_-(0)=a.
$$

From the right:

$$
f'_+(0)
=
\lim_{h\to0^+}
\frac{h^2}{h}
=
0.
$$

Differentiability requires:

$$
a=0.
$$

Thus:

$$
a=0,
\qquad
b=0.
$$

With these values, the resulting function is x² for x ≥ 0 and 0 for x < 0, and its derivative is continuous at zero.

**Final Result**

$$
a=0,
\qquad
b=0
$$

---

### Exercise 7 — Smoothness of Absolute Powers

For which real values of a is:

$$
f(x)=|x|^a
$$

of class Cᵏ on ℝ?

**Solution.**

First, if a < 0, the function is not defined at zero.

If:

$$
a=0,
$$

then:

$$
|x|^0=1,
$$

so the function is infinitely differentiable.

If a is a positive even integer:

$$
a=2m,
$$

then:

$$
|x|^{2m}=x^{2m}.
$$

Thus the function is a polynomial and belongs to C∞(ℝ).

Now suppose a > 0 and a is not an even integer.

For x ≠ 0, repeated differentiation produces terms whose magnitude behaves like:

$$
|x|^{a-j}
$$

after j derivatives.

If:

$$
a>k,
$$

all derivatives up to order k extend continuously to zero.

If a is an odd positive integer, say:

$$
a=2m+1,
$$

then |x|ᵃ is of class C²ᵐ but not C²ᵐ⁺¹.

For non-integer positive a, the same general threshold applies: the function belongs to Cᵏ whenever k < a, while smoothness fails once the differentiation order reaches or exceeds the relevant singular exponent.

Therefore, for an integer k ≥ 0, the complete criterion is:

$$
|x|^a\in C^k(\mathbb{R})
$$

if a = 0, or a is a positive even integer, or a > k.

**Author’s note:** The even-integer case is exceptional because the absolute value disappears algebraically: |x|²ᵐ = x²ᵐ.

**Final Result**

$$
|x|^a\in C^k(\mathbb{R})
\iff
a=0
\ \text{or}\
a\in2\mathbb{N}
\ \text{or}\
a>k
$$

---

### Exercise 8 — Matching Derivatives

Consider:

$$
f(x)=
\begin{cases}
ax^2+bx, & x\ge0,\\
\sin x, & x<0.
\end{cases}
$$

Find a and b so that f is continuous and differentiable at x = 0.

**Solution.**

For continuity:

$$
\lim_{x\to0^-}\sin x=0.
$$

For the right branch:

$$
f(0)=0.
$$

Therefore continuity is automatic.

Now consider the derivatives.

From the left:

$$
f'_-(0)
=
\cos0
=
1.
$$

For x > 0:

$$
f'(x)=2ax+b.
$$

Hence:

$$
f'_+(0)=b.
$$

Differentiability requires:

$$
b=1.
$$

The parameter a does not affect differentiability at zero.

**Final Result**

$$
b=1,
\qquad
a\in\mathbb{R}
$$

---

### Exercise 9 — The Absolute Value Function

Study continuity and differentiability of:

$$
f(x)=|x|
$$

at x = 0.

**Solution.**

Since:

$$
\lim_{x\to0}|x|=0=f(0),
$$

the function is continuous at zero.

Now consider the difference quotient:

$$
\frac{|h|-0}{h}.
$$

For h > 0:

$$
\frac{|h|}{h}=1.
$$

Thus:

$$
f'_+(0)=1.
$$

For h < 0:

$$
\frac{|h|}{h}=-1.
$$

Thus:

$$
f'_-(0)=-1.
$$

Since the one-sided derivatives are different:

$$
f'_-(0)\ne f'_+(0).
$$

Therefore f is not differentiable at zero.

Geometrically, the graph has a corner at the origin.

**Final Result**

$$
f\in C^0(\mathbb{R}),
\qquad
f\notin C^1(\mathbb{R})
$$

---

### Exercise 10 — A C² Piecewise Function

Find a, b and c so that:

$$
f(x)=
\begin{cases}
ax^2+bx+c, & x<0,\\
\cos x, & x\ge0
\end{cases}
$$

belongs to C²(ℝ).

**Solution.**

Both branches are infinitely differentiable away from zero. Therefore we only need to match the function and its first two derivatives at x = 0.

For continuity:

$$
\lim_{x\to0^-}f(x)=c.
$$

Since:

$$
f(0)=\cos0=1,
$$

we require:

$$
c=1.
$$

For x < 0:

$$
f'(x)=2ax+b.
$$

Thus:

$$
f'_-(0)=b.
$$

For x > 0:

$$
f'(x)=-\sin x.
$$

Therefore:

$$
f'_+(0)=0.
$$

Hence:

$$
b=0.
$$

Now compute the second derivatives.

For x < 0:

$$
f''(x)=2a.
$$

Thus:

$$
f''_-(0)=2a.
$$

For x > 0:

$$
f''(x)=-\cos x.
$$

Therefore:

$$
f''_+(0)=-1.
$$

For the second derivative to be continuous:

$$
2a=-1.
$$

Hence:

$$
a=-\frac12.
$$

**Final Result**

$$
a=-\frac12,
\qquad
b=0,
\qquad
c=1
$$

</div>

---

<div class="content-box">

## Explore More Topics in Calculus

- [Limits]({{ "/mathematics/calculus/limits/" | relative_url }})
- [Sequences]({{ "/mathematics/calculus/sequences/" | relative_url }})
- [Series]({{ "/mathematics/calculus/series/" | relative_url }})
- [Continuity]({{ "/mathematics/calculus/continuity/" | relative_url }})
- [Integration by Parts]({{ "/mathematics/calculus/integration-by-parts/" | relative_url }})
- [Integration by Substitution]({{ "/mathematics/calculus/integration-by-substitution/" | relative_url }})
- [Ordinary Differential Equations]({{ "/mathematics/calculus/odes-general/" | relative_url }})
- [Cauchy Problems]({{ "/mathematics/calculus/odes-cauchy/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>