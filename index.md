---
layout: default
title: "Logic & Motion — Mathematics, Physics, Logic and Language"
permalink: /
nav_exclude: false
background_image: "/images/spirale.png"
description: "Articles, notes, exercises, and resources on mathematics, physics, logic, linguistics, formal systems, and artificial intelligence."
last_modified_at: 2026-10-13
---

# Logic & Motion

Logic & Motion is an independent educational project devoted to mathematics, physics, logic, language, and artificial intelligence. It brings together conceptual articles, theoretical notes, proofs, worked exercises, and visual material for students, teachers, and interested readers.

<div class="content-box">

## Selected Readings

<style>
.featured-readings {
  display: grid;
  gap: 1.25rem;
}
.featured-reading {
  display: grid;
  grid-template-columns: 120px minmax(0, 1fr);
  gap: 1.25rem;
  align-items: center;
  padding: 0.75rem;
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 0.75rem;
  background: rgba(0, 0, 0, 0.22);
  color: #eee;
}
.featured-reading:hover,
.featured-reading:focus-visible {
  background: rgba(255, 255, 255, 0.08);
  color: #fff;
  text-decoration: none;
}
.featured-reading:focus-visible {
  outline: 2px solid #aadfff;
  outline-offset: 4px;
}
.featured-reading img {
  display: block;
  width: 120px;
  height: 120px;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  border-radius: 0.45rem;
}
.featured-reading h3 {
  margin: 0 0 0.4rem;
  color: #aadfff;
  font-size: 1.15rem;
  line-height: 1.3;
}
.featured-reading p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.5;
  text-align: left;
}
@media (max-width: 600px) {
  .featured-reading {
    grid-template-columns: 88px minmax(0, 1fr);
    gap: 0.85rem;
    padding: 0.6rem;
    align-items: start;
  }
  .featured-reading img {
    width: 88px;
    height: 88px;
  }
  .featured-reading h3 { font-size: 1.05rem; }
  .featured-reading p { margin: 0; font-size: 0.9rem; }
}
</style>

<div class="featured-readings" markdown="0">
  <a class="featured-reading" href="{{ "/logic-language/large-language-models-grammar/" | relative_url }}">
    <img src="{{ "/images/LLM.png" | relative_url }}" alt="" width="120" height="120" loading="lazy" decoding="async">
    <div>
      <h3>Do Large Language Models Learn Grammar?</h3>
      <p>Andrea Padovan examines how language models learn grammar and how this compares with human language acquisition.</p>
    </div>
  </a>
  <a class="featured-reading" href="{{ "/logic-language/axiom-of-choice/" | relative_url }}">
    <img src="{{ "/images/assioma.png" | relative_url }}" alt="" width="120" height="120" loading="lazy" decoding="async">
    <div>
      <h3>Choice and Infinity: The Axiom of Choice</h3>
      <p>Infinite sets, Zermelo–Fraenkel axioms, and the consequences of assuming that a choice is always possible.</p>
    </div>
  </a>
  <a class="featured-reading" href="{{ "/physics/thermodynamics/maxwells-demon/" | relative_url }}">
    <img src="{{ "/images/demon.png" | relative_url }}" alt="" width="120" height="120" loading="lazy" decoding="async">
    <div>
      <h3>Maxwell's Demon</h3>
      <p>A thought experiment connecting irreversibility, entropy, information, and the physical cost of erasing memory.</p>
    </div>
  </a>
  <a class="featured-reading" href="{{ "/physics/quantum-physics/blackbody-quantum-revolution/" | relative_url }}">
    <img src="{{ "/images/body.png" | relative_url }}" alt="" width="120" height="120" loading="lazy" decoding="async">
    <div>
      <h3>Blackbody Radiation and the Quantum Revolution</h3>
      <p>How the problem of thermal radiation led to Planck’s hypothesis and the beginnings of quantum theory.</p>
    </div>
  </a>
</div>

</div>

<div class="content-box">

## Sections

### [Mathematics]({{ "/mathematics/" | relative_url }})

Articles and resources on foundations, algebra, calculus, mathematical methods, and proof.

### [Physics]({{ "/physics/" | relative_url }})

Conceptual material and worked problems on mechanics, thermodynamics, dynamical systems, and quantum physics.

### [Logic & Language]({{ "/logic-language/" | relative_url }})

Articles on logic, linguistics, formal systems, symbolic representation, and artificial intelligence.

### [Art & Mathematics]({{ "/gallery/" | relative_url }})

Visual explorations of mathematical structures, patterns and scientific ideas.

### [About]({{ "/about/" | relative_url }})

Information about the project, its contents, and its author.

</div>
