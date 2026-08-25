---
layout: default
date: 2026-08-24
original_date: 2025-08-29
title: "Solved Exercises — Integration by Substitution"
permalink: /mathematics/calculus/integration-by-substitution/
redirect_from:
  - /university/math/calculus-1/integration-by-substitution/
background_image: "/images/integrali.png"
description: "Solved integration by substitution exercises with step-by-step changes of variables, including logarithmic, trigonometric, and hyperbolic substitutions."
area: mathematics
topic: calculus
subtopic: integration-by-substitution
level: university
content_type: solved-exercises
---

<div class="content-box">

# Integration by Substitution — Theory and Solved Exercises

## Theoretical Recall

Integration by substitution is the integral counterpart of the chain rule.

Suppose that:

$$
x=g(t)
$$

is a differentiable change of variable. Then:

$$
dx=g'(t)\,dt.
$$

Therefore:

$$
\int f(x)\,dx
=
\int f(g(t))g'(t)\,dt.
$$

Another common form begins with:

$$
u=g(x).
$$

Then:

$$
du=g'(x)\,dx.
$$

Whenever an integral contains a composition together with the derivative of the inner function, we can use:

$$
\int f(g(x))g'(x)\,dx
=
\int f(u)\,du.
$$

After evaluating the new integral, the original variable must be restored.

### Common Strategies

A useful substitution often reveals a simpler structure hidden inside the original integrand.

Typical choices include:

- a linear expression raised to a power;
- the argument of a logarithm;
- the denominator of a rational expression;
- the expression inside a radical;
- trigonometric substitutions for quadratic radicals;
- hyperbolic substitutions for expressions involving sums or differences of squares.

For radicals of the form:

$$
\sqrt{1-x^2},
$$

the substitution:

$$
x=\sin t
$$

is often useful because:

$$
1-\sin^2t=\cos^2t.
$$

For expressions involving:

$$
1+x^2,
$$

the substitution:

$$
x=\tan t
$$

can be useful because:

$$
1+\tan^2t=\sec^2t.
$$

Hyperbolic substitutions can similarly exploit:

$$
\cosh^2t-\sinh^2t=1.
$$

**Author’s note:** Always transform both the integrand and the differential consistently. A substitution is not complete until every occurrence of the original variable has been removed from the transformed integral.

</div>

---

<div class="content-box">

## Exercises

### Exercise 1 — Linear Substitution

Evaluate:

$$
\int(2x+1)^5\,dx.
$$

**Solution.**

Set:

$$
u=2x+1.
$$

Then:

$$
du=2\,dx.
$$

Therefore:

$$
dx=\frac12\,du.
$$

Substituting:

$$
\int(2x+1)^5\,dx
=
\frac12\int u^5\,du.
$$

Integrating:

$$
\frac12\int u^5\,du
=
\frac12\frac{u^6}{6}+C.
$$

Thus:

$$
\frac{u^6}{12}+C.
$$

Returning to x:

$$
\frac{(2x+1)^6}{12}+C.
$$

**Final Result**

$$
\frac{(2x+1)^6}{12}+C
$$

---

### Exercise 2 — Logarithmic Substitution

Evaluate, for x > 1:

$$
\int\frac{1}{x\log x}\,dx.
$$

**Solution.**

Set:

$$
u=\log x.
$$

Then:

$$
du=\frac1x\,dx.
$$

The integral becomes:

$$
\int\frac1u\,du.
$$

Therefore:

$$
\int\frac1u\,du
=
\log|u|+C.
$$

Since x > 1:

$$
\log x>0.
$$

Thus the absolute value can be omitted:

$$
\log(\log x)+C.
$$

**Final Result**

$$
\log(\log x)+C
$$

---

### Exercise 3 — Substitution in a Rational Expression

Evaluate:

$$
\int\frac{x}{1+x^2}\,dx.
$$

**Solution.**

Set:

$$
u=1+x^2.
$$

Then:

$$
du=2x\,dx.
$$

Therefore:

$$
x\,dx=\frac12\,du.
$$

The integral becomes:

$$
\frac12\int\frac1u\,du.
$$

Hence:

$$
\frac12\log|u|+C.
$$

Since:

$$
1+x^2>0
$$

