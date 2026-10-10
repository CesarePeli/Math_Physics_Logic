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
description: "Eight solved integrals combining integration by parts, substitutions, definite bounds and logarithmic endpoint singularities."
area: mathematics
topic: calculus
subtopic: integration-by-parts
level: university
content_type: solved-exercises
featured: true
---


<div class="content-box">

# Integration by Parts: Original University Exercises

*Exercise editors and source: Prof. Antonino De Martino and Dr. Luana Manfredini, Eserciziario 2.1. The original exercises and source theory are presented here in English for Logic & Motion.*

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

## Worked Exercises

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

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6283. -->

Solve the following exercise:

$$
\int_{1}^{2} \log(2x^{2}-3x+1) \, dx
$$


**Solution.**

Factor the logarithm argument: 2x²−3x+1=(x−1)(2x−1). On (1,2] both factors are positive, so split the logarithm into log(x−1)+log(2x−1). Each term is integrated by parts after a linear substitution:
$$\int\log t\,dt=t\log t-t.$$
For the first integral use t=x−1 with bounds 0 and 1; the limit t log t→0 gives −1. For the second use u=2x−1 with bounds 1 and 3:
$$\frac12\int_1^3\log u\,du=\frac12[u\log u-u]_1^3=\frac32\log3-1.$$
The singularity at x=1 is logarithmic and integrable. Add the two values.

**Final result**

$$
\frac32\log3-2
$$

</div>

<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6577. -->

Solve the following exercise:

$$
\int_{0}^{1} \log \frac{2-x^{2}}{x^{2}+3} \, dx
$$


**Solution.**

Split the logarithm into log(2−x²)−log(x²+3). Both arguments are positive on [0,1]. Applying integration by parts to each gives
$$\int\log(2-x^2)\,dx=x\log(2-x^2)+2\int\frac{x^2}{2-x^2}\,dx,$$
$$\int\log(x^2+3)\,dx=x\log(x^2+3)-2\int\frac{x^2}{x^2+3}\,dx.$$
Divide the rational terms:
$$\frac{x^2}{2-x^2}=-1+\frac2{2-x^2},\qquad\frac{x^2}{x^2+3}=1-\frac3{x^2+3}.$$
The linear terms cancel in the difference. A primitive for the original integrand on [0,1] is
$$F(x)=x\log\frac{2-x^2}{x^2+3}+\sqrt2\log\frac{\sqrt2+x}{\sqrt2-x}-2\sqrt3\arctan\frac{x}{\sqrt3}.$$
Here F(0)=0. Evaluate at x=1 and use arctan(1/√3)=π/6.

**Final result**

$$
-\log4+\sqrt2\log\frac{\sqrt2+1}{\sqrt2-1}-\frac\pi{\sqrt3}
$$

</div>


<div class="content-box">

[**← Back to Integrals**]({{ "/mathematics/calculus/integrals/" | relative_url }})

</div>
