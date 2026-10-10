---
layout: default
last_modified_at: 2026-10-10
date: 2026-10-10
original_date: 2025-08-29
title: "Integration by Parts: Original University Exercises"
permalink: /mathematics/calculus/integration-by-parts/
redirect_from:
  - /university/math/calculus-1/integration-by-parts/
background_image: "/images/integrali.png"
description: "Six original solved integrals combining integration by parts, substitutions, definite bounds and logarithmic endpoint singularities."
area: mathematics
topic: calculus
subtopic: integration-by-parts
level: university
content_type: solved-exercises
featured: true
---

# Integration by Parts: Original University Exercises


<div class="content-box">

The theory and selected worked exercises are adapted into English from *Eserciziario 2.1* by Antonino De Martino and Luana Manfredini. Original exercise statements and parameter cases are retained. Mathematical corrections are identified explicitly.

</div>


<div class="content-box">


## Theoretical Recall

Integration by parts is obtained directly from the product rule for derivatives.

For two differentiable functions f and g:

$$
(fg)'=f'g+fg'.
$$

Integrating both sides gives:

$$
\int (fg)'\,dx
=
\int f'g\,dx
+
\int fg'\,dx.
$$

Therefore:

$$
fg
=
\int f'g\,dx
+
\int fg'\,dx.
$$

Rearranging:

$$
\int f(x)g'(x)\,dx
=
f(x)g(x)
-
\int f'(x)g(x)\,dx.
$$

This is the **integration by parts formula**.

A common alternative notation is:

$$
\int u\,dv
=
uv-\int v\,du.
$$

### Choosing the Functions

The goal is to choose the factor to differentiate so that it becomes simpler, while the other factor can be integrated easily.

A useful heuristic is the **LIATE rule**:

- **L** — Logarithmic functions
- **I** — Inverse trigonometric functions
- **A** — Algebraic functions
- **T** — Trigonometric functions
- **E** — Exponential functions

Functions appearing earlier in this list are often good candidates for the factor to differentiate.

This is a guideline rather than a theorem: the best choice is always the one that simplifies the resulting integral.

**Author’s note:** Integration by parts should not be viewed merely as a formula to memorize. Its real purpose is to transform an integral into another one whose structure is easier to handle.

</div>


<div class="content-box">

## Exercises

</div>


<div class="content-box">

## Original Worked Exercises

These retain the definite and improper bounds in the original statements. C denotes an arbitrary integration constant on each interval of definition.

</div>

<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5921. -->

Evaluate the integral:

$$
\int \sin x e^{x} \, dx
$$



**Solution.**

Integrate by parts twice, as in the source:
$$
I=\int e^x\sin x\,dx=e^x\sin x-\int e^x\cos x\,dx.
$$
$$
\int e^x\cos x\,dx=e^x\cos x+\int e^x\sin x\,dx.
$$
Substitution gives the original integral on both sides:
$$
I=e^x(\sin x-\cos x)-I,
\qquad2I=e^x(\sin x-\cos x).
$$

**Final result**

$$
\frac{e^x}{2}(\sin x-\cos x)+C
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5947. -->

Evaluate the integral:

$$
\int_{1}^{e} \sin( \log x) \, dx
$$



**Solution.**

Write the integrand as a product of one and sin(log x):
$$
I=\left[x\sin(\log x)\right]_1^e-\int_1^e\cos(\log x)\,dx.
$$
Apply integration by parts to the remaining integral:
$$
\int_1^e\cos(\log x)\,dx
=\left[x\cos(\log x)\right]_1^e+\int_1^e\sin(\log x)\,dx.
$$
$$
I=e\sin1-e\cos1+1-I.
$$
$$
2I=e(\sin1-\cos1)+1.
$$

**Final result**

$$
\frac{e(\sin1-\cos1)+1}{2}
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5932. -->

Evaluate the integral:

$$
\int_{0}^{1} e^{2x} \log(1+e^{x}) \, dx.
$$



**Solution.**

