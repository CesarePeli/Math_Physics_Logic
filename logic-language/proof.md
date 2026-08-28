---
layout: default
title: "What Is a Proof?"
author: Cesare Peli
date: 2026-08-27
permalink: /logic-language/proof/
background_image: "/images/complessi2.png"
description: "What is a mathematical proof? Explore formal derivation, logical consequence, axiomatic systems, and the historical development of proof across mathematical traditions."
area: logic-language
content_type: article
---

<div class="content-box">

## What Is a Proof?

*By Cesare Peli*

In this article, we will mention some major historical developments through which proof entered mathematics and, later, science. It should emerge, among other things, that there is no absolute definition of what a proof is. The standards by which a proof is accepted have always depended on a historical and disciplinary context. Many theologians, for example, have claimed to prove the existence of God while also arguing that the proofs offered before theirs were invalid.

Any discussion of proof therefore needs to be historicized. An exhaustive account would require many separate and complex analyses, far beyond the scope of a single article. Here we will focus on two questions: what formal logic tells us about mathematical proof, and whether the birth of proof can really be described as a uniquely Greek achievement.

</div>

<div class="content-box">

## A Proof in Formal Terms

Before turning to history, let us pause over a more basic question: what is a proof in mathematics? To pose the question in the most general terms possible, we can begin from the point of view of formal logic. This perspective seems to involve the fewest assumptions, yet even here the answer is less self-contained than it first appears.

In axiomatic mathematics, let $T$ be a theory and $A$ a statement. We want to establish that $A$ follows from the axioms of $T$. For example, $T$ might contain the axioms of an ordered field together with a completeness principle, while $A$ might be Rolle's theorem:

> If a real-valued function $f$ is continuous on a closed interval $[a,b]$, differentiable on the open interval $(a,b)$, and $f(a)=f(b)$, then there exists at least one $c\in(a,b)$ such that $f'(c)=0$.

The compact formula does not carry its intended mathematical meaning by itself. A reader may know what function, continuity, differentiability, closed interval, and open interval mean, but those meanings must be supplied by definitions, by the language of the theory, and by an interpretation of its symbols. They are the result of mathematical construction, not of logical syntax alone.

Consider a more elementary example. Let $T$ be Euclidean geometry and $A$ the Pythagorean theorem. We still need to know what triangle, square, right angle, and hypotenuse mean. Without the surrounding definitions and conventions, the proposition does not determine a unique mathematical claim. It acquires that meaning within a theory—or, in ordinary practice, within something as concrete as a geometry textbook.

One could try to include every necessary definition and rule explicitly. Mathematical writing rarely does so. Practice does not reproduce the entire foundational architecture behind every theorem: it selects the level of detail appropriate to its readers and purpose. Mathematics, considered as a discipline rather than as a pure abstraction, is also a practice.

There is a deeper foundational problem. The usual formulation of Rolle's theorem presupposes real numbers, functions, intervals, and the machinery of analysis. These objects may be treated axiomatically, as they normally are in an analysis course. If we insist on reducing them to a standard foundational theory, however, we must begin much further back: with axiomatic set theory, then construct the natural numbers, integers, rational numbers, and real numbers, and finally recover the definitions and results needed for analysis.

The reason for using axiomatic set theory is not merely a preference for formal elegance. Unrestricted set formation leads to contradictions. If we define

$$
R=\{x\mid x\notin x\},
$$

then asking whether $R\in R$ gives

$$
R\in R \Longleftrightarrow R\notin R.
$$

This is Russell's paradox. Axiomatic systems such as Zermelo–Fraenkel set theory restrict the ways in which sets may be formed and make the foundational assumptions explicit. They also lead to delicate questions, including the status of the axiom of choice. None of this has to be reconstructed whenever Rolle's theorem is proved. Even in university mathematics, foundational work is usually left in the background so that attention can remain on the theory being studied.

### Derivability and Logical Consequence

At this point a distinction is essential. If $A$ can be obtained from the axioms of $T$ by the rules of a formal calculus, we write

$$
T\vdash A.
$$

This is a syntactic relation: there is a finite formal derivation of $A$ from $T$.

If $A$ is true in every interpretation, or model, in which the axioms of $T$ are true, we write

$$
T\models A.
$$

This is a semantic relation. A sound deductive system guarantees that

$$
T\vdash A \quad\Longrightarrow\quad T\models A.
$$

In first-order logic, completeness also gives the converse. The two symbols therefore express connected ideas, but they do not mean the same thing: one concerns formal derivation, the other truth in models.

The word *true* introduces another level. To speak about the truth of sentences in a language, we need a metalanguage in which the object language and its interpretations can be discussed. Gabriele Lolli writes:

> To state the truth about a domain of knowledge, it is necessary to use a language that speaks about the language in which that knowledge is formulated—the object language—and to assume further knowledge able to establish properties of the object language and its meanings. [...] No truth is definable absolutely; even truth in a limited domain cannot be defined without passing to a higher domain.