for every real x, we obtain:

$$
\frac12\log(1+x^2)+C.
$$

**Final Result**

$$
\frac12\log(1+x^2)+C
$$

---

### Exercise 4 — Trigonometric Substitution

Evaluate:

$$
\int\frac{1}{\sqrt{1-x^2}}\,dx.
$$

**Solution.**

Use the substitution:

$$
x=\sin t.
$$

Then:

$$
dx=\cos t\,dt.
$$

Moreover:

$$
\sqrt{1-x^2}
=
\sqrt{1-\sin^2t}.
$$

Using:

$$
1-\sin^2t=\cos^2t,
$$

and choosing t in the standard range of arcsin, we have:

$$
\sqrt{1-\sin^2t}
=
\cos t.
$$

Therefore:

$$
\int
\frac{\cos t}{\cos t}
\,dt
=
\int1\,dt.
$$

Thus:

$$
t+C.
$$

Since:

$$
t=\arcsin x,
$$

we obtain:

$$
\arcsin x+C.
$$

**Final Result**

$$
\arcsin x+C
$$

---

### Exercise 5 — Tangent Substitution

Evaluate:

$$
\int\frac{1}{1+x^2}\,dx.
$$

**Solution.**

Set:

$$
x=\tan t.
$$

Then:

$$
dx=\sec^2t\,dt.
$$

Using the identity:

$$
1+\tan^2t=\sec^2t,
$$

the integral becomes:

$$
\int
\frac{\sec^2t}{\sec^2t}
\,dt.
$$

Therefore:

$$
\int1\,dt=t+C.
$$

Since:

$$
t=\arctan x,
$$

we obtain:

$$
\arctan x+C.
$$

**Final Result**

$$
\arctan x+C
$$

---

### Exercise 6 — Radical of a Sum of Squares

Evaluate:

$$
\int\frac{1}{\sqrt{x^2+4}}\,dx.
$$

**Solution.**

Set:

$$
x=2\tan t.
$$

Then:

$$
dx=2\sec^2t\,dt.
$$

The radical becomes:

$$
\sqrt{x^2+4}
=
\sqrt{4\tan^2t+4}.
$$

Factor out 4:

$$
\sqrt{x^2+4}
=
2\sqrt{1+\tan^2t}.
$$

Using:

$$
1+\tan^2t=\sec^2t,
$$

we obtain:

$$
\sqrt{x^2+4}=2\sec t.
$$

Therefore:

$$
\int
\frac{2\sec^2t}{2\sec t}
\,dt
=
\int\sec t\,dt.
$$

Recall that:

$$
\int\sec t\,dt
=
\log|\sec t+\tan t|+C.
$$

From:

$$
\tan t=\frac{x}{2},
$$

we have:

$$
\sec t
=
\sqrt{1+\tan^2t}
=
\frac{\sqrt{x^2+4}}{2}.
$$

Therefore:

$$
\log\left|
\frac{\sqrt{x^2+4}+x}{2}
\right|
+C.
$$

The constant factor 1/2 inside the logarithm contributes only an additive constant, which can be absorbed into C.

Hence the standard form is:

$$
\log\left|x+\sqrt{x^2+4}\right|+C.
$$

**Final Result**

$$
\log\left|x+\sqrt{x^2+4}\right|+C
$$

---

### Exercise 7 — Exponential Substitution

Evaluate:

$$
\int\frac{e^x}{1+e^{2x}}\,dx.
$$

**Solution.**

Set:

$$
u=e^x.
$$

Then:

$$
du=e^x\,dx.
$$

Moreover:

$$
e^{2x}=u^2.
$$

Therefore the integral becomes:

$$
\int\frac{1}{1+u^2}\,du.
$$

Using the standard antiderivative:

$$
\int\frac{1}{1+u^2}\,du
=
\arctan u+C,
$$

we obtain:

$$
\arctan u+C.
$$

Returning to x:

$$
\arctan(e^x)+C.
$$

**Final Result**

$$
\arctan(e^x)+C
$$

---

### Exercise 8 — Hyperbolic Substitution

Evaluate, for x > 1:

$$
\int\frac{1}{\sqrt{x^2-1}}\,dx.
$$

**Solution.**

