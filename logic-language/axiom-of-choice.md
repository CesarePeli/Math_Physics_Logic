---
layout: default
date: 2026-08-30
title: "Choice and Infinity: The Axiom of Choice"
author: Cesare Peli
permalink: /logic-language/axiom-of-choice/
background_image: "/images/assioma.png"
description: "Explore the axiom of choice through choice functions, well-ordering, cardinality, Zorn's lemma, vector-space bases, and non-measurable sets."
area: logic-language
content_type: article
---

<div class="content-box">

# Choice and Infinity: The Axiom of Choice

*By Cesare Peli*

## Introduction

Choosing an element from a nonempty set seems entirely obvious. If there are only finitely many sets, we can consider them one after another and take one element from each. Some infinite cases are also simple: from every nonempty subset of the natural numbers, for example, we can choose the least number.

The axiom of choice concerns the passage to the most general case. Consider a possibly infinite family of nonempty sets. We know that each of them contains at least one element, and we want to collect all the choices in a single function, called a choice function. This function must assign to each set in the family one of its elements.

The axiom of choice states that such a function always exists.

The statement may seem almost trivial. If every set contains something, why should it be impossible to choose an element from each? The logical point is that these are two different claims. To say that every set contains at least one element is to assert separately the existence of many elements; to say that a choice function exists is to assert the existence of a single mathematical object that makes all the choices simultaneously. For a finite family, the second claim follows from the first. For an arbitrary infinite family, this passage requires an additional principle.

Zermelo–Fraenkel set theory, abbreviated ZF, lays down through a number of basic axioms how sets may be formed and related. Since numbers, functions, and many other mathematical structures can be represented in terms of sets, ZF is one of the most widely used foundations of modern mathematics. The axioms of ZF alone do not prove that a choice function exists for every family of nonempty sets. When the axiom of choice is added, the resulting theory is called ZFC.

The choice between ZF and ZFC has far-reaching consequences. Assuming the axiom of choice, one can prove that every set admits an ordering in which each nonempty subset has a first element, and that any two sets can always be compared in size. Without the axiom, these results are not guaranteed. In some theories without suitable forms of choice, even the union of a sequence of countable sets need not be countable.

Gödel and Cohen proved that the axiom of choice can be neither proved nor refuted from the other axioms of ZF, provided that ZF is consistent. It is therefore possible to develop a set theory in which the axiom of choice holds and another in which it does not. The two theories share a vast part of mathematics, but diverge on fundamental results concerning infinite sets and the objects whose existence can be proved.

The historical origin of the axiom lies in Cantor's study of infinity. Cantor had shown that infinite sets can have different sizes and had attempted to arrange them in a hierarchy. In 1904 Zermelo explicitly introduced the axiom of choice to prove that every set can be ordered so that each of its nonempty subsets has a first element. A principle that, considered in isolation, appears almost self-evident thus made it possible to solve one of the central problems of set theory.

To understand the scope of the axiom, we must therefore clarify how infinite sets are compared, what it means to order them, and how many simultaneous choices can be represented by a function. From these concepts emerge both the equivalent formulations of the axiom and the consequences that distinguish mathematics developed with the axiom of choice from mathematics developed without it.

</div>

<div class="content-box">

## Cardinality and equipotent sets

To compare two finite sets, we count their elements. With infinite sets, this process cannot be completed in the same way. The comparison is instead made by matching the elements of one set with those of the other.

Two sets $A$ and $B$ are called **equipotent** when there is a one-to-one correspondence, or bijection, between them. This means that each element of $A$ is associated with exactly one element of $B$, distinct elements of $A$ have distinct images, and no element of $B$ is left out.

In symbols, we write

$$
A\sim B
$$

or

$$
|A|=|B|.
$$

The notation $|A|$ denotes the cardinality of $A$. Equipotent sets have the same cardinality.

Consider the set of natural numbers

$$
\mathbb N=\{0,1,2,3,\ldots\}
$$

and its subset consisting of the even numbers:

