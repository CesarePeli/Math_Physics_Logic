---
layout: default
date: 2026-08-24
original_date: 2025-08-30
title: "Solved Exercises — Limits with L’Hôpital’s Rule"
permalink: /mathematics/calculus/limits/limits-hopital/
redirect_from:
  - /university/math/calculus-1/limits-hopital/
background_image: "/images/limiti.png"
description: "Ten worked limit examples using L’Hôpital’s rule, including 0/0 and ∞/∞ forms, repeated applications, logarithmic transformations, and alternative methods."
area: mathematics
topic: calculus
subtopic: limits
method: lhopital
level: university
content_type: solved-exercises
---

<div class="content-box">

# Limits with L’Hôpital’s Rule

## L’Hôpital’s Theorem

Let f and g be functions defined in a neighborhood of c, except possibly at c.

Suppose that the quotient

$$
\frac{f(x)}{g(x)}
$$

has one of the indeterminate forms

$$
\frac{0}{0}
$$

or

$$
\frac{\infty}{\infty}
$$

as x approaches c.

Assume that f and g are differentiable in a punctured neighborhood of c, with

$$
g'(x)\neq0.
$$

If the limit

$$
\lim_{x\to c}
\frac{f'(x)}{g'(x)}
$$

exists, either as a finite value or as ±∞, then, under the hypotheses of L’Hôpital’s theorem,

$$
\lim_{x\to c}
\frac{f(x)}{g(x)}
=
\lim_{x\to c}
\frac{f'(x)}{g'(x)}.
$$

The theorem also applies to suitable one-sided limits and limits at infinity.

</div>

---

<div class="content-box">

## Exercises

### Exercise 1

Evaluate

$$
\lim_{x\to0^+}
\frac{e^{x^x}-e}{x}.
$$

**Solution.**

The limit must be taken from the right because xˣ is being considered as a real-valued function near zero.

Since

$$
x^x=e^{x\log x},
$$

and

$$
x\log x\to0,
$$

we have

$$
x^x\to1.
$$

Therefore

$$
e^{x^x}-e\to0,
$$

and the quotient has the indeterminate form 0/0.

Apply L’Hôpital’s rule.

First,

$$
(x^x)'
=
x^x(\log x+1).
$$

Hence

$$
\frac{d}{dx}e^{x^x}
=
e^{x^x}x^x(\log x+1).
$$

Therefore

$$
\lim_{x\to0^+}
\frac{e^{x^x}-e}{x}
=
\lim_{x\to0^+}
e^{x^x}x^x(\log x+1).
$$

As x → 0⁺,

$$
e^{x^x}\to e,
$$

$$
x^x\to1,
$$

while

$$
\log x+1\to-\infty.
$$

Thus the product tends to −∞.

**Final Result**

$$
-\infty
$$

---

### Exercise 2

Evaluate

$$
\lim_{x\to0}
\left(
\frac{\sin x}{x}
\right)^{1/x^2}.
$$

**Solution.**

Let

$$
L=
\lim_{x\to0}
\left(
\frac{\sin x}{x}
\right)^{1/x^2}.
$$

Take logarithms:

$$
\log L
=
\lim_{x\to0}
\frac{
\log\left(\frac{\sin x}{x}\right)
}{
x^2
}.
$$

This is a 0/0 form.

Apply L’Hôpital:

$$
\log L
=
\lim_{x\to0}
\frac{
\cot x-\frac1x
}{
2x
}.
$$

Rewrite the numerator:

$$
\cot x-\frac1x
=
\frac{x\cos x-\sin x}{x\sin x}.
$$

Therefore

$$
\log L
=
\lim_{x\to0}
\frac{
x\cos x-\sin x
}{
2x^2\sin x
}.
$$

This is again 0/0.

Apply L’Hôpital:

$$
\log L
=
\lim_{x\to0}
\frac{
-x\sin x
}{
4x\sin x+2x^2\cos x
}.
$$

Simplifying by x,

$$
\log L
=
\lim_{x\to0}
\frac{
-\sin x
}{
4\sin x+2x\cos x
}.
$$

We still have 0/0, so apply L’Hôpital once more:

$$
\log L
=
\lim_{x\to0}
\frac{
-\cos x
}{
6\cos x-2x\sin x
}.
$$

Thus

$$
\log L=-\frac16.
$$

Exponentiating,

$$
L=e^{-1/6}.
$$

**Final Result**

$$
e^{-1/6}
$$

---

### Exercise 3

Evaluate

$$
\lim_{x\to0}
\frac{
e^{\sin x}-\cos x
}{
e^{\cos x}-e\log(x+e)
}.
$$

**Solution.**

At x = 0, numerator and denominator both tend to zero.

Apply L’Hôpital:

$$
\lim_{x\to0}
\frac{
e^{\sin x}-\cos x
}{
e^{\cos x}-e\log(x+e)
}
=
\lim_{x\to0}
\frac{
\cos x\,e^{\sin x}+\sin x
}{
-\sin x\,e^{\cos x}-\frac{e}{x+e}
}.
$$