Consider the familiar expression

$$
2+2=4.
$$

It is often invoked as the clearest possible example of mathematical certainty. Yet even this statement presupposes a domain and an interpretation of its symbols. In the natural numbers it is true. In the ring $\mathbb{Z}_4=\{0,1,2,3\}$, where addition is interpreted modulo four, the result of adding $2$ and $2$ is the equivalence class of $4$, which coincides with the equivalence class of $0$:

$$
[2]+[2]=[4]=[0].
$$

Using the customary representatives, this is often written simply as

$$
2+2=0 \pmod 4.
$$

There is no need to leave arithmetic in order to prove $2+2=4$. Using $S$ for the successor operation, define

$$
2=S(S(0)), \qquad 4=S(S(S(S(0)))),
$$

and addition recursively by

$$
x+0=x, \qquad x+S(y)=S(x+y).
$$

Then

$$
\begin{aligned}
2+2
&=2+S(S(0))\\
&=S(2+S(0))\\
&=S(S(2+0))\\
&=S(S(2))\\
&=4.
\end{aligned}
$$

The result follows formally once the language, axioms, and definitions have been fixed. Set theory can be used to construct a particular model of the natural numbers, but it is not required for this elementary derivation.

So what is a proof? Within a formal calculus, the answer can be precise: a proof is a finite derivation constructed according to specified rules. It need not be easy to understand or psychologically convincing. Outside a fully formalized calculus, however, mathematical proofs are written for human readers. Which steps may be omitted, which definitions may be assumed, and which arguments count as sufficiently rigorous depend on the theory, the historical period, and the community in which the proof is used.

The formal and human dimensions should therefore be kept together. A derivation can be objectively checked relative to a formal system; the choice and interpretation of that system, and the recognition of an informal argument as a legitimate proof, belong to a broader mathematical practice. We work confidently with numbers every day, yet the question *what are numbers?* soon takes us from mathematics into its foundations and philosophy.

</div>

<div class="content-box">

## Was the Birth of Proof a “Greek Miracle”?

From within the Western intellectual tradition, questions such as *Who first used proofs as we understand them today?* and *Who established the logical canons of proof?* tend to lead immediately to Plato, Aristotle, and the familiar image of Greek reason emerging from a world of superstition. This account contains important truths, but it also encourages excessive simplification.

Three points provide a reasonable starting place:

1. The earliest surviving systematic presentation of mathematical demonstration in the Greek tradition is Euclid's *Elements* (around 300 BC), followed by the geometric works of Archimedes (c. 287–212 BC) and Apollonius of Perga (c. 240–190 BC).

2. Aristotle (384–322 BC), especially in the *Prior Analytics* and *Posterior Analytics*, developed a general theory of deductive reasoning and scientific demonstration.

3. Modern mathematics and philosophy have identified errors, implicit assumptions, and gaps in these ancient works. Even so, they remained points of reference for more than two thousand years and decisively shaped Western conceptions of rationality.

It is tempting to infer that pre-Greek or non-Greek mathematics contained no proofs, and that mathematics detached from immediate application arose only in Greece. The historical evidence does not support so simple a division. It is more accurate to say that Greek mathematics developed a particularly explicit and influential general framework for organizing propositions deductively. Other traditions established correctness in different forms, often through problems, algorithms, transformations, and diagrams.

Karine Chemla's 2012 collection *The History of Mathematical Proof in Ancient Traditions* examines these different settings and the historiography through which they have been interpreted. In the opening study, *Historiography and History of Mathematical Proof: A Research Programme*, Chemla analyzes the sharp opposition constructed between Greek mathematics and the mathematics of the “East,” and indicates how it might be overcome.

Translations of Euclid's *Elements* circulated in Greek, Arabic, Latin, Hebrew, and later in European vernacular languages. For centuries the work occupied a central place in mathematical education. Its proofs became models of incontrovertibility for philosophers as well as mathematicians. Proof therefore acquired an identity-forming role in Western knowledge, and its presence in Greek mathematics was repeatedly used to assert superiority over Arabic, Chinese, Indian, Babylonian, and Egyptian traditions.

Nineteenth-century historians nevertheless found traces of proof in mathematical traditions older than or independent of Greek geometry. These findings did not immediately dislodge the dominant account. In 1841 Jean-Baptiste Biot could still write:

> This peculiar habit of mind, following which the Arabs, as the Chinese and Hindus, limited their scientific writings to the statement of a series of rules, which, once given, ought only to be verified by their applications, without requiring any logical demonstration or connections between them: this gives those Oriental nations a remarkable character of dissimilarity, I would even add of intellectual inferiority, comparatively to the Greeks, with whom any proposition is established by reasoning, and generates logically deduced consequences.