$$
P=\{0,2,4,6,\ldots\}.
$$

The function

$$
f(n)=2n
$$

associates each natural number with an even number. The correspondence is bijective: different natural numbers produce different even numbers, and every even number is twice a unique natural number.

It follows that

$$
|\mathbb N|=|P|.
$$

The set of even numbers is a proper subset of $\mathbb N$, since it does not contain the odd numbers, yet it has the same cardinality as $\mathbb N$. The possibility that a set may be equipotent to one of its proper subsets is a fundamental feature of infinite sets.

Infinite sets do not all have the same cardinality. Cantor proved that the set of real numbers is not equipotent to the set of natural numbers. There is therefore no sequence

$$
x_0,x_1,x_2,\ldots
$$

that contains every real number. The set $\mathbb N$ is countable, whereas $\mathbb R$ is not.

To compare sets that may have different cardinalities, we use injective functions. A function

$$
f:A\longrightarrow B
$$

is injective when distinct elements of $A$ have distinct images in $B$. The existence of an injection from $A$ to $B$ shows that the elements of $A$ can be placed in $B$ without overlap.

In this case, we write

$$
|A|\leq |B|.
$$

The formula means that there is an injection from $A$ into $B$.

The Cantor–Schröder–Bernstein theorem states that if there is an injection from $A$ into $B$ and also an injection from $B$ into $A$, then the two sets are equipotent:

$$
|A|\leq |B| \quad\text{and}\quad |B|\leq |A|
\quad\Longrightarrow\quad |A|=|B|.
$$

For finite sets, two cardinalities are always comparable. Given two sets $A$ and $B$, one of them has no more elements than the other. For infinite sets, the comparison is expressed by the question

$$
|A|\leq |B| \quad\text{or}\quad |B|\leq |A|?
$$

In words: given any two sets, is there always an injection from one into the other?

The definition of cardinality alone does not answer this question. Cantor's theory settled it for well-orderable sets. It remained to establish whether every set could be well-ordered.

</div>

<div class="content-box">

## Transfinite cardinals and the alephs

Cantor introduced new numbers to represent the cardinalities of infinite sets. He denoted them by the Hebrew letter $\aleph$, *aleph*, the first letter of the Hebrew alphabet.

The first transfinite cardinal is written

$$
\aleph_0,
$$

and is read “aleph zero.” The subscript $0$ indicates that it is the first cardinal in the sequence of alephs. The cardinal $\aleph_0$ is the cardinality of the natural numbers:

$$
|\mathbb N|=\aleph_0.
$$

Every infinite set equipotent to $\mathbb N$ has cardinality $\aleph_0$. The integers $\mathbb Z$ and the rational numbers $\mathbb Q$, for example, are countable.

The next aleph is denoted by $\aleph_1$. It is the cardinality of the set of all countable ordinals and is the least uncountable **well-orderable** cardinal. In ZFC, where every set can be well-ordered, it is simply the least cardinal strictly greater than $\aleph_0$. It is followed by $\aleph_2,\aleph_3$, and so on, with the alephs indexed by all ordinals.

Cantor had proved that

$$
|\mathbb R|>\aleph_0.
$$

The cardinality of the real numbers is also denoted by

$$
\mathfrak c,
$$

where $\mathfrak c$ stands for the continuum. In ZFC, the continuum hypothesis states that

$$
\mathfrak c=\aleph_1,
$$

or equivalently that no cardinality lies strictly between that of the natural numbers and that of the real numbers.

To place every set within the hierarchy of the alephs, its cardinality must be associated with an ordinal. This is possible for well-orderable sets. The problem was therefore to prove that every set, including $\mathbb R$, could be given a well-ordering.

</div>

<div class="content-box">

## Orders and well-orders

An order establishes which elements precede which others. On the natural numbers, we normally use the relation

$$
0<1<2<3<\cdots.
$$

This order is total: given any two distinct natural numbers, one precedes the other.

A totally ordered set is **well-ordered** when each of its nonempty subsets has a least element.

