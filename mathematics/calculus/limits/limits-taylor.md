---
layout: default
date: 2026-10-10
original_date: 2025-08-30
title: "Limits Using Taylor Expansions: Original Solved Exercises"
last_modified_at: 2026-10-10
permalink: /mathematics/calculus/limits/limits-taylor/
redirect_from:
  - /university/math/calculus-1/limits-taylor/
background_image: "/images/limiti.png"
description: "Complete Taylor and Maclaurin theory with fifteen original university-level limits, composite expansions, cancellation and parameters."
area: mathematics
topic: calculus
subtopic: limits
method: taylor-expansion
level: university
content_type: solved-exercises
---


<div class="content-box">

**Exercise editors and source:** **Antonino De Martino and Luana Manfredini**, *Eserciziario 2.1*. The original exercises and source theory are presented here in English for Logic & Motion.

</div>

# Limits Using Taylor Expansions: Original Solved Exercises


<div class="content-box">

## Complete Taylor and Maclaurin Recall

Taylor expansions are useful because they replace transcendental functions by polynomial expressions, with a remainder that records the approximation order. For a function with the required derivatives near x₀, Taylor's formula with Peano remainder is:

$$
f(x)=f(x_0)+\frac{f'(x_0)}{1!}(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2
+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n+o((x-x_0)^n).
$$

At x₀ = 0 this is called a Maclaurin expansion.

### Algebra of Little-o Terms

$$
o(x^m)+o(x^m)=o(x^m).
$$

$$
o(x^m)o(x^n)=o(x^{m+n}).
$$

$$
o(x^n)+o(x^m)=o(x^{\min\{m,n\}}).
$$

$$
x^n o(x^m)=o(x^{n+m}).
$$

$$
o(x^n+o(x^n))=o(x^n).
$$

The last identity is the composition rule used when the argument of a remainder itself has an asymptotic expansion.

### All Maclaurin Formulas in the Source

$$
(1+x)^\alpha=1+\alpha x+\frac{\alpha(\alpha-1)}{2!}x^2
+\cdots+\binom{\alpha}{n}x^n+o(x^n).
$$

$$
e^x=1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}+o(x^n).
$$

For a > 0:

$$
a^x=1+x\log a+\frac{x^2}{2!}\log^2 a
+\cdots+\frac{x^n}{n!}\log^n a+o(x^n).
$$

$$
\log(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}
+\cdots+(-1)^{n+1}\frac{x^n}{n}+o(x^n).
$$

$$
\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}
+\cdots+(-1)^n\frac{x^{2n+1}}{(2n+1)!}+o(x^{2n+2}).
$$

$$
\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}
+\cdots+(-1)^n\frac{x^{2n}}{(2n)!}+o(x^{2n+1}).
$$

$$
\tan x=x+\frac{x^3}{3}+\frac{2x^5}{15}
+\frac{17x^7}{315}+\frac{62x^9}{2835}+o(x^{10}).
$$

$$
\arctan x=x-\frac{x^3}{3}+\frac{x^5}{5}
+\cdots+(-1)^n\frac{x^{2n+1}}{2n+1}+o(x^{2n+2}).
$$

$$
\arcsin x=x+\frac{x^3}{6}+\frac{3x^5}{40}
+\cdots+\frac{(2n)!}{4^n(n!)^2(2n+1)}x^{2n+1}+o(x^{2n+2}).
$$

$$
\arccos x=\frac\pi2-x-\frac{x^3}{6}-\frac{3x^5}{40}
-\cdots-\frac{(2n)!}{4^n(n!)^2(2n+1)}x^{2n+1}+o(x^{2n+2}).
$$

$$
\sinh x=x+\frac{x^3}{3!}+\frac{x^5}{5!}
+\cdots+\frac{x^{2n+1}}{(2n+1)!}+o(x^{2n+2}).
$$

$$
\cosh x=1+\frac{x^2}{2!}+\frac{x^4}{4!}
+\cdots+\frac{x^{2n}}{(2n)!}+o(x^{2n+1}).
$$


### L'Hôpital's Theorem

Let f and g be defined on a punctured neighborhood of c. Suppose both tend to zero, or both are infinite, and both are differentiable there with g′ nonzero. If the following limit exists, finite or infinite:

$$
\lim_{x\to c}\frac{f'(x)}{g'(x)}=L,
$$

then:

$$
\lim_{x\to c}\frac{f(x)}{g(x)}=L.
$$

The theorem also applies to one-sided limits and limits at infinity under the corresponding hypotheses. 

