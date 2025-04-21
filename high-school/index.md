---
layout: default
title: High School Materials
permalink: /high-school/
background_image: "/images/slide.png"
description: "Teaching and study resources for high school mathematics and physics: slides, solved exercises and formula sheets."
---

## High School Math and Physics

A collection of digital resources designed for both teachers and students. Materials cover mathematics and physics topics typically taught in high school.

### 👩‍🏫 For teachers:
- Ready-to-use slides for interactive whiteboards or projectors
- Structured exercises with solutions for class tests
- Clean, printable formula sheets for student support

### 🧑‍🎓 For students:
- Clear explanations and visual aids
- Solved exercises for test preparation
- Concise and complete formula sheets

### 📘 [Explained Slides](/high-school/explained-slides/)
### ✍️ [Solved Exercises](/high-school/solved-exercises/)
### 📑 [Formula Sheets](/high-school/formula-sheets/)

## Test grafico Plotly

Questo è un semplice grafico interattivo generato direttamente nel file `.md`:

<div id="plot-test" style="height: 400px;"></div>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    Plotly.newPlot('plot-test', [{
      x: [1, 2, 3, 4],
      y: [10, 15, 13, 17],
      mode: 'lines+markers',
      marker: { color: 'blue' }
    }], {
      title: 'Plotly Test'
    });
  });
</script>