The set $\mathbb N$, with its usual order, is well-ordered. Consider, for example, the subset of natural numbers greater than $10$:

$$
\{11,12,13,\ldots\}.
$$

Its least element is $11$. The same property holds for every nonempty subset of $\mathbb N$.

The set of integers

$$
\mathbb Z=\{\ldots,-2,-1,0,1,2,\ldots\}
$$

is not well-ordered by the usual relation. The set $\mathbb Z$ itself has no least element: for every integer $n$, the integer $n-1$ is smaller.

This does not prevent us from assigning a different order to $\mathbb Z$. We can arrange the integers in the sequence

$$
0,1,-1,2,-2,3,-3,\ldots
$$

and declare that one integer precedes another when it appears earlier in the sequence.

With respect to this new order, $\mathbb Z$ is well-ordered. Every nonempty subset of the integers contains an element that appears first in the list.

The same set can therefore be ordered in different ways. Being well-ordered is a property of a set together with the order relation assigned to it.

The usual order on $\mathbb R$ is not a well-order either. The subset

$$
(0,1)=\{x\in\mathbb R:0<x<1\}
$$

has no least element. Given any $x\in(0,1)$, the number $x/2$ also belongs to the interval and is smaller than $x$.

To say that $\mathbb R$ can be well-ordered does not mean that the usual numerical order is a well-order. It means that there is another relation, which we may denote by $\prec$, with respect to which every nonempty subset of the real numbers has a first element.

For $\mathbb Z$, we explicitly exhibited a well-order. For $\mathbb R$, the axiom of choice guarantees the existence of a well-order without providing a comparably explicit description of it.

</div>

<div class="content-box">

## Isomorphisms and ordinals

Two ordered sets may contain different elements and still have the same order structure.

Consider

$$
A=\{1,2,3\}
$$

with the usual order, and

$$
B=\{a,b,c\}
$$

with

$$
a\prec b\prec c.
$$

The function

$$
f(1)=a,\qquad f(2)=b,\qquad f(3)=c
$$

is a bijection that preserves the order: $x<y$ in $A$ if and only if $f(x)\prec f(y)$ in $B$.

A bijection of this kind is called an **order isomorphism**. Two ordered sets are isomorphic when there is a bijection between them that preserves the order. Their elements may be entirely different; what remains the same is the way in which they are arranged.

Ordinals represent the order types of well-ordered sets. Every well-ordered set is order-isomorphic to a unique ordinal.

For finite sets, cardinality and order type essentially coincide. Any total ordering of a three-element set has three successive positions.

For infinite sets, the two notions come apart. Consider the usual order of the natural numbers,

$$
0,1,2,3,\ldots,
$$

and an order in which a new element is placed after all the natural numbers:

$$
0,1,2,3,\ldots,\omega.
$$

The two sets have the same cardinality: both are countable. Their order types are different. The first order is represented by the ordinal $\omega$, the second by $\omega+1$.

Ordinals are always comparable. Given two ordinals $\alpha$ and $\beta$, either one precedes the other or they are equal. It follows that any two well-ordered sets are comparable: one is order-isomorphic to the other or to an initial segment of the other.

This property made well-ordering decisive for the comparison of cardinalities.

</div>

<div class="content-box">

## The problem left open by Cantor

The hierarchy of the alephs describes the cardinalities of well-orderable sets. If a set $A$ can be well-ordered, it can be associated with an ordinal, and the least ordinal equipotent to $A$ can be identified. The cardinality of this ordinal is an aleph.

It remained to prove that every set was well-orderable.

Without this result, one could not conclude that every cardinality belonged to the sequence of the alephs. Nor could one assert that, given arbitrary sets $A$ and $B$, there was always an injection from one into the other.

The point can be summarized as follows:

- ordinals are comparable;
- well-ordered sets are represented by ordinals;
- well-ordered sets are therefore comparable;
- to extend the comparison to all sets, one must prove that every set can be well-ordered.

