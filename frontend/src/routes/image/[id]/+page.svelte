<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';
  import { Button, P } from 'flowbite-svelte';
  import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
  import { faUpload, faChevronLeft, faChevronRight, faTimes } from '@fortawesome/free-solid-svg-icons';
  import 'leaflet/dist/leaflet.css';
  import { images } from './images.js';
  import './images.css';

  let imageId;
  let image;
  let uploadedImages = [];
  let loading = true;
  let errorMessage = '';
  let scrollContainer;
  let L;
  let selectedImageDetails = null; 

  const backendImagePath = 'http://127.0.0.1:8017/media/images/';

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
      const response = await fetch(`http://127.0.0.1:8017/api/posts/${imageId}`);
      if (!response.ok) {
        throw new Error('An error occurred while loading the image.');
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
      const response = await fetch(`http://127.0.0.1:8017/api/posts/`);
      if (!response.ok) {
        throw new Error('An error occurred while loading the image.');
      }
      uploadedImages = await response.json();
      uploadedImages.forEach(uploadedImage => {
        uploadedImage.image = `${backendImagePath}${uploadedImage.image.split('/').pop()}`;
      });
      console.log('Uploaded Images:', uploadedImages);
    } catch (error) {
      console.error(error);
      errorMessage = error.message;
    }
  }

  async function deleteImage(id) {
    if (confirm('Are you sure you want to delete the image?')) {
      console.log('Attempting to delete image with id:', id);
      if (!id) {
        console.error('Invalid ID for deletion:', id);
        errorMessage = 'Invalid image ID.';
        return;
      }

      try {
        const response = await fetch(`http://127.0.0.1:8017/api/posts/${id}/`, {
          method: 'DELETE',
        });
        if (!response.ok) {
          throw new Error('An error occurred while deleting the image.');
        }
        uploadedImages = uploadedImages.filter(image => image.id !== id);
        console.log('Remaining Uploaded Images after deletion:', uploadedImages);
      } catch (error) {
        console.error(error);
        errorMessage = error.message;
      }
    }
  }

  async function showImageDetails(id) {
    try {
      const response = await fetch(`http://127.0.0.1:8017/api/posts/${id}`);
      if (!response.ok) {
        throw new Error('An error occurred while loading the image.');
      }
      selectedImageDetails = await response.json();
      selectedImageDetails.image = `${backendImagePath}${selectedImageDetails.image.split('/').pop()}`;
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
      console.error('Image not found.', imageId);
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
    <div class="image-and-description flex flex-col sm:flex-row">
      <img src={image.src || image.image} alt={image.alt || image.title} class="image-size sm:w-1/2" />
      <div class="image-description  sm:w-1/2">
        <P class="mb-3" color="text-gray-600 dark:text-gray-400" firstupper style="line-height: 1.2;">
          {@html image.description}
        </P>
      </div>
    </div>
    <div id="map" class="map"></div>
  </div>
{/if}

{#if uploadedImages.length > 0}
  <div class="uploaded-images-container mb-10">
    <div class="flex items-center justify-between">
      <h2>Uploaded Images</h2>
      <Button on:click={navigateToUploadPage} class="font-bold bg-darkblue-600 text-lightyellow-100 hover:text-lightyellow-50 hover:bg-darkblue-500">
        <FontAwesomeIcon icon={faUpload} class="w-5 h-5 me-2" /> Upload
      </Button>
    </div>
    <div class="scroll-arrows">
      <button on:click={scrollLeft} class="scroll-button">
        <FontAwesomeIcon icon={faChevronLeft} />
      </button>
      <div class="uploaded-images" bind:this={scrollContainer}>
        {#each uploadedImages as uploadedImage, i}
          <div class="uploaded-image-details flex flex-col items-center">
            <button type="button" on:click={() => showImageDetails(uploadedImage.id)} class="uploaded-image-button">
              <img src={uploadedImage.image} alt={uploadedImage.title} class="uploaded-image-size" />
            </button>
            <Button 
              on:click={() => deleteImage(uploadedImage.id)} 
              class="delete-button font-bold bg-darkblue-300 mt-2 mr-2 text-xs p-1 rounded-full flex items-center justify-center w-4 h-4">
              <FontAwesomeIcon icon={faTimes} />
            </Button>
          </div>
        {/each}
      </div>
      <button on:click={scrollRight} class="scroll-button">
        <FontAwesomeIcon icon={faChevronRight} />
      </button>
    </div>
  </div>
{/if}

{#if selectedImageDetails}
  <div class="modal" style="z-index: 1000;">
    <div class="modal-content">
      <h2>{selectedImageDetails.title}</h2>
      <img src={selectedImageDetails.image} alt={selectedImageDetails.title} style="max-width: 300px; max-height: 300px; object-fit: cover;" />
      <p>{new Date(selectedImageDetails.date).toLocaleDateString()}</p>
      <p>{selectedImageDetails.content}</p>
      <Button on:click={() => selectedImageDetails = null} class="bg-black text-white">Close</Button>
    </div>
  </div>
{/if}