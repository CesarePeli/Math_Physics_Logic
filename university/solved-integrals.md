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
$$ \int \sin x \, dx = -\cos x + c $$
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
\int \frac{e^x - e^{-x}}{x} \, dx
$$
</div>

<div class="content-box">

## Solutions

### Exercise 1

Evaluate the integral:

$$
\int_{\frac{1}{e}}^e \frac{\log(|\log x|)}{x} \, dx
$$

**Solution:**

We split the integral at \( x = 1 \):

$$
\int_{\frac{1}{e}}^e \frac{\log(|\log x|)}{x} \, dx =
\int_{\frac{1}{e}}^1 \frac{\log(-\log x)}{x} \, dx +
\int_1^e \frac{\log(\log x)}{x} \, dx
$$

Letting \( t = -\log x \) and \( dt = -\frac{1}{x} dx \) in the first integral:

$$
\int_{\frac{1}{e}}^1 \frac{\log(-\log x)}{x} dx =
- \int_1^0 \log t \, dt = \int_0^1 \log t \, dt
$$

Similarly, the second becomes:

$$
\int_1^e \frac{\log(\log x)}{x} dx = \int_0^1 \log t \, dt
$$

Hence:

$$
\int_{\frac{1}{e}}^e \frac{\log(|\log x|)}{x} \, dx =
2 \int_0^1 \log t \, dt = -2
$$

---

### Exercise 2

Evaluate the integral:

$$
\int \frac{1}{\sin^2 x \cos^2 x} \, dx
$$

**Solution:**

We write:

$$
\frac{1}{\sin^2 x \cos^2 x} = \frac{\sin^2 x + \cos^2 x}{\sin^2 x \cos^2 x}
= \frac{1}{\cos^2 x} + \frac{1}{\sin^2 x}
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

Using the substitution \( x = \sin t \), \( dx = \cos t dt \), and identity \( \sqrt{1 - \sin^2 t} = |\cos t| \):

Since \( \cos t \geq 0 \) in \( [-\pi/2, \pi/2] \):

$$
\int_{-1}^{1} \sqrt{1 - x^2} \, dx =
\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \cos^2 t \, dt =
\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \frac{1 + \cos(2t)}{2} \, dt =
\frac{\pi}{2}
$$

---

### Exercise 4

Evaluate the definite integral:

$$
\int_{-1}^{1} \frac{1}{\sqrt{4 - x^2}} \, dx
$$

**Solution:**

Using the substitution \( x = 2 \sin t \), so \( dx = 2 \cos t dt \), and the integrand becomes:

$$
\int_{-1}^1 \frac{1}{\sqrt{4 - x^2}} \, dx =
2 \int_0^1 \frac{1}{\sqrt{4 - x^2}} \, dx =
2 \arcsin\left( \frac{x}{2} \right) \bigg|_0^1 = \frac{\pi}{3}
$$

---

### Exercise 5

Evaluate the indefinite integral:

$$
\int \frac{x^2}{x^2 + 2} \, dx
$$

**Solution:**

Split numerator:

$$
\int \frac{x^2 + 2 - 2}{x^2 + 2} \, dx =
\int 1 \, dx - \int \frac{2}{x^2 + 2} \, dx =
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
\int \frac{1}{\sin x} \, dx =
\log\left| \tan \frac{x}{2} \right| + c
$$

---

### Exercise 7

Evaluate the definite integral:

$$
\int_{-2}^{2} \sqrt{4 - x^2} \, dx
$$

**Solution:**

Use symmetry and \( x = 2 \sin t \), \( dx = 2 \cos t dt \):

$$
\int_{-2}^2 \sqrt{4 - x^2} \, dx =
2 \int_0^2 \sqrt{4 - x^2} \, dx =
8 \int_0^{\pi/2} \cos^2 t \, dt =
8 \cdot \frac{\pi}{4} = 2\pi
$$

---

### Exercise 8

Evaluate the indefinite integral:

$$
\int \sin x \, e^x \, dx
$$

**Solution:**

Integration by parts twice:

Let \( I = \int \sin x \, e^x \, dx \). Then:

$$
I = e^x \sin x - \int e^x \cos x \, dx =
e^x (\sin x - \cos x) + I
$$

So:

$$
2I = e^x (\sin x - \cos x) \Rightarrow
I = \frac{e^x(\sin x - \cos x)}{2} + c
$$

---

### Exercise 9

Evaluate the definite integral:

$$
\int_0^1 e^{2x} \log(1 + e^x) \, dx
$$

**Solution:**

Substitute \( t = e^x \), \( dt = e^x dx \), so \( dx = \frac{dt}{t} \), and bounds become \( t \in [1, e] \):

$$
\int_0^1 e^{2x} \log(1 + e^x) \, dx =
\int_1^e t \log(1 + t) \, dt
$$

Apply integration by parts or polynomial division to simplify the integrand. Final result is a rational expression involving logs and powers (detailed steps omitted for brevity).

---

### Exercise 10

Evaluate the indefinite integral:

$$
\int \frac{e^x - e^{-x}}{x} \, dx
$$

**Solution:**

Split into two known integrals:

$$
\int \frac{e^x - 1}{x} \, dx + \int \frac{1 - e^{-x}}{x} \, dx
$$

These define the exponential integral:

$$
\text{Ein}(x) + \text{Ein}(-x) + c
$$

</div>