Cantor regarded the well-ordering principle as valid, though he had not provided a satisfactory proof. In 1904 Zermelo addressed the problem by explicitly introducing the axiom of choice.

</div>

<div class="content-box">

## The choice function

Suppose that we are given a family of nonempty sets, denoted by

$$
\mathcal A=\{A_i\}_{i\in I}.
$$

The letter $I$ denotes the index set. For each $i\in I$, the set $A_i$ is one member of the family.

A **choice function** assigns to every index $i$ an element of the corresponding set $A_i$. In symbols,

$$
f(i)\in A_i \qquad\text{for every }i\in I.
$$

The formula simply says that $f$ chooses one element from each $A_i$.

If we have three sets

$$
A_1=\{a,b\},\qquad A_2=\{3,5,7\},\qquad A_3=\{\alpha,\beta\},
$$

one possible choice function is

$$
f(1)=b,\qquad f(2)=5,\qquad f(3)=\alpha.
$$

For a finite family, such a function can be constructed by making finitely many choices.

Some infinite families also admit a choice function defined by a rule. Suppose that each $A_i$ is a nonempty subset of $\mathbb N$. We can set

$$
f(i)=\min A_i.
$$

In this case the choice is not arbitrary: the least number is always selected.

The difficulty concerns an infinite family of sets for which no common rule is available. We know that

$$
A_i\neq\varnothing \qquad\text{for every }i\in I,
$$

so each set contains at least one element. We want to conclude that there is a single function $f$ that simultaneously chooses an element from every $A_i$.

The axiom of choice states precisely this:

> For every family of nonempty sets, there exists a choice function.

In set-theoretic notation,

$$
\bigl(\forall i\in I,\ A_i\neq\varnothing\bigr)
\quad\Longrightarrow\quad
\exists f\ \forall i\in I,\ f(i)\in A_i.
$$

In words: if every set in the family is nonempty, there is a function that chooses an element from each of them.

</div>

<div class="content-box">

## Zermelo and the well-ordering theorem

To well-order a set $A$, we may imagine choosing a first element, then an element from those that remain, then another element from those not yet chosen, and continuing the process.

A single choice presents no difficulty. The problem is to guarantee all the choices that are needed when $A$ is an arbitrary infinite set and no criterion determines which element should be selected at each stage.

Zermelo assumes a function defined on all nonempty subsets of $A$. If $X\subseteq A$ and $X\neq\varnothing$, the function assigns to $X$ an element

$$
f(X)\in X.
$$

Using this function, one can choose an element from those that have not yet been assigned a position whenever any remain. The construction leads to a well-ordering of $A$.

The full proof requires the theory of ordinals and methods that go beyond ordinary induction. For our purpose, the role of the axiom is what matters: the choice function supplies a next element whenever unplaced elements remain.

Zermelo therefore proved:

> Every set can be well-ordered.

This result is known as the **well-ordering theorem**.

The converse implication is simpler. Suppose that every set can be well-ordered, and consider a family $\mathcal A$ of nonempty sets. Well-order the union of all the sets in the family:

$$
X=\bigcup_{A\in\mathcal A}A.
$$

The symbol $\bigcup$ denotes the union: $X$ contains every element that belongs to at least one set in $\mathcal A$.

Each $A\in\mathcal A$ is a nonempty subset of $X$, so it has a least element with respect to the chosen well-order of $X$. We can define $f$ by assigning to every $A$ its least element.

We have thereby constructed a choice function. The well-ordering theorem implies the axiom of choice.

The two statements are therefore equivalent:

$$
\boxed{\text{axiom of choice}
\quad\Longleftrightarrow\quad
\text{every set can be well-ordered}}
$$

The equivalence clarifies the role of the axiom in Cantor's theory. Assuming the axiom of choice means being able to well-order every set; being able to well-order every set means being able to place every cardinality within the hierarchy of the alephs.

</div>

<div class="content-box">

## The Cartesian product of a family

The axiom of choice can also be formulated in terms of Cartesian products.

