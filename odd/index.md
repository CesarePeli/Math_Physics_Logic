---
layout: default
title: Logic & Motion – Curated Science Resources
permalink: /
nav_exclude: false
background_image: "/images/spirale.png"
description: "Explore curated, high-quality resources in math, physics, and logic — designed for conceptual clarity and intellectual exploration."
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3P4GLVFYWW"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-3P4GLVFYWW');
</script>

<!-- ──────────── PAGE TITLE ──────────── -->
<div class="homepage-header" style="text-align:center;margin:2rem auto;">
  <h1 style="font-size:2.5rem;font-weight:bold;">Logic & Motion</h1>
  <p style="font-size:1.2rem;margin-top:.5rem;">Tools for students and teachers — grounded in reasoning and clarity.</p>
</div>

<!-- ─────────  FEATURED  ───────── -->
<section id="featured" style="margin:4rem auto;max-width:1000px;padding:0 1rem;">
<h2 style="font-size:1.6rem;margin-bottom:1rem;">Featured</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1.2rem;">
{% assign spotlight = site.pages | where_exp:"p","p.featured" | sort:"date" | reverse | slice:0,6 %}
{% for item in spotlight %}
{% assign bg = item.background_image %}
{% unless bg %}
{% assign raw = item.content | split:'src="' | slice:1,1 | first %}
{% assign bg  = raw | split:'"' | first %}
{% endunless %}
{% unless bg %}{% assign bg = "/images/placeholder.jpg" %}{% endunless %}
<a href="{{ item.url | relative_url }}" style="display:block;height:180px;border-radius:1rem;overflow:hidden;text-decoration:none;color:#fff;background:url('{{ bg | relative_url }}') center/cover no-repeat;"><span style="display:flex;align-items:flex-end;justify-content:center;height:100%;width:100%;padding-bottom:1rem;font-size:1rem;font-weight:600;text-align:center;text-shadow:0 2px 6px rgba(0,0,0,0.9);">{{ item.title }}</span></a>
{% endfor %}
</div>
</section>
<!-- ─────────────────────────────── -->

<!-- ─────────────  INTRO  ───────────── -->
<div class="content-box">

Mathematics is not mere calculation—at least, not only.  
It is a form of thought, a structure of understanding, a language of precision. In a world that moves fast—chasing shortcuts and quick results—mathematics invites us to slow down, to think with order, and to separate the essential from the accidental. It teaches us to *see*: recurring patterns, possible transformations, hidden connections between ideas that at first seem distant.

There is no single path to insight. Some minds see structure immediately, others begin with concrete examples, others imagine abstract relations. All of these approaches are valuable, because mathematics welcomes diverse styles of reasoning—deductive, inductive, analogical, abstract, visual—and in this variety lies its universality.

In this spirit, **Mathematics** is not a list of formulas to memorize, but a way of thinking grounded in reasoning, proof, and internal coherence.  
**Physics** is approached as the science of models: abstract principles expressed through mathematics and applied across diverse real-world contexts.

**Logic & Motion** bridges education and exploration — offering curated resources for students and teachers: slides, guided exercises, printable summaries, and original writing that invite reflection as well as understanding.

Rooted in logic, inquiry, and the desire to understand, *Logic & Motion* presents science as a structured way of thinking — intellectually rigorous, yet always human and meaningful.

</div>

<!-- ─────────────  SECTION LINKS  ───────────── -->
<div class="content-box">

## Explore the Sections

- [**Odd Questions**]({{ "/odd-questions/" | relative_url }})  
  Paradoxes, contradictions, and curious questions from the edges of mathematics and physics — where logic meets mystery.

- [**Scientific Essays**]({{ "/insights/" | relative_url }})  
  Essays and reflections on mathematics and physics — exploring theory, structure, and the history of scientific thought.

- [**High School**]({{ "/high-school/" | relative_url }})  
  Slides, solved math and physics exercises, and printable formula sheets designed for high school learning and exam preparation.

- [**University**]({{ "/university/" | relative_url }})  
  Detailed calculus, linear algebra, and physics resources — complete solutions and conceptual notes for undergraduate students.

- [**Gallery**]({{ "/gallery/" | relative_url }})  
  A visual collection of generative art and mathematical structures, exploring the beauty of science through images.

- [**About**]({{ "/about/" | relative_url }})  
  Learn more about the educational vision of Logic & Motion — and meet the people who shape the project.

</div>
