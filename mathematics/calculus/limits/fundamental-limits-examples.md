---
layout: default
date: 2026-08-29
original_date: 2025-04-15
title: "Notable Limits in Calculus — 10 Solved Examples"
author: "Professor Antonino De Martino and Dr. Luana Manfredini"
permalink: /mathematics/calculus/limits/fundamental-limits-examples/
redirect_from:
  - /university/solved-exercises/fundamental-limits-examples/
  - /university/math/calculus-1/notable-limits/
background_image: "/images/exercises.png"
description: "Notable and remarkable limits in calculus: key formulas and 10 solved examples using logarithms, exponentials, substitutions, and the Squeeze Theorem."
featured: true
area: mathematics
topic: calculus
subtopic: limits
level: university
content_type: solved-exercises
---

**Prepared by Professor Antonino De Martino (Polytechnic University of Milan) and Dr. Luana Manfredini.**

<div class="content-box">

# Notable Limits in Calculus: 10 Solved Examples

## Notable and Remarkable Limits in Calculus

### Fundamental Limit Formulas

The expressions below are commonly known as fundamental, notable, or remarkable limits in calculus:

$$
\lim_{x\to 0} \frac{\sin x}{x} = 1,
\quad
\lim_{x\to \infty} \frac{\sin x}{x} = 0,
\quad
\lim_{x\to 0} \frac{\log(1+x)}{x} = 1,
$$

$$
\lim_{x\to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2},
\quad
\lim_{x\to \pm\infty} \left(1 + \frac{1}{x}\right)^x = e,
\quad
\lim_{x\to 0} (1+x)^{1/x} = e,
$$

$$
\lim_{x\to 0} \frac{e^x - 1}{x} = 1,
\quad
\lim_{x\to 0} \frac{\tan x}{x} = 1,
\quad
\lim_{x\to 0} \frac{\arcsin x}{x} = 1,
\quad
\lim_{x\to 0} \frac{\arctan x}{x} = 1.
$$

</div>

<div class="content-box">

### Key Theorems

#### Theorem: Non-Existence via Sequences

If there exist two sequences aₙ → c and bₙ → c such that:

$$
\lim_{n \to \infty} f(a_n) \ne \lim_{n \to \infty} f(b_n),
$$

then

$$
\lim_{x \to c} f(x)
$$

does not exist.

#### Theorem: Squeeze Theorem

If f(x) ≤ g(x) ≤ h(x) near x = c, and:

$$
\lim_{x \to c} f(x) = \lim_{x \to c} h(x) = L,
$$

then:

$$
\lim_{x \to c} g(x) = L.
$$

</div>

<div class="content-box">

## 10 Examples Using Notable Limits

### Example 1

$$
\lim_{x \to +\infty} \left( \sqrt{x^2 + x + 1} - \sqrt{x^2 - x + 1} \right)
$$

### Example 2

$$
\lim_{x \to \infty} x \log\left(\frac{x + 4}{x + 5}\right)
$$

### Example 3

$$
\lim_{x \to \infty} \left(\frac{2x+9}{2x+1}\right)^x
$$

### Example 4

$$
\lim_{x \to \infty} x \log\left(\frac{x^2 + 1}{x^2 + x}\right)
$$

### Example 5

$$
\lim_{x \to \infty} \frac{\log(x^3 + 1)}{x}
$$

### Example 6

$$
\lim_{x \to \infty} \frac{\sin x - x}{\cos x + \sqrt{1 + x^2}}
$$

### Example 7

$$
\lim_{x \to \infty} \sin x \cdot \left[ \log(\sqrt{x} + 1) - \log(\sqrt{x + 1}) \right]
$$

### Example 8

$$
\lim_{x \to \infty} \left(\frac{x + 3}{x - 1}\right)^{x + 1}
$$

### Example 9

$$
\lim_{x \to 0^+} x^{1/\log(3x)}
$$

### Example 10

$$
\lim_{x \to 0} \frac{e^x - e^{-x}}{x}
$$

</div>

<div class="content-box">

## Step-by-Step Solutions

<div class="content-box exercise-box" markdown="1">

### Exercise 1

$$
\lim_{x \to +\infty} \left( \sqrt{x^2 + x + 1} - \sqrt{x^2 - x + 1} \right)
$$

**Solution.**

We multiply and divide by the conjugate expression:

