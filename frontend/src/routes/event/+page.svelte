<script>
	import { onMount } from 'svelte';
	import { tweened } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';
  
	// Utility function to get a random integer
	function getRandomInt(min, max) {
	  min = Math.ceil(min);
	  max = Math.floor(max);
	  return Math.floor(Math.random() * (max - min + 1)) + min;
	}
  
	let prizes = ["Prize 1", "Prize 2", "Prize 3", "Prize 4", "Prize 5", "Prize 6"];
	let angle = tweened(0, { duration: 4000, easing: cubicOut });
	let spinning = false;
	let selectedPrize = null;
  
	function spin() {
	  if (spinning) return;
  
	  spinning = true;
	  selectedPrize = null;
	  let randomAngle = getRandomInt(1440, 2160); // Random angle between 4 to 6 full rotations
	  angle.set(randomAngle).then(() => {
		spinning = false;
		let finalAngle = randomAngle % 360;
		let prizeIndex = Math.floor(finalAngle / (360 / prizes.length));
		selectedPrize = prizes[prizeIndex];
	  });
	}
  
	onMount(() => {
	  angle.subscribe(value => {
		document.querySelector(".wheel").style.transform = `rotate(${value}deg)`;
	  });
	});
  </script>
  
  <style>
	.wheel-container {
	  display: flex;
	  flex-direction: column;
	  align-items: center;
	}
	.wheel {
	  width: 300px;
	  height: 300px;
	  border: 5px solid #333;
	  border-radius: 50%;
	  position: relative;
	  overflow: hidden;
	  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	}
	.wheel::before {
	  content: "";
	  position: absolute;
	  top: 50%;
	  left: 50%;
	  width: 0;
	  height: 0;
	  border-left: 10px solid transparent;
	  border-right: 10px solid transparent;
	  border-bottom: 20px solid #333;
	  transform: translate(-50%, -100%);
	  z-index: 10;
	}
	.segment {
	  position: absolute;
	  width: 50%;
	  height: 50%;
	  background-color: #fff;
	  transform-origin: 100% 100%;
	  border-top-right-radius: 100%;
	  border: 1px solid #333;
	  clip-path: polygon(0% 0%, 100% 0%, 100% 100%);
	}
	.prize {
	  position: absolute;
	  width: 100%;
	  text-align: center;
	  top: 50%;
	  left: 50%;
	  transform: translate(-50%, -50%) rotate(90deg);
	  font-size: 1rem;
	  color: #333;
	}
	.pointer {
	  width: 0;
	  height: 0;
	  border-left: 20px solid transparent;
	  border-right: 20px solid transparent;
	  border-bottom: 40px solid red;
	  position: absolute;
	  top: -50px;
	}
	.spin-button {
	  margin-top: 20px;
	  padding: 10px 20px;
	  font-size: 1rem;
	  cursor: pointer;
	}
	.spin-button:disabled {
	  cursor: not-allowed;
	}
  </style>
  
  <div class="wheel-container">
	<div class="pointer"></div>
	<div class="wheel">
	  {#each prizes as prize, index}
		<div class="segment" style="transform: rotate({index * (360 / prizes.length)}deg)">
		  <div class="prize" style="transform: rotate({index * -(360 / prizes.length)}deg)">
			{prize}
		  </div>
		</div>
	  {/each}
	</div>
	<button class="spin-button" on:click={spin} disabled={spinning}>
	  {#if spinning}
		Spinning...
	  {:else}
		Spin
	  {/if}
	</button>
	{#if selectedPrize}
	  <h2>Congratulations! You won {selectedPrize}!</h2>
	{/if}
  </div>
  