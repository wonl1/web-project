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
      console.log('Uploaded Images:', uploadedImages);
    } catch (error) {
      console.error(error);
      errorMessage = error.message;
    }
  }

  async function deleteImage(id) {
    if (confirm('이미지를 삭제하시겠습니까?')) {
      console.log('Attempting to delete image with id:', id);
      if (!id) {
        console.error('Invalid ID for deletion:', id);
        errorMessage = '유효하지 않은 이미지 ID입니다.';
        return;
      }

      try {
        const response = await fetch(`http://127.0.0.1:8007/api/posts/${id}/`, {
          method: 'DELETE',
        });
        if (!response.ok) {
          throw new Error('이미지 삭제 중 오류가 발생했습니다.');
        }
        uploadedImages = uploadedImages.filter(image => image.id !== id);
        console.log('Remaining Uploaded Images after deletion:', uploadedImages);
      } catch (error) {
        console.error(error);
        errorMessage = error.message;
      }
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
        <P class="mb-3" color="text-gray-600 dark:text-gray-400" firstupper style="line-height: 1.2;">
          {@html image.description}
        </P>
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
        {#each uploadedImages as uploadedImage, i}
          <div class="uploaded-image-details">
            <img src={uploadedImage.image} alt={uploadedImage.title} class="uploaded-image-size" />
            <h3>{uploadedImage.title}</h3>
            <Button on:click={() => deleteImage(uploadedImage.id)} 
              class="delete-button font-bold bg-red-600 text-lightyellow-100 hover:text-lightyellow-50 hover:bg-red-500 mt-2 text-xs p-1">
              <FontAwesomeIcon icon={faTimes}  />
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
