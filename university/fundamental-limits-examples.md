---
title: "Worked Examples with Foundamental Limits"
meta-description: "A collection of solved exercises using foundamental limits, with detailed step-by-step reasoning and key theoretical results. Perfect for students preparing for calculus."
permalink: "/university/solved-exercises/fundamental-limits-examples/"
background_image: "/images/exercises.png"
---

**Prepared by Professor Antonino De Martino (Polytechnic University of Milan) and Dr. Luana Manfredini.**

<div class="content-box">

## Using Fundamental Limits

### Theoretical Background

Here are the most important notable limits in calculus:

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
If there exist two sequences $ a_n \to c $, $ b_n \to c $ such that:
$$
\lim_{n \to \infty} f(a_n) \ne \lim_{n \to \infty} f(b_n),
$$
then $ \lim_{x \to c} f(x) $ does not exist.

#### Theorem: Squeeze Theorem
If $ f(x) \leq g(x) \leq h(x) $ near $ x = c $, and:
$$
\lim_{x \to c} f(x) = \lim_{x \to c} h(x) = L,
$$
then:
$$
\lim_{x \to c} g(x) = L.
$$

</div>

<div class="content-box">

## Exercises

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

## Solutions


### Exercise 1

$$
\lim_{x \to +\infty} \left( \sqrt{x^2 + x + 1} - \sqrt{x^2 - x + 1} \right)
$$

**Solution:**

We multiply and divide by the conjugate expression:

$$
\begin{aligned}
\lim_{x \to +\infty} 
&\left( \sqrt{x^2 + x + 1} - \sqrt{x^2 - x + 1} \right) \\
&= \lim_{x \to +\infty} 
\frac{(x^2 + x + 1) - (x^2 - x + 1)}{\sqrt{x^2 + x + 1} + \sqrt{x^2 - x + 1}} \\
&= \lim_{x \to +\infty} 
\frac{2x}{\sqrt{x^2 + x + 1} + \sqrt{x^2 - x + 1}} \\
&= \lim_{x \to +\infty} 
\frac{2x}{x \left( \sqrt{1 + \frac{1}{x} + \frac{1}{x^2}} + \sqrt{1 - \frac{1}{x} + \frac{1}{x^2}} \right)} \\
&= \frac{2}{1 + 1} = 1
\end{aligned}
$$

---

### Exercise 2

$$
\lim_{x \to \infty} x \cdot \log\left( \frac{x + 4}{x + 5} \right)
$$

**Solution:**

We rewrite the logarithmic expression:

$$
\lim_{x \to \infty} x \cdot \log\left( 1 - \frac{1}{x + 5} \right)
$$

Let $$ t = -\frac{1}{x + 5} \), so $$ x = \frac{-1 - 5t}{t} $$. Then:

$$
\lim_{t \to 0} \frac{-1 - 5t}{t} \cdot \log(1 + t) = -1
$$

---

### Exercise 3

$$
\lim_{x \to +\infty} \left( \frac{2x + 9}{2x + 1} \right)^x
$$

**Solution:**

We write:

$$
\left( \frac{2x + 9}{2x + 1} \right)^x = \left( 1 + \frac{8}{2x + 1} \right)^x
$$

Let $$ t = \frac{8}{2x + 1} $$, so $$ x = \frac{4}{t} - \frac{1}{2} $$. Then:

$$
(1 + t)^{\frac{4}{t} - \frac{1}{2}} = 
\frac{(1 + t)^{4/t}}{(1 + t)^{1/2}} \to \frac{e^4}{1} = e^4
$$

---

### Exercise 4

$$
\lim_{x \to +\infty} x \cdot \log\left( \frac{x^2 + 1}{x^2 + x} \right)
$$

**Solution:**

We simplify the ratio:

$$
\frac{x^2 + 1}{x^2 + x} = \frac{1 + \frac{1}{x^2}}{1 + \frac{1}{x}}
$$

Let $$ t = \frac{1}{x} $$, so $$ x = \frac{1}{t} $$. Then:

$$
\lim_{t \to 0} \frac{1}{t} \cdot \log\left( \frac{1 + t^2}{1 + t} \right)
= \lim_{t \to 0} \left( \frac{\log(1 + t^2)}{t} - \frac{\log(1 + t)}{t} \right) = -1
$$

