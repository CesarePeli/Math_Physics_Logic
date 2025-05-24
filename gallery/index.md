---
layout: default
title: Scientific Gallery
permalink: /gallery/
meta_description: "Explore a visual gallery of AI-generated artworks inspired by mathematics and science."
---

<style>
  body {
    background-color: #1c1f2b;
  }
</style>

<div class="relative h-96 flex items-center justify-center text-center text-white bg-cover bg-center" style="background-image: url('/gallery-images/header.jpg');">
  <div class="absolute inset-0 bg-black bg-opacity-50"></div>
  <div class="relative z-10">
    <h1 class="text-4xl font-bold mb-2">The Scientific Gallery</h1>
    <p class="text-lg max-w-2xl mx-auto">Images at the intersection of abstraction and form.</p>
  </div>
</div>

{% assign sorted_gallery = site.gallery | sort: "order" %}
<div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-2 gap-8 px-6 py-12">
  {% for item in sorted_gallery %}
    <div class="overflow-hidden rounded-xl shadow-lg">
      <a href="#" data-index="{{ forloop.index0 }}" onclick="openLightbox({{ forloop.index0 }}); return false;">
        <img src="{{ item.image }}" alt="{{ item.title }}" class="w-full h-auto object-cover rounded-xl">
      </a>
      <div class="mt-3 px-2">
        <h2 class="text-2xl font-semibold text-white">{{ item.title }}</h2>
        <p class="text-sm text-gray-400">{{ item.description }}</p>
      </div>
    </div>
  {% endfor %}
</div>

<!-- Lightbox Modal -->
<div id="lightbox" class="fixed inset-0 bg-black bg-opacity-90 flex items-center justify-center hidden z-50">
  <button onclick="closeLightbox()" class="absolute top-4 right-4 text-white text-2xl">&times;</button>
  <img id="lightbox-img" src="" alt="" class="max-w-5xl w-full h-auto rounded-lg">
  <button onclick="prevImage()" class="absolute left-4 text-white text-3xl">&#10094;</button>
  <button onclick="nextImage()" class="absolute right-4 text-white text-3xl">&#10095;</button>
</div>

<script>
  const galleryItems = [
    {% for item in sorted_gallery %}
      {
        image: "{{ item.image }}",
        title: "{{ item.title }}"
      }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];

  let currentIndex = 0;

  function openLightbox(index) {
    currentIndex = index;
    const item = galleryItems[index];
    document.getElementById('lightbox-img').src = item.image;
    document.getElementById('lightbox').classList.remove('hidden');

    if (window.innerWidth < 768) {
      const lightbox = document.getElementById('lightbox');
      if (lightbox.requestFullscreen) {
        lightbox.requestFullscreen().catch(err => console.log("Fullscreen denied:", err));
      } else if (lightbox.webkitRequestFullscreen) {
        lightbox.webkitRequestFullscreen();
      }
    }
  }

  function closeLightbox() {
    document.getElementById('lightbox').classList.add('hidden');
    if (document.fullscreenElement) {
      document.exitFullscreen().catch(err => console.log("Exit fullscreen error:", err));
    }
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
