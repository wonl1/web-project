<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';
  import { Button } from 'flowbite-svelte';
  import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
  import { faUpload } from '@fortawesome/free-solid-svg-icons';
  import L from 'leaflet';
  import 'leaflet/dist/leaflet.css';
  import { images } from './images.js';

  /**
   * @type {string}
   */
  let imageId;
  /**
   * @type {{ id: string; alt: string; src: string; lat: number; lng: number; } | undefined}
   */
  let image;


$: {
    imageId = $page.params.id;
    image = images.find(img => img.id === imageId);
  }

  onMount(() => {
    if (!image) {
      // Handle the case where the image is not found
      console.error('Image not found');
    } else {
      // Initialize the map
      const map = L.map('map').setView([image.lat, image.lng], 10);

      // Add OpenStreetMap tiles
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
      }).addTo(map);

      // Add a marker
      L.marker([image.lat, image.lng]).addTo(map)
        .bindPopup(image.alt)
        .openPopup();
    }
  });

  function navigateToUploadPage() {
    goto('/upload'); // Replace with the actual path to your upload page
  }
</script>

{#if image}
  <div class="image-details">
    <div class="image-text">
      <h1>{image.alt}</h1>
      <!-- Add more image details here if needed -->
    </div>
    <div class="image-and-map">
      <img src={image.src} alt={image.alt} class="image-size" />
      <div id="map" class="map"></div> <!-- Map is placed here -->
    </div>
  </div>
{:else}
  <p>Loading...</p>
{/if}

<Button on:click={navigateToUploadPage} class="font-bold bg-darkblue-600 text-lightyellow-100 hover:text-lightyellow-50 hover:bg-darkblue-500 mt-4">
  <FontAwesomeIcon icon={faUpload} class="w-5 h-5 me-2" /> Upload
</Button>

<style>
  .image-details {
    display: flex;
    flex-direction: column; /* Stack elements vertically */
    align-items: flex-start; /* Align text to the left */
    margin-top: 2rem; /* Add space between navigation and content */
  }

  .image-text {
    margin-bottom: 1rem; /* Add space between text and image */
  }

  h1 {
    font-size: 2rem; /* Increase font size */
    font-weight: bold; /* Bold text */
  }

  .image-and-map {
    display: flex;
    align-items: flex-start; /* Align the image and map to the top */
    gap: 1rem; /* Add space between the image and the map */
    width: 100%; /* Ensure the container takes the full width */
  }

  .image-size {
    flex: 1; /* Allow the image to take up available space */
    height: 700px; /* Set the height of the image */
    object-fit: cover; /* Ensure the image covers the allocated space */
  }

  .map {
    flex: 1; /* Allow the map to take up the remaining space */
    height: 300px; /* Set height for the map to match the image */
    min-width: 300px; /* Ensure the map has a minimum width */
    margin-top: 25rem
  }
</style>