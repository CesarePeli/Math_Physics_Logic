---
layout: default
area: mathematics
topic: calculus
level: university
content_type: solved-exercises
background_image: "/images/limiti.png"
permalink: /mathematics/calculus/definite-integrals/
title: "Definite Integrals: Original Solved Exercises"
description: "Original definite integrals with trigonometric substitution, symmetry, logarithmic absolute values and composite exponential substitutions."
date: 2026-10-10
last_modified_at: 2026-10-10
---


<div class="content-box">

**Exercise editors and source:** **Antonino De Martino and Luana Manfredini**, *Eserciziario 2.1*. The original exercises and source theory are presented here in English for Logic & Motion. Any editorial corrections are marked explicitly.

</div>

# Definite Integrals: Original Solved Exercises




<div class="content-box">

## Original Bounds, Symmetry and Changes of Variable

The original integration bounds are part of each problem. Under substitution, change the bounds along with the differential. Half-angle identities and integration by parts are collected in [the complete integration recall]({{ "/mathematics/calculus/immediate-integrals/" | relative_url }}).

</div>

<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5861. -->

Evaluate the definite integral:

$$
\int_{-1}^{1} \sqrt{1-x^{2}} \, dx.
$$



**Solution.**

Use x = sin t, with −π/2 ≤ t ≤ π/2 and dx = cos t dt:
$$
I=\int_{-\pi/2}^{\pi/2}\sqrt{1-\sin^2t}\cos t\,dt
=\int_{-\pi/2}^{\pi/2}|\cos t|\cos t\,dt.
$$
**Author's observation:** cosine is positive on the open interval (−π/2,π/2), so the absolute value can be removed here. Use the half-angle formula:
$$
I=\int_{-\pi/2}^{\pi/2}\frac{1+\cos2t}{2}\,dt
=\left[\frac t2+\frac{\sin2t}{4}\right]_{-\pi/2}^{\pi/2}.
$$

**Final result**

$$
\frac\pi2
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5908. -->

Evaluate the definite integral:

$$
\int_{-2}^{2} \sqrt{4-x^{2}} \, dx.
$$



**Solution.**

The integrand is even:
$$
I=2\int_0^2\sqrt{4-x^2}\,dx.
$$
Set x = 2 sin t. On 0 ≤ t ≤ π/2, cosine is nonnegative:
$$
I=2\int_0^{\pi/2}\sqrt{4-4\sin^2t}\,2\cos t\,dt
=8\int_0^{\pi/2}\cos^2t\,dt.
$$
$$
I=8\left[\frac t2+\frac{\sin2t}{4}\right]_0^{\pi/2}=2\pi.
$$
**Author's observation:** integrals involving √(a²−x²) can be treated with x = a sin t. For a nonzero radius, choose a suitable branch and account for the absolute value of a.

**Final result**

$$
2\pi
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6436. -->

Evaluate the definite integral:

$$
\int_{2}^{4} | \log (x-2) | \, dx.
$$



**Solution.**

The logarithm changes sign at three. Preserve the split and the improper endpoint:
$$
I=-\int_2^3\log(x-2)\,dx+\int_3^4\log(x-2)\,dx.
$$
Integration by parts on the second integral gives:
$$
\int_3^4\log(x-2)\,dx
=\left[x\log(x-2)\right]_3^4-\int_3^4\frac{x}{x-2}\,dx.
$$
$$
\frac{x}{x-2}=1+\frac2{x-2},
\qquad\int_3^4\log(x-2)\,dx=2\log2-1.
$$
Use the same primitive at the singular endpoint:
$$
\int_2^3\log(x-2)\,dx
=\lim_{a\to2^+}\left[x\log(x-2)-x-2\log(x-2)\right]_a^3.
$$
$$
\int_2^3\log(x-2)\,dx
=\lim_{a\to2^+}\left(a-3-(a-2)\log(a-2)\right)=-1.
$$
Therefore I = 1 + 2 log 2 − 1.

**Final result**

$$
\log4
$$

</div>

<div class="content-box">

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6564. -->

Evaluate the definite integral:

$$
\int_{1}^{e} x^{\log x} \frac{\log^{3} x}{x} \, dx.
$$



**Solution.**

Rewrite the variable power and substitute t = log x:
$$
x^{\log x}=e^{(\log x)^2},\qquad\frac{dx}{x}=dt,
\qquad I=\int_0^1e^{t^2}t^3\,dt.
$$
Integrate by parts, writing t³ as t·t²:
$$
I=\left[\frac{t^2e^{t^2}}2\right]_0^1
-\frac12\int_0^1e^{t^2}2t\,dt.
$$
$$
I=\left[\frac{t^2e^{t^2}}2-\frac{e^{t^2}}2\right]_0^1=\frac12.
$$

**Final result**

$$
\frac12
$$

</div>



<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6244. -->

Solve the following exercise:

$$
\int_{0}^{1} \frac{x^{2}}{\sqrt{1-x^{2}}} \, dx.
$$



**Solution.**

Set x=sin t, with t from 0 to π/2. Since cos t≥0 on that interval, √(1−x²)=cos t and dx=cos t dt. The radical cancels:
$$I=\int_0^{\pi/2}\sin^2t\,dt=\frac12\int_0^{\pi/2}(1-\cos2t)\,dt=\frac\pi4.$$
The endpoint x=1 is improper; the transformed integral proves convergence.

**Final result**

$$
\frac\pi4
$$

</div>

<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6337. -->

Solve the following exercise:

$$
\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}(\log \sin x) \cos x \, dx.
$$



**Solution.**

Set t=sin x, dt=cos x dx. The bounds become 1/√2 and 1:
$$I=\int_{1/\sqrt2}^{1}\log t\,dt=[t\log t-t]_{1/\sqrt2}^{1}.$$
Using log(1/√2)=−(log 2)/2 gives the stated value.

**Final result**

$$
-1+\frac{1+\frac12\log2}{\sqrt2}
$$

</div>

<div class="content-box">

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6361. -->

Solve the following exercise:

$$
\int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\log(1+\sin x)^{\sin x}}{\tan x} \, dx.
$$



**Solution.**

Interpret the numerator exactly as log((1+sin x)ˢⁱⁿ ˣ)=sin x log(1+sin x). Since 1/tan x=cos x/sin x, the sine factors cancel. Set t=1+sin x and dt=cos x dx:
$$I=\int_{3/2}^{1+\sqrt3/2}\log t\,dt=[t\log t-t]_{3/2}^{1+\sqrt3/2}.$$
Evaluate both endpoints.

**Final result**

$$
\left(1+\frac{\sqrt3}2\right)\log\left(1+\frac{\sqrt3}2\right)-\frac32\log\frac32+\frac{1-\sqrt3}2
$$

</div>

<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 6507. -->

Solve the following exercise:

$$
\int_{\frac{1}{2}}^{\frac{1}{\sqrt{2}}} \frac{\sqrt{1-x^{2}}}{x^{2}} \, dx
$$



**Solution.**

Set x=sin t, with t from π/6 to π/4. On this interval cos t>0, so
$$I=\int_{\pi/6}^{\pi/4}\frac{\cos^2t}{\sin^2t}\,dt=\int_{\pi/6}^{\pi/4}(\csc^2t-1)\,dt=[-\cot t-t]_{\pi/6}^{\pi/4}.$$
Use cot(π/6)=√3 and cot(π/4)=1.

**Final result**

$$
\sqrt3-1-\frac\pi{12}
$$

</div>


<div class="content-box">

[**← Back to Integrals**]({{ "/mathematics/calculus/integrals/" | relative_url }})

</div>
