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

Two ordered sets have the same **order type** when their elements occupy the same relative positions. More precisely, an order isomorphism between \(A\) and \(B\) is a bijection

\[
f:A\to B
\]

such that

\[
x<_A y \quad\Longleftrightarrow\quad f(x)<_B f(y).
\]

For example, the ordered sets

\[
1<2<3
\]

and

\[
a<b<c
\]

have the same order type: the names of the elements differ, but their positions do not.

An **ordinal** is the canonical object used in set theory to represent the order type of a well-ordered set. Thus every well-ordered set has exactly one ordinal with the same order type. Ordinals record positions, not merely quantities.

The usual order on the natural numbers has order type

\[
\omega.
\]

If a new element is placed after every natural number,

\[
0<1<2<\cdots<a,
\]

the resulting order type is

\[
\omega+1.
\]

Both sets are countably infinite, so they have the same cardinality, but they have different order types. Cardinal numbers answer “how many?”; ordinal numbers answer “in what well-ordered arrangement?”

Any two ordinals are comparable: one is equal to, or occurs as an initial part of, the other. This is why ordinals make it possible to compare the sizes of well-ordered sets.

</div>

<div class="content-box">

## Transfinite cardinals and the alephs

For a well-orderable set, its cardinality can be represented by the least ordinal equinumerous with it. Such ordinals are called **initial ordinals**, and their cardinalities are denoted by the Hebrew letter aleph,

\[
\aleph.
\]

The first infinite cardinal is

\[
\aleph_0 = |\mathbb N|,
\]

read “aleph zero.” Every set that can be put in bijection with the natural numbers is called **countably infinite**. The integers and the rational numbers are countably infinite:

\[
|\mathbb Z|=|\mathbb Q|=\aleph_0.
\]

The next well-orderable infinite cardinal is

\[
\aleph_1.
\]

It is the least uncountable cardinal and is also the cardinality of the set of all countable ordinals. Continuing in this way gives

\[
\aleph_0,\aleph_1,\aleph_2,\ldots
\]

and, more generally, \(\aleph_\alpha\) for every ordinal \(\alpha\).

Cantor proved that the real numbers are uncountable. Their cardinality is called the **cardinality of the continuum** and is written

\[
\mathfrak c = |\mathbb R|.
\]

The continuum hypothesis asks whether

\[
\mathfrak c=\aleph_1.
\]

Before that question can be placed inside the aleph hierarchy, however, one must know that the real numbers can be well-ordered. More generally, one must know that every set can be well-ordered. That is precisely where the axiom of choice enters.

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

Let

\[
\mathcal A=\{A_i\}_{i\in I}
\]

be a family of sets indexed by a set \(I\). The family may be finite or infinite. A **choice function** for this family is a function

\[
f:I\to \bigcup_{i\in I}A_i
\]

such that

\[
f(i)\in A_i
\]

for every \(i\in I\).

If the family is finite, one can make the choices one after another. Some infinite families also come with a natural rule. For example, if every \(A_i\) is a nonempty subset of \(\mathbb N\), one may set

\[
f(i)=\min A_i.
\]

For a completely arbitrary infinite family, no such rule need be given. The statement \(A_i\neq\varnothing\) tells us, separately for each index \(i\), that at least one element exists in \(A_i\). It does not by itself produce a single function that makes all those choices simultaneously.

The axiom of choice asserts exactly that this simultaneous selection is always possible:

\[
\boxed{
\text{If }A_i\neq\varnothing\text{ for every }i\in I,
\text{ then there exists }f\text{ with }f(i)\in A_i\text{ for every }i.
}
\]

This is an existence statement. It does not say how to define \(f\), calculate its values, or describe the selected elements.

There is a compact notation for the same idea. The **Cartesian product** of the family is defined by

\[
\prod_{i\in I}A_i
=
\left\{
f:I\to\bigcup_{i\in I}A_i
\;\middle|\;
f(i)\in A_i\text{ for every }i\in I
\right\}.
\]

Thus the elements of \(\prod_{i\in I}A_i\) are precisely the choice functions for the family. Saying that every \(A_i\) is nonempty does not, in ZF alone, guarantee that this product is nonempty. The axiom of choice is equivalent to the statement

\[
\boxed{
A_i\neq\varnothing\text{ for every }i\in I
\quad\Longrightarrow\quad
\prod_{i\in I}A_i\neq\varnothing.
}
\]

