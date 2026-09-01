---
layout: default
date: 2026-08-24
original_date: 2025-08-31
title: "Solved Exercises — Recursively Defined Sequences"
permalink: /mathematics/calculus/sequences/
redirect_from:
  - /university/math/calculus-1/recurrence-sequences/
background_image: "/images/sequences.png"
description: "Ten solved exercises on recursively defined sequences, including monotonicity, bounds, induction proofs, fixed points, convergence, and divergence."
featured: false
area: mathematics
topic: calculus
subtopic: sequences
level: university
content_type: solved-exercises
---

<div class="content-box">

# Solved Exercises — Recursively Defined Sequences

## Theoretical Recall

A sequence {aₙ} is a function:

$$
a:\mathbb{N}\to\mathbb{R}.
$$

The only accumulation point of ℕ in the extended real line ℝ ∪ {±∞} is +∞, so limits of sequences are always taken as n → +∞.

### Key Results

- If {aₙ} converges, then it is bounded. The converse does not hold.

- **Monotone Convergence Theorem.** A monotone and bounded sequence converges.

- **Recursive sequences.** For k ∈ ℕ and a function:

$$
f:\mathbb{N}\times\mathbb{R}^{k+1}\to\mathbb{R},
$$

a recursive sequence can be defined by:

$$
\begin{cases}
a_{n+1}=f(n,a_n,\dots,a_{n-k}), & n\ge k,\\
a_0,\dots,a_k\in\mathbb{R}, & \text{initial data}.
\end{cases}
$$

Unlike explicit formulas, here each term depends on the previous ones; behavior depends critically on the initial values.

</div>


<div class="content-box">

## Worked Exercises

Below are ten selected recursive sequences. Each solution shows:

- study of monotonicity and boundedness,
- induction arguments when needed,
- passage to the limit via the fixed-point equation,
- final result isolated.

</div>

<div class="content-box">

### Exercise 1

$$
\begin{cases}
a_1=-\frac{3}{2},\\
a_{n+1}=a_n^{2}+4a_n+2.
\end{cases}
$$

**Solution.**

We first show that the interval [−2, −1] is invariant.

If:

$$
-2\le a_n\le-1,
$$

then:

$$
a_{n+1}+2
=
a_n^2+4a_n+4
=
(a_n+2)^2
\ge0.
$$

Therefore:

$$
a_{n+1}\ge-2.
$$

Moreover:

$$
a_{n+1}+1
=
a_n^2+4a_n+3
=
(a_n+1)(a_n+3).
$$

For −2 ≤ aₙ ≤ −1:

$$
a_n+1\le0,
$$

while:

$$
a_n+3>0.
$$

Hence:

$$
a_{n+1}+1\le0,
$$

so:

$$
a_{n+1}\le-1.
$$

Since a₁ = −3/2 belongs to [−2, −1], induction gives:

$$
-2\le a_n\le-1
$$

for every n.

Now:

$$
a_{n+1}-a_n
=
a_n^2+3a_n+2.
$$

Factorizing:

$$
a_{n+1}-a_n
=
(a_n+1)(a_n+2).
$$

On [−2, −1]:

$$
(a_n+1)(a_n+2)\le0.
$$

Therefore:

$$
a_{n+1}\le a_n.
$$

The sequence is decreasing and bounded below by −2, so it converges.

Let:

$$
a_n\to\ell.
$$

Passing to the limit:

$$
\ell=\ell^2+4\ell+2.
$$

Therefore:

$$
\ell^2+3\ell+2=0.
$$

Thus:

$$
(\ell+1)(\ell+2)=0.
$$

Hence:

$$
\ell\in\{-2,-1\}.
$$

Since the sequence is decreasing and starts from:

$$
a_1=-\frac32,
$$

it cannot converge to −1.

**Final Result**

$$
\lim_{n\to\infty}a_n=-2
$$


</div>

<div class="content-box">

### Exercise 2

$$
\begin{cases}
a_1=2,\\
a_{n+1}=2\sqrt{a_n}.
\end{cases}
$$

**Solution.**

We show that:

$$
0\le a_n\le4.
$$

The initial value satisfies:

$$
0\le a_1=2\le4.
$$

If 0 ≤ aₙ ≤ 4, then:

$$
0\le2\sqrt{a_n}\le4.
$$

Hence:

$$
0\le a_{n+1}\le4.
$$

Therefore [0,4] is invariant.

For 0 ≤ aₙ ≤ 4:

$$
2\sqrt{a_n}\ge a_n.
$$

Thus:

$$
a_{n+1}\ge a_n.
$$