[**Original exercises using L'Hôpital →**]({{ "/mathematics/calculus/limits/limits-hopital/" | relative_url }})

</div>

<div class="content-box">

## Original Worked Exercises

The first ten exercises below replace the earlier elementary substitutes. The five source exercises added previously are retained.

</div>

<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 2899. -->

Evaluate the following limit:

$$
\lim_{x \to 0}\frac{\sin x -\frac{1}{2}x+x^{3}}{\tan x -1+ \cos x}.
$$


**Solution.**

Expand numerator and denominator to third order:
$$
\sin x-\frac x2+x^3=\frac x2+\frac56x^3+o(x^3).
$$
$$
\tan x-1+\cos x=x-\frac{x^2}{2}+\frac{x^3}{3}+o(x^3).
$$
Factor x in both expressions:
$$
\frac{\frac12+\frac56x^2+o(x^2)}{1-\frac x2+\frac{x^2}{3}+o(x^2)}\longrightarrow\frac12.
$$

**Final result**

$$
\frac12
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 2907. -->

Evaluate the following limit:

$$
\lim_{x \to 0}\frac{\sinh x -\sin x}{x^{3}}.
$$


**Solution.**

The linear terms cancel:
$$
\sinh x-\sin x
=\left(x+\frac{x^3}{6}+o(x^3)\right)
-\left(x-\frac{x^3}{6}+o(x^3)\right).
$$
$$
\frac{\sinh x-\sin x}{x^3}=\frac{x^3/3+o(x^3)}{x^3}\longrightarrow\frac13.
$$

**Final result**

$$
\frac13
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 2930. -->

Evaluate the following limit:

$$
\lim_{x \to 0}\frac{(2+\cos(3x)-3 \cosh x)^{4}}{\log(1+x^{2})}.
$$


**Solution.**

Use the quadratic terms before taking the fourth power:
$$
2+\cos(3x)-3\cosh x
=2+1-\frac92x^2-3-\frac32x^2+o(x^2)
=-6x^2+o(x^2).
$$
$$
\log(1+x^2)=x^2-\frac{x^4}{2}+o(x^4).
$$
$$
\frac{(-6x^2+o(x^2))^4}{x^2-x^4/2+o(x^4)}
=\frac{6^4x^8+o(x^8)}{x^2(1-x^2/2+o(x^2))}\longrightarrow0.
$$


**Final result**

$$
0
$$

</div>

<div class="content-box">

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 2946. -->

Evaluate the following limit:

$$
\lim_{x \to 0}(\log(1+x)+\cos ^{2}x)^{\frac{1}{x}}
$$


**Solution.**

The base is positive near zero. Write the expression as an exponential:
$$
(\log(1+x)+\cos^2x)^{1/x}
=\exp\!\left(\frac{\log(\log(1+x)+\cos^2x)}{x}\right).
$$
$$
\log(1+x)+\cos^2x=1+x+o(x).
$$
The composition rule for little-o terms gives:
$$
\log(1+x+o(x))=x+o(x)+o(x+o(x))=x+o(x).
$$
$$
\frac{\log(\log(1+x)+\cos^2x)}x\longrightarrow1.
$$

**Final result**

$$
e
$$

</div>

<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 2966. -->

Evaluate the following limit:

$$
\lim_{x \to 1^{+}}\frac{\sin (\sqrt{x-1})-\sqrt{\log x}}{x-1}.
$$


**Solution.**

Set h = x − 1 > 0. Expand the two radicals to the same order:
$$
\sin\sqrt h=\sqrt h-\frac{h^{3/2}}6+o(h^{3/2}).
$$
$$
\log(1+h)=h-\frac{h^2}{2}+o(h^2).
$$
$$
\sqrt{\log(1+h)}=\sqrt h\left(1-\frac h2+o(h)\right)^{1/2}.
$$
$$
\sqrt{\log(1+h)}=\sqrt h\left(1-\frac h4+o(h)\right)
=\sqrt h-\frac{h^{3/2}}4+o(h^{3/2}).
$$
$$
\frac{\sin\sqrt h-\sqrt{\log(1+h)}}h
=\frac{h^{3/2}/12+o(h^{3/2})}h
=\frac{\sqrt h}{12}+o(\sqrt h)\longrightarrow0.
$$


**Final result**

$$
0
$$

</div>

<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 2985. -->

Evaluate the following limit:

$$
\lim_{x \to 0}\frac{\sin (2x) e^{-x}-\log(1+2x)}{x^{3}}.
$$


**Solution.**

Expand both factors and the logarithm to third order:
$$
\sin(2x)=2x-\frac43x^3+o(x^3).
$$
$$
e^{-x}=1-x+\frac{x^2}{2}-\frac{x^3}{6}+o(x^3).
$$
$$
\log(1+2x)=2x-2x^2+\frac83x^3+o(x^3).
$$
$$
\sin(2x)e^{-x}=2x-2x^2+x^3-\frac43x^3+o(x^3).
$$
Subtracting cancels the first two orders:
$$
\frac{\sin(2x)e^{-x}-\log(1+2x)}{x^3}
=\frac{-3x^3+o(x^3)}{x^3}\longrightarrow-3.
$$

**Final result**

$$
-3
$$

</div>

<div class="content-box">

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 2995. -->

Evaluate the following limit:

$$
\lim_{x \to 0}\frac{e^{x-x^{2}}-\log(1+x)-1}{x-\sin x}.
$$


**Solution.**

Expand the exponential at the composite argument x − x²:
$$
e^{x-x^2}=1+x-x^2+\frac{(x-x^2)^2}{2}+\frac{(x-x^2)^3}{6}+o(x^3).
$$
$$
e^{x-x^2}=1+x-\frac{x^2}{2}-\frac56x^3+o(x^3).
$$
$$
\log(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}+o(x^3).
$$
$$
e^{x-x^2}-\log(1+x)-1=-\frac76x^3+o(x^3).
$$
$$
x-\sin x=\frac{x^3}{6}+o(x^3).
$$
$$
\frac{-7x^3/6+o(x^3)}{x^3/6+o(x^3)}\longrightarrow-7.
$$

**Final result**

$$
-7
$$

</div>

<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 3014. -->

Evaluate the following limit:

$$
\lim_{x \to 0}\frac{5^{1+\tan^{2}x}-5}{1-\cos x}.
$$


**Solution.**

Factor the constant exponential and use the tangent expansion:
$$
5^{1+\tan^2x}-5=5\left(e^{(\log5)\tan^2x}-1\right).
$$
$$
e^{(\log5)\tan^2x}-1=(\log5)\tan^2x+o(\tan^2x).
$$
$$
\tan^2x=x^2+o(x^2),\qquad1-\cos x=\frac{x^2}{2}+o(x^2).
$$
$$
\frac{5(\log5)x^2+o(x^2)}{x^2/2+o(x^2)}\longrightarrow10\log5.
$$

**Final result**

$$
10\log5
$$

</div>

<div class="content-box">

### Exercise 9

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 3023. -->

Evaluate the following limit:

$$
\lim_{x \to 0}\frac{x^{2}-\sin^{2} x}{x^{3}(e^{x}-\cos x)}.
$$


**Solution.**

Square the sine expansion before subtracting:
$$
\sin^2x=\left(x-\frac{x^3}{6}+o(x^3)\right)^2
=x^2-\frac{x^4}{3}+o(x^4).
$$
$$
e^x-\cos x
=1+x+\frac{x^2}{2}+o(x^2)-1+\frac{x^2}{2}+o(x^2)
=x+x^2+o(x^2).
$$
$$
\frac{x^2-\sin^2x}{x^3(e^x-\cos x)}
=\frac{x^4/3+o(x^4)}{x^4+x^5+o(x^5)}\longrightarrow\frac13.
$$

**Final result**

$$
\frac13
$$

</div>

<div class="content-box">

### Exercise 10

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 3129. -->

Evaluate the following limit:

$$
\lim_{x \to 1}\biggl(\frac{x}{x-1}-\frac{1}{\log x}\biggl).
$$


**Solution.**

Put y = x − 1, so x = 1 + y:
$$
\frac{x}{x-1}-\frac1{\log x}
=\frac{(1+y)\log(1+y)-y}{y\log(1+y)}.
$$
$$
\log(1+y)=y-\frac{y^2}{2}+o(y^2).
$$
$$
(1+y)\log(1+y)-y
=y+y^2-\frac{y^2}{2}+o(y^2)-y
=\frac{y^2}{2}+o(y^2).
$$
$$
\frac{y^2/2+o(y^2)}{y^2(1-y/2+o(y))}\longrightarrow\frac12.
$$

**Final result**

$$
\frac12
$$

</div>

<div class="content-box">

### Exercise 11 — Expansion around x = 1

$$
\lim_{x\to1}\frac{\log(1+\pi-4\arctan x)}{\sin(1-x)}.
$$

**Solution.**

First expand the logarithm and sine, whose arguments tend to zero:

$$
\frac{\log(1+\pi-4\arctan x)}{\sin(1-x)}
=\frac{\pi-4\arctan x+o(\pi-4\arctan x)}{(1-x)+o(1-x)}.
$$

Expand arctan at x = 1:

$$
\arctan x=\frac\pi4+\frac{x-1}{2}+o(x-1).
$$

Substituting gives:

$$
\frac{2(1-x)+o(1-x)+o(1-x)}{(1-x)+o(1-x)}
=\frac{2+o(1)}{1+o(1)}\longrightarrow2.
$$

**Final Result**

$$
2
$$

</div>

<div class="content-box">

### Exercise 12 — Fourth-order cancellation

$$
\lim_{x\to0}\frac{x\arcsin x-x^2}{\sqrt{1+x^4}-\cos(x^2)}.
$$

**Solution.**

Use the expansions in the source:

$$
\arcsin x=x+\frac{x^3}{6}+o(x^3).
$$

$$
\sqrt{1+x^4}=1+\frac{x^4}{2}+o(x^4),
\qquad \cos(x^2)=1-\frac{x^4}{2}+o(x^4).
$$

Multiply the arcsine expansion by x and cancel the quadratic terms:

$$
x\left(x+\frac{x^3}{6}+o(x^3)\right)-x^2
=\frac{x^4}{6}+o(x^4).
$$

The denominator is:

$$
1+\frac{x^4}{2}+o(x^4)-1+\frac{x^4}{2}+o(x^4)
=x^4+o(x^4).
$$

Therefore:

$$
\frac{x^4/6+o(x^4)}{x^4+o(x^4)}\longrightarrow\frac16.
$$

**Final Result**

$$
\frac16
$$

</div>

<div class="content-box">

### Exercise 13 — A product with fourth-order cancellation

$$
\lim_{x\to0}\frac{\sin(3x)\log(1+2x)-6x^2+6x^3}{x^4}.
$$

**Solution.**

Expand each factor to the order used in the source:

$$
\sin(3x)=3x-\frac{27}{6}x^3+o(x^3).
$$

$$
\log(1+2x)=2x-2x^2+\frac83x^3-4x^4+o(x^4).
$$

Multiplying and applying the little-o rules gives:

$$
\sin(3x)\log(1+2x)
=6x^2-6x^3+8x^4-9x^4+o(x^4).
$$

Thus the quotient becomes:

$$
\frac{6x^2-6x^3+8x^4-9x^4+o(x^4)-6x^2+6x^3}{x^4}
=\frac{-x^4+o(x^4)}{x^4}\longrightarrow-1.
$$

**Final Result**

$$
-1
$$

</div>

<div class="content-box">

### Exercise 14 — A fifth root and the binomial expansion

$$
\lim_{x\to0}\frac{\sqrt[5]{1-5x^2+x^4}-1+x^2}{x^4}.
$$

**Solution.**

Use the binomial expansion with exponent 1/5 and argument −5x²+x⁴:

$$
(1-5x^2+x^4)^{1/5}
=1+\frac{-5x^2+x^4}{5}
-\frac2{25}(-5x^2+x^4)^2
+o((-5x^2+x^4)^2).
$$

The square contributes 25x⁴ at the required order. Hence:

$$
\frac{1-x^2+x^4/5-2x^4-1+x^2+o(x^4)}{x^4}
=-\frac95+o(1).
$$

**Final Result**

$$
-\frac95
$$

</div>

<div class="content-box">

### Exercise 15 — Matching eighth-order terms

$$
\lim_{x\to0}\frac{x^5(e^{2x^3}-1)}{\sqrt{1+x^8}-\sqrt[3]{1+x^8}}.
$$

**Solution.**

Apply the exponential and binomial expansions exactly as in the source:

$$
e^{2x^3}=1+2x^3+o(x^3).
$$

$$
\sqrt{1+x^8}=1+\frac{x^8}{2}+o(x^8),
\qquad \sqrt[3]{1+x^8}=1+\frac{x^8}{3}+o(x^8).
$$

Then:

$$
\frac{x^5(1+2x^3+o(x^3)-1)}{1+x^8/2+o(x^8)-1-x^8/3+o(x^8)}
=\frac{2x^8+o(x^8)}{x^8/6+o(x^8)}\longrightarrow12.
$$

**Final Result**

$$
12
$$

</div>


<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
