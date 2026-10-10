---
layout: default
last_modified_at: 2026-10-10
date: 2026-10-10
original_date: 2025-08-31
title: "Sequences and Series of Functions: Complete Theory and Exercises"
permalink: /mathematics/calculus/series/
redirect_from:
  - /university/math/calculus-1/series/
  - /mathematics/calculus/fourier-series/
background_image: "/images/serie.png"
description: "Pointwise, uniform and total convergence, power-series radii and ten original solved exercises."
featured: false
area: mathematics
topic: calculus
subtopic: series
level: university
content_type: solved-exercises
---


<div class="content-box">

**Exercise editors and source:** **Antonino De Martino and Luana Manfredini**, *Eserciziario 2.1*. The original exercises and source theory are presented here in English for Logic & Motion. Any editorial corrections are marked explicitly.

</div>

# Sequences and Series of Functions: Complete Theory and Exercises




<div class="content-box">

## Complete Recall: Sequences and Series of Functions

Let fₙ:A→ℝ and f:A→ℝ, where A⊆ℝ. Pointwise convergence means
$$
\forall x\in A\ \forall\varepsilon>0\ \exists N_{\varepsilon,x}\ \forall n>N_{\varepsilon,x}:\quad |f_n(x)-f(x)|<\varepsilon.
$$
Equivalently fₙ(x)→f(x) for every x; the notation is fₙ→f. The threshold depends both on ε and on x, and may change with x even for fixed ε.

Uniform convergence means
$$
\forall\varepsilon>0\ \exists N_\varepsilon\ \forall n>N_\varepsilon\ \forall x\in A:\quad |f_n(x)-f(x)|<\varepsilon.
$$
Here the threshold depends only on ε. Writing fₙ⇉f, this is equivalent to
$$
\alpha_n=\sup_{x\in A}|f_n(x)-f(x)|,\qquad \lim_{n\to\infty}\alpha_n=0.
$$
Uniform convergence implies pointwise convergence; the converse fails. The source lists three transfer properties on an interval I:

1. If continuous fₙ converge uniformly to f, then f is continuous.
2. For continuous fₙ converging uniformly on I, integration commutes with the limit on every [a,b]⊆I:
$$
\lim_{n\to\infty}\int_a^b f_n(x)\,dx=\int_a^b f(x)\,dx.
$$
3. If fₙ∈C¹(I), fₙ→f pointwise and fₙ′⇉g uniformly, then f∈C¹(I) and
$$
f'=g,\qquad \lim_{n\to\infty}f_n'(x)=\left(\lim_{n\to\infty}f_n(x)\right)'.
$$

For a function series, take partial sums exactly as for a numerical series, treating x as a parameter:
$$
\sum_{n=0}^\infty f_n(x),\qquad s_n(x)=\sum_{k=0}^n f_k(x).
$$
Pointwise convergence to s on B⊆A means sₙ(x)→s(x) at every x∈B; uniform convergence means the supremum of the tail tends to zero:
$$
|s_n(x)-s(x)|=\left|\sum_{k=n+1}^\infty f_k(x)\right|\to0\quad\text{(pointwise)},
$$
$$
\sup_{x\in B}|s_n(x)-s(x)|=\sup_{x\in B}\left|\sum_{k=n+1}^\infty f_k(x)\right|\to0\quad\text{(uniform)}.
$$
**Total convergence** means that the series of suprema converges:
$$
\beta_n=\sup_{x\in A}|f_n(x)|,\qquad \sum_{n=0}^\infty\beta_n<\infty.
$$
Total convergence implies uniform convergence. Starting the sum at 1, as the book does, does not affect convergence when the omitted term has finite supremum.

**Power series** have a center x₀ and coefficient sequence aₙ:
$$
f_n(x)=a_n(x-x_0)^n,\qquad \sum_{n=0}^\infty a_n(x-x_0)^n.
$$
**Editorial correction:** the defining formula in the source omits the exponent n. If X is the convergence set, its radius is
$$
r=\sup\{|x-x_0|:x\in X\}.
$$
Inside |x−x₀|<r the series converges absolutely; outside |x−x₀|>r it does not converge. For every 0<ρ<r it converges totally on the closed interval [x₀−ρ,x₀+ρ]. Boundary points require separate checks.

