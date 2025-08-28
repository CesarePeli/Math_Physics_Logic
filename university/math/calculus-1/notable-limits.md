---
layout: default
date: 2025-04-21
title: "Solved Exercises — Notable Limits"
meta-description: "A curated selection of solved exercises on notable limits: fundamental indeterminate forms, exponential and trigonometric limits, and classical remarkable results."
permalink: "/university/math/calculus-1/notable-limits/"
background_image: "/images/euclide.png"
featured: true
---

<div class="content-box">

## Theoretical Recall

Here are the most important notable limits in calculus:

$$
\lim_{x\to 0} \frac{\sin x}{x} = 1,
\quad
\lim_{x\to 0} \frac{1 - \cos x}{x^2} = \tfrac{1}{2},
\quad
\lim_{x\to 0} \frac{\tan x}{x} = 1,
$$

$$
\lim_{x\to 0} \frac{e^x - 1}{x} = 1,
\quad
\lim_{x\to 0} \frac{\log(1+x)}{x} = 1,
\quad
\lim_{x\to 0} (1+x)^{1/x} = e,
$$

$$
\lim_{x\to +\infty} \left(1+\frac{1}{x}\right)^x = e,
\quad
\lim_{x\to 0} \frac{\arcsin x}{x} = 1,
\quad
\lim_{x\to 0} \frac{\arctan x}{x} = 1.
$$

### Key Theorems

#### Theorem: Squeeze Theorem
If $f(x) \leq g(x) \leq h(x)$ near $x = c$, and

$$
\lim_{x \to c} f(x) = \lim_{x \to c} h(x) = L,
$$

then

$$
\lim_{x \to c} g(x) = L.
$$

#### Theorem: Non-Existence via Sequences
If there exist two sequences $a_n \to c$, $b_n \to c$ such that

$$
\lim_{n \to \infty} f(a_n) \ne \lim_{n \to \infty} f(b_n),
$$

then $\lim_{x \to c} f(x)$ does not exist.

</div>

<div class="content-box">

## Exercises

### Exercise 1
$$
\lim_{x \to 0} \frac{\sin(3x)}{x}
$$

**Solution:**

Substitute $t = 3x$. Then as $x \to 0$, also $t \to 0$.

$$
\frac{\sin(3x)}{x} = 3 \cdot \frac{\sin t}{t}.
$$

Since $\lim_{t \to 0} \frac{\sin t}{t} = 1$:

**Final Result:**

$$
\lim_{x \to 0} \frac{\sin(3x)}{x} = 3
$$

---

### Exercise 2
$$
\lim_{x \to 0} \frac{1 - \cos(2x)}{x^2}
$$

**Solution:**

Use the identity $1 - \cos(2x) = 2 \sin^2 x$:

$$
\frac{1 - \cos(2x)}{x^2} = \frac{2 \sin^2 x}{x^2}.
$$

Rewrite as:

$$
2 \left( \frac{\sin x}{x} \right)^2.
$$

As $x \to 0$, $\frac{\sin x}{x} \to 1$.

**Final Result:**

$$
\lim_{x \to 0} \frac{1 - \cos(2x)}{x^2} = 2
$$

---

### Exercise 3
$$
\lim_{x \to 0} \frac{e^x - 1}{x}
$$

**Solution:**

Expand $e^x = 1 + x + \tfrac{x^2}{2} + o(x^2)$.

Then:

$$
\frac{e^x - 1}{x} = 1 + \tfrac{x}{2} + o(x).
$$

**Final Result:**

$$
\lim_{x \to 0} \frac{e^x - 1}{x} = 1
$$

---

### Exercise 4
$$
\lim_{x \to 0} \frac{\tan x}{x}
$$

**Solution:**

Rewrite $\tan x = \frac{\sin x}{\cos x}$:

$$
\frac{\tan x}{x} = \frac{\sin x}{x} \cdot \frac{1}{\cos x}.
$$

As $x \to 0$, $\frac{\sin x}{x} \to 1$ and $\cos x \to 1$.

**Final Result:**

$$
\lim_{x \to 0} \frac{\tan x}{x} = 1
$$

---

### Exercise 5
$$
\lim_{x \to +\infty} \left(1 + \frac{2}{x}\right)^x
$$

**Solution:**

We recall $\lim_{x \to +\infty} \left(1 + \tfrac{1}{x}\right)^x = e$.

Here:

$$
\left(1 + \frac{2}{x}\right)^x = \left[\left(1 + \frac{2}{x}\right)^{x/2}\right]^2.
$$

As $x \to +\infty$, $(1 + \tfrac{2}{x})^{x/2} \to e$. Thus the whole expression tends to $e^2$.

**Final Result:**

$$
\lim_{x \to +\infty} \left(1 + \frac{2}{x}\right)^x = e^2
$$

---

### Exercise 6
$$
\lim_{x \to 0} \frac{\log(1+x)}{x}
$$

**Solution:**

Expand $\log(1+x) = x - \tfrac{x^2}{2} + o(x^2)$.

So:

$$
\frac{\log(1+x)}{x} = 1 - \tfrac{x}{2} + o(x).
$$

**Final Result:**

$$
\lim_{x \to 0} \frac{\log(1+x)}{x} = 1
$$

---

### Exercise 7
$$
\lim_{x \to 0} \frac{\sin^2 x}{x^2}
$$

**Solution:**

Rewrite as:

$$
\left( \frac{\sin x}{x} \right)^2.
$$

Since $\lim_{x \to 0} \frac{\sin x}{x} = 1$:

**Final Result:**

$$
\lim_{x \to 0} \frac{\sin^2 x}{x^2} = 1
$$

---

### Exercise 8
$$
\lim_{x \to 0} \frac{e^{2x} - 1}{x}
$$

**Solution:**

Expand $e^{2x} = 1 + 2x + 2x^2 + o(x^2)$.

Then:

$$
\frac{e^{2x} - 1}{x} = 2 + 2x + o(x).
$$

**Final Result:**

$$
\lim_{x \to 0} \frac{e^{2x} - 1}{x} = 2
$$

---

### Exercise 9
$$
\lim_{x \to 0} \frac{\cos x - 1}{x}
$$

**Solution:**

Expand $\cos x = 1 - \tfrac{x^2}{2} + o(x^2)$.

So:

$$
\frac{\cos x - 1}{x} = -\tfrac{x}{2} + o(x) \to 0.
$$

**Final Result:**

$$
\lim_{x \to 0} \frac{\cos x - 1}{x} = 0
$$

---

### Exercise 10
$$
\lim_{x \to 0} \frac{\arctan x}{x}
$$

**Solution:**

Use $\arctan x = x - \tfrac{x^3}{3} + o(x^3)$.

Then:

$$
\frac{\arctan x}{x} = 1 - \tfrac{x^2}{3} + o(x^2).
$$

**Final Result:**

$$
\lim_{x \to 0} \frac{\arctan x}{x} = 1
$$

</div>
