---
title: "Introduction to Logarithms"
meta-description: "A clear and simple introduction to logarithms with definitions, examples, and useful properties for students."
permalink: "/high-school/math/intro-logarithms/"
background_image: "/images/hsex.png"
---

<div class="content-box">

## 📘 Introduction to Logarithms

A **logarithm** answers the question:  
**"To what exponent must we raise a number (called the base) to get another number?"**

If we know that  
$$ a^x = b $$  
then the logarithm tells us that  
$$ x = \log_a b $$

So, the logarithm is simply the **exponent** we need to give to the base \( a \) in order to obtain the number \( b \).

</div>

<div class="content-box">

## ⚠️ When is a Logarithm Defined?

The logarithm \( \log_a b \) is defined when:
- The base \( a \) is **positive** and **not equal to 1**
- The argument \( b \) is **positive**

</div>

<div class="content-box">

## 🧠 Basic Examples

- $$ \log_7 49 = 2 $$ because $$ 7^2 = 49 $$
- $$ \log_2 \frac{1}{2} = -1 $$ because $$ 2^{-1} = \frac{1}{2} $$

What if we want to solve $$ 2^x = 3 $$?
We write:
$$ \log_2 3 \approx 1.5849... $$
This gives a **precise symbolic expression**, just like using \( \sqrt{2} \) instead of its decimal approximation.

</div>

<div class="content-box">

## 🔁 Logarithms and Exponentials are Inverses

The **logarithmic function** is the inverse of the **exponential function**.

Let’s consider:
- $$ f(x) = 2^x $$
- $$ g(x) = \log_2 x $$

If you compute values for \( f(x) \) and plug them into \( g(x) \), you'll get back the original \( x \).

</div>

<div class="content-box">

## 📈 The Logarithmic Function

The general form is:
$$ y = \log_a x $$

### Key Properties:
- Domain: \( x > 0 \)
- Passes through \( (1, 0) \) because $$ \log_a 1 = 0 $$
- Increasing if $$ a > 1 $$, decreasing if $$ 0 < a < 1 $$

Example:
$$ \log_{1/2} 8 = -3 $$ because $$ (1/2)^{-3} = 8 $$

</div>

<div class="content-box">

## 🧩 Quick Examples with Explanation

- $$ \log_5 \frac{1}{5} = -1 $$ since $$ 5^{-1} = \frac{1}{5} $$
- $$ \log_{1/3} 3 = -1 $$ since $$ (1/3)^{-1} = 3 $$
- $$ \log_2 \frac{1}{32} = -5 $$ since $$ 2^{-5} = \frac{1}{32} $$
- $$ \log_6 1 = 0 $$ because $$ 6^0 = 1 $$
- $$ \log_2 \sqrt[3]{16} = \frac{4}{3} $$ because $$ \sqrt[3]{16} = 2^{4/3} $$

</div>

<div class="content-box">

## 🔧 Logarithmic Properties

### Product Rule
$$ \log_a (bc) = \log_a b + \log_a c $$

### Quotient Rule
$$ \log_a \left( \frac{b}{c} \right) = \log_a b - \log_a c $$

### Power Rule
$$ \log_a (b^c) = c \cdot \log_a b $$

### Change of Base
$$ \log_a b = \frac{\log_c b}{\log_c a} $$

</div>

<div class="content-box">

## 📝 Practice Problems

1. $$ 3 \log x + 2 \log y = \log(x^3 y^2) $$
2. $$ 2 \log x - 3 \log y = \log \left( \frac{x^2}{y^3} \right) $$
3. $$ \frac{1}{2} \log x + \frac{1}{2} \log y = \log(\sqrt{xy}) $$
4. $$ 2 \log 2 - \frac{1}{2} \log 9 + \log 6 = \log 8 $$
5. $$ 4 \log x - 3 \log x + \log(x+1) = \log(x(x+1)) $$
6. Convert: $$ \log_3 4 = \frac{\log_2 4}{\log_2 3} $$
7. Convert: $$ \log_4 6 = \frac{\log_2 6}{\log_2 4} $$
8. Solve: $$ \log_3 x = 3 \Rightarrow x = 27 $$
9. Solve: $$ \log_2 x = -4 \Rightarrow x = \frac{1}{16} $$
10. Solve: $$ \log_4 (2x - 1) = -1 \Rightarrow x = \frac{5}{8} $$

</div>

<div class="content-box">
<p><a href="/high-school/concepts-and-exercises/">⬅ Back to Concepts and Exercises</a></p>
</div>