Among the nineteenth-century studies of non-European mathematics, the work of the mathematician and orientalist Henry Thomas Colebrooke was especially important. In 1817 he published *Algebra, with Arithmetic and Mensuration, from the Sanscrit of Brahmegupta and Bháscara*, one of the first major English translations of Sanskrit mathematics. He encountered an algebraic tradition that used symbolic and literal procedures and included geometrical justifications of algebraic rules. Other scholars identified forms of demonstration in Indian, Chinese, Egyptian, and Arabic texts. Some judged them inferior to the proofs of the *Elements*; others recognized them as different demonstrative practices whose value did not depend on conformity to the Greek model.

Early Chinese writings, like some Babylonian tablets, often present mathematical activity through problems and the algorithms used to solve them. The proofs embodied in these sources may aim to establish the correctness of a procedure. In some Chinese texts, operations are applied to the sequence of operations that constitutes an algorithm: a known procedure is transformed into another whose correctness is thereby made visible. Here proof is connected to the transformation and explanation of algorithms rather than to deduction from an explicit list of axioms.

The publication in 1959 of the third volume of Joseph Needham's *Science and Civilisation in China* opened an influential line of historical research. Frank Swetz and T. I. Kao's provocatively titled *Was Pythagoras Chinese?* later presented material from the *Jiǔzhāng Suànshù*, or *Nine Chapters on the Mathematical Art*, including a demonstration of the relation known in the West as the Pythagorean theorem.

The dating of the *Nine Chapters* is complex. It is a composite work that took shape over several centuries, contains material that may be considerably older than its received form, and was given its most famous commentary by Liu Hui in AD 263. It should therefore not be assigned a single early date with false precision.

<figure>
  <img src="{{ '/images/pit.jpg' | relative_url }}" alt="The Chinese hsuan-thu diagram associated with the Pythagorean theorem">
  <figcaption>The diagram known in China as <em>hsuan-thu</em>.</figcaption>
</figure>

<figure>
  <img src="{{ '/images/quadrato.png' | relative_url }}" alt="Four congruent right triangles arranged inside a square with an inner square">
  <figcaption>A rearrangement proof of the Pythagorean theorem.</figcaption>
</figure>

The second diagram contains four congruent right triangles. Let $c$ be the hypotenuse of each triangle, $a$ its longer leg, and $b$ its shorter leg. The outer square has side $c$, while the inner square has side $a-b$. The four triangles have total area $2ab$. Therefore

$$
\begin{aligned}
c^2 &= 2ab+(a-b)^2 \\
    &= 2ab+a^2-2ab+b^2 \\
    &= a^2+b^2.
\end{aligned}
$$

The argument proves the theorem through a geometrical decomposition. It is concise, general, and rigorous, although it does not belong to the axiomatic structure of Euclid's Elements.

Chemla's broader point is that proof must be studied within the activities, goals, and values of the groups that use it. She writes:

> Proving is an activity that takes place in specific social and professional groups which have specific agendas. [...] Only along these lines can we hope to bring to light and accommodate the variety of practices in a way more satisfactory than the old model of competing civilizations which has been pre-eminent from the nineteenth century onwards.

> We have seen that some proofs seem to be conducted in order to understand the statement proved or the text which states it. In other cases, proofs have appeared to have had as one of their goals the identification of fundamental operations or the display of a technique. We have also seen that in some contexts, proofs were expected to be general or to comply with an ideal of generality. In others, they should bring clarity, yield fruitfulness or manifest simplicity.

The history of proof becomes distorted when all these practices are ranked according to a single inherited model.

These reflections highlight the cultural dimension of proof, retrospectively claimed as the defining achievement of a civilization. Must an argument belong to a structured axiomatic theory in order to count as a proof, or is demonstrating the validity of an algorithm enough? Asking whether an algorithm is valid already places us fully within mathematics. Proof is therefore neither a neutral label nor a final destination: it is the beginning of a construction.

</div>

<div class="content-box">

## References


- Chemla, Karine, ed. *The History of Mathematical Proof in Ancient Traditions*. Cambridge University Press, 2012.

- Colebrooke, Henry Thomas. *Algebra, with Arithmetic and Mensuration, from the Sanscrit of Brahmegupta and Bháscara*. John Murray, 1817.

- Lolli, Gabriele. *QED: Fenomenologia della dimostrazione*. Bollati Boringhieri, 2005.

- Needham, Joseph, with Wang Ling. *Science and Civilisation in China*, vol. 3, *Mathematics and the Sciences of the Heavens and the Earth*. Cambridge University Press, 1959.

- Russell, Bertrand. *The Principles of Mathematics*. Cambridge University Press, 1903.

- Swetz, Frank J., and T. I. Kao. *Was Pythagoras Chinese? An Examination of Right Triangle Theory in Ancient China*. Pennsylvania State University Press, 1977.

</div>