$$
\begin{aligned}
\lim_{x \to +\infty} 
&\left( \sqrt{x^2 + x + 1} - \sqrt{x^2 - x + 1} \right) \\
&= \lim_{x \to +\infty} 
\frac{(x^2 + x + 1) - (x^2 - x + 1)}
{\sqrt{x^2 + x + 1} + \sqrt{x^2 - x + 1}} \\
&= \lim_{x \to +\infty} 
\frac{2x}
{\sqrt{x^2 + x + 1} + \sqrt{x^2 - x + 1}} \\
&= \lim_{x \to +\infty} 
\frac{2x}
{x \left(
\sqrt{1 + \frac{1}{x} + \frac{1}{x^2}}
+
\sqrt{1 - \frac{1}{x} + \frac{1}{x^2}}
\right)} \\
&= \frac{2}{1+1}.
\end{aligned}
$$

**Final result**

$$
1
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 2

$$
\lim_{x \to \infty} x \cdot \log\left( \frac{x + 4}{x + 5} \right)
$$

**Solution.**

We rewrite the logarithmic expression:

$$
\lim_{x \to \infty}
x \cdot \log\left( 1 - \frac{1}{x + 5} \right).
$$

Let:

$$
t = -\frac{1}{x+5}.
$$

Then:

$$
x = \frac{-1-5t}{t}.
$$

Therefore:

$$
\lim_{t \to 0}
\frac{-1-5t}{t}\log(1+t).
$$

Using the fundamental limit:

$$
\lim_{t\to0}\frac{\log(1+t)}{t}=1,
$$

we obtain:

$$
\lim_{t \to 0}
(-1-5t)\frac{\log(1+t)}{t}
=
-1.
$$

**Final result**

$$
-1
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 3

$$
\lim_{x \to +\infty}
\left( \frac{2x + 9}{2x + 1} \right)^x
$$

**Solution.**

We write:

$$
\left( \frac{2x + 9}{2x + 1} \right)^x
=
\left( 1 + \frac{8}{2x + 1} \right)^x.
$$

Let:

$$
t = \frac{8}{2x+1}.
$$

Then:

$$
x = \frac{4}{t}-\frac{1}{2}.
$$

Therefore:

$$
(1+t)^{\frac{4}{t}-\frac{1}{2}}
=
\frac{(1+t)^{4/t}}{(1+t)^{1/2}}.
$$

Using:

$$
\lim_{t\to0}(1+t)^{1/t}=e,
$$

we obtain:

$$
\frac{e^4}{1}=e^4.
$$

**Final result**

$$
e^4
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 4

$$
\lim_{x \to +\infty}
x \cdot \log\left( \frac{x^2 + 1}{x^2 + x} \right)
$$

**Solution.**

We simplify the ratio:

$$
\frac{x^2 + 1}{x^2 + x}
=
\frac{1 + \frac{1}{x^2}}
{1 + \frac{1}{x}}.
$$

Let:

$$
t = \frac{1}{x}.
$$

Then:

$$
x = \frac{1}{t}.
$$

Therefore:

$$
\lim_{t \to 0}
\frac{1}{t}
\log\left(
\frac{1+t^2}{1+t}
\right).
$$

Using the logarithm of a quotient:

$$
\lim_{t \to 0}
\left(
\frac{\log(1+t^2)}{t}
-
\frac{\log(1+t)}{t}
\right).
$$

For the first term:

$$
\frac{\log(1+t^2)}{t}
=
t\frac{\log(1+t^2)}{t^2}
\to 0.
$$

For the second:

$$
\frac{\log(1+t)}{t}\to1.
$$

Hence:

$$
0-1=-1.
$$

**Final result**

$$
-1
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 5

$$
\lim_{x \to +\infty}
\frac{\log(x^3 + 1)}{x}
$$

**Solution.**

We use the identity:

$$
\log(x^3 + 1)
=
\log\left(
x^3
\left(
1 + \frac{1}{x^3}
\right)
\right).
$$

Therefore:

$$
\log(x^3+1)
=
3\log x
+
\log\left(
1+\frac{1}{x^3}
\right).
$$

Hence:

$$
\frac{\log(x^3+1)}{x}
=
\frac{3\log x}{x}
+
\frac{
\log\left(1+\frac{1}{x^3}\right)
}{x}.
$$

Both terms tend to zero:

$$
\frac{3\log x}{x}\to0,
$$

and

$$
\frac{
\log\left(1+\frac{1}{x^3}\right)
}{x}\to0.
$$

**Final result**

$$
0
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 6

$$
\lim_{x \to +\infty}
\frac{\sin x - x}
{\cos x + \sqrt{1 + x^2}}
$$

**Solution.**

We divide numerator and denominator by x:

$$
\frac{
\frac{\sin x}{x}-1
}{
\frac{\cos x}{x}
+
\sqrt{1+\frac{1}{x^2}}
}.
$$

As x → +∞:

$$
\frac{\sin x}{x}\to0,
\qquad
\frac{\cos x}{x}\to0,
$$

