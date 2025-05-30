---
layout: default
title: The Scientific Gallery
permalink: /gallery/
background_image: "/gallery-images/header.jpg"
description: "Explore a visual gallery of AI-generated artworks inspired by mathematics and science."
---

<div class="content-box">
  <h1>The Scientific Gallery</h1>
  <p><em>Images at the intersection of abstraction and form — blending visual intuition with conceptual structure.</em></p>
</div>

<div class="content-box">
  <div class="gallery-grid" id="gallery-grid"></div>
</div>

<!-- Lightbox -->
<div id="lightbox" class="lightbox">
  <div class="lightbox-text">
    <h2 id="lightbox-title"></h2>
    <p id="lightbox-description"></p>
  </div>
  <img id="lightbox-img" src="" alt="">
  <div class="lightbox-nav">
    <button onclick="prevImage()">&#10094;</button>
    <button onclick="nextImage()">&#10095;</button>
  </div>
  <button class="close-btn" onclick="closeLightbox()">&times;</button>
</div>

<style>
  .gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    padding: 2rem;
  }

  .gallery-item {
    background: #262c3d;
    border-radius: 1rem;
    overflow: hidden;
    padding: 1rem;
    text-align: center;
  }

  .gallery-item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 0.5rem;
    cursor: pointer;
  }

  .gallery-item h2 {
    margin-top: 0.5rem;
    color: white;
    font-size: 1.1rem;
  }

  .lightbox {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.97);
    z-index: 1000;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }

  .lightbox.active {
    display: flex;
  }

  .lightbox-text {
    position: absolute;
    top: 2rem;
    text-align: center;
    color: white;
    padding: 0 1rem;
  }

  .lightbox-text h2 {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
  }

  .lightbox-text p {
    font-size: 0.9rem;
    color: #aaa;
  }

  .lightbox img {
    width: 100vw;
    height: auto;
    max-height: 90vh;
    object-fit: scale-down;
  }

  .lightbox-nav {
    position: absolute;
    bottom: 2rem;
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 0 2rem;
  }

  .lightbox-nav button {
    font-size: 2rem;
    background: none;
    border: none;
    color: white;
    cursor: pointer;
  }

  .close-btn {
    position: absolute;
    top: 1rem;
    right: 2rem;
    font-size: 2rem;
    color: white;
    background: none;
    border: none;
    cursor: pointer;
  }
</style>

<script>
  const galleryItems = [
    {
      image: "/gallery-images/cat.png",
      title: "The Observed Has Left the Box",
      description: "A cat, observed, sits at the heart of a geometric corridor. Presence replaces uncertainty."
    },
    {
      image: "/gallery-images/emergent-line.png",
      title: "Emergent Phenomenon",
      description: "A minimal composition inspired by linear regression and geometric emergence."
    }
    // Aggiungi altri oggetti qui
  ];

  const galleryGrid = document.getElementById("gallery-grid");

  galleryItems.forEach((item, index) => {
    const container = document.createElement("div");
    container.className = "gallery-item";
    container.innerHTML = `
      <img src="${item.image}" alt="${item.title}" onclick="openLightbox(${index})">
      <h2>${item.title}</h2>
    `;
    galleryGrid.appendChild(container);
  });

  let currentIndex = 0;

  function openLightbox(index) {
    currentIndex = index;
    const item = galleryItems[index];
    document.getElementById("lightbox-img").src = item.image;
    document.getElementById("lightbox-title").textContent = item.title;
    document.getElementById("lightbox-description").textContent = item.description;
    document.getElementById("lightbox").classList.add("active");
  }

  function closeLightbox() {
    document.getElementById("lightbox").classList.remove("active");
  }

  function nextImage() {
    currentIndex = (currentIndex + 1) % galleryItems.length;
    openLightbox(currentIndex);
  }

  function prevImage() {
    currentIndex = (currentIndex - 1 + galleryItems.length) % galleryItems.length;
    openLightbox(currentIndex);
  }
</script>
