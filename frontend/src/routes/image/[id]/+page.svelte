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
	  { id: 'Zhangye Danxia Geopark, China', alt: 'Zhangye Danxia Geopark, China', src: 'https://hips.hearstapps.com/hmg-prod/images/hbz-zhangye-gettyimages-175323801-1505334995.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Amalfi Coast, Italy', alt: 'Amalfi Coast, Italy', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/1280x1919/gallery-gettyimages-159582943-1.jpg?resize=980:*' },
	  { id: 'Banff National Park, Canada', alt: 'Banff National Park, Canada', src: 'https://hips.hearstapps.com/hmg-prod/images/banff-517747003-1494616292.jpg?crop=0.9997418022205009xw:1xh;center,top&resize=980:*' },
	  { id: 'Venice, Italy', alt: 'Venice, Italy', src: 'https://hips.hearstapps.com/hmg-prod/images/hbz-venice-gettyimages-489741024-1505338894.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Great Ocean Road, Australia', alt: 'Great Ocean Road, Australia', src: 'https://hips.hearstapps.com/hmg-prod/images/great-ocean-road-128394846-1494616348.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Machu Picchu', alt: 'Machu Picchu', src: 'https://hips.hearstapps.com/hmg-prod/images/hbz-machu-ppichu-gettyimages-629556601-1505338681.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Pamukkale, Turkey', alt: 'Pamukkale, Turkey', src: 'https://hips.hearstapps.com/hmg-prod/images/hbz-pamukkale-gettyimages-466129341-1505338681.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Pitons, St Lucia', alt: 'Pitons, St Lucia', src: 'https://hips.hearstapps.com/hmg-prod/images/st-lucia-154917524-1494616323.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Maya Bay, Thailand', alt: 'Maya Bay, Thailand', src: 'https://hips.hearstapps.com/hmg-prod/images/gettyimages-1393618379-65f44307eb229.jpg?crop=0.891xw:1.00xh;0.0486xw,0&resize=980:*' },
	  { id: 'Japan in Cherry Blossom Season',alt: 'Japan in Cherry Blossom Season', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/1280x1919/japan-gettyimages-137098062.jpg?resize=980:*' },
	  { id: 'Marrakesh, Morocco',alt: 'Marrakesh, Morocco', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/marrakech-gettyimages-152834676.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Chiang Mai, Thailand',alt: 'Chiang Mai, Thailand', src: 'https://hips.hearstapps.com/hmg-prod/images/chiang-mai-thailand-65f4473216a4b.jpg?crop=0.446xw:1.00xh;0.142xw,0&resize=980:*' },
	  { id: 'Bora Bora, French Polynesia', alt: 'Bora Bora, French Polynesia', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/bora-bora-gettyimages-575766591.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Oia, Santorini, Greece', alt: 'Oia, Santorini, Greece', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/1461265325-santorini-gettyimages-107741204.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Mù Cang Chải, Vietnam', alt: 'Mù Cang Chải, Vietnam', src: 'https://hips.hearstapps.com/hmg-prod/images/hbz-mu-cang-chai-gettyimages-625247432-1505338864.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Tamil Nadu, India', alt: 'Tamil Nadu, India', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/tamil-nadu-gettyimages-152415224.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Torres del Paine National Park, Chile', alt: 'Torres del Paine National Park, Chile', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/mirador-las-torres-gettyimages-512588114.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Forbidden City, Beijing, China', alt: 'Forbidden City, Beijing, China', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/gettyimages-116147513.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Fiordland National Park, New Zealand', alt: 'Fiordland National Park, New Zealand', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/new-zealand.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Bagan, Myanmar', alt: 'Bagan, Myanmar', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/myanmar-gettyimages-137671616_1.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Havasu Falls, Arizona', alt: 'Havasu Falls, Arizona', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/havasu-gettyimages-rh252-10343_1.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Sheikh Zayed Grand Mosque, Abu Dhabi, UAE',alt: 'Sheikh Zayed Grand Mosque, Abu Dhabi, UAE', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/abu-dhabi-gettyimages-487888511_1.jpg?crop=1xw:0.9998272287491361xh;center,top&resize=980:*' },
	  { id: 'Lisbon, Portugal',alt: 'Lisbon, Portugal', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/lisbon-gettyimages-488108027_1.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Cairngorms National Park, Scotland',alt: 'Cairngorms National Park, Scotland', src: 'https://hips.hearstapps.com/hmg-prod/images/cairngorms-national-park-scotland-gettyimages-560495935-1655139358.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Fernando de Noronha, Brazil', alt: 'Fernando de Noronha, Brazil', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/3200x4799/brazil_1.jpg?resize=980:*' },
	  { id: 'St. Basil Cathedral, Moscow, Russia', alt: 'St. Basil Cathedral, Moscow, Russia', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/moscow-gettyimages-552609685_1.jpg?crop=1xw:0.9999035865792518xh;center,top&resize=980:*' },
	  { id: 'Cape Town, South Africa', alt: 'Cape Town, South Africa', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/cape-town-gettyimages-471380295.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Blue Lagoon, Iceland', alt: 'Blue Lagoon, Iceland', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/iceland-gettyimages-511371497_1.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Paris, France', alt: 'Paris, France', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/1461268850-paris-gettyimages-182176376.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'Sossusvlei, Namibia', alt: 'Sossusvlei, Namibia', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/3200x4894/namibia-gettyimages-501211045_1.jpg?resize=980:*' },
	  { id: 'Hawa Mahal, Jaipur, India', alt: 'Hawa Mahal, Jaipur, India', src: 'https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/india.jpg?crop=1.0xw:1xh;center,top&resize=980:*' },
	  { id: 'El Yunque National Forest, Puerto Rico', alt: 'El Yunque National Forest, Puerto Rico', src: 'https://hips.hearstapps.com/hmg-prod/images/puerto-rico-el-yunque-rain-forest-waterfall-news-photo-1578672814.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Zlatni Rat, Croatia',alt: 'Zlatni Rat, Croatia', src: 'https://hips.hearstapps.com/hmg-prod/images/croatia-hvar-island-bol-aerial-view-at-the-zlatni-royalty-free-image-1571860455.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Lofoten Islands, Norway',alt: 'Lofoten Islands, Norway', src: 'https://hips.hearstapps.com/hmg-prod/images/aerial-view-of-lofoten-islands-in-norway-royalty-free-image-1571860561.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Miho no Matsubara, Japan',alt: 'Miho no Matsubara, Japan', src: 'https://hips.hearstapps.com/hmg-prod/images/miho-no-matsubara-beach-and-fuji-san-in-twilight-royalty-free-image-1571860640.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Isla Holbox, Mexico', alt: 'Isla Holbox, Mexico', src: 'https://hips.hearstapps.com/hmg-prod/images/holbox-island-palm-tree-huts-mexico-royalty-free-image-1571860719.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Barcelona, Spain', alt: 'Barcelona, Spain', src: 'https://hips.hearstapps.com/hmg-prod/images/barcelona-parc-guell-at-sunset-royalty-free-image-1571860792.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Iguazú Falls, Argentina', alt: 'Iguazú Falls, Argentina', src: 'https://hips.hearstapps.com/hmg-prod/images/brazil-iguazu-waterfalls-in-national-park-royalty-free-image-1571860861.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Key West, Florida', alt: 'Key West, Florida', src: 'https://hips.hearstapps.com/hmg-prod/images/wooden-signs-royalty-free-image-1571861059.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Giza, Egypt', alt: 'Giza, Egypt', src: 'https://hips.hearstapps.com/hmg-prod/images/camel-in-desert-with-pyramids-background-royalty-free-image-1571860986.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Comino Island, Malta', alt: 'Comino Island, Malta', src: 'https://hips.hearstapps.com/hmg-prod/images/deck-chairs-on-rocks-by-sea-against-clear-blue-sky-royalty-free-image-1571861100.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Antarctic Peninsula, Antarctica', alt: 'Antarctic Peninsula, Antarctica', src: 'https://hips.hearstapps.com/hmg-prod/images/antarctic-peninsula-antarctica-gettyimages-534975764-1655139358.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Atacama Desert, Chile', alt: 'Atacama Desert, Chile', src: 'https://hips.hearstapps.com/hmg-prod/images/atacama-desert-chile-gettyimages-175189565-1655139358.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Caño Cristales, Colombia', alt: 'Caño Cristales, Colombia', src: 'https://hips.hearstapps.com/hmg-prod/images/cano-cristales-colombia-gettyimages-1655139359.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'South Luangwa National Park, Zambia',alt: 'South Luangwa National Park, Zambia', src: 'https://hips.hearstapps.com/hmg-prod/images/south-luangwa-national-park-zambia-gettyimages-492890344-1655139357.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Nahanni National Park Reserve, Northwest Territories',alt: 'Nahanni National Park Reserve, Northwest Territories', src: 'https://hips.hearstapps.com/hmg-prod/images/nahanni-national-park-reserve-northwest-territories-gettyimages-594908028-1655139358.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Okavango Delta, Botswana',alt: 'Okavango Delta, Botswana', src: 'https://hips.hearstapps.com/hmg-prod/images/okavango-delta-botswana-gettyimages-111650618-1655139359.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Salar de Uyuni, Bolivia',alt: 'Salar de Uyuni, Bolivia', src: 'https://hips.hearstapps.com/hmg-prod/images/salar-de-uyuni-bolivia-gettyimages-495741683-1655139359.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Vorarlberg, Austria',alt: 'Vorarlberg, Austria', src: 'https://hips.hearstapps.com/hmg-prod/images/vorarlberg-austria-gettyimages-1655139358.jpg?crop=1xw:1xh;center,top&resize=980:*' },
	  { id: 'Whitsunday Islands, Queensland, Australia',alt: 'Whitsunday Islands, Queensland, Australia', src: 'https://hips.hearstapps.com/hmg-prod/images/whitsunday-islands-gettyimages-1655139358.jpg?crop=1xw:1xh;center,top&resize=980:*' },
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
    <img src={image.src} alt={image.alt} class="image-size" />
    <!-- Add more details about the image here -->
  </div>
{:else}
  <p>Loading...</p>
{/if}

<Button on:click={navigateToUploadPage} class="font-bold bg-darkblue-600 text-lightyellow-100 hover:text-lightyellow-50 hover:bg-darkblue-500">
  <FontAwesomeIcon icon={faUpload} class="w-5 h-5 me-2" /> Upload
</Button>

<style>
  .image-size {
    width: 100%;
    max-width: 500px; /* Set the maximum width for the image */
    height: 600px; /* Maintain the aspect ratio of the image */
  }
</style>
