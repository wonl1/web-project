<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';
  import { Button } from 'flowbite-svelte';
  import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
  import { faUpload } from '@fortawesome/free-solid-svg-icons';

  /**
   * @type {string}
   */
  let imageId;
  /**
   * @type {{ id: string; alt: string; src: string; } | undefined}
   */
  let image;

  const images = [
    { id: 'erbology', alt: 'erbology', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image.jpg' },
    { id: 'shoes', alt: 'shoes', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg' },
    { id: 'small bag', alt: 'small bag', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg' },
    { id: 'plants', alt: 'plants', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg' },
    { id: 'watch', alt: 'watch', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg' },
    { id: 'shoe', alt: 'shoe', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg' },
    { id: 'cream', alt: 'cream', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-6.jpg' },
    { id: 'small bag', alt: 'small bag', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-7.jpg' },
    { id: 'lamp', alt: 'lamp', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-8.jpg' },
    { id: 'toiletbag', alt: 'toiletbag', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-9.jpg' },
    { id: 'playstation', alt: 'playstation', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-10.jpg' },
    { id: 'bag', alt: 'bag', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-11.jpg' }
  ];

  $: {
    imageId = $page.params.id;
    image = images.find(img => img.id === imageId);
  }

  onMount(() => {
    if (!image) {
      // Handle the case where the image is not found
      console.error('Image not found');
    }
  });

  function navigateToUploadPage() {
    goto('/upload'); // Replace with the actual path to your upload page
  }
</script>

{#if image}
  <div class="image-details">
    <h1>{image.alt}</h1>
    <img src={image.src} alt={image.alt} style="width: 700px;" />
    <!-- Add more details about the image here -->
  </div>
{:else}
  <p>Loading...</p>
{/if}

<Button on:click={navigateToUploadPage} class="font-bold bg-darkblue-600 text-lightyellow-100 hover:text-lightyellow-50 hover:bg-darkblue-500">
  <FontAwesomeIcon icon={faUpload} class="w-5 h-5 me-2" /> Upload
</Button>
