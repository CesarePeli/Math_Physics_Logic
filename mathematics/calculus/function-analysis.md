---
layout: default
area: mathematics
topic: calculus
level: university
content_type: solved-exercises
background_image: "/images/limiti.png"
permalink: /mathematics/calculus/function-analysis/
title: "Function Analysis: Domain, Asymptotes and Original Exercises"
description: "Three original function studies with extrema, asymptotes, convexity and the exercise book\u2019s original diagrams."
date: 2026-10-10
last_modified_at: 2026-10-10
---

# Function Analysis: Domain, Asymptotes and Original Exercises


<div class="content-box">

The theory and selected worked exercises are adapted into English from *Eserciziario 2.1* by Antonino De Martino and Luana Manfredini. Original exercise statements and parameter cases are retained. Mathematical corrections are identified explicitly.

</div>

<div class="content-box">

## Complete Function-Analysis Recall

Follow the exercise book's six stages: determine the domain; check symmetry and periodicity; study the sign; find asymptotes; study the first derivative; study the second derivative when possible.

An even function has symmetry about the vertical axis; an odd function has symmetry about the origin:
$$
f(-x)=f(x)\quad\text{(even)},\qquad f(-x)=-f(x)\quad\text{(odd)}.
$$
The authors ask whether a function graph can have symmetry about the horizontal axis. For a single-valued real function this requires every ordinate to equal its negative, so the function must be zero. Periodicity means f(x+T)=f(x), for a positive period T and all applicable domain points.

A vertical asymptote x=x₀ occurs on a side where the corresponding limit is infinite:
$$
\lim_{x\to x_0^-}f(x)=\pm\infty\quad\text{(left)},\qquad
\lim_{x\to x_0^+}f(x)=\pm\infty\quad\text{(right)}.
$$
It is bilateral when both limits are infinite, with signs that may differ. **Editorial correction:** the source's bilateral definition says “one” of these conditions; both are required for bilateral behavior.

Horizontal asymptotes y=k, with real k, are determined separately on each side:
$$
\lim_{x\to-\infty}f(x)=k\quad\text{(left)},\qquad
\lim_{x\to+\infty}f(x)=k\quad\text{(right)}.
$$
The same line is bilateral if both limits equal the same k. Oblique asymptotes y=mx+q require finite m≠0 and finite q:
$$
m_+=\lim_{x\to+\infty}\frac{f(x)}x,\quad q_+=\lim_{x\to+\infty}[f(x)-m_+x],
$$
$$
m_-=\lim_{x\to-\infty}\frac{f(x)}x,\quad q_-=\lim_{x\to-\infty}[f(x)-m_-x].
$$
An oblique line is bilateral when it is both the left and right asymptote.

Fermat's theorem states that an interior local extremum at which f is differentiable satisfies f′(x₀)=0. This necessary condition is not sufficient. **Editorial correction:** the source's theorem incorrectly uses “stationary point” in place of “interior local extremum.”

An absolute maximum or minimum satisfies the respective inequality for every domain point; a relative maximum or minimum satisfies it in a neighborhood of x₀ within the domain:
$$
f(x)\le f(x_0)\quad\text{(maximum)},\qquad f(x)\ge f(x_0)\quad\text{(minimum)}.
$$
Suppose f is continuous on [a,b] and differentiable on (a,b) (the source additionally assumes a continuous derivative). The four monotonicity cases are
$$
\begin{array}{c|c}f'\ge0&\text{nondecreasing}\\f'>0&\text{strictly increasing}\\f'\le0&\text{nonincreasing}\\f'<0&\text{strictly decreasing}.\end{array}
$$
In practice: calculate f′; find its zeros; solve f′>0 and determine the other signs; read the monotonicity intervals. Increasing then decreasing gives a local maximum; decreasing then increasing gives a local minimum. Also examine domain endpoints and points where the derivative fails to exist when seeking extrema.

For a twice differentiable function on (a,b), the source's convexity criteria are
$$
f\text{ convex}\iff f''(x)\ge0\ \forall x\in(a,b),\qquad
f\text{ concave}\iff f''(x)\le0\ \forall x\in(a,b).
$$

</div>

<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5361. -->

Analyze and sketch the following function:

$$
f(x)= \frac{\log^{2} x}{x}.
$$



**Solution.**