Evaluating the transformed limit at zero gives

$$
\frac{1}{-1}.
$$

**Final Result**

$$
-1
$$

---

### Exercise 4

Evaluate

$$
\lim_{x\to-1}
\frac{
e^{\sqrt{1-3x}}
-
e^{\sqrt{3-x}}
}{
e^x-e^{2x+1}
}.
$$

**Solution.**

At x = −1, numerator and denominator both vanish.

Apply L’Hôpital:

$$
\lim_{x\to-1}
\frac{
-\frac{3e^{\sqrt{1-3x}}}{2\sqrt{1-3x}}
+
\frac{e^{\sqrt{3-x}}}{2\sqrt{3-x}}
}{
e^x-2e^{2x+1}
}.
$$

At x = −1,

$$
\sqrt{1-3(-1)}=2,
$$

and

$$
\sqrt{3-(-1)}=2.
$$

Thus the numerator becomes

$$
-\frac34e^2+\frac14e^2
=
-\frac12e^2.
$$

The denominator becomes

$$
\frac1e-\frac2e
=
-\frac1e.
$$

Therefore

$$
\frac{-e^2/2}{-1/e}
=
\frac{e^3}{2}.
$$

**Final Result**

$$
\frac{e^3}{2}
$$

---

### Exercise 5

Evaluate

$$
\lim_{x\to1^-}
\log x\,\log(1-x).
$$

**Solution.**

Rewrite the product as a quotient:

$$
\log x\,\log(1-x)
=
\frac{
\log(1-x)
}{
1/\log x
}.
$$

As x → 1⁻, both numerator and denominator tend to −∞.

Apply L’Hôpital:

$$
\lim_{x\to1^-}
\frac{
-\frac1{1-x}
}{
-\frac1{x\log^2x}
}.
$$

This simplifies to

$$
\lim_{x\to1^-}
\frac{x\log^2x}{1-x}.
$$

Rewrite:

$$
\frac{x\log^2x}{1-x}
=
-x\log x
\frac{\log x}{x-1}.
$$

Now

$$
\log x\to0,
$$

and

$$
\frac{\log x}{x-1}\to1.
$$

Therefore the product tends to zero.

**Final Result**

$$
0
$$

---

### Exercise 6

Evaluate

$$
\lim_{x\to3^+}
\frac{
\sqrt{x}-\sqrt3+\sqrt{x-3}
}{
\sqrt{x^2-9}
}.
$$

**Solution.**

Since

$$
x^2-9=(x-3)(x+3),
$$

we have

$$
\sqrt{x^2-9}
=
\sqrt{x-3}\sqrt{x+3}.
$$

Therefore

$$
\frac{
\sqrt{x}-\sqrt3+\sqrt{x-3}
}{
\sqrt{x^2-9}
}
=
\frac{
\frac{\sqrt{x}-\sqrt3}{\sqrt{x-3}}+1
}{
\sqrt{x+3}
}.
$$

Consider

$$
\lim_{x\to3^+}
\frac{
\sqrt{x}-\sqrt3
}{
\sqrt{x-3}
}.
$$

This is a 0/0 form.

Apply L’Hôpital:

$$
\lim_{x\to3^+}
\frac{
1/(2\sqrt{x})
}{
1/(2\sqrt{x-3})
}
=
\lim_{x\to3^+}
\frac{
\sqrt{x-3}
}{
\sqrt{x}
}
=
0.
$$

Thus the original limit becomes

$$
\frac{0+1}{\sqrt6}.
$$

**Final Result**

$$
\frac1{\sqrt6}
$$

---

### Exercise 7

Evaluate

$$
\lim_{x\to0^+}
\frac{
x^2-\arctan(x^2)
}{
x(1-\cos x)^3
}.
$$

**Solution.**

The quotient has the indeterminate form 0/0.

Apply L’Hôpital:

$$
\lim_{x\to0^+}
\frac{
2x-\frac{2x}{1+x^4}
}{
(1-\cos x)^3
+
3x(1-\cos x)^2\sin x
}.
$$

Simplify the numerator:

$$
2x-\frac{2x}{1+x^4}
=
\frac{2x^5}{1+x^4}.
$$

Factor the denominator:

$$
(1-\cos x)^2
\left[
(1-\cos x)+3x\sin x
\right].
$$

Using the standard equivalents

$$
1-\cos x
\sim
\frac{x^2}{2},
$$

and

$$
\sin x\sim x,
$$

we obtain

$$
(1-\cos x)^2
\sim
\frac{x^4}{4},
$$

and

$$
(1-\cos x)+3x\sin x
\sim
\frac{x^2}{2}+3x^2.
$$

Therefore

$$
(1-\cos x)+3x\sin x
\sim
\frac{7x^2}{2}.
$$

Hence the denominator behaves like

$$
\frac{x^4}{4}
\cdot
\frac{7x^2}{2}
=
\frac{7x^6}{8}.
$$