</div>

<div class="content-box">

## Zermelo and the well-ordering theorem

A set is **well-ordered** when its elements are arranged so that every nonempty subset has a first element. The natural numbers with their usual order are well-ordered; the integers with their usual order are not, because the whole set of integers has no least element.

Zermelo proved that the axiom of choice is equivalent to the following statement.

\[
\boxed{\text{Every set can be well-ordered.}}
\]

This is the **well-ordering theorem**.

Here is the idea of the implication from choice to well-ordering. Let \(X\) be any set. Apply the axiom of choice to the family of all nonempty subsets of \(X\). We obtain a function \(c\) such that

\[
c(S)\in S
\]

whenever \(S\subseteq X\) and \(S\neq\varnothing\).

Use \(c\) first on \(X\), then on the set of elements not yet selected, and continue choosing from what remains. For an arbitrary set, “continue” may require more than finitely or countably many stages. A complete proof formalizes the continuation by indexing successive choices with ordinals. A basic theorem of set theory guarantees that the process cannot keep choosing distinct elements of \(X\) through every ordinal stage; it must eventually exhaust \(X\). Order the elements of \(X\) by the stage at which they were selected. Every nonempty subset then has a first selected element, so this order is a well-order.

The reverse implication is shorter. Suppose every set can be well-ordered, and let \(\{A_i\}_{i\in I}\) be a family of nonempty sets. Well-order the union

\[
X=\bigcup_{i\in I}A_i.
\]

Each \(A_i\) now has a least element in that order. Defining \(f(i)\) to be that least element gives a choice function.

Therefore

\[
\boxed{
\text{axiom of choice}
\iff
\text{well-ordering theorem}.
}
\]

The theorem does not say that a useful or explicit well-order of every familiar set can be written down. It asserts that such an order exists.

</div>

<div class="content-box">

## Comparability of cardinalities

For finite sets, one of two sets always has at most as many elements as the other. For arbitrary sets, the corresponding statement is expressed with injections:

\[
|A|\le |B|
\]

means that there is an injective function from \(A\) to \(B\). The **comparability principle** says that for all sets \(A\) and \(B\),

\[
|A|\le |B|
\quad\text{or}\quad
|B|\le |A|.
\]

Assume the axiom of choice. By the well-ordering theorem, both \(A\) and \(B\) can be well-ordered. Their order types are ordinals, and any two ordinals are comparable. This yields an injection in one direction, so their cardinalities are comparable.

The converse needs one additional result that is provable in ZF, without the axiom of choice. **Hartogs's theorem** says that for every set \(A\) there is an ordinal \(h(A)\) for which no injection

\[
h(A)\to A
\]

exists. Informally, \(h(A)\) is a well-ordered set that is too large to fit injectively inside \(A\).

Now assume that all cardinalities are comparable. Applied to \(A\) and \(h(A)\), comparability gives an injection in one of the two directions. The direction \(h(A)\to A\) is impossible by Hartogs's theorem, so there must be an injection

\[
A\to h(A).
\]

Because \(h(A)\) is well-ordered, this injection allows us to order the elements of \(A\) according to the positions of their images. Hence \(A\) can be well-ordered. Since \(A\) was arbitrary, the well-ordering theorem holds, and therefore so does the axiom of choice.

Thus

\[
\boxed{
\text{axiom of choice}
\iff
\text{well-ordering theorem}
\iff
\text{comparability of all cardinalities}.
}
\]

</div>

<div class="content-box">

## Zorn's lemma

A common way to use the axiom of choice is to replace it with an equivalent principle called **Zorn's lemma**.

Zorn's lemma concerns a **partially ordered set**: a set \(P\) equipped with a relation \(\le\) that is reflexive, antisymmetric, and transitive. Unlike a total order, a partial order does not require every pair of elements to be comparable. For example, subsets of a set can be ordered by inclusion; two subsets need not contain one another.

A **chain** in \(P\) is a subset whose elements are mutually comparable. An element \(u\in P\) is an **upper bound** of a chain \(C\) if

\[
x\le u
\]

for every \(x\in C\).

An element \(m\in P\) is **maximal** if there is no element strictly above it. This is not the same as being a **maximum**: a maximum lies above every element of \(P\), whereas a partially ordered set may have several incomparable maximal elements.

Zorn's lemma states:

