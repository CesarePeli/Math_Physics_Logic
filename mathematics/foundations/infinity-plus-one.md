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

The expression \(\infty+1\) does not have a single mathematical meaning. Its value depends on the object represented by the infinity symbol and on the operation being used. In a limit, \(+\infty\) describes unbounded behavior; in the extended real numbers it is an added element with restricted arithmetic rules; in set theory, infinite cardinal and ordinal numbers are genuine mathematical objects, but they answer different questions.

The distinction matters because the same notation can lead to different results. For cardinal numbers, adding one element to a countably infinite set does not change its cardinality. For ordinal numbers, placing one element after an infinite sequence produces a new order type.

</div>

<div class="content-box">

<h2>Countability and Hilbert's Hotel</h2>

Hilbert's Hotel gives a concrete representation of countable infinity. Suppose that the rooms are indexed by the natural numbers

\[
\mathbb N=\{0,1,2,3,\ldots\}
\]

and that every room is occupied. A new guest can be accommodated by moving the guest in room \(n\) to room \(n+1\). The map

\[
f(n)=n+1
\]

pairs the original guests with the rooms \(1,2,3,\ldots\), leaving room \(0\) available.

The mathematical point is the existence of a bijection. If a new element \(a\) is added to \(\mathbb N\), the set

\[
\mathbb N\cup\{a\}
\]

can still be placed in one-to-one correspondence with \(\mathbb N\): assign \(a\) to \(0\) and \(n\) to \(n+1\). The two sets therefore have the same cardinality even though one is a proper subset of the other.

The same construction can accommodate a countably infinite collection of new guests. Represent the original and new guests by the disjoint union

\[
\mathbb N\times\{0,1\}.
\]

The map

\[
(n,0)\longmapsto 2n,
\qquad
(n,1)\longmapsto 2n+1
\]

is a bijection from this union to \(\mathbb N\). The even rooms receive one group and the odd rooms the other.

</div>

<div class="content-box">

<h2>Cardinal Addition</h2>

Cardinal numbers describe the size of sets without recording an order among their elements. The cardinality of \(\mathbb N\) is denoted by

\[
\aleph_0.
\]

Cardinal addition is defined through disjoint unions. The bijections above establish

\[
\aleph_0+1=\aleph_0
\]

and

\[
\aleph_0+\aleph_0=\aleph_0.
\]

These equalities do not say that one has disappeared. They say that the resulting sets can be paired element by element with the natural numbers. Finite intuition fails because an infinite set can have the same cardinality as one of its proper subsets.

The result extends to every finite natural number \(n\):

\[
\aleph_0+n=\aleph_0.
\]

It also extends to the addition of any two countably infinite sets. None of these formulas licenses the unrestricted manipulation of a generic infinity symbol; they belong specifically to cardinal arithmetic.

</div>

<div class="content-box">

<h2>Ordinal Addition</h2>

Ordinal numbers describe positions and order types. The ordinal

\[
\omega
\]

is the order type of the natural numbers in their usual order:

\[
0<1<2<3<\cdots.
\]

If one new element is placed after all natural numbers, the resulting order has type

\[
\omega+1.
\]

It contains a greatest element, whereas \(\omega\) does not. The two orders cannot therefore be isomorphic:

\[
\omega+1\ne\omega.
\]

They nevertheless have the same cardinality:

\[
|\omega+1|=|\omega|=\aleph_0.
\]

Placing the new element before the natural numbers gives a different result. The order

\[
a<0<1<2<3<\cdots
\]

has type \(1+\omega\), and it is order-isomorphic to \(\omega\). Consequently,

\[
1+\omega=\omega,
\qquad
\omega+1>\omega.
\]

Ordinal addition is not commutative. The position of the added part affects the order type, even when it does not affect cardinality. Thus the formula infinity plus one remains infinity is correct for \(\aleph_0+1\), but false for \(\omega+1\).

</div>

<div class="content-box">

<h2>Infinity in Limits</h2>

In elementary calculus, the statement

\[
\lim_{x\to+\infty}(x+1)=+\infty
\]

does not treat \(+\infty\) as a real number. It means that \(x+1\) eventually exceeds every prescribed real bound. More precisely, for every real number \(M\), there exists a number \(N\) such that

\[
x>N\quad\Longrightarrow\quad x+1>M.
\]

Adding one does not change the fact that the function is unbounded. The notation summarizes a pattern of behavior; it is not an equation obtained by substituting a number called infinity for \(x\).

This also explains why subtracting infinity from both sides is invalid. Expressions such as

\[
+\infty-\infty
\]

are indeterminate in limit calculations. Different functions may both tend to \(+\infty\), while their difference tends to a finite number, to either infinity, or has no limit.

</div>

<div class="content-box">

<h2>The Extended Real Numbers</h2>

Analysis sometimes enlarges the real line by adjoining two elements:

\[
\overline{\mathbb R}
=
\mathbb R\cup\{-\infty,+\infty\}.
\]

Within this extended system, useful conventions include

\[
+\infty+a=+\infty
\]

for every real \(a\), and

\[
\frac{1}{+\infty}=0
\]

when the latter notation is understood as a convention reflecting limiting behavior.

The extension is not a field. Several operations must remain undefined, including

\[
+\infty+(-\infty),\qquad
0\cdot\infty,\qquad
\frac{\infty}{\infty}.
\]

The restrictions prevent the ordinary algebra of real numbers from being applied where its hypotheses no longer hold.

</div>

<div class="content-box">

<h2>Four Different Statements</h2>

The notation can now be separated into four mathematically different claims:

- In cardinal arithmetic, \(\aleph_0+1=\aleph_0\).
- In ordinal arithmetic, \(\omega+1\ne\omega\), although \(1+\omega=\omega\).
- In a limit, \(x+1\to+\infty\) states that \(x+1\) is unbounded.
- In the extended real numbers, \(+\infty+1=+\infty\) is an adopted arithmetic rule within a structure that does not satisfy all the field axioms.

The symbol \(\infty\) acquires meaning from the mathematical structure in which it occurs. Specifying that structure is therefore part of the calculation.

---

[← Back to Foundations of Mathematics]({{ "/mathematics/foundations/" | relative_url }})

</div>