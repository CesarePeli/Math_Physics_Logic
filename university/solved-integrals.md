---
title: "Worked Examples with Integrals"
meta-description: "A curated collection of solved integrals, with theoretical summaries and detailed step-by-step reasoning. Ideal for students in calculus courses."
permalink: "/university/solved-exercises/solved-integrals/"
background_image: "/images/exercises.png"
---

**Prepared by Professor Antonino De Martino (Polytechnic University of Milan) and Dr. Luana Manfredini.**

<div class="content-box">

## Basic Integral Formulas

### Indefinite Integrals

$$ \int k \, dx = kx + c $$
$$ \int x^\alpha \, dx = \frac{x^{\alpha +1}}{\alpha +1} + c $$
$$ \int \frac{1}{x} \, dx = \log |x| + c $$
$$ \int a^{kx} \, dx = \frac{a^{kx}}{k \log a} + c $$
$$ \int (f(x))^\alpha f'(x) \, dx =
\frac{(f(x))^{\alpha +1}}{\alpha +1} + c $$
$$ \int \frac{f'(x)}{f(x)} \, dx = \log|f(x)| + c $$
$$ \int a^{f(x)} f'(x) \, dx =
\frac{a^{f(x)}}{\log a} + c $$

### Trigonometric and Hyperbolic Functions

$$ \int \cos x \, dx = \sin x + c $$
$$ \int \sin x \, dx = -\cos x + c $
$$ \int f'(x) \cos f(x) \, dx = \sin f(x) + c $$
$$ \int f'(x) \sin f(x) \, dx = -\cos f(x) + c $$
$$ \int \frac{1}{\cos^2 x} \, dx = \tan x + c $$
$$ \int \frac{1}{\sin^2 x} \, dx = -\cot x + c $$
$$ \int \frac{1}{\sqrt{1 - x^2}} \, dx = \arcsin x + c $$
$$ \int \frac{1}{1 + x^2} \, dx = \arctan x + c $$
$$ \int \frac{f'(x)}{1 + f(x)^2} \, dx = \arctan f(x) + c $$
$$ \int \cosh x \, dx = \sinh x + c $$
$$ \int \sinh x \, dx = \cosh x + c $$

### Useful Trig Identities

$$ \cos^2 x = \frac{1 + \cos(2x)}{2} $$
$$ \sin^2 x = \frac{1 - \cos(2x)}{2} $$

### Integration Techniques

**Integration by parts:**

$$ \int f(x) g'(x) \, dx =
f(x)g(x) - \int f'(x) g(x) \, dx $$

**Substitution rule:**

$$ \int f(x) \, dx =
\int f(g(t)) g'(t) \, dt \quad \text{with } x = g(t) $$

### Notable Improper Integrals

1. If \( \alpha > 0 \):

$$
\int_0^\alpha \frac{1}{x^p} \, dx =
\begin{cases}
\text{converges if } p < 1 \\\\
\text{diverges if } p \geq 1
\end{cases}
$$

2. If \( \alpha > 0 \):

$$
\int_\alpha^{+\infty} \frac{1}{x^p} \, dx =
\begin{cases}
\text{converges if } p > 1 \\\\
\text{diverges if } p \leq 1
\end{cases}
$$

3. If \( \alpha > 1 \):

$$
\int_1^\alpha \frac{1}{(\log x)^p} \, dx =
\begin{cases}
\text{converges if } p < 1 \\\\
\text{diverges if } p \geq 1
\end{cases}
$$

</div>

<div class="content-box">

### Exercises

#### Exercise 1

Evaluate the integral:

$$
\int_{\frac{1}{e}}^e \frac{\log(|\log x|)}{x} \, dx
$$

#### Exercise 2

Evaluate the integral:

$$
\int \frac{1}{\sin^2 x \cos^2 x} \, dx
$$

#### Exercise 3

Evaluate the definite integral:

$$
\int_{-1}^{1} \sqrt{1 - x^2} \, dx
$$

#### Exercise 4

Evaluate the definite integral:

$$
\int_{-1}^{1} \frac{1}{\sqrt{4 - x^2}} \, dx
$$

#### Exercise 5

Evaluate the indefinite integral:

$$
\int \frac{x^2}{x^2 + 2} \, dx
$$

#### Exercise 6

Evaluate the indefinite integral:

$$
\int \frac{1}{\sin x} \, dx
$$

#### Exercise 7

Evaluate the definite integral:

$$
\int_{-2}^{2} \sqrt{4 - x^2} \, dx
$$

#### Exercise 8

Evaluate the indefinite integral:

$$
\int \sin x \, e^x \, dx
$$

#### Exercise 9

Evaluate the definite integral:

$$
\int_0^1 e^{2x} \log(1 + e^x) \, dx
$$

#### Exercise 10

Evaluate the indefinite integral:

$$
\int_0^1 e^{2x} \log(1 + e^x) \, dx
$$
</div>

<div class="content-box">

### Exercise 1

Evaluate the integral:

$$
\int_{\frac{1}{e}}^e \frac{\log(|\log x|)}{x} \, dx
$$

**Solution:**

We split the integral at the point where the argument of the logarithm changes sign:

$$
\int_{\frac{1}{e}}^e \frac{\log(|\log x|)}{x} \, dx =
\int_{\frac{1}{e}}^1 \frac{\log(-\log x)}{x} \, dx +
\int_1^e \frac{\log(\log x)}{x} \, dx
$$

In the first part, let

$$
t = -\log x, \quad dt = -\frac{dx}{x}
$$

Then:

$$
\int_{\frac{1}{e}}^1 \frac{\log(-\log x)}{x} \, dx =
- \int_1^0 \log t \, dt = \int_0^1 \log t \, dt
$$

For the second part, let

$$
t = \log x, \quad dt = \frac{dx}{x}
$$

So:

$$
\int_1^e \frac{\log(\log x)}{x} \, dx = \int_0^1 \log t \, dt
$$

Therefore:

$$
\int_{\frac{1}{e}}^e \frac{\log(|\log x|)}{x} \, dx =
2 \int_0^1 \log t \, dt
$$

Using integration by parts:

$$
\int_0^1 \log t \, dt = \lim_{a \to 0^+} \left( t \log t - t \right)\bigg|_a^1 =
\lim_{a \to 0^+} \left( -1 - a \log a + a \right) = -1
$$

Thus:

$$
\int_{\frac{1}{e}}^e \frac{\log(|\log x|)}{x} \, dx = -2
$$

---

### Exercise 2

Evaluate the integral:

$$
\int \frac{1}{\sin^2 x \cos^2 x} \, dx
$$

**Solution:**

We use the identity:

$$
\sin^2 x + \cos^2 x = 1
$$

Then:

$$
\frac{1}{\sin^2 x \cos^2 x} =
\frac{\sin^2 x + \cos^2 x}{\sin^2 x \cos^2 x} =
\frac{1}{\cos^2 x} + \frac{1}{\sin^2 x}
$$

So:

$$
\int \frac{1}{\sin^2 x \cos^2 x} \, dx =
\int \frac{1}{\cos^2 x} \, dx + \int \frac{1}{\sin^2 x} \, dx =
\tan x - \cot x + c
$$

---

### Exercise 3

Evaluate the definite integral:

$$
\int_{-1}^{1} \sqrt{1 - x^2} \, dx
$$

**Solution:**

Let

$$
x = \sin t, \quad dx = \cos t \, dt
$$

Then:

$$
\int_{-1}^{1} \sqrt{1 - x^2} \, dx =
\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \cos^2 t \, dt
$$

Use the identity:

$$
\cos^2 t = \frac{1 + \cos(2t)}{2}
$$

So:

$$
\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \frac{1 + \cos(2t)}{2} \, dt =
\left( \frac{t}{2} + \frac{\sin(2t)}{4} \right)\bigg|_{-\frac{\pi}{2}}^{\frac{\pi}{2}} =
\frac{\pi}{2}
$$

---

### Exercise 4

Evaluate the definite integral:

$$
\int_{-1}^{1} \frac{1}{\sqrt{4 - x^2}} \, dx
$$

**Solution:**

We write:

$$
\int_{-1}^{1} \frac{1}{\sqrt{4 - x^2}} \, dx =
\int_{-1}^{1} \frac{1}{2 \sqrt{1 - \left( \frac{x}{2} \right)^2}} \, dx
$$

Let

$$
t = \frac{x}{2}
$$

Then:

$$
\int_{-1}^{1} \frac{1}{\sqrt{4 - x^2}} \, dx =
2 \int_0^{\frac{1}{2}} \frac{1}{\sqrt{1 - t^2}} \, dt =
2 \arcsin t \bigg|_0^{\frac{1}{2}} = \frac{\pi}{3}
$$

---

### Exercise 5

Evaluate the indefinite integral:

$$
\int \frac{x^2}{x^2 + 2} \, dx
$$

**Solution:**

We rewrite the numerator:

$$
\int \frac{x^2 + 2 - 2}{x^2 + 2} \, dx =
\int 1 \, dx - \int \frac{2}{x^2 + 2} \, dx
$$

Now:

$$
\int \frac{2}{x^2 + 2} \, dx =
\int \frac{1}{\left( \frac{x}{\sqrt{2}} \right)^2 + 1} \, dx
$$

Let

$$
t = \frac{x}{\sqrt{2}}, \quad dt = \frac{dx}{\sqrt{2}}
$$

Then:

$$
\sqrt{2} \int \frac{1}{1 + t^2} \, dt = \sqrt{2} \arctan t + c
$$

So the result is:

$$
x - \sqrt{2} \arctan\left( \frac{x}{\sqrt{2}} \right) + c
$$

---

### Exercise 6

Evaluate the indefinite integral:

$$
\int \frac{1}{\sin x} \, dx
$$

**Solution:**

Using the identity:

$$
\int \frac{1}{\sin x} \, dx = \log \left| \tan \frac{x}{2} \right| + c
$$

---

### Exercise 7

Evaluate the definite integral:

$$
\int_{-2}^{2} \sqrt{4 - x^2} \, dx
$$

**Solution:**

By symmetry:

$$
\int_{-2}^{2} \sqrt{4 - x^2} \, dx = 2 \int_0^2 \sqrt{4 - x^2} \, dx
$$

Let

$$
x = 2 \sin t, \quad dx = 2 \cos t \, dt
$$

Then:

$$
8 \int_0^{\frac{\pi}{2}} \cos^2 t \, dt =
8 \left( \frac{t}{2} + \frac{\sin(2t)}{4} \right) \bigg|_0^{\frac{\pi}{2}} =
2\pi
$$

---

### Exercise 8

Evaluate the indefinite integral:

$$
\int \sin x \, e^x \, dx
$$

**Solution:**

Integration by parts twice:

Let

$$
I = \int \sin x \, e^x \, dx
$$

Then:

$$
I = \sin x \, e^x - \int e^x \cos x \, dx
$$

and

$$
\int e^x \cos x \, dx = e^x \cos x + I
$$

So:

$$
2I = e^x (\sin x - \cos x)
$$

and therefore:

$$
\int \sin x \, e^x \, dx = \frac{e^x (\sin x - \cos x)}{2} + c
$$

---

### Exercise 9

Evaluate the definite integral:

$$
\int_0^1 e^{2x} \log(1 + e^x) \, dx
$$

**Solution:**

Let

$$
t = e^x, \quad dx = \frac{dt}{t}
$$

Then the bounds become \( t \in [1, e] \), and the integral becomes:

$$
\int_1^e t \log(1 + t) \, dt
$$

Apply integration by parts:

$$
\int_1^e t \log(1 + t) \, dt =
\frac{t^2}{2} \log(1 + t) \bigg|_1^e -
\frac{1}{2} \int_1^e \frac{t^2}{1 + t} \, dt
$$

We divide:

$$
\frac{t^2}{1 + t} = t - 1 + \frac{1}{1 + t}
$$

So:

$$
\int_1^e \frac{t^2}{1 + t} \, dt =
\int_1^e \left( t - 1 + \frac{1}{1 + t} \right) \, dt =
\left( \frac{t^2}{2} - t + \log(1 + t) \right) \bigg|_1^e
$$

Final result:

$$
\frac{e^2}{2} \log(1 + e) - \frac{e^2}{4} + \frac{e}{2}
- \frac{1}{4} - \frac{\log(1 + e)}{2}
$$

### Exercise 10

Evaluate the definite integral:

$$
\int_0^1 e^{2x} \log(1 + e^x) \, dx
$$

**Solution:**

Let

$$
t = e^x, \quad dx = \frac{dt}{t}
$$

Bounds: when \( x = 0 \), \( t = 1 \); when \( x = 1 \), \( t = e \)

The integral becomes:

$$
\int_1^e t \log(1 + t) \, dt
$$

Use integration by parts:

$$
\int_1^e t \log(1 + t) \, dt =
\frac{t^2}{2} \log(1 + t) \bigg|_1^e -
\frac{1}{2} \int_1^e \frac{t^2}{1 + t} \, dt
$$

Divide the integrand:

$$
\frac{t^2}{1 + t} = t - 1 + \frac{1}{1 + t}
$$

Then:

$$
\int_1^e \frac{t^2}{1 + t} \, dt =
\left( \frac{t^2}{2} - t + \log(1 + t) \right) \bigg|_1^e
$$

Putting it all together:

$$
\int_0^1 e^{2x} \log(1 + e^x) \, dx =
\frac{e^2}{2} \log(1 + e)
- \frac{e^2}{4}
+ \frac{e}{2}
- \frac{1}{4}
- \frac{\log(1 + e)}{2}
$$

</div>
