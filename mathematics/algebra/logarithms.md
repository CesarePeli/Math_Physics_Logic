---
date: 2025-05-02
layout: default
title: "Introduction to Logarithms"
permalink: /mathematics/algebra/logarithms/
redirect_from:
  - /high-school/math/intro-logarithms/
background_image: "/images/hsex.png"
description: "Learn logarithms through definitions, domain conditions, inverse functions, logarithmic rules, graphs, and detailed examples."
area: mathematics
topic: algebra
subtopic: logarithms
level: high-school
content_type: theory
---

<div class="content-box">

# Introduction to Logarithms

## What Is a Logarithm?

A **logarithm** answers a very specific question:

> *To what power must we raise a given base to obtain a certain number?*

This relationship is written:

$$
\log_a b = x \quad \Longleftrightarrow \quad a^x = b
$$

We are used to reading powers from left to right:

- For example:

$$
2^3 = 8
$$

But a logarithm goes in the opposite direction:

- It asks:

$$
\log_2 8 = ?
$$

and answers:

$$
\log_2 8 = 3
$$

because

$$
2^3 = 8
$$

</div>

<div class="content-box">

## When Is a Logarithm Defined?

A logarithm like logₐ b is **only defined** under two conditions:

1. The **base** a must be **positive** and **different from 1**
2. The **argument** b must be **positive**

In symbols:

$$
a > 0,\quad a \neq 1,\quad b > 0
$$

Why? Because:

- We can't raise a negative base to arbitrary real powers in general
- a = 1 would always give the same result: 1ˣ = 1
- The result of an exponential function aˣ is always **positive**, so the **inverse** (logarithm) is only defined for positive inputs

</div>

<div class="content-box">

## A Step-by-Step Example

Let’s say we want to solve this exponential equation:

$$
2^x = 5
$$

We ask: "What power of 2 gives 5?"

There is **no integer** that works exactly, so we use logarithms:

$$
x = \log_2 5
$$

This is a **precise** expression, just like √2.

Its decimal approximation is:

$$
\log_2 5 \approx 2.3219...
$$

This means:

> “2 raised to the power 2.3219 is approximately 5.”

</div>

<div class="content-box">

## Logarithms and Exponentials: Inverse Functions

The **logarithm base a** is the inverse of the exponential function base a:

- Exponential:

$$
f(x) = a^x
$$

- Logarithm:

$$
g(x) = \log_a x
$$

These functions "undo" each other:

$$
\log_a (a^x) = x
$$

and

$$
a^{\log_a x} = x
$$

A similar relationship exists between squaring and square roots, but with an important restriction.

For every real number x:

$$
\sqrt{x^2} = |x|
$$

If we restrict the squaring function to x ≥ 0, then the square root is its inverse, and:

$$
\sqrt{x^2} = x
$$

for x ≥ 0.

Likewise:

$$
(\sqrt{x})^2 = x
$$

for x ≥ 0.

</div>

<div class="content-box">

## Graphical Features of the Logarithmic Function

For the function:

$$
f(x) = \log_a x
$$

we know:

- It is defined only for x > 0
- It passes through the point (1, 0), since

$$
\log_a 1 = 0
$$

- It increases if a > 1, and decreases if 0 < a < 1
- It grows slowly: logarithms increase very slowly for large values

A classic example:

$$
\log_{10} 1000 = 3 \qquad \text{because} \qquad 10^3 = 1000
$$

But:

$$
\log_{10} 10000 = 4 \quad \Rightarrow \quad \text{just one unit more}
$$

So even multiplying by 10 gives only a small change in the logarithm.

</div>

<div class="content-box">

## Core Logarithmic Rules

These rules are essential for simplifying logarithmic expressions:

### Product Rule

$$
\log_a (bc) = \log_a b + \log_a c
$$

### Quotient Rule

$$
\log_a \left( \frac{b}{c} \right) = \log_a b - \log_a c
$$

### Power Rule

$$
\log_a (b^n) = n \cdot \log_a b
$$

### Change of Base Formula

To compute logarithms with a base you don’t have on your calculator:

$$
\log_a b = \frac{\log_c b}{\log_c a}
$$

Most often, we use log₁₀ or ln (log base e).

</div>

<div class="content-box">

## Practice: A Detailed Example

Let’s simplify this expression:

$$
2 \log x + 3 \log y
$$

We apply the **power rule** first:

$$
= \log(x^2) + \log(y^3)
$$

Now the **product rule**:

$$
= \log(x^2 y^3)
$$

This shows how multiple terms can be **condensed into a single logarithm**.

Another common question:

> What is log₂ ∛16?

We note:

$$
\sqrt[3]{16} = 2^{4/3}
$$

So:

$$
\log_2(2^{4/3}) = \frac{4}{3}
$$

This uses the rule:

$$
\log_a (a^x) = x
$$

</div>

<div class="content-box">

## Want to Go Further?

Try proving these properties from the definition:

- Why does the product rule work?
- Can you explain why logarithms grow slowly?
- Explore the graph of y = logₐ x for different values of a

---

[**← Back to Algebra**]({{ "/mathematics/algebra/" | relative_url }})

</div>