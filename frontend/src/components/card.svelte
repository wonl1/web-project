<script>
    import { Card, Button } from 'flowbite-svelte';
    
    let vCard = false;
</script>
  
<div class="flex space-x-4">
    {#each [1, 2, 3, 4] as _}
        <Card reverse={vCard} class="flex-1">
          <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Noteworthy technology acquisitions 2021</h5>
          <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.</p>
          <textarea class="mb-3 p-2 w-full h-20 border rounded-md" placeholder="Enter your text here"></textarea>
          <Button>
            Read more
          </Button>
        </Card>
    {/each}
</div>