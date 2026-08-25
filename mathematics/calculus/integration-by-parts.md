---
layout: default
date: 2026-08-24
original_date: 2025-08-29
title: "Solved Exercises — Integration by Parts"
permalink: /mathematics/calculus/integration-by-parts/
redirect_from:
  - /university/math/calculus-1/integration-by-parts/
background_image: "/images/integrali.png"
description: "Solved integration by parts exercises with step-by-step solutions for polynomial, exponential, trigonometric, and logarithmic integrals."
area: mathematics
topic: calculus
subtopic: integration-by-parts
level: university
content_type: solved-exercises
featured: true
---

<div class="content-box">

# Integration by Parts — Theory and Solved Exercises

## Theoretical Recall

Integration by parts is obtained directly from the product rule for derivatives.

For two differentiable functions f and g:

$$
(fg)'=f'g+fg'.
$$

Integrating both sides gives:

$$
\int (fg)'\,dx
=
\int f'g\,dx
+
\int fg'\,dx.
$$

Therefore:

$$
fg
=
\int f'g\,dx
+
\int fg'\,dx.
$$

Rearranging:

$$
\int f(x)g'(x)\,dx
=
f(x)g(x)
-
\int f'(x)g(x)\,dx.
$$

This is the **integration by parts formula**.

A common alternative notation is:

$$
\int u\,dv
=
uv-\int v\,du.
$$

### Choosing the Functions

The goal is to choose the factor to differentiate so that it becomes simpler, while the other factor can be integrated easily.

A useful heuristic is the **LIATE rule**:

- **L** — Logarithmic functions
- **I** — Inverse trigonometric functions
- **A** — Algebraic functions
- **T** — Trigonometric functions
- **E** — Exponential functions

Functions appearing earlier in this list are often good candidates for the factor to differentiate.

This is a guideline rather than a theorem: the best choice is always the one that simplifies the resulting integral.

**Author’s note:** Integration by parts should not be viewed merely as a formula to memorize. Its real purpose is to transform an integral into another one whose structure is easier to handle.

</div>

---

<div class="content-box">

## Exercises

### Exercise 1

Evaluate:

$$
\int xe^x\,dx.
$$

**Solution.**

Choose:

f = x

and:

g′ = eˣ.

Then:

f′ = 1

and:

g = eˣ.

Using integration by parts:

$$
\int xe^x\,dx
=
xe^x-\int e^x\,dx.
$$

Therefore:

$$
\int xe^x\,dx
=
xe^x-e^x+C.
$$

Factor out the exponential:

$$
\int xe^x\,dx
=
(x-1)e^x+C.
$$

**Final Result**

$$
(x-1)e^x+C
$$

---

### Exercise 2

Evaluate:

$$
\int x\cos x\,dx.
$$

**Solution.**

Choose:

f = x

and:

g′ = cos x.

Then:

f′ = 1

and:

g = sin x.

Therefore:

$$
\int x\cos x\,dx
=
x\sin x-\int\sin x\,dx.
$$

Since:

$$
\int\sin x\,dx=-\cos x,
$$

we obtain:

$$
\int x\cos x\,dx
=
x\sin x+\cos x+C.
$$

**Final Result**

$$
x\sin x+\cos x+C
$$

---

### Exercise 3

Evaluate:

$$
\int x\sin x\,dx.
$$

**Solution.**

Choose:

f = x

and:

g′ = sin x.

Then:

f′ = 1

and:

g = −cos x.

Applying integration by parts:

$$
\int x\sin x\,dx
=
-x\cos x+\int\cos x\,dx.
$$

Therefore:

$$
\int x\sin x\,dx
=
-x\cos x+\sin x+C.
$$

**Final Result**

$$
-x\cos x+\sin x+C
$$

---

### Exercise 4

Evaluate:

$$
\int xe^{2x}\,dx.
$$

**Solution.**

Choose:

f = x

and:

g′ = e²ˣ.

