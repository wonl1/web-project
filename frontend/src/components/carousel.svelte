<script>
  import { onMount } from 'svelte'; 

  let slides = ['Slide 1', 'Slide 2', 'Slide 3']; 
  let activeSlide = 0;
  let colors = ['#ffadad', '#ffd6a5', '#fdffb6']; 
  let intervalId;

  function goToSlide(index) {
    activeSlide = index;
  }

  // 슬라이드가 자동으로 넘어가도록 하는 함수
  function startAutoSlide() {
    intervalId = setInterval(() => {
      activeSlide = (activeSlide + 1) % slides.length;
    }, 8000); // 3초마다 슬라이드 변경
  }

 
  onMount(startAutoSlide);
</script>

<div class="carousel">
  {#each slides as slide, i}
    <div class="slide {i === activeSlide ? 'active' : ''}" style="background-color: {colors[i]}">
      <div class="slide-box">
        {slide}
      </div>
      <div class="dots">
        {#each slides as _, j}
            <button class="dot {j === i ? 'active' : ''}" on:click={() => goToSlide(j)} on:keydown={(event) => {if (event.key === 'Enter') goToSlide(j)}} role="button" tabindex="0"></button>
        {/each}
      </div>
    </div>
  {/each}
</div>

<style>
  .carousel {
    display: flex;
    overflow: hidden;
  }

  .slide {
    display: none;
    flex-shrink: 0;
    width: 100%;
    height: 300px; 
    position: relative;
    border-radius: 10px; /*둥근 모서리*/
  }

  .slide.active {
    display: block;
  }

  .slide-box {
    padding: 20px;
    margin: 10px;
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