The sequence is increasing and bounded above by 4, so it converges.

Let:

$$
a_n\to\ell.
$$

Then:

$$
\ell=2\sqrt{\ell}.
$$

Squaring:

$$
\ell^2=4\ell.
$$

Therefore:

$$
\ell(\ell-4)=0.
$$

Since aₙ ≥ 2:

$$
\ell=4.
$$

**Final Result**

$$
\lim_{n\to\infty}a_n=4
$$


</div>

<div class="content-box">

### Exercise 3

$$
\begin{cases}
a_1=5,\\
a_{n+1}=\dfrac{a_n}{\frac12+a_n}.
\end{cases}
$$

**Solution.**

For aₙ > 0:

$$
\frac{a_n}{\frac12+a_n}\le a_n
$$

is equivalent to:

$$
\frac{1}{\frac12+a_n}\le1.
$$

Hence:

$$
a_n\ge\frac12.
$$

We now show that [1/2, +∞) is invariant.

If:

$$
a_n\ge\frac12,
$$

then:

$$
\frac{a_n}{\frac12+a_n}\ge\frac12.
$$

Indeed, this is equivalent to:

$$
2a_n\ge\frac12+a_n,
$$

that is:

$$
a_n\ge\frac12.
$$

Thus:

$$
a_{n+1}\ge\frac12.
$$

Since a₁ = 5, induction gives:

$$
a_n\ge\frac12.
$$

Therefore:

$$
a_{n+1}\le a_n.
$$

The sequence is decreasing and bounded below, so it converges.

Let:

$$
a_n\to\ell.
$$

Then:

$$
\ell
=
\frac{\ell}{\frac12+\ell}.
$$

Multiplying:

$$
\ell\left(\frac12+\ell\right)=\ell.
$$

Hence:

$$
\ell\left(\ell-\frac12\right)=0.
$$

Since:

$$
\ell\ge\frac12,
$$

we obtain:

$$
\ell=\frac12.
$$

**Final Result**

$$
\lim_{n\to\infty}a_n=\frac12
$$


</div>

<div class="content-box">

### Exercise 4

$$
\begin{cases}
a_1=\frac12,\\
a_{n+1}=a_n^3.
\end{cases}
$$

**Solution.**

By induction:

$$
0\le a_n\le1.
$$

For every aₙ in [0,1]:

$$
a_n^3\le a_n.
$$

Therefore:

$$
a_{n+1}\le a_n.
$$

The sequence is decreasing and bounded below by zero, so it converges.

Let:

$$
a_n\to\ell.
$$

Passing to the limit:

$$
\ell=\ell^3.
$$

Thus:

$$
\ell(\ell-1)(\ell+1)=0.
$$

Hence:

$$
\ell\in\{-1,0,1\}.
$$

Since:

$$
0\le\ell\le\frac12,
$$

only zero is possible.

**Final Result**

$$
\lim_{n\to\infty}a_n=0
$$


</div>

<div class="content-box">

### Exercise 5 — Parameter a > 0

$$
\begin{cases}
a_1=a,\\
a_{n+1}=\frac12(a+a_n^2).
\end{cases}
$$

**Solution.**

A finite limit ℓ must satisfy:

$$
\ell=\frac12(a+\ell^2).
$$

Therefore:

$$
\ell^2-2\ell+a=0.
$$

For 0 < a < 1, the two fixed points are:

$$
\ell_-=1-\sqrt{1-a},
$$

and:

$$
\ell_+=1+\sqrt{1-a}.
$$

We compare the initial value a with the smaller fixed point.

Since:

$$
a
=
(1-\sqrt{1-a})(1+\sqrt{1-a}),
$$

and:

$$
1+\sqrt{1-a}>1,
$$

we obtain:

$$
a>\ell_-.
$$

Moreover:

$$
a<1<\ell_+.
$$

Thus:

$$
\ell_-<a_1<\ell_+.
$$

Now:

$$
a_{n+1}-a_n
=
\frac12(a+a_n^2-2a_n).
$$

Factorizing:

$$
a_{n+1}-a_n
=
\frac12(a_n-\ell_-)(a_n-\ell_+).
$$

For:

$$
\ell_-<a_n<\ell_+,
$$

we therefore have:

$$
a_{n+1}-a_n<0.
$$

Thus the sequence is decreasing.

We also show that it remains above ℓ₋.

Since:

$$
a=2\ell_- -\ell_-^2,
$$

we obtain:

$$
a_{n+1}-\ell_-
=
\frac12(a_n^2-\ell_-^2).
$$

Hence:

$$
a_{n+1}-\ell_-
=
\frac12(a_n-\ell_-)(a_n+\ell_-).
$$

If aₙ ≥ ℓ₋, then:

$$
a_{n+1}\ge\ell_-.
$$

The sequence is therefore decreasing and bounded below by ℓ₋.

Hence:

$$
\ell=1-\sqrt{1-a}.
$$

If a = 1, then:

$$
a_1=1,
$$

and the sequence is constant:

$$
a_n=1.
$$

Now suppose a > 1.

Then:

$$
a_{n+1}-a_n
=
\frac12\left[(a_n-1)^2+a-1\right].
$$

Since a > 1:

$$
a_{n+1}-a_n>0.
$$

Thus the sequence is strictly increasing.

If it had a finite limit, that limit would satisfy:

$$
\ell^2-2\ell+a=0.
$$

But the discriminant is:

$$
4-4a<0.
$$

There is no real fixed point. Therefore the increasing sequence cannot have a finite limit and is unbounded above.

**Final Result**

$$
\lim_{n\to\infty}a_n=
\begin{cases}
1-\sqrt{1-a}, & 0<a<1,\\
1, & a=1,\\
+\infty, & a>1.
\end{cases}
$$


</div>

<div class="content-box">

### Exercise 6

$$
\begin{cases}
a_1=\frac32,\\
a_{n+1}=\frac{a_n}{2}+\frac{1}{a_n}.
\end{cases}
$$

**Solution.**

For aₙ > 0:

$$
a_{n+1}-\sqrt2
=
\frac{a_n}{2}
+
\frac{1}{a_n}
-
\sqrt2.
$$

Combining the terms:

$$
a_{n+1}-\sqrt2
=
\frac{(a_n-\sqrt2)^2}{2a_n}.
$$

Therefore:

$$
a_{n+1}\ge\sqrt2.
$$

Since:

$$
a_1=\frac32>\sqrt2,
$$

we have:

$$
a_n\ge\sqrt2
$$

for every n.

Now:

$$
a_{n+1}-a_n
=
-\frac{a_n}{2}+\frac{1}{a_n}.
$$

Hence:

$$
a_{n+1}-a_n
=
\frac{2-a_n^2}{2a_n}.
$$

Since aₙ ≥ √2:

$$
a_{n+1}-a_n\le0.
$$

The sequence is decreasing and bounded below by √2, so it converges.

Let:

$$
a_n\to\ell.
$$

Then:

$$
\ell
=
\frac{\ell}{2}
+
\frac{1}{\ell}.
$$

Multiplying by 2ℓ:

$$
2\ell^2=\ell^2+2.
$$

Therefore:

$$
\ell^2=2.
$$

Since all terms are positive:

$$
\ell=\sqrt2.
$$

**Final Result**

$$
\lim_{n\to\infty}a_n=\sqrt2
$$


</div>

<div class="content-box">

### Exercise 7 — Parameter α > 0

$$
\begin{cases}
a_0=\alpha,\\
a_{n+1}=a_n^2-a_n+1.
\end{cases}
$$

**Solution.**

Compute:

$$
a_{n+1}-a_n
=
a_n^2-2a_n+1.
$$

Therefore:

$$
a_{n+1}-a_n
=
(a_n-1)^2\ge0.
$$

The sequence is increasing.

If:

$$
0<\alpha\le1,
$$

we show that the sequence remains in [0,1].

If:

$$
0<a_n\le1,
$$

then:

$$
a_{n+1}
=
1-a_n(1-a_n).
$$

Therefore:

$$
0<a_{n+1}\le1.
$$

Thus [0,1] is invariant.

The sequence is increasing and bounded above by 1, so it converges.

Let:

$$
a_n\to\ell.
$$

Then:

$$
\ell=\ell^2-\ell+1.
$$

Hence:

$$
(\ell-1)^2=0.
$$

Therefore:

$$
\ell=1.
$$

If α > 1, the sequence is strictly increasing and:

$$
a_n\ge\alpha>1.
$$

A finite limit would again have to equal 1, which is impossible.

Therefore the sequence is unbounded above.

**Final Result**

$$
\lim_{n\to\infty}a_n=
\begin{cases}
1, & 0<\alpha\le1,\\
+\infty, & \alpha>1.
\end{cases}
$$


</div>

<div class="content-box">

### Exercise 8

$$
\begin{cases}
a_1=\frac12,\\
a_{n+1}=\frac{1}{4-a_n}.
\end{cases}
$$

**Solution.**

The fixed points satisfy:

$$
\ell=\frac{1}{4-\ell}.
$$

