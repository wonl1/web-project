<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';
  import { Button } from 'flowbite-svelte';
  import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
  import { faUpload, faChevronLeft, faChevronRight } from '@fortawesome/free-solid-svg-icons';
  import 'leaflet/dist/leaflet.css';
  import { images } from './images.js';

  let imageId;
  let image;
  let uploadedImages = []; 
  let loading = true;
  let errorMessage = '';
  let scrollContainer;
  let L;

  const backendImagePath = 'http://127.0.0.1:8007/media/images/';

  $: {
    imageId = $page.params.id;
    console.log('imageId:', imageId);

    if (isNaN(parseInt(imageId))) {
      image = images.find(img => img.id === imageId);
      loading = false;
    } else {
      fetchImage();
    }
  }

  async function fetchImage() {
    try {
      const response = await fetch(`http://127.0.0.1:8007/api/posts/${imageId}`);
      if (!response.ok) {
        throw new Error('이미지 로드 중 오류가 발생했습니다.');
      }
      image = await response.json();

      image.image = `${backendImagePath}${image.image.split('/').pop()}`;
      loading = false;
      loadMap();
    } catch (error) {
      console.error(error);
      errorMessage = error.message;
      loading = false;
    }
  }

  async function fetchUploadedImages() {
    try {
      const response = await fetch(`http://127.0.0.1:8007/api/posts/`);
      if (!response.ok) {
        throw new Error('이미지 로드 중 오류가 발생했습니다.');
      }
      uploadedImages = await response.json();

      uploadedImages.forEach(uploadedImage => {
        uploadedImage.image = `${backendImagePath}${uploadedImage.image.split('/').pop()}`;
      });
    } catch (error) {
      console.error(error);
      errorMessage = error.message;
    }
  }

  function loadMap() {
    if (typeof window !== 'undefined' && image && L) {
      const map = L.map('map').setView([image.lat, image.lng], 10);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
      }).addTo(map);
      L.marker([image.lat, image.lng]).addTo(map)
        .bindPopup(image.alt)
        .openPopup();
    }
  }

  onMount(async () => {
    if (typeof window !== 'undefined') {
      const module = await import('leaflet');
      L = module.default;
    }
    if (!image) {
      console.error('이미지를 찾을 수 없습니다.', imageId);
    } else if (!loading) {
      loadMap();
    }
    fetchUploadedImages();
  });

  function navigateToUploadPage() {
    goto('/upload');
  }

  function scrollLeft() {
    scrollContainer.scrollBy({ left: -300, behavior: 'smooth' });
  }

  function scrollRight() {
    scrollContainer.scrollBy({ left: 300, behavior: 'smooth' });
  }
</script>

{#if loading}
  <p>Loading...</p>
{:else if errorMessage}
  <p>{errorMessage}</p>
{:else if image}
  <div class="image-details">
    <div class="image-text">
      <h1>{image.alt || image.title}</h1>
    </div>
    <div class="image-and-description">
      <img src={image.src || image.image} alt={image.alt || image.title} class="image-size" />
      <div class="image-description">
        <p class="mb-3 text-gray-600 dark:text-gray-400" style="line-height: 1.2;">
          {@html image.description}
        </p>
      </div>
    </div>
    <div id="map" class="map"></div>
  </div>
{/if}

<Button on:click={navigateToUploadPage} class="font-bold bg-darkblue-600 text-lightyellow-100 hover:text-lightyellow-50 hover:bg-darkblue-500 mt-4">
  <FontAwesomeIcon icon={faUpload} class="w-5 h-5 me-2" /> 업로드
</Button>

{#if uploadedImages.length > 0}
  <div class="uploaded-images-container">
    <h2>업로드된 이미지</h2>
    <div class="scroll-arrows">
      <button on:click={scrollLeft} class="scroll-button">
        <FontAwesomeIcon icon={faChevronLeft} />
      </button>
      <div class="uploaded-images" bind:this={scrollContainer}>
        {#each uploadedImages as uploadedImage}
          <div class="uploaded-image-details">
            <img src={uploadedImage.image} alt={uploadedImage.title} class="uploaded-image-size" />
            <h3>{uploadedImage.title}</h3>
          </div>
        {/each}
      </div>
      <button on:click={scrollRight} class="scroll-button">
        <FontAwesomeIcon icon={faChevronRight} />
      </button>
    </div>
  </div>
{/if}

<style>
  .image-details, .uploaded-image-details {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-top: 2rem;
  }

  .image-text {
    margin-bottom: 1rem;
  }

  h1, h2, h3 {
    font-size: 2rem;
    font-weight: bold;
  }

  .image-and-description {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    width: 100%;
  }

  .image-size {
    flex: 1;
    height: 800px;
    object-fit: cover;
  }

  .image-description {
    flex: 1;
  }

  .map {
    height: 300px; 
    min-width: 300px;
    width: 100%;
    margin-top: 1rem;
  }

  .uploaded-images-container {
    margin-top: 2rem;
    position: relative;
  }

  .uploaded-images {
    display: flex;
    flex-direction: row;
    overflow-x: auto;
    gap: 1rem;
    scroll-behavior: smooth;
  }

  .uploaded-image-details {
    flex: 0 0 auto;
    width: 300px;
    text-align: center; 
  }

  .uploaded-image-size {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }

  .scroll-arrows {
    display: flex;
    align-items: center;
  }

  .scroll-button {
    background-color: transparent;
    border: none;
    cursor: pointer;
    font-size: 2rem;
    margin: 0 0.5rem;
  }

  .scroll-button:focus {
    outline: none;
  }
</style>