Either of the following coefficient limits, when it exists (the ratio requires eventually nonzero coefficients), determines the radius:
$$
\lim_{n\to\infty}\sqrt[n]{|a_n|}=L,\qquad
\lim_{n\to\infty}\frac{|a_{n+1}|}{|a_n|}=L.
$$
$$
r=\begin{cases}1/L&0<L<\infty,\\0&L=+\infty,\\+\infty&L=0.\end{cases}
$$
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

</div>
<div class="content-box">

### Exercise 1

For x ∈ [0,1] and p ∈ ℝ, consider:

$$
f_n(x)=n^p x e^{-nx^2}.
$$

Study pointwise and uniform convergence as p varies.

**Solution.**

For x = 0:

$$
f_n(0)=0.
$$

For every fixed x > 0, the exponential factor dominates every power of n:

$$
n^p x e^{-nx^2}\to0.
$$

Therefore:

$$
\lim_{n\to\infty}f_n(x)=0
$$

for every x ∈ [0,1].

Thus fₙ converges pointwise to zero.

For uniform convergence, compute the derivative:

$$
f_n'(x)
=
n^p e^{-nx^2}(1-2nx^2).
$$

The interior critical point is determined by:

$$
1-2nx^2=0.
$$

Hence:

$$
x=\frac{1}{\sqrt{2n}}.
$$

At this point:

$$
\alpha_n
=
\sup_{x\in[0,1]}|f_n(x)|.
$$

Therefore:

$$
\alpha_n
=
n^p
\frac{1}{\sqrt{2n}}
e^{-1/2}.
$$

Thus:

$$
\alpha_n
=
\frac{e^{-1/2}}{\sqrt2}
n^{p-\frac12}.
$$

Consequently:

$$
\lim_{n\to\infty}\alpha_n
=
\begin{cases}
0, & p<\frac12,\\
\dfrac{e^{-1/2}}{\sqrt2}, & p=\frac12,\\
+\infty, & p>\frac12.
\end{cases}
$$

**Observation:** The exponential decay dominates only if p < 1/2.

**Final Result**

$$
f_n\to0
\text{ pointwise on }[0,1],
\qquad
f_n\to0
\text{ uniformly iff }p<\frac12.
$$


</div>

<div class="content-box">

### Exercise 2

For x ≥ 0:

$$
f_n(x)=\sqrt[n]{n+x^n}.
$$

Study pointwise and uniform convergence.

**Solution.**

For 0 ≤ x ≤ 1:

$$
n
\le
n+x^n
\le
n+1.
$$

Taking n-th roots:

$$
n^{1/n}
\le
f_n(x)
\le
(n+1)^{1/n}.
$$

Both bounds tend to 1, so:

$$
f_n(x)\to1.
$$

For x > 1:

$$
f_n(x)
=
x\left(1+\frac{n}{x^n}\right)^{1/n}.
$$

Since:

$$
\frac{n}{x^n}\to0,
$$

we obtain:

$$
f_n(x)\to x.
$$

Thus the pointwise limit is:

$$
f(x)
=
\begin{cases}
1, & 0\le x\le1,\\
x, & x>1.
\end{cases}
$$

For uniform convergence on [0,1]:

$$
\alpha_{n,1}
=
\sup_{x\in[0,1]}|f_n(x)-1|.
$$

Since fₙ is increasing in x:

$$
\alpha_{n,1}
=
(n+1)^{1/n}-1.
$$

Hence:

$$
\alpha_{n,1}\to0.
$$

On [1,+∞), define:

$$
g_n(x)
=
(n+x^n)^{1/n}-x.
$$

Its derivative is:

$$
g_n'(x)
=
x^{n-1}(n+x^n)^{\frac1n-1}-1.
$$

Equivalently:

$$
g_n'(x)
=
\left(1+\frac{n}{x^n}\right)^{\frac{1-n}{n}}-1.
$$

For x ≥ 1:

$$
g_n'(x)<0.
$$

Therefore gₙ is decreasing and its maximum occurs at x = 1:

$$
\alpha_{n,2}
=
\sup_{x\in[1,\infty)}|f_n(x)-x|.
$$

Hence:

$$
\alpha_{n,2}
=
(n+1)^{1/n}-1.
$$

Therefore:

$$
\alpha_{n,2}\to0.
$$

Combining the two regions:

$$
\alpha_n
=
\sup_{x\in[0,\infty)}|f_n(x)-f(x)|
\to0.
$$

