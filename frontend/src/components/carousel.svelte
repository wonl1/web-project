<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let slides = [
    { src: '/c1.jpg', alt: 'Slide 1' },
    { src: '/c2.jpg', alt: 'Slide 2' },
    { src: '/c3.jpg', alt: 'Slide 3' }
  ]; 
  let activeSlide = 0;
  let intervalId;

  function goToSlide(index) {
    activeSlide = index;
  }

  function goToEventPage() {
    goto('/event');
  }

  // 슬라이드가 자동으로 넘어가도록 하는 함수
  function startAutoSlide() {
    intervalId = setInterval(() => {
      activeSlide = (activeSlide + 1) % slides.length;
    }, 20000); // 20초마다 슬라이드 변경
  }

  onMount(startAutoSlide);
</script>

<div class="carousel">
  {#each slides as slide, i}
    <div class="slide {i === activeSlide ? 'active' : ''}">
      <div class="slide-box">
        <img src={slide.src} alt={slide.alt} class="slide-image" />
        {#if i === 0}
          <div class="text-right-container">
            <p class="text-right">
              Find the world's hidden gems<br>Share your travel stories and pictures
            </p>
          </div>
        {/if}
        {#if i === 1}
          <button class="text-center-container" on:click={goToEventPage} on:keydown={(event) => {if (event.key === 'Enter') goToEventPage()}} aria-label="Go to event page">
            <p class="text-center">
              Choose the best picture
            </p>
          </button>
        {/if}
        {#if i === 2}
          <div class="overlay-gray">
            <p class="overlay-text">
              The 50 most beautiful destinations<br>in the world
            </p>
          </div>
        {/if}
      </div>
      <div class="dots">
        {#each slides as _, j}
          <button class="dot {j === i ? 'active' : ''}" on:click={() => goToSlide(j)} on:keydown={(event) => {if (event.key === 'Enter') goToSlide(j)}} tabindex="0" aria-label="Go to slide {j + 1}"></button>
        {/each}
      </div>
    </div>
  {/each}
</div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Mogra&display=swap');

  .carousel {
    display: flex;
    overflow: hidden;
    width: 100%;
  }

  .slide {
    display: none;
    flex-shrink: 0;
    width: 100%;
    height: 500px; 
    position: relative;
    border-radius: 10px; /* 둥근 모서리 */
  }

  .slide.active {
    display: block;
  }

  .slide-box {
    width: 100%;
    height: 100%;
    overflow: hidden;
    border-radius: 10px;
    position: relative;
  }

  .slide-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .text-right-container {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    display: flex;
    align-items: center;
    padding: 20px;
    box-sizing: border-box;
    background: none;
    text-align: center;
  }

  .text-center-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 20px;
    box-sizing: border-box;
    background: none;
    border: none; /* Remove default button styles */
    cursor: pointer; /* Ensure it's clickable */
  }

  .text-right {
    color: white;
    font-size: 35px;
    font-family: 'Mogra', cursive;
    padding: 20px;
    background: none;
  }

  .text-center {
    color: white;
    font-size: 55px;
    font-family: 'Mogra', cursive;
    padding: 20px;
    background: none;
    text-align: center;
  }

  .overlay-gray {
    background: rgba(0, 0, 0, 0.5);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 24px;
    text-align: center;
    padding: 20px;
    box-sizing: border-box;
    border-radius: 10px;
  }

  .overlay-text {
    font-size: 55px;
    font-family: 'Mogra', cursive;
  }

  .dots {
    position: absolute;
    bottom: 10px;
    width: 100%;
    display: flex;
    justify-content: center;
  }

  .dot {
    height: 10px;
    width: 10px;
    background-color: #bbb;
    border-radius: 50%;
    display: inline-block;
    margin: 0 2px;
    cursor: pointer;
  }

  .dot.active {
    background-color: #717171;
  }
</style>
