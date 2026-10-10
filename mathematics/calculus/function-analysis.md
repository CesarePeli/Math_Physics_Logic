---
layout: default
area: mathematics
topic: calculus
level: university
content_type: solved-exercises
background_image: "/images/limiti.png"
permalink: /mathematics/calculus/function-analysis/
title: "Function Analysis: Domain, Asymptotes and Original Exercises"
description: "Eight original function studies with extrema, asymptotes, convexity and the exercise book\u2019s original diagrams."
date: 2026-10-10
last_modified_at: 2026-10-10
---


<div class="content-box">

# Function Analysis: Domain, Asymptotes and Original Exercises

*Exercise editors and source: Prof. Antonino De Martino and Dr. Luana Manfredini, Eserciziario 2.1. The original exercises and source theory are presented here in English for Logic & Motion.*

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
It is bilateral when both limits are infinite, with signs that may differ. 

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

Fermat's theorem states that an interior local extremum at which f is differentiable satisfies f′(x₀)=0. This necessary condition is not sufficient. 

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

Original diagram:

<img class="exercise-book-graph" src="{{ "/images/exercise-book/log-squared-over-x.png" | relative_url }}" alt="Graph of log squared x divided by x" style="display:block;width:100%;max-width:100%;height:auto;box-sizing:border-box;background-color:#fff;padding:1rem;border-radius:8px;" />

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

Original diagram:

<img class="exercise-book-graph" src="{{ "/images/exercise-book/arctan-minus-half-x.png" | relative_url }}" alt="Graph of arctan x minus x divided by two" style="display:block;width:100%;max-width:100%;height:auto;box-sizing:border-box;background-color:#fff;padding:1rem;border-radius:8px;" />

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

Original diagram:

<img class="exercise-book-graph" src="{{ "/images/exercise-book/five-minus-x-over-root.png" | relative_url }}" alt="Graph of five minus x divided by the square root of five plus x squared" style="display:block;width:100%;max-width:100%;height:auto;box-sizing:border-box;background-color:#fff;padding:1rem;border-radius:8px;" />

**Final result**

$$
\max f=\sqrt6\text{ at }x=-1,\qquad\inf f=-1\text{ (not attained)}
$$

</div>


<div class="content-box">

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5385. -->

Analyze and sketch the following function:

$$
f(x)= \log| \log(x^{2}-1)|.
$$


**Solution.**

For the nested logarithms, require x²−1>0 and log(x²−1)≠0. Thus |x|>1 and x≠±√2. The function is even, so the analysis may be restricted to x>1 and reflected. Its zeros satisfy |log(x²−1)|=1:
$$x=\pm\sqrt{1+e^{-1}},\qquad x=\pm\sqrt{1+e}.$$
There is no vertical-axis intercept. On x>1, the function is positive on (1,√(1+e⁻¹)) and (√(1+e),∞); negative between these zeros, with the excluded point √2 splitting that interval. Reflect the signs to x<−1. The limits at 1 from the right and at −1 from the left are +∞; both limits at each of ±√2 are −∞. These four lines are vertical asymptotes. At either infinity f tends to +∞, so there are no horizontal asymptotes; f/x tends to zero, so there is no nonzero-slope oblique asymptote. Differentiate:
$$f'(x)=\frac{2x}{(x^2-1)\log(x^2-1)}.$$
For x>1 it is negative on (1,√2) and positive on (√2,∞); evenness reverses these signs on the reflected intervals. The derivative never vanishes in the domain, so there are no extrema. The source leaves the second derivative optional.

**Final result**

$$
D=(-\infty,-\sqrt2)\cup(-\sqrt2,-1)\cup(1,\sqrt2)\cup(\sqrt2,\infty);\quad\text{no extrema}
$$

</div>

<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5435. -->

Analyze and sketch the following function:

$$
f(x)=x e^{\frac{1}{1+x}}.
$$


**Solution.**

The domain is ℝ excluding −1; the function is neither even nor odd. Its only intercept is (0,0), and its sign is the sign of x. At −1 the left limit is 0 and the right limit is −∞, so x=−1 is only a right vertical asymptote. At the two infinities f tends respectively to −∞ and +∞. Since
$$\lim_{x\to\pm\infty}\frac{f(x)}x=1,\qquad\lim_{x\to\pm\infty}(f(x)-x)=1,$$
the bilateral oblique asymptote is y=x+1. The derivatives are
$$f'(x)=e^{1/(x+1)}\frac{x^2+x+1}{(x+1)^2}>0,\qquad f''(x)=-e^{1/(x+1)}\frac{x+2}{(x+1)^4}.$$
The numerator x²+x+1=(x+1/2)²+3/4 is positive. The function therefore increases on each domain interval and has no extrema. It is convex on (−∞,−2), concave on (−2,−1) and (−1,∞); the inflection point is (−2,−2/e).