**Observation:** Uniform convergence holds globally, even though the pointwise limit function changes definition at x = 1.

**Final Result**

$$
f_n\to f
\text{ uniformly on }[0,\infty),
\qquad
f(x)=
\begin{cases}
1, & 0\le x\le1,\\
x, & x>1.
\end{cases}
$$


</div>

<div class="content-box">

### Exercise 3

For x ∈ [0,1]:

$$
f_n(x)
=
n^2x^n(1-x^4).
$$

**Solution.**

For every fixed x ∈ [0,1):

$$
x^n\to0.
$$

At x = 1:

$$
f_n(1)=0.
$$

Therefore:

$$
f_n(x)\to0
$$

pointwise on [0,1].

Differentiate:

$$
f_n'(x)
=
n^2x^{n-1}
\left(n-(n+4)x^4\right).
$$

The maximum occurs when:

$$
x^4
=
\frac{n}{n+4}.
$$

Thus:

$$
x
=
\left(\frac{n}{n+4}\right)^{1/4}.
$$

At this point:

$$
\alpha_n
=
n^2
\left(\frac{n}{n+4}\right)^{n/4}
\frac{4}{n+4}.
$$

Now:

$$
\left(\frac{n}{n+4}\right)^{n/4}
=
\left(1+\frac4n\right)^{-n/4}
\to e^{-1}.
$$

Moreover:

$$
\frac{4n^2}{n+4}\sim4n.
$$

Therefore:

$$
\alpha_n\to+\infty.
$$

**Observation:** The growth of n² prevents uniform convergence despite pointwise vanishing.

**Final Result**

$$
f_n\to0
\text{ pointwise on }[0,1],
\qquad
\text{the convergence is not uniform}.
$$


</div>

<div class="content-box">

### Exercise 4

For x ∈ [0,1] and p ∈ ℝ:

$$
f_n(x)
=
n^p x^n(1-x^2).
$$

**Solution.**

For every x ∈ [0,1):

$$
x^n\to0.
$$

At x = 1:

$$
f_n(1)=0.
$$

Hence:

$$
f_n(x)\to0
$$

pointwise.

Differentiate:

$$
f_n'(x)
=
n^p x^{n-1}
\left(n-(n+2)x^2\right).
$$

The maximum occurs at:

$$
x
=
\sqrt{\frac{n}{n+2}}.
$$

Therefore:

$$
\alpha_n
=
n^p
\left(\frac{n}{n+2}\right)^{n/2}
\frac{2}{n+2}.
$$

Since:

$$
\left(\frac{n}{n+2}\right)^{n/2}
=
\left(1+\frac2n\right)^{-n/2}
\to e^{-1},
$$

we have:

$$
\alpha_n
\sim
\frac{2}{e}n^{p-1}.
$$

Hence:

$$
\alpha_n\to
\begin{cases}
0, & p<1,\\
\dfrac2e, & p=1,\\
+\infty, & p>1.
\end{cases}
$$

**Observation:** The balance between polynomial growth and exponential decay breaks precisely at p = 1.

**Final Result**

$$
f_n\to0
\text{ pointwise on }[0,1],
\qquad
f_n\to0
\text{ uniformly iff }p<1.
$$


</div>

<div class="content-box">

### Exercise 5

For x ∈ [0,1]:

$$
f_n(x)
=
\frac{\sin(nx)}{n}.
$$

**Solution.**

For every x:

$$
|\sin(nx)|\le1.
$$

Therefore:

$$
|f_n(x)|
\le
\frac1n.
$$

Since:

$$
\frac1n\to0,
$$

we obtain pointwise convergence:

$$
f_n(x)\to0.
$$

Moreover:

$$
\alpha_n
=
\sup_{x\in[0,1]}|f_n(x)|
\le
\frac1n.
$$

Therefore:

$$
\alpha_n\to0.
$$

**Observation:** The sine oscillation, bounded by 1, ensures uniform convergence at the same rate as 1/n.

**Final Result**

$$
f_n\to0
\text{ uniformly on }[0,1].
$$


</div>

<div class="content-box">

### Exercise 6

For x ∈ ℝ:

$$
f_n(x)=\arctan(nx).
$$

**Solution.**

For x > 0:

$$
nx\to+\infty,
$$

so:

