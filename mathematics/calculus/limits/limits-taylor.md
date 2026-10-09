---
layout: default
date: 2026-08-29
original_date: 2025-08-30
title: "Limits Using Taylor Expansions: Formulas and Solved Examples"
last_modified_at: 2026-10-09
permalink: /mathematics/calculus/limits/limits-taylor/
redirect_from:
  - /university/math/calculus-1/limits-taylor/
background_image: "/images/limiti.png"
description: "Evaluate limits using Taylor and Maclaurin expansions: formulas, little-o rules and 15 solved examples, including fourth- and eighth-order cancellations."
area: mathematics
topic: calculus
subtopic: limits
method: taylor-expansion
level: university
content_type: solved-exercises
---

<div class="content-box">

# Limits Using Taylor Expansions: Formulas and Solved Examples

Taylor expansions turn many indeterminate limits into algebraic calculations. The essential step is to expand each function far enough to identify the first nonzero term that remains after cancellation.

This page collects the Maclaurin formulas most often used in limits, the main rules of little-o notation, and fifteen solved examples involving exponential, logarithmic, and trigonometric functions.

## How to Evaluate Limits Using Taylor Expansions

If $f$ is sufficiently differentiable near $x_0$, its Taylor expansion at $x_0$ is:

$$
f(x)
=
f(x_0)
+
\frac{f'(x_0)}{1!}(x-x_0)
+
\frac{f''(x_0)}{2!}(x-x_0)^2
+
\dots
+
\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n
+
o((x-x_0)^n).
$$

If $x_0=0$, we obtain the **Maclaurin expansion**.

### Rules for Little-o Notation

$$
o(x^m)+o(x^m)=o(x^m)
$$

$$
o(x^m)\cdot o(x^n)=o(x^{m+n})
$$

$$
o(x^n)+o(x^m)=o(x^{\min\{m,n\}})
$$

$$
x^n\cdot o(x^m)=o(x^{n+m})
$$

For any nonzero constant $C$, $C\,o(x^n)=o(x^n)$.

### Taylor and Maclaurin Expansions Commonly Used in Limits

Up to the relevant order:

$$
(1+x)^\alpha
=
1+\alpha x
+
\frac{\alpha(\alpha-1)}{2!}x^2
+
\dots
+
o(x^n)
$$

$$
e^x
=
1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+o(x^3)
$$

$$
\log(1+x)
=
x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+o(x^4)
$$

$$
\sin x
=
x-\frac{x^3}{3!}+\frac{x^5}{5!}+o(x^5)
$$

$$
\cos x
=
1-\frac{x^2}{2}+\frac{x^4}{4!}+o(x^4)
$$

$$
\tan x
=
x+\frac{x^3}{3}+\frac{2}{15}x^5+o(x^5)
$$

**Author’s note:**  
The expansions must be truncated only after ensuring the approximation order is sufficient to determine the limit. A common mistake is cutting the series too early.

</div>

<div class="content-box">

## How Many Taylor Terms Do You Need?

Start from the denominator's order, then check which numerator terms cancel. Expand far enough that the remainder, after division, tends to zero. A zero coefficient is a reason to continue the expansion, not evidence that the limit is zero.

For example, first-order approximations alone cannot determine this limit:

$$
\lim_{x\to0}\frac{e^x-1-x}{x^2}.
$$

Keep the quadratic term and a remainder smaller than x²:

$$
e^x-1-x=\frac{x^2}{2}+o(x^2).
$$

After division, the remainder tends to zero:

$$
\frac{e^x-1-x}{x^2}=\frac12+o(1).
$$

$$
\frac12
$$

### Taylor or L'Hôpital?

For the same quotient, both numerator and denominator tend to zero. The functions are differentiable near zero and the denominator derivatives used below are nonzero on a punctured neighborhood. Two applications of L'Hôpital's rule give:

$$
\lim_{x\to0}\frac{e^x-1-x}{x^2}
=\lim_{x\to0}\frac{e^x-1}{2x}
=\lim_{x\to0}\frac{e^x}{2}.
$$

$$
\frac12
$$

Taylor makes the cancellation and surviving order explicit. L'Hôpital can be shorter when successive differentiation simplifies the quotient. Check its hypotheses before applying it; it is not a rule for arbitrary quotients.

## Solved Limits Using Taylor Expansions

</div>

<div class="content-box">

### Exercise 1

$$
\lim_{x\to0} \frac{e^x-1-x}{x^2}
$$

**Solution.**

Using the Maclaurin expansion:

$$
e^x
=
1+x+\frac{x^2}{2}+o(x^2).
$$

Therefore:

$$
e^x-1-x
=
\frac{x^2}{2}+o(x^2).
$$

Dividing by x²:

$$
\frac{e^x-1-x}{x^2}
=
\frac{1}{2}+o(1).
$$

**Final Result**

$$
\frac{1}{2}
$$


</div>

<div class="content-box">

### Exercise 2

$$
\lim_{x\to0} \frac{\log(1+x)-x}{x^2}
$$

**Solution.**

Using:

$$
\log(1+x)
=
x-\frac{x^2}{2}+o(x^2),
$$

we obtain:

$$
\log(1+x)-x
=
-\frac{x^2}{2}+o(x^2).
$$

Therefore:

$$
\frac{\log(1+x)-x}{x^2}
=
-\frac{1}{2}+o(1).
$$

**Final Result**

$$
-\frac{1}{2}
$$


</div>

<div class="content-box">

### Exercise 3

$$
\lim_{x\to0} \frac{\sin x-x}{x^3}
$$

**Solution.**

Using:

$$
\sin x
=
x-\frac{x^3}{6}+o(x^3),
$$

we obtain:

$$
\sin x-x
=
-\frac{x^3}{6}+o(x^3).
$$

Therefore:

$$
\frac{\sin x-x}{x^3}
=
-\frac{1}{6}+o(1).
$$

**Final Result**

$$
-\frac{1}{6}
$$


</div>

<div class="content-box">

### Exercise 4

$$
\lim_{x\to0} \frac{1-\cos x}{x^2}
$$

**Solution.**

Using:

$$
\cos x
=
1-\frac{x^2}{2}+o(x^2),
$$

we obtain:

$$
1-\cos x
=
\frac{x^2}{2}+o(x^2).
$$

Therefore:

$$
\frac{1-\cos x}{x^2}
=
\frac{1}{2}+o(1).
$$

**Final Result**

$$
\frac{1}{2}
$$


</div>

<div class="content-box">

### Exercise 5

$$
\lim_{x\to0} \frac{e^{2x}-1-2x}{x^2}
$$

**Solution.**

Using the exponential expansion with argument 2x:

$$
e^{2x}
=
1+2x+\frac{(2x)^2}{2}+o(x^2).
$$

Hence:

$$
e^{2x}
=
1+2x+2x^2+o(x^2).
$$

Therefore:

$$
e^{2x}-1-2x
=
2x^2+o(x^2).
$$

Dividing by x²:

$$
\frac{e^{2x}-1-2x}{x^2}
=
2+o(1).
$$

**Final Result**

$$
2
$$


</div>

<div class="content-box">

### Exercise 6

$$
\lim_{x\to0} \frac{\tan x-x}{x^3}
$$

**Solution.**

Using:

$$
\tan x
=
x+\frac{x^3}{3}+o(x^3),
$$

we obtain:

$$
\tan x-x
=
\frac{x^3}{3}+o(x^3).
$$

Therefore:

$$
\frac{\tan x-x}{x^3}
=
\frac{1}{3}+o(1).
$$

**Final Result**

$$
\frac{1}{3}
$$


</div>

<div class="content-box">

### Exercise 7

$$
\lim_{x\to0} \frac{\log(1+x)-\sin x}{x^3}
$$

**Solution.**

Use the expansions:

$$
\log(1+x)
=
x-\frac{x^2}{2}+\frac{x^3}{3}+o(x^3),
$$

and:

$$
\sin x
=
x-\frac{x^3}{6}+o(x^3).
$$

Subtracting:

$$
\log(1+x)-\sin x
=
-\frac{x^2}{2}
+
\frac{x^3}{2}
+
o(x^3).
$$

Dividing by x³:

$$
\frac{\log(1+x)-\sin x}{x^3}
=
-\frac{1}{2x}
+
\frac{1}{2}
+
o(1).
$$

As x → 0⁺:

$$
-\frac{1}{2x}
+
\frac{1}{2}
+
o(1)
\to
-\infty.
$$

As x → 0⁻:

$$
-\frac{1}{2x}
+
\frac{1}{2}
+
o(1)
\to
+\infty.
$$

The two one-sided limits are different.

**Final Result**

$$
\text{The two-sided limit does not exist.}
$$


</div>

<div class="content-box">

### Exercise 8

$$
\lim_{x\to0} \frac{e^x-\cos x}{x}
$$

**Solution.**

Use:

$$
e^x
=
1+x+\frac{x^2}{2}+o(x^2),
$$

and:

$$
\cos x
=
1-\frac{x^2}{2}+o(x^2).
$$

Subtracting:

$$
e^x-\cos x
=
x+x^2+o(x^2).
$$

Dividing by x:

$$
\frac{e^x-\cos x}{x}
=
1+x+o(x).
$$

Therefore:

$$
1+x+o(x)\to1.
$$

**Final Result**

$$
1
$$


</div>

<div class="content-box">

### Exercise 9

$$
\lim_{x\to0} \frac{\sin x-\tan x}{x^3}
$$

**Solution.**

Use:

$$
\sin x
=
x-\frac{x^3}{6}+o(x^3),
$$

and:

$$
\tan x
=
x+\frac{x^3}{3}+o(x^3).
$$

Subtracting:

$$
\sin x-\tan x
=
-\frac{x^3}{6}
-
\frac{x^3}{3}
+
o(x^3).
$$

Hence:

$$
\sin x-\tan x
=
-\frac{x^3}{2}+o(x^3).
$$

Therefore:

$$
\frac{\sin x-\tan x}{x^3}
=
-\frac{1}{2}+o(1).
$$

**Final Result**

$$
-\frac{1}{2}
$$


</div>

<div class="content-box">

### Exercise 10

$$
\lim_{x\to0} \frac{e^x-\sin x-1}{x}
$$

**Solution.**

Use:

$$
e^x
=
1+x+\frac{x^2}{2}+\frac{x^3}{6}+o(x^3),
$$

and:

$$
\sin x
=
x-\frac{x^3}{6}+o(x^3).
$$

Therefore:

$$
e^x-\sin x-1
=
\frac{x^2}{2}
+
\frac{x^3}{3}
+
o(x^3).
$$

Dividing by x:

$$
\frac{e^x-\sin x-1}{x}
=
\frac{x}{2}
+
\frac{x^2}{3}
+
o(x^2).
$$

As x → 0:

$$
\frac{x}{2}
+
\frac{x^2}{3}
+
o(x^2)
\to0.
$$

**Final Result**

$$
0
$$


</div>




<div class="content-box">

## Further Taylor Limits from the Exercise Book

These additional exercises and their solutions are translated from *Eserciziario 2.1* by Antonino De Martino and Luana Manfredini. No new exercise statements have been introduced.

</div>

<div class="content-box">

### Exercise 11 — Expansion around x = 1

$$
\lim_{x\to1}\frac{\log(1+\pi-4\arctan x)}{\sin(1-x)}.
$$

**Solution.**

First expand the logarithm and sine, whose arguments tend to zero:

$$
\frac{\log(1+\pi-4\arctan x)}{\sin(1-x)}
=\frac{\pi-4\arctan x+o(\pi-4\arctan x)}{(1-x)+o(1-x)}.
$$

Expand arctan at x = 1:

$$
\arctan x=\frac\pi4+\frac{x-1}{2}+o(x-1).
$$

Substituting gives:

$$
\frac{2(1-x)+o(1-x)+o(1-x)}{(1-x)+o(1-x)}
=\frac{2+o(1)}{1+o(1)}\longrightarrow2.
$$

**Final Result**

$$
2
$$

</div>

<div class="content-box">

### Exercise 12 — Fourth-order cancellation

$$
\lim_{x\to0}\frac{x\arcsin x-x^2}{\sqrt{1+x^4}-\cos(x^2)}.
$$

**Solution.**

Use the expansions in the source:

$$
\arcsin x=x+\frac{x^3}{6}+o(x^3).
$$

$$
\sqrt{1+x^4}=1+\frac{x^4}{2}+o(x^4),
\qquad \cos(x^2)=1-\frac{x^4}{2}+o(x^4).
$$

Multiply the arcsine expansion by x and cancel the quadratic terms:

$$
x\left(x+\frac{x^3}{6}+o(x^3)\right)-x^2
=\frac{x^4}{6}+o(x^4).
$$

The denominator is:

$$
1+\frac{x^4}{2}+o(x^4)-1+\frac{x^4}{2}+o(x^4)
=x^4+o(x^4).
$$

Therefore:

$$
\frac{x^4/6+o(x^4)}{x^4+o(x^4)}\longrightarrow\frac16.
$$

**Final Result**

$$
\frac16
$$

</div>

<div class="content-box">

### Exercise 13 — A product with fourth-order cancellation

$$
\lim_{x\to0}\frac{\sin(3x)\log(1+2x)-6x^2+6x^3}{x^4}.
$$

**Solution.**

Expand each factor to the order used in the source:

$$
\sin(3x)=3x-\frac{27}{6}x^3+o(x^3).
$$

$$
\log(1+2x)=2x-2x^2+\frac83x^3-4x^4+o(x^4).
$$

Multiplying and applying the little-o rules gives:

$$
\sin(3x)\log(1+2x)
=6x^2-6x^3+8x^4-9x^4+o(x^4).
$$

Thus the quotient becomes:

$$
\frac{6x^2-6x^3+8x^4-9x^4+o(x^4)-6x^2+6x^3}{x^4}
=\frac{-x^4+o(x^4)}{x^4}\longrightarrow-1.
$$

**Final Result**

$$
-1
$$

</div>

<div class="content-box">

### Exercise 14 — A fifth root and the binomial expansion

$$
\lim_{x\to0}\frac{\sqrt[5]{1-5x^2+x^4}-1+x^2}{x^4}.
$$

**Solution.**

Use the binomial expansion with exponent 1/5 and argument −5x²+x⁴:

$$
(1-5x^2+x^4)^{1/5}
=1+\frac{-5x^2+x^4}{5}
-\frac2{25}(-5x^2+x^4)^2
+o((-5x^2+x^4)^2).
$$

The square contributes 25x⁴ at the required order. Hence:

$$
\frac{1-x^2+x^4/5-2x^4-1+x^2+o(x^4)}{x^4}
=-\frac95+o(1).
$$

**Final Result**

$$
-\frac95
$$

</div>

<div class="content-box">

### Exercise 15 — Matching eighth-order terms

$$
\lim_{x\to0}\frac{x^5(e^{2x^3}-1)}{\sqrt{1+x^8}-\sqrt[3]{1+x^8}}.
$$

**Solution.**

Apply the exponential and binomial expansions exactly as in the source:

$$
e^{2x^3}=1+2x^3+o(x^3).
$$

$$
\sqrt{1+x^8}=1+\frac{x^8}{2}+o(x^8),
\qquad \sqrt[3]{1+x^8}=1+\frac{x^8}{3}+o(x^8).
$$

Then:

$$
\frac{x^5(1+2x^3+o(x^3)-1)}{1+x^8/2+o(x^8)-1-x^8/3+o(x^8)}
=\frac{2x^8+o(x^8)}{x^8/6+o(x^8)}\longrightarrow12.
$$

**Final Result**

$$
12
$$

</div>

<div class="content-box">

## Continue Exploring Limits

Taylor expansions are particularly useful when several terms cancel and the dominant order of an expression is not immediately visible.

The key is to expand each function **far enough to identify the first nonzero term that survives the cancellation**.

[**Explore all Limits resources →**]({{ "/mathematics/calculus/limits/" | relative_url }})

[**Fundamental and Notable Limits →**]({{ "/mathematics/calculus/limits/fundamental-limits-examples/" | relative_url }})

[**Limits with L’Hôpital’s Rule →**]({{ "/mathematics/calculus/limits/limits-hopital/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>