> **Zorn's lemma.** If every chain in a nonempty partially ordered set has an upper bound in that set, then the set contains a maximal element.

Why does this imply the axiom of choice? Given a family \(\{A_i\}_{i\in I}\) of nonempty sets, consider all **partial choice functions**: functions that choose an element from \(A_i\) only for indices in some subset of \(I\). Order these functions by extension. The union of a chain of compatible partial choice functions is again a partial choice function, so every chain has an upper bound.

Zorn's lemma therefore gives a maximal partial choice function \(f\). If its domain omitted an index \(j\), the fact that \(A_j\neq\varnothing\) would let us choose one element of that single set and extend \(f\) to \(j\). That would contradict maximality. Hence the domain of \(f\) is all of \(I\), and \(f\) is a choice function.

For the reverse implication, assume the axiom of choice. By the well-ordering theorem, the elements of \(P\) can be well-ordered. Scan them in that order, adding an element whenever it remains comparable with every element already accepted. The formal construction proceeds through the ordinal stages of the well-order and produces a maximal chain \(C\).

By hypothesis, \(C\) has an upper bound \(u\in P\). If some \(v\) satisfied \(u<v\), then every element of \(C\) would also lie below \(v\), so \(C\cup\{v\}\) would be a larger chain. This contradicts the maximality of \(C\). Therefore \(u\) is a maximal element of \(P\).

Consequently,