Set:

$$
x=\cosh t.
$$

Then:

$$
dx=\sinh t\,dt.
$$

Using the hyperbolic identity:

$$
\cosh^2t-\sinh^2t=1,
$$

we obtain:

$$
x^2-1
=
\cosh^2t-1
=
\sinh^2t.
$$

For the relevant values of t:

$$
\sqrt{x^2-1}
=
\sinh t.
$$

Therefore:

$$
\int
\frac{\sinh t}{\sinh t}
\,dt
=
\int1\,dt.
$$

Thus:

$$
t+C.
$$

Since:

$$
x=\cosh t,
$$

we have:

$$
t=\operatorname{arcosh}(x).
$$

The inverse hyperbolic cosine satisfies:

$$
\operatorname{arcosh}(x)
=
\log\left(x+\sqrt{x^2-1}\right).
$$

Therefore:

$$
\log\left(x+\sqrt{x^2-1}\right)+C.
$$

**Final Result**

$$
\log\left(x+\sqrt{x^2-1}\right)+C
$$

---

### Exercise 9 — Hyperbolic Substitution with a Radical

Evaluate:

$$
\int\sqrt{1+x^2}\,dx.
$$

**Solution.**

Set:

$$
x=\sinh t.
$$

Then:

$$
dx=\cosh t\,dt.
$$

Using:

$$
1+\sinh^2t=\cosh^2t,
$$

we obtain:

$$
\sqrt{1+x^2}
=
\cosh t.
$$

Therefore:

$$
\int\sqrt{1+x^2}\,dx
=
\int\cosh^2t\,dt.
$$

Use the identity:

$$
\cosh^2t
=
\frac{1+\cosh(2t)}{2}.
$$

Hence:

$$
\int\cosh^2t\,dt
=
\frac12\int1\,dt
+
\frac12\int\cosh(2t)\,dt.
$$

Therefore:

$$
\int\cosh^2t\,dt
=
\frac{t}{2}
+
\frac{\sinh(2t)}{4}
+
C.
$$

Using:

$$
\sinh(2t)=2\sinh t\cosh t,
$$

we obtain:

$$
\frac{t}{2}
+
\frac12\sinh t\cosh t
+
C.
$$

Now:

$$
\sinh t=x,
$$

and:

$$
\cosh t=\sqrt{1+x^2}.
$$

Moreover:

$$
t=\operatorname{arsinh}(x).
$$

Thus:

$$
\frac12x\sqrt{1+x^2}
+
\frac12\operatorname{arsinh}(x)
+
C.
$$

Equivalently:

$$
\operatorname{arsinh}(x)
=
\log\left(x+\sqrt{1+x^2}\right).
$$

**Final Result**

$$
\frac12
\left(
x\sqrt{1+x^2}
+
\operatorname{arsinh}(x)
\right)
+C
$$

---

### Exercise 10 — Secant Substitution

Evaluate, for x > 1:

$$
\int\frac{1}{x\sqrt{x^2-1}}\,dx.
$$

**Solution.**

Set:

$$
x=\sec t.
$$

Then:

$$
dx=\sec t\tan t\,dt.
$$

Moreover:

$$
x^2-1
=
\sec^2t-1.
$$

Using:

$$
\sec^2t-1=\tan^2t,
$$

we obtain:

$$
\sqrt{x^2-1}
=
\tan t
$$

in the relevant range.

The integral becomes:

$$
\int
\frac{\sec t\tan t}
{\sec t\tan t}
\,dt.
$$

Therefore:

$$
\int1\,dt=t+C.
$$

Since:

$$
x=\sec t,
$$

we have:

$$
t=\operatorname{arcsec}(x).
$$

Thus:

$$
\operatorname{arcsec}(x)+C.
$$

For x > 1, this can also be written as:

$$
\arccos\left(\frac1x\right)+C.
$$

**Final Result**

$$
\operatorname{arcsec}(x)+C
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
- [Integration by Parts]({{ "/mathematics/calculus/integration-by-parts/" | relative_url }})
- [Ordinary Differential Equations]({{ "/mathematics/calculus/odes-general/" | relative_url }})
- [Cauchy Problems]({{ "/mathematics/calculus/odes-cauchy/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>