$$
\arctan(nx)\to\frac{\pi}{2}.
$$

For x = 0:

$$
f_n(0)=0.
$$

For x < 0:

$$
nx\to-\infty,
$$

so:

$$
\arctan(nx)\to-\frac{\pi}{2}.
$$

Therefore:

$$
f(x)
=
\begin{cases}
\dfrac{\pi}{2}, & x>0,\\
0, & x=0,\\
-\dfrac{\pi}{2}, & x<0.
\end{cases}
$$

Every fₙ is continuous on ℝ, while the pointwise limit f is discontinuous at x = 0.

Therefore the convergence cannot be uniform on ℝ.

For any a > 0:

$$
\sup_{x\ge a}
\left|
f_n(x)-\frac{\pi}{2}
\right|
=
\frac{\pi}{2}-\arctan(na).
$$

Hence:

$$
\frac{\pi}{2}-\arctan(na)\to0.
$$

Similarly:

$$
\sup_{x\le-a}
\left|
f_n(x)+\frac{\pi}{2}
\right|
=
\frac{\pi}{2}-\arctan(na)
\to0.
$$

**Observation:** Uniform convergence holds only away from the discontinuity at x = 0.

**Final Result**

$$
\text{The convergence is not uniform on }\mathbb{R},
\text{ but it is uniform on }
[a,\infty)
\text{ and }
(-\infty,-a]
\text{ for every }a>0.
$$


</div>

<div class="content-box">

### Exercise 7

Study convergence and compute the sum:

$$
\sum_{n=1}^{\infty}
\frac{n+1}{n!}x^n.
$$

**Solution.**

The factorial in the denominator implies an infinite radius of convergence:

$$
r=+\infty.
$$

Therefore the series converges absolutely for every real x.

Split the series:

$$
\sum_{n=1}^{\infty}
\frac{n+1}{n!}x^n
=
\sum_{n=1}^{\infty}
\frac{n}{n!}x^n
+
\sum_{n=1}^{\infty}
\frac{x^n}{n!}.
$$

For the first term:

$$
\frac{n}{n!}
=
\frac{1}{(n-1)!}.
$$

Thus:

$$
\sum_{n=1}^{\infty}
\frac{n}{n!}x^n
=
x
\sum_{n=1}^{\infty}
\frac{x^{n-1}}{(n-1)!}.
$$

Hence:

$$
\sum_{n=1}^{\infty}
\frac{n}{n!}x^n
=
xe^x.
$$

For the second term:

$$
\sum_{n=1}^{\infty}
\frac{x^n}{n!}
=
e^x-1.
$$

Therefore:

$$
s(x)
=
xe^x+e^x-1.
$$

**Observation:** The manipulation uses the standard exponential power series and the algebraic identity n/n! = 1/(n−1)!.

**Final Result**

$$
\sum_{n=1}^{\infty}
\frac{n+1}{n!}x^n
=
e^x(1+x)-1
$$


</div>

<div class="content-box">

### Exercise 8

Study the series:

$$
\sum_{n=1}^{\infty}
(2^n+3^n)x^n.
$$

**Solution.**

Let:

$$
a_n=2^n+3^n.
$$

Then:

$$
\lim_{n\to\infty}
\frac{a_{n+1}}{a_n}
=
3.
$$

Therefore the radius of convergence is:

$$
r=\frac13.
$$

For:

$$
|x|<\frac13,
$$

the series converges absolutely.

At:

$$
x=\frac13,
$$

we obtain:

$$
\sum_{n=1}^{\infty}
\left[
\left(\frac23\right)^n+1
\right].
$$

The general term does not tend to zero, so the series diverges.

At:

$$
x=-\frac13,
$$

we obtain:

$$
\sum_{n=1}^{\infty}
(-1)^n
\left[
\left(\frac23\right)^n+1
\right].
$$

Again, the general term does not tend to zero.

Therefore the series diverges.

**Observation:** Even if the radius is finite, both endpoints fail here.

**Final Result**

$$
X=
\left(
-\frac13,
\frac13
\right)
$$


</div>

<div class="content-box">

### Exercise 9

Study and sum:

$$
\sum_{n=1}^{\infty}
(-1)^n n x^{2n-1}.
$$

**Solution.**

The convergence condition is:

$$
|x|<1.
$$

At x = 1 and x = −1, the general term does not tend to zero, so both endpoints are excluded.

