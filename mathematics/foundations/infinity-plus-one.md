---
date: 2025-04-14
layout: default
title: "What Is Infinity Plus One?"
permalink: /mathematics/foundations/infinity-plus-one/
redirect_from:
  - /odd-questions/infinity-plus-one/
background_image: "/images/odd-infinity.png"
description: "What does infinity plus one mean? Compare limits, extended real numbers, cardinal arithmetic, and ordinal arithmetic."
area: mathematics
topic: foundations
content_type: article
---

<div class="content-box">

<h1>What Is Infinity Plus One?</h1>

The expression $\infty+1$ has no meaning in ordinary real arithmetic, because infinity is not a real number. It acquires a meaning only after the mathematical context has been specified.

The most familiar context is calculus, where $+\infty$ describes unbounded behavior. Analysis can also enlarge the real line by adjoining two infinite elements. Set theory introduces a different distinction: cardinal numbers measure the size of sets, whereas ordinal numbers describe ordered arrangements. The same informal phrase, infinity plus one, therefore corresponds to several different statements.

</div>

<div class="content-box">

<h2>Infinity in Limits</h2>

Consider

$$
\lim_{x\to+\infty}(x+1)=+\infty.
$$

This does not result from substituting an infinite number for $x$. It states that $x+1$ eventually exceeds every prescribed real bound. More precisely, for every real number $M$, there exists a real number $N$ such that

$$
x>N
\quad\Longrightarrow\quad
x+1>M.
$$

Adding one does not alter the unbounded behavior of the function. The same is true more generally when a fixed real constant is added:

$$
f(x)\to+\infty
\quad\Longrightarrow\quad
f(x)+c\to+\infty.
$$

The statement concerns the eventual values of a function, rather than an arithmetic operation performed on an object called infinity. This is also why expressions such as

$$
+\infty-\infty
$$

cannot be simplified algebraically in a limit. Two functions may both tend to $+\infty$, while their difference tends to a finite number, tends to either infinity, or fails to have a limit.

</div>

<div class="content-box">

<h2>The Extended Real Line</h2>

For some purposes, analysis enlarges the real line by adjoining two elements:

$$
\overline{\mathbb R}
=
\mathbb R\cup\{-\infty,+\infty\}.
$$

In this system one defines, for every real number $a$,

$$
+\infty+a=+\infty,
\qquad
-\infty+a=-\infty.
$$

Consequently,

$$
+\infty+1=+\infty
$$

is a valid formula in the extended real line. It expresses an arithmetic convention compatible with the order of the extension: $+\infty$ remains greater than every real number after a finite quantity is added.

The extended real line is not a field. Operations such as

$$
+\infty+(-\infty),
\qquad
0\cdot\infty,
\qquad
\frac{\infty}{\infty}
$$

remain undefined. The familiar algebraic rules of the real numbers therefore cannot be transferred to it without restrictions.

</div>

<div class="content-box">

<h2>Cardinal Numbers</h2>

Cardinal numbers measure the size of sets. Two sets have the same cardinality when there is a bijection between them: every element of the first set is paired with exactly one element of the second, and conversely.

The natural numbers have cardinality

$$
|\mathbb N|=\aleph_0.
$$

To add two cardinal numbers, one takes two disjoint sets having those cardinalities and measures the size of their union. If

$$
|A|=\kappa,
\qquad
|B|=\lambda,
\qquad
A\cap B=\varnothing,
$$

then cardinal addition is defined by

$$
\kappa+\lambda=|A\cup B|.
$$

The requirement that the sets be disjoint prevents a common element from being counted only once. When the original sets overlap, disjoint copies can be formed by attaching different labels:

$$
A\times\{0\},
\qquad
B\times\{1\}.
$$

The labels serve only to distinguish the two copies.

Now add one new element, denoted by $a$, to the natural numbers. The cardinal sum $\aleph_0+1$ is the size of

$$
\mathbb N\cup\{a\},
$$

where $a\notin\mathbb N$. Define a map from this set to $\mathbb N$ by

$$
f(a)=0,
\qquad
f(n)=n+1
\quad\text{for }n\in\mathbb N.
$$

Every element of $\mathbb N\cup\{a\}$ receives a different natural number, and every natural number is reached. The map is therefore a bijection, so

$$
\aleph_0+1=\aleph_0.
$$

The equality compares sizes. It does not assert that the new element disappears; it asserts that the enlarged set can still be placed in one-to-one correspondence with the natural numbers.

The same method gives

$$
\aleph_0+\aleph_0=\aleph_0.
$$

Take two labelled copies of $\mathbb N$. Map the first copy to the even numbers and the second to the odd numbers:

$$
(n,0)\longmapsto 2n,
\qquad
(n,1)\longmapsto 2n+1.
$$

Together the two copies still form a countable set. Likewise, adding any finite number $m$ of elements gives

$$
\aleph_0+m=\aleph_0.
$$

Hilbert's Hotel is a spatial version of the first bijection. If every room numbered by a natural number is occupied, moving the guest in room $n$ to room $n+1$ leaves room $0$ free. The rearrangement illustrates why adjoining one element does not change countable cardinality; the bijection is the mathematical argument.

</div>

<div class="content-box">

<h2>Ordinal Numbers</h2>

Cardinality ignores order. Ordinal numbers retain it.

The ordinal

$$
\omega
$$

is the order type of the natural numbers in their usual order:

$$
0<1<2<3<\cdots.
$$

Ordinal addition is defined by placing one ordered set after another. Thus $\alpha+\beta$ is obtained by taking an ordered copy of $\alpha$ and placing a copy of $\beta$ after all its elements.

If one new element is placed after the entire sequence of natural numbers, the resulting order has type

$$
\omega+1.
$$

This order has a greatest element, whereas $\omega$ has none. They cannot be order-isomorphic, and therefore

$$
\omega+1\ne\omega.
$$

They do, however, have the same cardinality:

$$
|\omega+1|=|\omega|=\aleph_0.
$$

Placing the new element before the natural numbers gives

$$
1+\omega.
$$

The order

$$
a<0<1<2<3<\cdots
$$

is order-isomorphic to the natural numbers: send $a$ to $0$, the old $0$ to $1$, the old $1$ to $2$, and so on. Hence

$$
1+\omega=\omega,
\qquad
\omega+1>\omega.
$$

Ordinal addition is therefore not commutative. The position of the added element changes the order type even when it does not change the number of elements.

</div>

<div class="content-box">

<h2>The Four Meanings</h2>

The original expression can now be separated into four claims:

- In ordinary real arithmetic, $\infty+1$ is not defined.
- In a limit, $f(x)+1\to+\infty$ describes unbounded behavior.
- In the extended real line, $+\infty+1=+\infty$ is one of the rules of the extension.
- In set theory, $\aleph_0+1=\aleph_0$ for cardinal addition, whereas $\omega+1\ne\omega$ for ordinal addition.

The notation alone does not determine which of these claims is intended. The relevant mathematical structure must be specified before the expression can be evaluated.

---

[← Back to Foundations of Mathematics]({{ "/mathematics/foundations/" | relative_url }})

</div>