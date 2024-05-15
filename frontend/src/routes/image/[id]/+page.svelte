<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores';
  
    let imageId;
    let image;
  
    const images = [
	  { id: 'erbology', alt: 'erbology', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image.jpg' },
	  { id: 'shoes', alt: 'shoes', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg' },
	  { id: 'small bag', alt: 'small bag', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg' },
	  { id: 'plants', alt: 'plants', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg' },
	  { id: 'watch', alt: 'watch', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg' },
	  { id: 'shoe', alt: 'shoe', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg' },
	  { id:'cream', alt: 'cream', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-6.jpg' },
	  { id: 'small bag', alt: 'small bag', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-7.jpg' },
	  { id: 'lamp', alt: 'lamp', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-8.jpg' },
	  { id: 'toiletbag',alt: 'toiletbag', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-9.jpg' },
	  { id: 'playstation',alt: 'playstation', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-10.jpg' },
	  { id: 'bag',alt: 'bag', src: 'https://flowbite.s3.amazonaws.com/docs/gallery/square/image-11.jpg' }
	];
    
    $: {
      imageId = $page.params.id;
      image = images.find(img => img.id === imageId);
    }
  
    onMount(() => {
      if (!image) {
        // 이미지를 찾을 수 없는 경우 처리
        console.error('Image not found');
      }
    });
  </script>
  
  {#if image}
    <div class="image-details">
      <h1>{image.alt}</h1>
      <img src={image.src} alt={image.alt} />
      <!-- 이미지에 대한 세부 정보를 더 추가합니다 -->
    </div>
  {:else}
    <p>Loading...</p>
  {/if}
  