For two sets $A$ and $B$, the Cartesian product is the set of ordered pairs

$$
A\times B=\{(a,b):a\in A,\ b\in B\}.
$$

If

$$
A=\{1,2\}, \qquad B=\{x,y\},
$$

then

$$
A\times B=\{(1,x),(1,y),(2,x),(2,y)\}.
$$

Each pair contains one choice from $A$ and one choice from $B$.

The same idea extends to an indexed family $\{A_i\}_{i\in I}$. An element of the Cartesian product

$$
\prod_{i\in I}A_i
$$

consists of a choice of one element from each $A_i$. More precisely, it is a function $f$ such that

$$
f(i)\in A_i \qquad\text{for every }i\in I.
$$

For example, an element of

$$
\prod_{n\in\mathbb N}\{0,1\}
$$

is an infinite sequence of zeros and ones:

$$
(0,1,1,0,1,0,\ldots).
$$

At position $n$ appears the element chosen from the copy of $\{0,1\}$ indexed by $n$.

If every set $A_i$ is nonempty, the axiom of choice guarantees a function $f$ with $f(i)\in A_i$. This function is an element of the Cartesian product, which is therefore nonempty.

Conversely, if the Cartesian product is nonempty, any one of its elements is already a choice function.

It follows that

$$
\boxed{\text{axiom of choice}
\quad\Longleftrightarrow\quad
\text{every product of a family of nonempty sets is nonempty}}
$$

For a finite product, the result does not require the axiom. This formulation concerns products indexed by arbitrary infinite sets.

</div>

<div class="content-box">

## Comparability of cardinalities

The well-ordering theorem makes it possible to compare any two sets.

Let $A$ and $B$ be sets. By the axiom of choice, both can be well-ordered. Each is then order-isomorphic to an ordinal.

Since any two ordinals are comparable, one of the two sets can be injected into the other. At least one of the following relations therefore holds:

$$
|A|\leq |B| \qquad\text{or}\qquad |B|\leq |A|.
$$

In words: for every pair of sets, there is an injection from one into the other.

This principle also implies the axiom of choice. The universal comparability of cardinalities, the well-ordering theorem, and the axiom of choice are equivalent.

Without the axiom, ZF does not guarantee that two arbitrary cardinalities are comparable. Nor does it guarantee that every set is equipotent to an aleph. This is the gap that the axiom fills in Cantor's theory of transfinite cardinals.

</div>

<div class="content-box">

## Zorn's lemma

In many areas of mathematics, the axiom of choice is used through Zorn's lemma.

To understand its statement, consider a set $P$ equipped with a partial order. In a partial order, some elements may be incomparable.

The power set of a set $X$, denoted by $\mathcal P(X)$, provides an example. Its elements can be ordered by inclusion. If

$$
A=\{1\}, \qquad B=\{2\},
$$

then neither $A\subseteq B$ nor $B\subseteq A$. The two elements are incomparable.

A **chain** is a subset of $P$ whose elements are pairwise comparable. For example,

$$
\varnothing\subseteq\{1\}\subseteq\{1,2\}\subseteq\{1,2,3\}
$$

is a chain under inclusion.

An element $u\in P$ is an upper bound of a chain if every element of the chain precedes $u$.

An element $m\in P$ is maximal when there is no element strictly greater than $m$. A maximal element need not be a maximum. A maximum must be greater than every element of the set; a maximal element only has to admit no further extension.

Consider

$$
P=\bigl\{\{1\},\{2\}\bigr\}
$$

ordered by inclusion. Both $\{1\}$ and $\{2\}$ are maximal, since neither is contained in the other. There is no maximum.

Zorn's lemma states:

> If $P$ is a nonempty partially ordered set and every chain in $P$ has an upper bound in $P$, then $P$ contains at least one maximal element.

The lemma guarantees the existence of an object that cannot be extended further, provided that every chain of compatible extensions itself has an extension.

Zorn's lemma is equivalent to the axiom of choice.