Hence:

$$
X=(-1,1).
$$

For |x| < 1, start from the geometric series:

$$
\sum_{n=0}^{\infty}
(-1)^n x^{2n}
=
\frac{1}{1+x^2}.
$$

Differentiate term by term:

$$
\sum_{n=1}^{\infty}
2n(-1)^n x^{2n-1}
=
-\frac{2x}{(1+x^2)^2}.
$$

Dividing by 2:

$$
\sum_{n=1}^{\infty}
n(-1)^n x^{2n-1}
=
-\frac{x}{(1+x^2)^2}.
$$

**Observation:** Differentiating a simple geometric series is the key step.

**Final Result**

$$
\sum_{n=1}^{\infty}
(-1)^n n x^{2n-1}
=
-\frac{x}{(1+x^2)^2},
\qquad
|x|<1
$$


</div>

<div class="content-box">

### Exercise 10

Study and sum:

$$
\sum_{n=0}^{\infty}
\frac{x^n}{(n+1)(n+2)}.
$$

**Solution.**

The radius of convergence is:

$$
r=1.
$$

At x = 1:

$$
\sum_{n=0}^{\infty}
\frac{1}{(n+1)(n+2)}
$$

converges.

Indeed:

$$
\frac{1}{(n+1)(n+2)}
=
\frac{1}{n+1}
-
\frac{1}{n+2}.
$$

Thus the series is telescopic.

At x = −1:

$$
\sum_{n=0}^{\infty}
\frac{(-1)^n}{(n+1)(n+2)}
$$

converges absolutely because:

$$
\sum_{n=0}^{\infty}
\frac{1}{(n+1)(n+2)}
$$

converges.

Therefore:

$$
X=[-1,1].
$$

For |x| < 1, begin with:

$$
\sum_{n=0}^{\infty}t^n
=
\frac{1}{1-t}.
$$

Integrating from 0 to y:

$$
\sum_{n=0}^{\infty}
\frac{y^{n+1}}{n+1}
=
-\log(1-y).
$$

Integrating again from 0 to x:

$$
\sum_{n=0}^{\infty}
\frac{x^{n+2}}{(n+1)(n+2)}
=
\int_0^x-\log(1-y)\,dy.
$$

The integral is:

$$
\int_0^x-\log(1-y)\,dy
=
x+(1-x)\log(1-x).
$$

Therefore, for x ≠ 0:

$$
\sum_{n=0}^{\infty}
\frac{x^n}{(n+1)(n+2)}
=
\frac{x+(1-x)\log(1-x)}{x^2}.
$$

Equivalently:

$$
\sum_{n=0}^{\infty}
\frac{x^n}{(n+1)(n+2)}
=
\frac{1}{x}
+
\frac{(1-x)\log(1-x)}{x^2}.
$$

At x = 0, the original series gives:

$$
\frac{1}{(0+1)(0+2)}
=
\frac12.
$$

The expression above has a removable singularity at x = 0, and its continuous extension has value 1/2.

At x = 1:

$$
\sum_{n=0}^{\infty}
\frac{1}{(n+1)(n+2)}
=
1.
$$

At x = −1, using the continuous endpoint value of the sum:

$$
\sum_{n=0}^{\infty}
\frac{(-1)^n}{(n+1)(n+2)}
=
2\log2-1.
$$

**Observation:** Double integration allows us to produce the denominator (n+1)(n+2) from the geometric series.

**Final Result**

$$
\sum_{n=0}^{\infty}
\frac{x^n}{(n+1)(n+2)}
=
\begin{cases}
\dfrac{x+(1-x)\log(1-x)}{x^2},
& -1\le x<1,\ x\ne0,\\[8pt]
\dfrac12,
& x=0,\\[8pt]
1,
& x=1.
\end{cases}
$$


</div>




<div class="content-box">

## Continue Exploring Calculus

Sequences and series of functions extend the idea of convergence from numbers to entire functions. The distinction between **pointwise and uniform convergence** becomes essential when studying continuity, integration, differentiation, and power series.

Power series also connect infinite processes with familiar elementary functions, allowing complicated sums to be studied through algebra, differentiation, and integration.

[**Explore Limits →**]({{ "/mathematics/calculus/limits/" | relative_url }})

[**Explore Sequences →**]({{ "/mathematics/calculus/sequences/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>

<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
