---
layout: default
area: mathematics
topic: calculus
level: university
content_type: solved-exercises
background_image: "/images/limiti.png"
permalink: /mathematics/calculus/mathematical-induction/
title: "Mathematical Induction: Proofs and Original Exercises"
description: "Induction, Peano\u2019s axiom, well-ordering, Bernoulli\u2019s inequality and a finite-sum identity."
date: 2026-10-10
last_modified_at: 2026-10-10
---

# Mathematical Induction: Proofs and Original Exercises


<div class="content-box">

The theory and selected worked exercises are adapted into English from *Eserciziario 2.1* by Antonino De Martino and Luana Manfredini. Original exercise statements and parameter cases are retained. Mathematical corrections are identified explicitly.

</div>

<div class="content-box">

## The Principle of Induction

> “Theories come and go, but examples stay forever.” — I. M. Gelfand, as quoted in the exercise book.

Let n₀ be an integer and Pₙ a predicate defined for integers n≥n₀. If the base case holds and every valid case implies the next, then all cases hold:
$$
P_{n_0},\qquad \forall n\ge n_0:\ P_n\Rightarrow P_{n+1}
\quad\Longrightarrow\quad\forall n\ge n_0:\ P_n.
$$
When the starting index is zero, this is Peano's fifth axiom: a subset F of the natural numbers that contains zero and contains the successor of each of its elements contains every natural number. Alternatively, induction follows from well-ordering: every nonempty subset of the natural numbers has a least element. A least counterexample cannot be the base case, and its predecessor would imply it, giving a contradiction.

</div>

<div class="content-box">

### Exercise 1

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 102. -->

Prove:

$$
2^n\le(n+1)!\quad(n\ge0)
$$



**Solution.**

The base case is 1≤1. Assume 2ⁿ≤(n+1)!. Since n≥0 implies 2≤n+2,
$$
2^{n+1}=2\cdot2^n\le2(n+1)!\le(n+2)(n+1)!=(n+2)!.
$$
This proves the induction step.

**Final result**

$$
2^n\le(n+1)!\quad(n\ge0)
$$

</div>

<div class="content-box">

### Exercise 2

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 117. -->

Prove:

$$
(1+a)^n\ge1+na\quad(n\ge0,\ a\ge-1)
$$



**Solution.**

For n=0 both sides are 1. Since 1+a≥0, multiplication preserves the induction hypothesis:
$$
(1+a)^{n+1}\ge(1+na)(1+a)=1+(n+1)a+na^2\ge1+(n+1)a.
$$
The term na² is nonnegative. This also treats the endpoint a=−1 (the zeroth power is interpreted as 1).

**Final result**

$$
(1+a)^n\ge1+na\quad(n\ge0,\ a\ge-1)
$$

</div>

<div class="content-box">

### Exercise 3

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 147. -->

Prove:

$$
\sum_{k=0}^n k=\frac{n(n+1)}2\quad(n\ge0)
$$



**Solution.**

For n=0 both sides vanish. Assume the identity through n, and add the next summand:
$$
\sum_{k=0}^{n+1}k=\frac{n(n+1)}2+(n+1)=\frac{(n+1)(n+2)}2.
$$
The expression on the right is exactly the claimed formula with n replaced by n+1.

**Final result**

$$
\sum_{k=0}^n k=\frac{n(n+1)}2\quad(n\ge0)
$$

</div>


<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
