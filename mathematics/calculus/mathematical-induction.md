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


<div class="content-box">

**Exercise editors and source:** **Antonino De Martino and Luana Manfredini**, *Eserciziario 2.1*. The original exercises and source theory are presented here in English for Logic & Motion.

</div>

# Mathematical Induction: Proofs and Original Exercises


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

### Exercise 4

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 132. -->

Solve the following exercise:

$$
\label{3}
		3^{n} \geq 2^{n+1} \qquad \forall n \geq 2.
$$


**Solution.**

For n=2, 9≥8. Assume 3ⁿ≥2ⁿ⁺¹. Multiplying by 3 and using 3≥2 proves the next case:
$$3^{n+1}\ge3\cdot2^{n+1}\ge2^{n+2}.$$
Both the base and induction step hold.

**Final result**

$$
3^n\ge2^{n+1}\quad\forall n\ge2
$$

</div>

<div class="content-box">

### Exercise 5

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 161. -->

Solve the following exercise:

$$
\label{5}
		\sum_{k=1}^{n}k^{2}=\frac{n(n+1)(2n+1)}{6} \qquad n \geq 1.
$$


**Solution.**

The base case n=1 gives 1=1. Add (n+1)² to the induction hypothesis:
$$\sum_{k=1}^{n+1}k^2=\frac{n(n+1)(2n+1)}6+(n+1)^2.$$
Factor (n+1) and combine the remaining terms:
$$\frac{(n+1)[2n^2+7n+6]}6=\frac{(n+1)(n+2)(2n+3)}6.$$
This is precisely the asserted formula at n+1.

**Final result**

$$
\sum_{k=1}^n k^2=\frac{n(n+1)(2n+1)}6\quad(n\ge1)
$$

</div>

<div class="content-box">

### Exercise 6

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 178. -->

Solve the following exercise:

$$
\label{6}
		\sum_{k=1}^{n}k^{3}=\biggl(\sum_{k=1}^{n} k \biggl)^{2} \qquad n \geq 1
$$


**Solution.**

For n=1 both sides equal one. Using the finite-sum identity established earlier, assume the sum of cubes through n equals n²(n+1)²/4. Then
$$\sum_{k=1}^{n+1}k^3=\frac{n^2(n+1)^2}4+(n+1)^3=\frac{(n+1)^2(n^2+4n+4)}4=\frac{(n+1)^2(n+2)^2}4.$$
The final expression is the square of the sum of the first n+1 integers. 

**Final result**

$$
\sum_{k=1}^n k^3=\left(\frac{n(n+1)}2\right)^2\quad(n\ge1)
$$

</div>

<div class="content-box">

### Exercise 7

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 225. -->

Prove that the following expression is divisible by 9 for every integer n≥1:

$$
\label{8}
		4^{n}+15n-1 \qquad \forall n\geq 1,
$$


**Solution.**

For n=1 the expression is 4+15−1=18, divisible by 9. Write Aₙ=4ⁿ+15n−1. The difference needed in the induction step is
$$A_{n+1}-4A_n=4^{n+1}+15n+14-4(4^n+15n-1)=18-45n=9(2-5n).$$
If 9 divides Aₙ, it divides 4Aₙ and this difference; therefore it divides Aₙ₊₁.

**Final result**

$$
9\mid(4^n+15n-1)\quad\forall n\ge1
$$

</div>

<div class="content-box">

### Exercise 8

<!-- Source: Eserciziario 2.1.tex, Ex beginning at line 242. -->

Solve the following exercise:

$$
\label{9}
		\sum_{k=1}^{n}(2k-1)=n^{2} \qquad  \forall n\geq 1.
$$


**Solution.**

For n=1 the sum is 1=1². Assume the sum through n is n². The next odd summand is 2(n+1)−1=2n+1, hence
$$\sum_{k=1}^{n+1}(2k-1)=n^2+2n+1=(n+1)^2.$$
This completes the induction.

**Final result**

$$
\sum_{k=1}^n(2k-1)=n^2\quad\forall n\ge1
$$

</div>
<div class="content-box">

[**Back to Calculus →**]({{ "/mathematics/calculus/" | relative_url }})

</div>