The numerator behaves like

$$
2x^5.
$$

Thus the quotient behaves like

$$
\frac{2x^5}{7x^6/8}
=
\frac{16}{7x}.
$$

Since x → 0⁺,

$$
\frac{16}{7x}\to+\infty.
$$

**Final Result**

$$
+\infty
$$

---

### Exercise 8

Evaluate

$$
\lim_{x\to0}
\frac{
e^x-\cos x-\sin x
}{
e^{x^2}-e^{x^3}
}.
$$

**Solution.**

At zero, numerator and denominator both vanish.

Apply L’Hôpital:

$$
\lim_{x\to0}
\frac{
e^x+\sin x-\cos x
}{
2xe^{x^2}-3x^2e^{x^3}
}.
$$

At zero this is again 0/0.

Apply L’Hôpital a second time.

The derivative of the numerator is

$$
e^x+\cos x+\sin x.
$$

The derivative of the denominator is

$$
2e^{x^2}
+
4x^2e^{x^2}
-
6xe^{x^3}
-
9x^4e^{x^3}.
$$

Therefore

$$
\lim_{x\to0}
\frac{
e^x+\cos x+\sin x
}{
2e^{x^2}
+
4x^2e^{x^2}
-
6xe^{x^3}
-
9x^4e^{x^3}
}.
$$

Evaluating at zero gives

$$
\frac{2}{2}.
$$

**Final Result**

$$
1
$$

---

### Exercise 9

Evaluate

$$
\lim_{x\to0}
\frac{
1-\cos x+\log(\cos x)
}{
x^4
}.
$$

**Solution.**

The quotient has the form 0/0.

Apply L’Hôpital:

$$
\lim_{x\to0}
\frac{
\sin x-\tan x
}{
4x^3
}.
$$

Again we obtain 0/0.

Apply L’Hôpital:

$$
\lim_{x\to0}
\frac{
\cos x-\sec^2x
}{
12x^2
}.
$$

Again:

$$
\frac00.
$$

Apply L’Hôpital once more:

$$
\lim_{x\to0}
\frac{
-\sin x
-
2\sec^2x\tan x
}{
24x
}.
$$

The form is still 0/0.

Apply L’Hôpital a fourth time:

$$
\lim_{x\to0}
\frac{
-\cos x
-
4\sec^2x\tan^2x
-
2\sec^4x
}{
24
}.
$$

At zero,

$$
\cos0=1,
$$

$$
\tan0=0,
$$

and

$$
\sec0=1.
$$

Therefore

$$
\frac{-1-0-2}{24}
=
-\frac{3}{24}.
$$

**Final Result**

$$
-\frac18
$$

---

### Exercise 10

Evaluate

$$
\lim_{x\to0}
\frac{
e^{x^2}-\cos^2x
}{
\sin^2x
}.
$$

**Solution — Method 1: L’Hôpital**

At zero, numerator and denominator both vanish.

Apply L’Hôpital:

$$
\lim_{x\to0}
\frac{
2xe^{x^2}
+
2\cos x\sin x
}{
2\cos x\sin x
}.
$$

Separate the quotient:

$$
\lim_{x\to0}
\left[
\frac{
xe^{x^2}
}{
\cos x\sin x
}
+
1
\right].
$$

Rewrite the first term:

$$
\frac{
xe^{x^2}
}{
\cos x\sin x
}
=
\frac{x}{\sin x}
\cdot
\frac{e^{x^2}}{\cos x}.
$$

As x → 0,

$$
\frac{x}{\sin x}\to1,
$$

and

$$
\frac{e^{x^2}}{\cos x}\to1.
$$

Therefore

$$
1\cdot1+1=2.
$$

**Solution — Method 2: Taylor Expansion**

Near zero,

$$
e^{x^2}
=
1+x^2+o(x^2),
$$

while

$$
\cos^2x
=
1-x^2+o(x^2).
$$

Therefore

$$
e^{x^2}-\cos^2x
=
2x^2+o(x^2).
$$

Also,

$$
\sin^2x
=
x^2+o(x^2).
$$

Hence

$$
\frac{
e^{x^2}-\cos^2x
}{
\sin^2x
}
\to2.
$$

**Final Result**

$$
2
$$

</div>

---

<div class="content-box">

## Continue Exploring Limits

L’Hôpital’s rule is one technique among several for resolving indeterminate forms. Its usefulness depends on recognizing the correct indeterminate form and checking the hypotheses before differentiating.

For some limits, algebraic transformations, fundamental limits, or Taylor expansions may provide a shorter or more illuminating solution.

[**Explore all Limits resources →**]({{ "/mathematics/calculus/limits/" | relative_url }})

[**Fundamental and Notable Limits →**]({{ "/mathematics/calculus/limits/fundamental-limits-examples/" | relative_url }})

[**Limits with Taylor Expansions →**]({{ "/mathematics/calculus/limits/limits-taylor/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>