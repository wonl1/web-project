<script>
  import { Card, Button } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
  
  function navigateToImagePage1() {
    goto('/image/Zhangye%20Danxia%20Geopark,%20China');
  }
  
  function navigateToImagePage2() {
    goto('/image/Amalfi%20Coast,%20Italy'); 
  }
  
  function navigateToImagePage3() {
    goto('/image/Banff%20National%20Park,%20Canada'); 
  }

  function navigateToImagePage4() {
    goto('/image/Venice,%20Italy');
  }
  
  let vCard = false;
</script>

<div class="card-container">
  <div class="card cursor-pointer" role="button" on:click={navigateToImagePage1} on:keydown={navigateToImagePage1} tabindex="0">
    <img src="https://hips.hearstapps.com/hmg-prod/images/hbz-zhangye-gettyimages-175323801-1505334995.jpg?crop=1xw:1xh;center,top&resize=980:*" alt="Zhangye Danxia Geopark, China" class="card-img">
    <div class="card-content">
      <h5 class="card-title">Zhangye Danxia Geopark, China</h5>
      <p class="card-description">Zhangye Danxia Geopark, located in the Gansu Province of China, is renowned for its stunning and colorful rock formations that resemble a layered, multicolored cake. These unique geological features are the result of millions of years of sedimentary rock layers being subjected to tectonic plate movements and erosion. The vibrant colors, ranging from deep reds and oranges to yellows and greens, are due to the mineral deposits within the rock layers.</p>
    </div>
  </div>

  <div class="card cursor-pointer" role="button" on:click={navigateToImagePage2} on:keydown={navigateToImagePage2} tabindex="0">
    <img src="https://hips.hearstapps.com/hbz.h-cdn.co/assets/16/16/1280x1919/gallery-gettyimages-159582943-1.jpg?resize=980:*" alt="Amalfi Coast, Italy" class="card-img">
    <div class="card-content">
      <h5 class="card-title">Amalfi Coast, Italy</h5>
      <p class="card-description">The Amalfi Coast, located in the Campania region of Italy, is one of the most stunning coastal regions in the world. Known for its dramatic cliffs, picturesque towns, and beautiful Mediterranean scenery, it attracts millions of visitors each year.</p>
    </div>
  </div>

  <div class="card cursor-pointer" role="button" on:click={navigateToImagePage3} on:keydown={navigateToImagePage3} tabindex="0">
    <img src="https://hips.hearstapps.com/hmg-prod/images/banff-517747003-1494616292.jpg?crop=0.9997418022205009xw:1xh;center,top&resize=980:*" alt="Banff National Park, Canada" class="card-img">
    <div class="card-content">
      <h5 class="card-title">Banff National Park, Canada</h5>
      <p class="card-description">Banff National Park, located in the Canadian Rockies of Alberta, Canada, is a renowned natural sanctuary known for its stunning mountain landscapes, diverse wildlife, and outdoor recreational activities. Established in 1885, it is Canada's oldest national park and a UNESCO World Heritage Site, celebrated for its breathtaking scenery and environmental significance.</p>
    </div>
  </div>
  
  <div class="card cursor-pointer" role="button" on:click={navigateToImagePage4} on:keydown={navigateToImagePage4} tabindex="0">
    <img src="https://hips.hearstapps.com/hmg-prod/images/hbz-venice-gettyimages-489741024-1505338894.jpg?crop=1xw:1xh;center,top&resize=980:*" alt="Venice, Italy" class="card-img">
    <div class="card-content">
      <h5 class="card-title">Venice, Italy</h5>
      <p class="card-description">Venice, known as "La Serenissima," is one of the most unique and enchanting cities in the world. Built on a network of 118 small islands separated by canals and connected by over 400 bridges, Venice is renowned for its stunning architecture, rich history, and cultural heritage. Located in the northeastern part of Italy, Venice is the capital of the Veneto region and a UNESCO World Heritage Site.</p>
    </div>
  </div>
</div>

<style>
  .card-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 1rem;
    width: 100%;
  }

  .card {
    flex: 1 1 calc(25% - 1rem); /* Adjust width to fit 4 cards in a row with a gap */
    min-width: 250px;
    max-width: 400px; /* Ensures cards do not exceed a reasonable size */
    border: 1px solid #e5e7eb;
    border-radius: 0.5rem;
    overflow: hidden;
    background-color: white;
    transition: transform 0.2s;
    display: flex;
    flex-direction: column;
  }

  .card:hover {
    transform: scale(1.002);
  }

  .card-img {
    width: 100%;
    height: 200px; /* Fixed height to ensure uniformity */
    object-fit: cover;
  }

  .card-content {
    flex: 1;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  .card-title {
    font-size: 1.25rem;
    font-weight: bold;
    color: #111827;
    margin-bottom: 0.5rem;
  }

  .card-description {
    font-size: 0.875rem;
    color: #6b7280;
    flex: 1;
  }

  .cursor-pointer {
    cursor: pointer;
  }
</style>
