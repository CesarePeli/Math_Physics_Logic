---
title: "Worked Examples with Notable Limits"
meta-description: "A collection of solved exercises using notable limits, with detailed step-by-step reasoning and key theoretical results. Perfect for students preparing for calculus."
permalink: "/university/solved-exercises/notable-limits-examples/"
---

## Using Notable Limits

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

---

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

---

## Solutions

<!-- solutions unchanged -->

---

[Download the PDF version](/materials/university/solved-exercises/notable-limits.pdf){:target="_blank"}

