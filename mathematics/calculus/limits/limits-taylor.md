---
layout: default
date: 2026-08-24
original_date: 2025-08-30
title: "Solved Exercises — Limits with Taylor Expansion"
permalink: /mathematics/calculus/limits/limits-taylor/
redirect_from:
  - /university/math/calculus-1/limits-taylor/
background_image: "/images/limiti.png"
description: "Worked limit examples using Taylor expansions of exponential, logarithmic, and trigonometric functions, with detailed solutions and author notes."
area: mathematics
topic: calculus
subtopic: limits
method: taylor-expansion
level: university
content_type: solved-exercises
---

<div class="content-box">

# Solved Exercises — Limits with Taylor Expansion

## Theoretical Recall

Taylor expansion of a function f at x₀:

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

If x₀ = 0 we obtain the **Maclaurin expansion**.

### Rules for o-notation

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

$$
o(x^n+o(x^n))=o(x^n)
$$

### Maclaurin Series

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

## Exercises

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

## Continue Exploring Limits

Taylor expansions are particularly useful when several terms cancel and the dominant order of an expression is not immediately visible.

The key is to expand each function **far enough to identify the first nonzero term that survives the cancellation**.

[**Explore all Limits resources →**]({{ "/mathematics/calculus/limits/" | relative_url }})

[**Fundamental and Notable Limits →**]({{ "/mathematics/calculus/limits/fundamental-limits-examples/" | relative_url }})

[**Limits with L’Hôpital’s Rule →**]({{ "/mathematics/calculus/limits/limits-hopital/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>