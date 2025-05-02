---
title: "Introduction to Logarithms"
meta-description: "A clear and simple introduction to logarithms with definitions, examples, and useful properties for students."
permalink: "/high-school/math/intro-logarithms/"
---

## 📘 Introduction to Logarithms

<div class="theory">

### What is a Logarithm?

A **logarithm** answers the question:  
**"To what exponent must we raise a number (called the base) to get another number?"**  

If we know that  
\[ a^x = b \]  
then the logarithm tells us that  
\[ x = \log_a b \]  

So, the logarithm is simply the **exponent** we need to give to the base `a` in order to obtain the number `b`.

</div>

<div class="theory">

### ⚠️ When is a logarithm defined?

The logarithm \(\log_a b\) is defined when:
- The base \(a\) is **positive** and **not equal to 1**
- The argument \(b\) is **positive**

This ensures the expression makes mathematical sense.

</div>

## 🧠 Basic Examples

<div class="example">

- \(\log_7 49 = 2\) because \(7^2 = 49\)
- \(\log_2 \frac{1}{2} = -1\) because \(2^{-1} = \frac{1}{2}\)

What if we want to solve \(2^x = 3\)?
We write:
\[ \log_2 3 \approx 1.5849... \]

This is just like writing \(\sqrt{2}\) instead of its decimal approximation. It gives us a precise symbolic expression.

</div>

## 🔁 Inverse Relationship

<div class="theory">

The **logarithmic function** is the inverse of the **exponential function**.

Let’s consider:
- \(f(x) = 2^x\)
- \(g(x) = \log_2 x\)

If you compute some values of \(f(x)\) and plug them into \(g(x)\), you'll get back the original \(x\). That’s the idea of inverse functions.

</div>

## 📈 The Logarithmic Function

<div class="theory">

A general logarithmic function is:
\[ y = \log_a x \]

### Key properties:
- Domain: \(x > 0\)
- Passes through \((1, 0)\)
- If \(a > 1\): increasing
- If \(0 < a < 1\): decreasing

Example:
\[ \log_{\frac{1}{2}} 8 = -3 \Rightarrow \left(\frac{1}{2}\right)^{-3} = 8 \]

</div>

## 🧩 Quick Examples with Explanation

<div class="example">

### 1. \(\log_5 \frac{1}{5}\)
What power of 5 gives \(\frac{1}{5}\)?  
\(5^{-1} = \frac{1}{5} \Rightarrow \log_5 \frac{1}{5} = -1\)

### 2. \(\log_{\frac{1}{3}} 3\)
\( \left(\frac{1}{3}\right)^{-1} = 3 \Rightarrow \log_{\frac{1}{3}} 3 = -1\)

### 3. \(\log_2 \frac{1}{32}\)
\(2^{-5} = \frac{1}{32} \Rightarrow \log_2 \frac{1}{32} = -5\)

### 4. \(\log_6 1\)
\(6^0 = 1 \Rightarrow \log_6 1 = 0\)

### 5. \(\log_2 \sqrt[3]{16}\)
\(16 = 2^4 \Rightarrow \sqrt[3]{16} = 2^{4/3} \Rightarrow \log_2 (2^{4/3}) = \frac{4}{3}\)

</div>

## 🔧 Logarithmic Properties

<div class="theory">

### Product Rule
\[ \log_a (bc) = \log_a b + \log_a c \]

Example:
\[ \log_2 20 = \log_2 (4 \cdot 5) = \log_2 4 + \log_2 5 = 2 + \log_2 5 \]

### Quotient Rule
\[ \log_a \left(\frac{b}{c}\right) = \log_a b - \log_a c \]

Example:
\[ \log_3 \left(\frac{7}{3}\right) = \log_3 7 - 1 \]

### Power Rule
\[ \log_a (b^c) = c \cdot \log_a b \]

Example:
\[ \log_2 9 = \log_2 (3^2) = 2 \cdot \log_2 3 \]

### Change of Base Formula
\[ \log_a b = \frac{\log_c b}{\log_c a} \]

Example:
\[ \log_5 3 = \frac{\log_2 3}{\log_2 5} \]

</div>

## 📝 Practice Problems

<div class="exercise">

1. \(3 \log x + 2 \log y = \log (x^3 y^2)\)
2. \(2 \log x - 3 \log y = \log \left(\frac{x^2}{y^3}\right)\)
3. \(\frac{1}{2} \log x + \frac{1}{2} \log y = \log (\sqrt{xy})\)
4. \(2 \log 2 - \frac{1}{2} \log 9 + \log 6 = \log 8\)
5. \(4 \log x - 3 \log x + \log(x+1) = \log(x(x+1))\)
6. Convert \(\log_3 4\) to base 2: \(\frac{\log_2 4}{\log_2 3}\)
7. Convert \(\log_4 6\) to base 2: \(\frac{\log_2 6}{\log_2 4}\)
8. Solve \(\log_3 x = 3\) → \(x = 27\)
9. Solve \(\log_2 x = -4\) → \(x = \frac{1}{16}\)
10. Solve \(\log_4 (2x - 1) = -1\) → \(x = \frac{5}{8}\)

</div>
