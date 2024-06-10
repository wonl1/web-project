<script>
	import { Button } from 'flowbite-svelte';
	import { goto } from '$app/navigation';
	import { images } from './images.js'; 
	
	let filteredImages = images;
	let showAll = true;
	let continents = ['Africa', 'Antarctica', 'Asia', 'Australia', 'Europe', 'North America', 'South America'];
	
	function handleImageClick(id) {
	  goto(`/image/${id}`);
	}
  
	function filterByContinent(continent) {
	  filteredImages = images.filter(image => image.continent === continent);
	  showAll = false;
	}
  
	function showAllImages() {
	  filteredImages = images;
	  showAll = true;
	}
  </script>
  
  <div class="flex justify-center py-4 md:py-8 flex-wrap gap-3 mb-3 mx-auto">
	<Button on:click={showAllImages} style="width: 140px; height: 50px;" pill size="xl" color="alternative">All Categories</Button>
	{#each continents as continent}
	  <Button on:click={() => filterByContinent(continent)} style="width: 140px; height: 50px;" pill size="xl" color="alternative">{continent}</Button>
	{/each}
  </div>
  
  <div class="gallery grid gap-4 grid-cols-2 md:grid-cols-4">
	{#each filteredImages as image}
	  <a href={`/image/${image.id}`} on:click|preventDefault={() => handleImageClick(image.id)} class="relative group">
		<img src={image.src} alt={image.alt} class="cursor-pointer w-full h-full object-cover transition-transform duration-300 transform group-hover:scale-105" />
		<div class="caption absolute inset-0 bg-black bg-opacity-60 flex items-center justify-center text-white text-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
		  <span class="text-lg font-semibold">{image.alt}</span>
		</div>
	  </a>
	{/each}
  </div>
  
  <style>
	.gallery {
	  margin-bottom: 2rem; 
	}
  
	.gallery img {
	  aspect-ratio: 1 / 1.2;
	}
  
	.relative {
	  position: relative;
	}
  
	.caption {
	  position: absolute;
	  inset: 0;
	  background: rgba(0, 0, 0, 0.6);
	  display: flex;
	  align-items: center;
	  justify-content: center;
	  color: white;
	  text-align: center;
	  opacity: 0;
	  transition: opacity 0.3s;
	}
  
	.group:hover .caption {
	  opacity: 1;
	}
  
	.group:hover img {
	  transform: scale(1.05);
	}
  </style>
  
  