**Final result**

$$
\text{Asymptote }y=x+1;\quad\text{inflection }(-2,-2/e)
$$

</div>

<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5464. -->

Analyze and sketch the following function:

$$
f(x)=x+ \frac{1}{x} \log x.
$$


**Solution.**

The domain is (0,∞), so the function has neither parity symmetry. Its unique horizontal-axis intercept α satisfies x²=−log x with 0<α<1; there is no vertical-axis intercept. At zero from the right the limit is −∞, giving a vertical asymptote; at infinity it is +∞. The oblique asymptote is y=x, since f/x→1 and f−x=log x/x→0. The first derivative is
$$f'(x)=\frac{x^2+1-\log x}{x^2}>0.$$
For 0<x≤1 positivity is immediate; for x>1 use log x<x−1<x²+1. Thus f is increasing throughout its domain, with no extrema, and changes sign at its unique zero α. A fresh differentiation gives
$$f''(x)=\frac{2\log x-3}{x^3}.$$
It is concave on (0,e³ᐟ²) and convex on (e³ᐟ²,∞), with inflection ordinate e³ᐟ²+(3/2)e⁻³ᐟ².


**Final result**

$$
\text{Inflection at }\left(e^{3/2},e^{3/2}+\frac32e^{-3/2}\right)
$$

</div>

<div class="content-box">

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5534. -->

Analyze and sketch the following function:

$$
f(x)=e^{-x} \sqrt[3]{x^{2}}.
$$


**Solution.**

The real cube root makes the domain all ℝ. The function is nonnegative, neither even nor odd, and has its only intercept at the origin. At −∞ it tends to +∞; at +∞ it tends to zero, giving the right horizontal asymptote y=0. There is no vertical asymptote and no finite-slope oblique asymptote at −∞. For x≠0,
$$f'(x)=e^{-x}\left(\frac{2}{3\sqrt[3]x}-\sqrt[3]{x^2}\right)=\frac{e^{-x}(2-3x)}{3\sqrt[3]x}.$$
It is negative for x<0, positive for 0<x<2/3, and negative for x>2/3. At zero the left and right difference quotients tend respectively to −∞ and +∞; the origin is a cusp and the absolute minimum. The point at x=2/3 is a local maximum, with value e⁻²ᐟ³(4/9)¹ᐟ³. There is no absolute maximum because of the unbounded behavior at −∞. The source leaves the second derivative optional.


**Final result**

$$
\min f=f(0)=0;\quad\text{local maximum at }\left(\frac23,e^{-2/3}\sqrt[3]{\frac49}\right)
$$

</div>

<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 5655. -->

Analyze and sketch the following function:

$$
f(x)= \frac{2x^{2}+x+2}{x^{2}+1}.
$$


**Solution.**

Write f(x)=2+x/(x²+1). The domain is ℝ; the function is neither even nor odd and is strictly positive, since 2x²+x+2 has negative discriminant. Its only axis intercept is (0,2). Both limits at infinity equal 2, so y=2 is a bilateral horizontal asymptote; there are no vertical asymptotes. The derivatives are
$$f'(x)=\frac{1-x^2}{(1+x^2)^2},\qquad f''(x)=\frac{2x(x^2-3)}{(1+x^2)^3}.$$
The function decreases on (−∞,−1), increases on (−1,1) and decreases on (1,∞). Hence f(−1)=3/2 is the absolute minimum and f(1)=5/2 the absolute maximum. The second derivative is negative on (−∞,−√3), positive on (−√3,0), negative on (0,√3), and positive on (√3,∞). All three sign-changing zeros give inflections:
$$(-\sqrt3,2-\sqrt3/4),\qquad(0,2),\qquad(\sqrt3,2+\sqrt3/4).$$


**Final result**

$$
\min f=\frac32,\quad\max f=\frac52;\quad\text{inflection abscissae }-\sqrt3,0,\sqrt3
$$

</div>
<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