To see the connection, consider a family of nonempty sets. We can form partial choice functions, initially defined on only some members of the family, and order them by extension. The union of a chain of compatible partial functions is again a partial choice function and is an upper bound of the chain.

Zorn's lemma therefore guarantees a maximal partial choice function. If this function were not defined on the whole family, we could take one set still outside its domain, choose one element from that set, and extend the function. This would contradict its maximality. The function must therefore be defined on the entire family.

This argument shows that

$$
\text{Zorn's lemma}\quad\Longrightarrow\quad\text{axiom of choice}.
$$

The converse implication follows from the well-ordering theorem. We thus obtain another equivalence:

$$
\boxed{\text{axiom of choice}\quad\Longleftrightarrow\quad\text{Zorn's lemma}}
$$

</div>

<div class="content-box">

## Why every vector space has a basis

We can now return to the result mentioned in the introduction.

Let $V$ be a vector space. A set of vectors is linearly independent when no nontrivial finite linear combination of its elements is equal to the zero vector.

In $\mathbb R^2$, for example, the vectors

$$
e_1=(1,0), \qquad e_2=(0,1)
$$

are linearly independent and span the whole space. Every vector $(x,y)$ can be written as

$$
(x,y)=xe_1+ye_2.
$$

The set $\{e_1,e_2\}$ is therefore a basis of $\mathbb R^2$.

For an arbitrary vector space, let $\mathcal L$ be the set of all linearly independent subsets of $V$, ordered by inclusion. The set $\mathcal L$ is nonempty because it contains the empty set.

Let $\mathcal C$ be any chain in $\mathcal L$, and consider its union

$$
L^*=\bigcup_{L\in\mathcal C}L.
$$

The set $L^*$ is still linearly independent. Every linear relation involves only finitely many vectors. Since the members of $\mathcal C$ are ordered by inclusion, all these vectors belong to a single member of the chain, which is linearly independent.

The union $L^*$ is therefore an upper bound of the chain in $\mathcal L$. The hypotheses of Zorn's lemma are satisfied, so there exists a maximal linearly independent set $B$.

It remains to show that $B$ spans all of $V$.

Suppose that some vector $v\in V$ is not a finite linear combination of elements of $B$. We could then add $v$ to $B$ and obtain a larger linearly independent set:

$$
B\cup\{v\}.
$$

This would contradict the maximality of $B$. Every vector in $V$ must therefore be a finite linear combination of elements of $B$.

The set $B$ is a basis.

The proof uses Zorn's lemma and therefore the axiom of choice. The converse is also true: over ZF, the universal statement that every vector space over every field has a basis implies the axiom of choice.

Without the axiom, we therefore cannot be certain that every arbitrary vector space has a basis. No difficulty arises for finitely generated vector spaces, since a basis can be obtained by a finite procedure. The axiom enters when the result is extended to all vector spaces.

</div>

<div class="content-box">

## Representatives and non-measurable sets

The axiom of choice makes it possible to select one representative from each equivalence class.

On the interval $[0,1]$, consider the relation

$$
x\sim y \quad\Longleftrightarrow\quad x-y\in\mathbb Q.
$$

The formula means that two real numbers are regarded as equivalent when their difference is rational.

For example,

$$
\frac{\sqrt2}{2}
\quad\text{and}\quad
\frac{\sqrt2}{2}+\frac1{10}
$$

belong to the same class because their difference is $1/10$, which is rational.

The relation partitions $[0,1]$ into equivalence classes. The axiom of choice allows us to select one element from each class. Let $V$ be the set of selected representatives. This is a **Vitali set**.

For each $q\in\mathbb Q\cap[-1,1]$, consider the translate

$$
V+q=\{v+q:v\in V\}.
$$

These translates are pairwise disjoint. Their union contains $[0,1]$ and is contained in the bounded interval $[-1,2]$.

If $V$ were measurable with measure zero, every rational translate would also have measure zero, and their countable union would have measure zero. This is impossible because the union contains $[0,1]$, which has measure one.

If $V$ had positive measure, the countably many disjoint translates would have infinite total measure. This too is impossible because their union lies inside the bounded interval $[-1,2]$.

Both possibilities lead to a contradiction. The set $V$ is therefore not Lebesgue measurable.

The axiom of choice does not provide an explicit description of the elements of $V$. It guarantees their existence by selecting a representative from each equivalence class.

</div>

<div class="content-box">

## The Banach–Tarski paradox

The Banach–Tarski paradox, published in 1924, states that a solid ball in three-dimensional space can be divided into finitely many parts and reassembled, by rotations and translations, into two balls congruent to the original.

The result appears to contradict the conservation of volume. The pieces cannot all be Lebesgue measurable. The usual rule that the volume of a union equals the sum of the volumes therefore cannot be applied to the decomposition.

The construction considers the action of certain rotations on the sphere and partitions points into orbits. A form of the principle of choice is used to select a representative from each orbit.

The word “paradox” therefore indicates a conflict with geometric intuition, not an internal contradiction in the theory.

Consequences of this kind contributed to resistance toward the axiom. The principle appeared reasonable in its formulation, yet it allowed the construction of sets lacking familiar geometric and analytic properties.

</div>

<div class="content-box">

## ZF and ZFC

Zermelo–Fraenkel set theory is denoted by ZF. Adding the axiom of choice gives ZFC:

$$
\mathrm{ZFC}=\mathrm{ZF}+\mathrm{AC}.
$$

The letter C comes from *Choice*.

The axiom of choice cannot be proved from the other axioms of ZF. Nor can it be refuted from those axioms, provided that ZF is consistent.

In 1938 Gödel announced, and in 1940 presented in detail, a construction of the **constructible universe**, a model in which both ZF and the axiom of choice hold. More precisely, his result shows that if ZF is consistent, then ZFC is consistent; indeed, the generalized continuum hypothesis also holds in the constructible universe.

In 1963 Cohen proved, by means of the method of forcing and symmetric models, that if ZF is consistent, then the theory obtained by adding the negation of the axiom of choice is also consistent.

Together, the two results establish the independence of the axiom from ZF. Assuming the consistency of ZF,

$$
\mathrm{ZF}\nvdash\mathrm{AC}
$$

and

$$
\mathrm{ZF}\nvdash\neg\mathrm{AC}.
$$

The symbol $\nvdash$ means “does not prove.” The formulas say that ZF proves neither the axiom of choice nor its negation.

These are results of relative consistency. They do not prove that ZF is consistent in an absolute sense. They state that if ZF contains no contradiction, then adding the axiom, or adding its negation, produces no contradiction either.

Mathematics can therefore be developed in different set theories. ZFC is the system most commonly used because the axiom simplifies cardinal arithmetic and guarantees many general results. There are also theories based on ZF or on weaker forms of choice.

</div>

<div class="content-box">

## Weaker forms of choice

The full axiom of choice concerns arbitrary families of nonempty sets. Weaker principles are also available.

The **axiom of countable choice** states that a choice function exists for every countable family of nonempty sets. Such a family can be indexed by the natural numbers:

$$
A_0,A_1,A_2,\ldots.
$$

The **axiom of dependent choice** concerns a nonempty set $X$ with a relation $R$ such that every element has an $R$-successor. It guarantees a sequence

$$
x_0,x_1,x_2,\ldots
$$

for which $x_n R x_{n+1}$ at every step. Each choice may therefore depend on the element chosen immediately before it.

These principles suffice for many results in analysis and do not imply the full axiom of choice over ZF.

The axiom of choice must therefore be distinguished from its weaker forms. Some theorems require the full principle; others can be proved with a more limited amount of choice.

The well-ordering theorem, the comparability of all cardinalities, Zorn's lemma, and the universal statement that every vector space has a basis are equivalent to the full axiom.

</div>

<div class="content-box">

## Conclusion

The axiom of choice arose from the problem of completing Cantor's theory of infinite cardinalities.

Cantor had shown that there are infinities of different sizes and had introduced the hierarchy of the alephs. Ordinals made it possible to compare well-ordered sets. It remained to prove that every set could be well-ordered and therefore placed within the hierarchy.

Zermelo obtained this result by assuming that one can simultaneously make a choice in each member of an arbitrary family of nonempty sets.

The principle can be formulated in different ways. The following are equivalent:

1. the axiom of choice;
2. the nonemptiness of the Cartesian product of every family of nonempty sets;
3. the well-ordering theorem;
4. the comparability of all cardinalities;
5. Zorn's lemma.

These equivalences show the reach of the axiom. It completes the classification of cardinalities, makes it possible to construct maximal structures, and guarantees that every vector space has a basis. It also allows the construction of non-measurable sets and enters the proof of the Banach–Tarski paradox.

Finally, the results of Gödel and Cohen show that the axiom is a genuine addition to ZF. Assuming it or rejecting it changes the objects whose existence the theory guarantees and the theorems that can be proved.

</div>

<div class="content-box">

## References

- Banach, Stefan, and Alfred Tarski. “Sur la décomposition des ensembles de points en parties respectivement congruentes.” *Fundamenta Mathematicae* 6 (1924): 244–277.

- Bell, John L. “The Axiom of Choice.” *The Stanford Encyclopedia of Philosophy*. First published 2008; substantive revision 10 December 2021. [https://plato.stanford.edu/entries/axiom-choice/](https://plato.stanford.edu/entries/axiom-choice/).

- Blass, Andreas. “Existence of Bases Implies the Axiom of Choice.” In *Axiomatic Set Theory*, edited by James E. Baumgartner, Donald A. Martin, and Saharon Shelah, 31–33. Contemporary Mathematics 31. Providence, RI: American Mathematical Society, 1984.

- Bottazzini, Umberto. *Il flauto di Hilbert: Storia della matematica moderna e contemporanea*. Turin: UTET Libreria, 1990.

- Cantor, Georg. *Contributions to the Founding of the Theory of Transfinite Numbers*. Translated and edited by Philip E. B. Jourdain. Chicago: Open Court, 1915.

- Cohen, Paul J. “The Independence of the Continuum Hypothesis.” *Proceedings of the National Academy of Sciences of the United States of America* 50, no. 6 (1963): 1143–1148. [https://doi.org/10.1073/pnas.50.6.1143](https://doi.org/10.1073/pnas.50.6.1143).

- Gödel, Kurt. *The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis with the Axioms of Set Theory*. Annals of Mathematics Studies 3. Princeton, NJ: Princeton University Press, 1940.

- Halmos, Paul R. *Teoria elementare degli insiemi*. Translated by M. Luisa Vesentini Ottolenghi and Edoardo Vesentini. Milan: Feltrinelli, 1970.

- Jech, Thomas. *The Axiom of Choice*. Studies in Logic and the Foundations of Mathematics 75. Amsterdam: North-Holland, 1973.

- Kline, Morris. *Storia del pensiero matematico*. Vol. 2, *Dal Settecento a oggi*. Italian edition edited by Alberto Conte. Turin: Einaudi, 1991.

- Lolli, Gabriele. *Dagli insiemi ai numeri: Storia e assiomatica della teoria degli insiemi*. Turin: Bollati Boringhieri, 1994.

- Moore, Gregory H. *Zermelo's Axiom of Choice: Its Origins, Development, and Influence*. New York: Springer-Verlag, 1982.

- Vitali, Giuseppe. *Sul problema della misura dei gruppi di punti di una retta*. Bologna: Tipografia Gamberini e Parmeggiani, 1905.

- Zermelo, Ernst. “Beweis, daß jede Menge wohlgeordnet werden kann (Aus einem an Herrn Hilbert gerichteten Briefe).” *Mathematische Annalen* 59 (1904): 514–516. [https://doi.org/10.1007/BF01445300](https://doi.org/10.1007/BF01445300).

</div>