Put t = eˣ, with dx = dt/t; the bounds become one and e:
$$
I=\int_1^e t\log(1+t)\,dt
=\left[\frac{t^2}{2}\log(1+t)\right]_1^e
-\frac12\int_1^e\frac{t^2}{1+t}\,dt.
$$
Polynomial division yields:
$$
\frac{t^2}{1+t}=t-1+\frac1{t+1}.
$$
$$
\int\frac{t^2}{1+t}\,dt=\frac{t^2}{2}-t+\log(1+t)+C.
$$
Evaluate all terms at the endpoints:
$$
I=\frac{e^2}{2}\log(1+e)-\frac{\log2}{2}
-\frac12\left[\frac{t^2}{2}-t+\log(1+t)\right]_1^e.
$$

**Editorial correction.** The source prints 1/(t+1) in a primitive where log(1+t) is required; its final evaluated expression uses the logarithm correctly.

**Final result**

$$
\frac{e^2-1}{2}\log(1+e)-\frac{e^2}{4}+\frac e2-\frac14
$$

</div>

<div class="content-box">

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6458. -->

Evaluate the integral:

$$
\int _{0}^{\frac{\pi}{2}}x \sin^{2} x \, dx.
$$



**Solution.**

The half-angle formula gives:
$$
\int\sin^2x\,dx=\frac x2-\frac{\sin2x}{4}+C.
$$
Integrate by parts with this primitive:
$$
I=\left[\frac{x^2}{2}-\frac{x\sin2x}{4}\right]_0^{\pi/2}
-\int_0^{\pi/2}\left(\frac x2-\frac{\sin2x}{4}\right)dx.
$$
$$
I=\frac{\pi^2}{8}-\left[\frac{x^2}{4}+\frac{\cos2x}{8}\right]_0^{\pi/2}
=\frac{\pi^2}{8}-\frac{\pi^2}{16}+\frac14.
$$

**Final result**

$$
\frac{\pi^2}{16}+\frac14
$$

</div>

<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6467. -->

Evaluate the integral:

$$
\int_{0}^{1} x^{2} \log \sqrt{1-x} \, dx.
$$



**Solution.**

Use the logarithm rule and substitute t = 1 − x:
$$
I=\frac12\int_0^1x^2\log(1-x)\,dx
=\frac12\int_0^1(1-t)^2\log t\,dt.
$$
This is improper at t = 0. Integration by parts gives the primitive:
$$
\int(1-t)^2\log t\,dt
=-\frac{(1-t)^3}{3}\log t+\frac13\int\frac{(1-t)^3}{t}\,dt.
$$
$$
F(t)=-\frac{(1-t)^3}{3}\log t+\frac{\log t}{3}
-\frac{t^3}{9}-t+\frac{t^2}{2}.
$$
The logarithmic part is [1 − (1 − t)³] log t/3 and tends to zero at zero. All polynomial terms also tend to zero:
$$
I=\frac12\lim_{a\to0^+}[F(t)]_a^1
=\frac12\left(-\frac19-1+\frac12\right).
$$

**Final result**

$$
-\frac{11}{36}
$$

</div>

<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6713. -->

Evaluate the integral:

$$
\int_{0}^{1} x^{2} \log \frac{1+x}{1-x} \, dx.
$$



**Solution.**

Split the logarithm, retaining the source's link with the preceding exercise:
$$
I=\int_0^1x^2\log(1+x)\,dx-\int_0^1x^2\log(1-x)\,dx.
$$
From Exercise 5, the second integral equals −11/18. For the first, integrate by parts and divide the rational term:
$$
\int_0^1x^2\log(1+x)\,dx
=\frac{\log2}{3}-\frac13\int_0^1\frac{x^3}{1+x}\,dx.
$$
$$
\frac{x^3}{1+x}=x^2-x+1-\frac1{1+x}.
$$
$$
\int_0^1x^2\log(1+x)\,dx
=\frac{\log2}{3}-\frac13\left[\frac{x^3}{3}-\frac{x^2}{2}+x-\log(1+x)\right]_0^1
=\frac{2\log2}{3}-\frac5{18}.
$$
Therefore:
$$
I=\frac{2\log2}{3}-\frac5{18}+\frac{11}{18}.
$$

**Final result**

$$
\frac{\log4+1}{3}
$$

</div>


<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