and:

$$
\sqrt{1+\frac{1}{x^2}}\to1.
$$

Therefore:

$$
\frac{0-1}{0+1}=-1.
$$

**Final result**

$$
-1
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 7

$$
\lim_{x \to +\infty}
\sin x
\left[
\log(\sqrt{x}+1)
-
\log(\sqrt{x+1})
\right]
$$

**Solution.**

We use the logarithm of a quotient:

$$
\log(\sqrt{x}+1)
-
\log(\sqrt{x+1})
=
\log\left(
\frac{\sqrt{x}+1}{\sqrt{x+1}}
\right).
$$

Now:

$$
\frac{\sqrt{x}+1}{\sqrt{x+1}}
=
\frac{
\sqrt{x}
\left(
1+\frac{1}{\sqrt{x}}
\right)
}{
\sqrt{x}
\sqrt{
1+\frac{1}{x}
}
}.
$$

Thus:

$$
\frac{\sqrt{x}+1}{\sqrt{x+1}}
=
\frac{
1+\frac{1}{\sqrt{x}}
}{
\sqrt{
1+\frac{1}{x}
}
}.
$$

As x → +∞, the ratio tends to 1, so:

$$
\log\left(
\frac{\sqrt{x}+1}{\sqrt{x+1}}
\right)
\to0.
$$

Since sin x is bounded, the product tends to zero.

**Final result**

$$
0
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 8

$$
\lim_{x \to +\infty}
\left(
\frac{x+3}{x-1}
\right)^{x+1}
$$

**Solution.**

We rewrite:

$$
\frac{x+3}{x-1}
=
1+\frac{4}{x-1}.
$$

Therefore:

$$
\left(
1+\frac{4}{x-1}
\right)^{x+1}.
$$

Let:

$$
y=\frac{4}{x-1}.
$$

Then:

$$
x=1+\frac{4}{y},
$$

and hence:

$$
x+1=2+\frac{4}{y}.
$$

Therefore:

$$
(1+y)^{2+\frac{4}{y}}
=
(1+y)^2
\left(
(1+y)^{1/y}
\right)^4.
$$

As y → 0:

$$
(1+y)^2\to1,
$$

while:

$$
(1+y)^{1/y}\to e.
$$

Hence:

$$
1\cdot e^4=e^4.
$$

**Final result**

$$
e^4
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 9

$$
\lim_{x \to 0^+}
x^{\frac{1}{\log(3x)}}
$$

**Solution.**

Let:

$$
y=\frac{1}{\log(3x)}.
$$

As x → 0⁺, we have:

$$
\log(3x)\to-\infty,
$$

so:

$$
y\to0^-.
$$

From the definition of y:

$$
\log(3x)=\frac{1}{y}.
$$

Therefore:

$$
3x=e^{1/y},
$$

and:

$$
x=\frac{e^{1/y}}{3}.
$$

The original expression becomes:

$$
x^y
=
\left(
\frac{e^{1/y}}{3}
\right)^y.
$$

Hence:

$$
x^y
=
\frac{
e^{(1/y)y}
}{
3^y
}.
$$

Therefore:

$$
x^y
=
\frac{e}{3^y}.
$$

As y → 0⁻:

$$
3^y\to1.
$$

Thus:

$$
\frac{e}{3^y}\to e.
$$

**Final result**

$$
e
$$


</div>

<div class="content-box exercise-box" markdown="1">

### Exercise 10

$$
\lim_{x \to 0}
\frac{e^x-e^{-x}}{x}
$$

**Solution.**

We split the expression:

$$
\frac{e^x-e^{-x}}{x}
=
\frac{e^x-1}{x}
+
\frac{1-e^{-x}}{x}.
$$

The second term can be rewritten as:

$$
\frac{1-e^{-x}}{x}
=
\frac{e^{-x}-1}{-x}.
$$

Therefore:

$$
\frac{e^x-e^{-x}}{x}
=
\frac{e^x-1}{x}
+
\frac{e^{-x}-1}{-x}.
$$

Using the fundamental limits:

$$
\lim_{x \to 0}
\frac{e^x-1}{x}
=
1,
$$

and:

$$
\lim_{x \to 0}
\frac{e^{-x}-1}{-x}
=
1,
$$

we obtain:

$$
1+1=2.
$$

**Final result**

$$
2
$$


</div>

</div>

<div class="content-box">

## Continue Exploring Limits

These examples show how algebraic transformations, fundamental limits, logarithms, exponentials, bounded functions, and substitutions can be combined to evaluate apparently different limiting forms.

[**Explore all Limits resources →**]({{ "/mathematics/calculus/limits/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>