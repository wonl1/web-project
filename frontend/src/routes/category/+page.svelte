<script>
	import { Button } from 'flowbite-svelte';
	import { goto } from '$app/navigation';
  
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
  
	function handleImageClick(id) {
	  goto(`/image/${id}`);
	}
  </script>
  
  <div class="flex items-center justify-center py-4 md:py-8 flex-wrap gap-3 mb-3 mx-auto">
	<Button pill size="xl" color="alternative">All categories</Button>
	<Button pill size="xl" color="alternative">Location</Button>
	<Button pill size="xl" color="alternative">Season</Button>
	<Button pill size="xl" color="alternative">Theme</Button>
  </div>
  
  <div class="gallery grid gap-4 grid-cols-2 md:grid-cols-3">
	{#each images as image}
	  <a href={`/image/${image.id}`} on:click|preventDefault={() => handleImageClick(image.id)}>
		<img src={image.src} alt={image.alt} class="cursor-pointer" />
	  </a>
	{/each}
  </div>

