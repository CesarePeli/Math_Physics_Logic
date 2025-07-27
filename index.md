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

<!-- ─────────────  HERO  ───────────── -->
<div class="homepage-header">
  <h1 class="homepage-title">Logic &amp; Motion</h1>
  <p class="homepage-subtitle">Tools for students and teachers — grounded in reasoning and clarity.</p>
</div>

<!-- ─────────  FEATURED CONTENT  ───────── -->
<section id="featured" style="margin:4rem auto;max-width:1000px;padding:0 1rem;">
<h2 style="font-size:1.6rem;margin-bottom:1rem;">Featured</h2>

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1.2rem;">

{% assign spotlight = site.pages | where_exp:"p","p.featured" | sort:"featured_rank" | slice: 0,4 %}

{% for item in spotlight %}
  {% assign bg = item.header_image | default:"/images/placeholder.jpg" | relative_url %}
  <div style="height:180px;border-radius:1rem;overflow:hidden;
              background:url('{{ bg }}') center/cover no-repeat,rgba(0,0,0,.55);
              background-blend-mode:darken;">

    <a href="{{ item.url | relative_url }}" style="display:flex;
              align-items:flex-end;justify-content:center;width:100%;height:100%;
              text-decoration:none;color:#fff;">

      <span style="font-size:1rem;font-weight:600;margin:0 1rem 1rem;text-align:center;display:block;width:100%;">
        {{ item.title }}
      </span>
    </a>
  </div>
{% endfor %}

</div>
</section>
<!-- ────────────────────────────────────── -->



<!-- ─────────────  INTRO  ───────────── -->
<div class="content-box">

Logic & Motion began from a simple idea: math and physics are not collections of facts, but languages to think with, and tools to see the world more clearly.  

**Mathematics** is not a list of formulas to memorize, but a way of thinking — grounded in reasoning, proof, and internal coherence.  
**Physics**, in turn, is approached as the science of models: abstract principles expressed through mathematics, applied across diverse real-world contexts.

The project bridges education and exploration — offering slides, guided exercises, printable summaries, and original writing that invite reflection as well as understanding.  
Rooted in logic, inquiry, and the desire to understand, *Logic & Motion* sees science as a structured way of thinking — intellectually rigorous, yet always human and meaningful.

</div>

<!-- ─────────────  SECTION LINKS  ───────────── -->
<div class="content-box">

## Explore the Sections

- [**The Odd Questions**]({{ "/odd-questions/" | relative_url }})  
  Explore strange and thought-provoking problems at the edge of math and science — where logic meets paradox.

- [**In-Depth Articles**]({{ "/insights/" | relative_url }})  
  Rigorous, reflective essays on mathematical and physical theory — from foundational principles to structural analysis.

- [**High School**]({{ "/high-school/" | relative_url }})  
  Explained slides, solved problems, and printable formula sheets in math and physics.

- [**University**]({{ "/university/" | relative_url }})  
  Detailed solutions and conceptual materials for calculus, linear algebra, and more.

- [**Gallery**]({{ "/gallery/" | relative_url }})  
  A visual collection of generative artworks exploring mathematical and scientific structure.

- [**About**]({{ "/about/" | relative_url }})  
  Learn more about the educational vision — and meet the people who shape Logic & Motion.

</div>