The domain is (0,∞), so the function is neither even nor odd. It is nonnegative and vanishes only at x=1; there is no vertical-axis intercept. Its endpoint limits are
$$
\lim_{x\to0^+}\frac{\log^2x}{x}=+\infty,\qquad
\lim_{x\to+\infty}\frac{\log^2x}{x}=0.
$$
Thus x=0 is a right vertical asymptote and y=0 a right horizontal asymptote. Differentiate:
$$
f'(x)=\frac{\log x(2-\log x)}{x^2}.
$$
The derivative is negative on (0,1), positive on (1,e²), and negative on (e²,∞). The point (1,0) is the absolute minimum; (e²,4/e²) is a relative maximum. The authors leave the second derivative as an optional completion. Carrying out that requested step gives
$$
f''(x)=\frac{2\log^2x-6\log x+2}{x^3},\qquad
x_\pm=\exp\!\left(\frac{3\pm\sqrt5}{2}\right).
$$
The function is convex outside [x₋,x₊] and concave between these two inflection abscissae.

Original diagram from the exercise book:

![Original function graph]({{ "/images/exercise-book/log-squared-over-x.png" | relative_url }})

**Final result**

$$
\min f=f(1)=0,\qquad f(e^2)=4/e^2\text{ is a local maximum}
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5554. -->

Analyze and sketch the following function:

$$
f(x)= \arctan x- \frac{x}{2}
$$



**Solution.**

The domain is all real numbers and f is odd. The source asks whether symmetry can shorten the analysis: yes, behavior on the negative half-axis follows from that on the positive half-axis. The origin is an intercept. As x→−∞ the function tends to +∞, and as x→+∞ it tends to −∞. Its oblique asymptotes are
$$
y=-\frac{x}{2}-\frac{\pi}{2}\quad(x\to-\infty),\qquad
y=-\frac{x}{2}+\frac{\pi}{2}\quad(x\to+\infty).
$$
The derivatives are
$$
f'(x)=\frac{1-x^2}{2(1+x^2)},\qquad f''(x)=-\frac{2x}{(1+x^2)^2}.
$$
The function decreases on (−∞,−1), increases on (−1,1), and decreases on (1,∞). Its local minimum is f(−1)=1/2−π/4; its local maximum is f(1)=π/4−1/2. It is convex for x<0 and concave for x>0; (0,0) is an inflection point. For completeness, besides zero there are two symmetric roots ±α, where α is the unique positive solution of arctan α=α/2 beyond 1. The signs follow from oddness and the monotonicity just established: positive on (−∞,−α) and (0,α), negative on (−α,0) and (α,∞).

Original diagram from the exercise book:

![Original function graph]({{ "/images/exercise-book/arctan-minus-half-x.png" | relative_url }})

**Final result**

$$
f(-1)=\frac12-\frac\pi4\text{ (local minimum)},\quad f(1)=\frac\pi4-\frac12\text{ (local maximum)}
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5633. -->

Analyze and sketch the following function:

$$
f(x)= \frac{5-x}{\sqrt{5+x^{2}}}
$$



**Solution.**

The domain is all real numbers. The function is neither even nor odd. Its intercepts are (0,√5) and (5,0); it is positive for x<5 and negative for x>5. Dividing numerator and denominator by |x| gives
$$
\lim_{x\to-\infty}f(x)=1,\qquad\lim_{x\to+\infty}f(x)=-1.
$$
Thus the horizontal asymptotes are y=1 on the left and y=−1 on the right. There are no finite-domain singularities. The first derivative is
$$
f'(x)=-\frac{5(x+1)}{(5+x^2)^{3/2}}.
$$
It is positive for x<−1 and negative for x>−1, so f(−1)=√6 is the absolute maximum. The second derivative is
$$
f''(x)=\frac{5(2x^2+3x-5)}{(5+x^2)^{5/2}}=\frac{5(2x+5)(x-1)}{(5+x^2)^{5/2}}.
$$
The function is convex on (−∞,−5/2) and (1,∞), and concave on (−5/2,1). The inflection points are (−5/2,√5) and (1,4/√6). The infimum is −1 and is not attained.

Original diagram from the exercise book:

![Original function graph]({{ "/images/exercise-book/five-minus-x-over-root.png" | relative_url }})

**Final result**

$$
\max f=\sqrt6\text{ at }x=-1,\qquad\inf f=-1\text{ (not attained)}
$$

</div>


<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
