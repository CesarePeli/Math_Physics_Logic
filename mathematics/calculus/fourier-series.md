---
layout: default
area: mathematics
topic: calculus
level: university
content_type: solved-exercises
background_image: "/images/limiti.png"
permalink: /mathematics/calculus/fourier-series/
title: "Fourier Series: The Exercise Book\u2019s Formulas"
description: "Fourier series and all three coefficient formulas from Eserciziario 2.1."
date: 2026-10-10
last_modified_at: 2026-10-10
---

# Fourier Series: The Exercise Book’s Formulas


<div class="content-box">

The theory and selected worked exercises are adapted into English from *Eserciziario 2.1* by Antonino De Martino and Luana Manfredini. Original exercise statements and parameter cases are retained. Mathematical corrections are identified explicitly.

</div>

<div class="content-box">

## Fourier Series

The source concludes its recall of function series with the Fourier expansion
$$
\frac{a_0}{2}+\sum_{n=1}^\infty\bigl(a_n\cos(nx)+b_n\sin(nx)\bigr).
$$
For a function integrable on [−π,π], the coefficients are determined by all three formulas given in the exercise book:
$$
a_0=\frac1\pi\int_{-\pi}^{\pi}f(x)\,dx,
$$
$$
a_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx\quad(n\ge1),
$$
$$
b_n=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx\quad(n\ge1).
$$
**Editorial correction:** the source starts the trigonometric sum at n=0 despite already writing a₀/2. Starting at n=1 avoids counting the constant term twice. These formulas define the coefficients; they alone do not guarantee pointwise or uniform convergence to f.

This section preserves the book's theoretical introduction. No additional exercise is attributed to the book.

</div>


<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