Then:

f′ = 1.

Moreover:

$$
g
=
\int e^{2x}\,dx
=
\frac12e^{2x}.
$$

Integration by parts gives:

$$
\int xe^{2x}\,dx
=
\frac{x}{2}e^{2x}
-
\frac12\int e^{2x}\,dx.
$$

Hence:

$$
\int xe^{2x}\,dx
=
\frac{x}{2}e^{2x}
-
\frac14e^{2x}
+
C.
$$

Factoring:

$$
\int xe^{2x}\,dx
=
\left(
\frac{x}{2}
-
\frac14
\right)e^{2x}
+
C.
$$

**Final Result**

$$
\left(\frac{x}{2}-\frac14\right)e^{2x}+C
$$

---

### Exercise 5

Evaluate:

$$
\int\ln x\,dx.
$$

**Solution.**

Although the integrand appears to contain only one function, write:

$$
\ln x
=
(\ln x)\cdot1.
$$

Choose:

f = ln x

and:

g′ = 1.

Then:

$$
f'
=
\frac1x,
$$

and:

g = x.

Integration by parts gives:

$$
\int\ln x\,dx
=
x\ln x
-
\int x\frac1x\,dx.
$$

Thus:

$$
\int\ln x\,dx
=
x\ln x-\int1\,dx.
$$

Therefore:

$$
\int\ln x\,dx
=
x\ln x-x+C.
$$

**Final Result**

$$
x\ln x-x+C
$$

---

### Exercise 6

Evaluate:

$$
\int x^2e^x\,dx.
$$

**Solution.**

Choose:

f = x²

and:

g′ = eˣ.

Then:

f′ = 2x

and:

g = eˣ.

Therefore:

$$
\int x^2e^x\,dx
=
x^2e^x
-
2\int xe^x\,dx.
$$

The remaining integral still requires integration by parts.

From Exercise 1:

$$
\int xe^x\,dx
=
xe^x-e^x.
$$

Substituting:

$$
\int x^2e^x\,dx
=
x^2e^x
-
2(xe^x-e^x)
+
C.
$$

Expanding:

$$
\int x^2e^x\,dx
=
x^2e^x
-
2xe^x
+
2e^x
+
C.
$$

Factoring out eˣ:

$$
\int x^2e^x\,dx
=
(x^2-2x+2)e^x+C.
$$

**Final Result**

$$
(x^2-2x+2)e^x+C
$$

---

### Exercise 7

Evaluate:

$$
\int x\ln x\,dx.
$$

**Solution.**

Choose the logarithmic factor for differentiation:

f = ln x.

Then choose:

g′ = x.

Therefore:

$$
f'
=
\frac1x,
$$

and:

$$
g
=
\frac{x^2}{2}.
$$

Integration by parts gives:

$$
\int x\ln x\,dx
=
\frac{x^2}{2}\ln x
-
\int
\frac{x^2}{2}
\frac1x
\,dx.
$$

Simplifying:

$$
\int x\ln x\,dx
=
\frac{x^2}{2}\ln x
-
\frac12\int x\,dx.
$$

Therefore:

$$
\int x\ln x\,dx
=
\frac{x^2}{2}\ln x
-
\frac{x^2}{4}
+
C.
$$

**Final Result**

$$
\frac{x^2}{2}\ln x-\frac{x^2}{4}+C
$$

---

### Exercise 8

Evaluate:

$$
\int e^x\cos x\,dx.
$$

**Solution.**

Let:

$$
I
=
\int e^x\cos x\,dx.
$$

Choose:

f = cos x

and:

g′ = eˣ.

Then:

f′ = −sin x

and:

g = eˣ.

Integration by parts gives:

$$
I
=
e^x\cos x
+
\int e^x\sin x\,dx.
$$

Now define:

$$
J
=
\int e^x\sin x\,dx.
$$

Apply integration by parts again, choosing:

f = sin x

and:

g′ = eˣ.

Then:

f′ = cos x

and:

g = eˣ.

Therefore:

$$
J
=
e^x\sin x
-
\int e^x\cos x\,dx.
$$

Since the remaining integral is I:

$$
J
=
e^x\sin x-I.
$$

Substitute this into the first equation:

$$
I
=
e^x\cos x
+
e^x\sin x
-
I.
$$

Hence:

$$
2I
=
e^x(\cos x+\sin x).
$$

Therefore:

$$
I
=
\frac12e^x(\sin x+\cos x)+C.
$$

**Final Result**

$$
\frac12e^x(\sin x+\cos x)+C
$$

---

### Exercise 9

Evaluate:

$$
\int e^x\sin x\,dx.
$$

**Solution.**

Let:

$$
I
=
\int e^x\sin x\,dx.
$$

Choose:

f = sin x

and:

g′ = eˣ.

Then:

f′ = cos x

and:

g = eˣ.

Integration by parts gives:

$$
I
=
e^x\sin x
-
\int e^x\cos x\,dx.
$$

Now apply integration by parts to the remaining integral:

$$
\int e^x\cos x\,dx.
$$

Choose:

f = cos x

and:

g′ = eˣ.

Then:

$$
\int e^x\cos x\,dx
=
e^x\cos x
+
\int e^x\sin x\,dx.
$$

The last integral is I, so:

$$
\int e^x\cos x\,dx
=
e^x\cos x+I.
$$

Substitute into the original equation:

$$
I
=
e^x\sin x
-
e^x\cos x
-
I.
$$

Therefore:

$$
2I
=
e^x(\sin x-\cos x).
$$

Hence:

$$
I
=
\frac12e^x(\sin x-\cos x)+C.
$$

**Final Result**

$$
\frac12e^x(\sin x-\cos x)+C
$$

---

### Exercise 10

Evaluate:

$$
\int x^3e^x\,dx.
$$

**Solution.**

Let:

$$
I
=
\int x^3e^x\,dx.
$$

Choose:

f = x³

and:

g′ = eˣ.

Then:

f′ = 3x²

and:

g = eˣ.

Therefore:

$$
I
=
x^3e^x
-
3\int x^2e^x\,dx.
$$

Now apply integration by parts to:

$$
\int x^2e^x\,dx.
$$

We obtain:

$$
\int x^2e^x\,dx
=
x^2e^x
-
2\int xe^x\,dx.
$$

For the remaining integral:

$$
\int xe^x\,dx
=
xe^x-e^x.
$$

Therefore:

$$
\int x^2e^x\,dx
=
x^2e^x
-
2xe^x
+
2e^x.
$$

Substitute this expression into I:

$$
I
=
x^3e^x
-
3(x^2e^x-2xe^x+2e^x)
+
C.
$$

Expanding:

$$
I
=
x^3e^x
-
3x^2e^x
+
6xe^x
-
6e^x
+
C.
$$

Factor out eˣ:

$$
I
=
(x^3-3x^2+6x-6)e^x+C.
$$

**Final Result**

$$
(x^3-3x^2+6x-6)e^x+C
$$

</div>

---

<div class="content-box">

## Explore More Topics in Calculus

- [Limits]({{ "/mathematics/calculus/limits/" | relative_url }})
- [Sequences]({{ "/mathematics/calculus/sequences/" | relative_url }})
- [Series]({{ "/mathematics/calculus/series/" | relative_url }})
- [Continuity]({{ "/mathematics/calculus/continuity/" | relative_url }})
- [Differentiability]({{ "/mathematics/calculus/differentiability/" | relative_url }})
- [Integration by Substitution]({{ "/mathematics/calculus/integration-by-substitution/" | relative_url }})
- [Ordinary Differential Equations]({{ "/mathematics/calculus/odes-general/" | relative_url }})
- [Cauchy Problems]({{ "/mathematics/calculus/odes-cauchy/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>