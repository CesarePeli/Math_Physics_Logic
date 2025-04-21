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



## Triangolo geometrico minimale

<div id="triangle-plot" style="height: 400px;"></div>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {
    Plotly.newPlot('triangle-plot', [{
      x: [0, 1, 0.5, 0],
      y: [0, 0, 1, 0],
      mode: 'lines',
      line: { color: 'white', width: 3 },
      type: 'scatter'
    }], {
      margin: { t: 20, b: 20, l: 20, r: 20 },
      xaxis: { visible: false },
      yaxis: { visible: false },
      plot_bgcolor: '#000',
      paper_bgcolor: '#000',
      showlegend: false
    }, { staticPlot: true });
  });
</script>