Therefore:

$$
\ell^2-4\ell+1=0.
$$

Hence:

$$
\ell=2\pm\sqrt3.
$$

Let:

$$
\alpha=2-\sqrt3.
$$

Since:

$$
\alpha<\frac12,
$$

the initial value satisfies:

$$
\alpha\le a_1\le\frac12.
$$

Consider:

$$
f(x)=\frac{1}{4-x}.
$$

This function is increasing on the interval under consideration.

Since α is a fixed point:

$$
f(\alpha)=\alpha.
$$

If:

$$
\alpha\le a_n\le\frac12,
$$

then:

$$
a_{n+1}\ge\alpha.
$$

Moreover:

$$
a_{n+1}
\le
f\left(\frac12\right)
=
\frac{2}{7}
<
\frac12.
$$

Thus [α, 1/2] is invariant.

Now:

$$
a_{n+1}-a_n
=
\frac{1}{4-a_n}-a_n.
$$

Combining terms:

$$
a_{n+1}-a_n
=
\frac{a_n^2-4a_n+1}{4-a_n}.
$$

Factorizing:

$$
a_{n+1}-a_n
=
\frac{
(a_n-(2-\sqrt3))(a_n-(2+\sqrt3))
}{
4-a_n
}.
$$

For:

$$
2-\sqrt3\le a_n\le\frac12,
$$

the numerator is non-positive and the denominator is positive.

Therefore:

$$
a_{n+1}\le a_n.
$$

The sequence is decreasing and bounded below by 2 − √3, so it converges.

The only fixed point in the invariant interval is:

$$
2-\sqrt3.
$$

**Final Result**

$$
\lim_{n\to\infty}a_n=2-\sqrt3
$$


</div>

<div class="content-box">

### Exercise 9

$$
\begin{cases}
a_1=4,\\
a_{n+1}=2\sqrt{a_n^2-6}.
\end{cases}
$$

**Solution.**

Since:

$$
a_1=4,
$$

the recursion is well defined.

For positive terms:

$$
a_{n+1}\ge a_n
$$

is equivalent to:

$$
2\sqrt{a_n^2-6}\ge a_n.
$$

Squaring:

$$
4(a_n^2-6)\ge a_n^2.
$$

Thus:

$$
3a_n^2\ge24.
$$

Therefore:

$$
a_n\ge2\sqrt2.
$$

Since:

$$
a_1=4>2\sqrt2,
$$

and the sequence is increasing, this condition remains satisfied.

Hence:

$$
a_{n+1}\ge a_n.
$$

Suppose the sequence had a finite limit ℓ. Then:

$$
\ell
=
2\sqrt{\ell^2-6}.
$$

Squaring:

$$
\ell^2
=
4\ell^2-24.
$$

Therefore:

$$
3\ell^2=24.
$$

Hence:

$$
\ell=2\sqrt2.
$$

But:

$$
a_n\ge a_1=4>2\sqrt2,
$$

which is incompatible with convergence to 2√2.

Thus the increasing sequence is not bounded above.

**Final Result**

$$
\lim_{n\to\infty}a_n=+\infty
$$


</div>

<div class="content-box">

### Exercise 10

$$
\begin{cases}
a_1=\frac{\pi}{2},\\
a_{n+1}=\sin a_n.
\end{cases}
$$

**Solution.**

On [0, π/2]:

$$
0\le\sin t\le t.
$$

Since:

$$
a_1=\frac{\pi}{2},
$$

induction gives:

$$
0\le a_n\le\frac{\pi}{2}.
$$

Moreover:

$$
a_{n+1}=\sin a_n\le a_n.
$$

Thus the sequence is decreasing and bounded below by zero.

Therefore it converges.

Let:

$$
a_n\to\ell.
$$

By continuity of the sine function:

$$
\ell=\sin\ell.
$$

On [0, π/2], the only solution is:

$$
\ell=0.
$$

**Final Result**

$$
\lim_{n\to\infty}a_n=0
$$


</div>




<div class="content-box">

## Continue Exploring Calculus

Recursively defined sequences show how local rules can generate global behavior. Monotonicity, invariant intervals, boundedness, and fixed points provide a systematic way to study convergence.

The initial value is often decisive: the same recurrence relation can converge or diverge depending on where the sequence begins.

[**Explore Limits →**]({{ "/mathematics/calculus/limits/" | relative_url }})

[**Explore Series →**]({{ "/mathematics/calculus/series/" | relative_url }})

[**← Back to Calculus**]({{ "/mathematics/calculus/" | relative_url }})

</div>