\[
\boxed{
\text{Zorn's lemma}
\iff
\text{axiom of choice}.
}
\]

</div>

<div class="content-box">

## Why every vector space has a basis

A **basis** of a vector space \(V\) is a set of vectors that satisfies two conditions:

1. it is linearly independent;
2. every vector in \(V\) is a finite linear combination of vectors from that set.

The second condition says that the set **spans** \(V\).

For a finite-dimensional vector space, a basis can be found by starting from a finite generating list and removing redundant vectors. For an arbitrary vector space, however, there may be no finite or countable generating list to start from. The problem is to prove that a linearly independent set can be enlarged until it spans the whole space, even when that enlargement may require arbitrarily many stages.

Let \(\mathcal L\) be the collection of all linearly independent subsets of \(V\), ordered by inclusion. It is nonempty because the empty set is linearly independent.

Consider a chain

\[
L_1\subseteq L_2\subseteq\cdots
\]

in \(\mathcal L\), or more generally any chain not necessarily indexed by the natural numbers. Its union

\[
L=\bigcup_\alpha L_\alpha
\]

is still linearly independent. Indeed, a linear dependence relation involves only finitely many vectors. Since the sets form a chain, all those vectors already lie together in one member \(L_\alpha\), where they are independent.

Thus every chain in \(\mathcal L\) has an upper bound in \(\mathcal L\). By Zorn's lemma, \(\mathcal L\) has a maximal element \(B\).

Suppose \(B\) did not span \(V\). Then some vector \(v\in V\) would not be a linear combination of vectors in \(B\). In that case,

\[
B\cup\{v\}
\]

would still be linearly independent, contradicting the maximality of \(B\). Therefore \(B\) spans \(V\), so \(B\) is a basis.

The axiom of choice enters through Zorn's lemma. It proves that a maximal independent set exists; it does not provide a procedure for listing its vectors.

</div>

<div class="content-box">

## Representatives and non-measurable sets

The axiom of choice also allows one to select a representative from every class of an equivalence relation.

On the interval \([0,1]\), define

\[
x\sim y
\]

when

\[
x-y\in\mathbb Q.
\]

This relation divides \([0,1]\) into disjoint equivalence classes. The class of \(x\) consists of all points of \([0,1]\) that differ from \(x\) by a rational number.

Using the axiom of choice, select exactly one point from each class and call the resulting set \(V\). This is a **Vitali set**.

For each rational number \(q\in[-1,1]\), consider the translate

\[
V+q=\{v+q:v\in V\}.
\]

These translates are pairwise disjoint. Their union contains \([0,1]\) and is contained in \([-1,2]\).

Suppose \(V\) had a Lebesgue measure. Translation invariance would give every \(V+q\) the same measure. If that measure were zero, their countable union would have measure zero, although it contains \([0,1]\). If it were positive, the union would have infinite measure, although it is contained in the bounded interval \([-1,2]\). Both conclusions are impossible.

Therefore \(V\) is not Lebesgue measurable. The contradiction is not in the real numbers or in measure theory; it arises only from assuming that this specially selected set has a measure.

</div>

<div class="content-box">

## The Banach–Tarski paradox

The Banach–Tarski theorem concerns an ideal mathematical ball: the set of all points at distance at most \(1\) from a center in three-dimensional space. It states that this set can be partitioned into finitely many disjoint subsets. By moving those subsets only with rotations and translations, one can arrange them into two balls, each congruent to the original.

This does **not** describe cutting a physical ball into ordinary solid pieces. The subsets are extremely scattered sets of points, not chunks bounded by surfaces, and they cannot all be assigned a Lebesgue volume.

That fact removes the apparent contradiction. Rotations and translations preserve the volume of measurable sets, and the volume of finitely many disjoint measurable pieces is the sum of their volumes. If the Banach–Tarski pieces were measurable, one ball of volume \(V\) could not become two balls of total volume \(2V\). But the pieces have no Lebesgue volume, so the rule being invoked simply does not apply to them.

Where does choice enter? In the standard construction, certain rotations are applied repeatedly to points on a sphere. Two points are placed in the same class, called an **orbit**, when one can be reached from the other by a finite sequence of those rotations and their inverses. There are uncountably many such orbits. The proof needs a set containing one representative from each orbit, much as the Vitali construction selects one representative from each equivalence class. A suitable form of the axiom of choice supplies that simultaneous selection.

The rotations have a special algebraic structure that allows the selected points and all their rotated copies to be grouped and rearranged into two copies of the original configuration. The technical proof is intricate, but the logical point is simple: choice creates non-measurable sets of representatives, and those are the “pieces” used in the decomposition.

The word **paradox** here means a result that conflicts sharply with geometric intuition, not a contradiction in mathematics. There is no physical duplication of matter: real objects are atomic, and physical cuts do not produce arbitrary non-measurable sets of points.

</div>

<div class="content-box">

## ZF and ZFC

**Zermelo–Fraenkel set theory**, abbreviated **ZF**, is the standard collection of axioms used to describe sets and their basic operations without assuming the axiom of choice. Adding the axiom of choice gives **ZFC**:

\[
\mathrm{ZFC}=\mathrm{ZF}+\mathrm{AC}.
\]

A **model** of an axiomatic theory is a mathematical structure in which all the axioms of that theory are true. Independence results compare different models rather than deciding the axiom of choice from the other ZF axioms.

In 1938, Kurt Gödel showed that if ZF is consistent, then ZF together with the axiom of choice is also consistent. He did this by constructing a model known as the **constructible universe**, in which choice holds.

In 1963, Paul Cohen developed the method of **forcing** and used it, together with related model constructions, to show that if ZF is consistent, then ZF together with the negation of the axiom of choice is also consistent.

Consequently, assuming ZF itself is consistent,

\[
\mathrm{ZF}\nvdash\mathrm{AC}
\]

and

\[
\mathrm{ZF}\nvdash\neg\mathrm{AC}.
\]

In words: the axioms of ZF neither prove nor disprove the axiom of choice.

This is why accepting or rejecting choice leads to genuinely different set theories. In ZFC every set can be well-ordered, all cardinalities are comparable, and Zorn's lemma is available. In models of ZF where choice fails, some of these statements fail as well. The two theories agree on much ordinary mathematics but diverge on important questions involving arbitrary infinite collections.

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

The axiom of choice begins with a statement that sounds almost trivial: from each nonempty set in a family, choose one element. Its force appears when the family may be infinite and no selection rule is given. Then the separate existence of an element in every set is not automatically the existence of one function making all choices at once.

Within ZF, the following statements are equivalent:

1. every family of nonempty sets has a choice function;
2. every Cartesian product of nonempty sets is nonempty;
3. every set can be well-ordered;
4. any two cardinalities are comparable;
5. Zorn's lemma holds.

These are not merely different phrasings. Each turns the same principle into a tool suited to a different problem: simultaneous selection, products, ordered sets, cardinal comparison, or maximal objects.

The examples also show why the axiom is both useful and unsettling. It proves that every vector space has a basis, even when no basis can be explicitly listed. It also permits representative sets that are non-measurable and underlie the Banach–Tarski decomposition.

Finally, Gödel's and Cohen's independence results show that ZF does not decide the issue. One may study mathematics with choice or without it. The resulting theories overlap extensively, but they are not the same mathematics.

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