---

### Exercise 5

$$
\lim_{x \to +\infty} \frac{\log(x^3 + 1)}{x}
$$

**Solution:**

We use the identity:

$$
\log(x^3 + 1) = \log\left(x^3\left(1 + \frac{1}{x^3}\right)\right) 
= 3 \log x + \log\left(1 + \frac{1}{x^3} \right)
$$

So:

$$
\frac{3 \log x + \log\left(1 + \frac{1}{x^3} \right)}{x}
= \frac{3 \log x}{x} + \frac{\log\left(1 + \frac{1}{x^3} \right)}{x} \to 0 + 0 = 0
$$


### Exercise 6

$$
\lim_{x \to +\infty} \frac{\sin x - x}{\cos x + \sqrt{1 + x^2}}
$$

**Solution:**

We rewrite the expression:

$$
\frac{\sin x - x}{\cos x + \sqrt{1 + x^2}} = 
\frac{\frac{\sin x}{x} - 1}{\frac{\cos x}{x} + \sqrt{1 + \frac{1}{x^2}}}
$$

As $$ x \to +\infty $$, we know:

$$
\frac{\sin x}{x} \to 0, \quad \frac{\cos x}{x} \to 0
$$

So the limit becomes:

$$
\frac{0 - 1}{0 + 1} = -1
$$

---

### Exercise 7

$$
\lim_{x \to +\infty} \sin x \cdot \left[ \log(\sqrt{x} + 1) - \log(\sqrt{x + 1}) \right]
$$

**Solution:**

We use the identity:

$$
\log(\sqrt{x} + 1) - \log(\sqrt{x + 1}) = \log\left( \frac{\sqrt{x} + 1}{\sqrt{x + 1}} \right)
$$

Now:

$$
\frac{\sqrt{x} + 1}{\sqrt{x + 1}} =
\frac{\sqrt{x}(1 + \frac{1}{\sqrt{x}})}{\sqrt{x} \cdot \sqrt{1 + \frac{1}{x}}}
= \frac{1 + \frac{1}{\sqrt{x}}}{\sqrt{1 + \frac{1}{x}}}
$$

As $$ x \to +\infty $$, this tends to 1, so the logarithm tends to 0.
Since $$ \sin x $$ is bounded, the product tends to 0:

$$
\lim_{x \to +\infty} \sin x \cdot \log\left( \frac{\sqrt{x} + 1}{\sqrt{x + 1}} \right) = 0
$$

---

### Exercise 8

$$
\lim_{x \to +\infty} \left( \frac{x + 3}{x - 1} \right)^{x + 1}
$$

**Solution:**

We rewrite:

$$
\left( \frac{x + 3}{x - 1} \right)^{x + 1} = 
\left( 1 + \frac{4}{x - 1} \right)^{x + 1}
= \left( 1 + \frac{4}{x - 1} \right)^x \cdot \left( 1 + \frac{4}{x - 1} \right)
$$

Let $$ y = \frac{4}{x - 1} $$, so $$ x = \frac{4 + y}{y} $$. Then:

$$
\lim_{y \to 0} (1 + y)^{\frac{4}{y}} \cdot (1 + y) = e^4
$$

---

### Exercise 9

$$
\lim_{x \to 0^+} x^{\frac{1}{\log(3x)}}
$$

**Solution:**

Let $$ y = \frac{1}{\log(3x)} $$, then $$ x = \frac{e^{1/y}}{3} $$, so:

$$
\lim_{y \to 0^+} \left( \frac{e^y}{3} \right)^y
= \frac{e^{y \cdot \frac{1}{y}}}{3^y} = \frac{e}{1} = e
$$

---

### Exercise 10

$$
\lim_{x \to 0} \frac{e^x - e^{-x}}{x}
$$

**Solution:**

We split the expression:

$$
\frac{e^x - e^{-x}}{x} = \frac{e^x - 1}{x} + \frac{1 - e^{-x}}{x}
= \frac{e^x - 1}{x} + \frac{e^{-x} - 1}{-x}
$$

Using the known limits:

$$
\lim_{x \to 0} \frac{e^x - 1}{x} = 1, \quad
\lim_{x \to 0} \frac{e^{-x} - 1}{-x} = 1
$$

So the total limit is:

$$
1 + 1 = 2
$$
</div>


