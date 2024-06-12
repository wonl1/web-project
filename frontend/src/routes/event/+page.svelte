<script>
  import { onMount } from 'svelte';
  import { Button } from 'flowbite-svelte';
  import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
  import { faVoteYea } from '@fortawesome/free-solid-svg-icons';
  
  let uploadedImages = []; 
  let selectedImage = null;
  let loading = true;
  let errorMessage = '';
  let votes = {};
  let totalVotes = 0; // 전체 득표 수를 저장합니다.

  const backendImagePath = 'http://127.0.0.1:8017/media/images/';

  async function fetchUploadedImages() {
      try {
          const response = await fetch(`http://127.0.0.1:8017/api/posts/`);
          if (!response.ok) {
              const serverMessage = await response.text();
              throw new Error(`이미지 로드 중 오류가 발생했습니다: ${serverMessage}`);
          }
          uploadedImages = await response.json();

          for (let uploadedImage of uploadedImages) {
              uploadedImage.image = `${backendImagePath}${uploadedImage.image.split('/').pop()}`;

              // 이미지에 대한 투표 수를 저장합니다.
              votes[uploadedImage.id] = uploadedImage.votes;
              totalVotes += uploadedImage.votes; // 전체 득표 수를 계산합니다.
          }

          // 득표 수가 높은 순서대로 이미지를 정렬합니다.
          uploadedImages.sort((a, b) => b.votes - a.votes);

          loading = false;
      } catch (error) {
          console.error(error);
          errorMessage = error.message;
          loading = false;
      }
  }

  onMount(() => {
    fetchUploadedImages();
  });

  function selectImage(image) {
    selectedImage = image;
  }

  async function voteForImage() {
        if (selectedImage) {
            const response = await fetch(`http://127.0.0.1:8017/api/posts/${selectedImage.id}/vote/`, {
                method: 'PUT',
            });
            if (!response.ok) {
                throw new Error('Error voting for image');
            }
            const data = await response.json();
            votes[selectedImage.id] = data.votes;
            totalVotes += 1; // 전체 득표 수를 업데이트합니다.

            // 득표 수가 높은 순서대로 이미지를 다시 정렬합니다.
            uploadedImages.sort((a, b) => votes[b.id] - votes[a.id]);

            // 선택한 이미지를 초기화합니다.
            selectedImage = null;
        }
    }

  function handleKeydown(event, image) {
    if (event.key === 'Enter') {
      selectImage(image);
    }
  }
</script>

{#if loading}
  <p>Loading...</p>
{:else if errorMessage}
  <p>{errorMessage}</p>
{:else}
  <div class="vote-page">
    <h2>VOTE</h2>
    <div class="uploaded-images-gallery">
      {#each uploadedImages as uploadedImage}
        <div class="uploaded-image-details {selectedImage === uploadedImage ? 'selected' : ''}" role="button" tabindex="0" on:click={() => selectImage(uploadedImage)} on:keydown={(event) => handleKeydown(event, uploadedImage)}>
          <img src={uploadedImage.image} alt={uploadedImage.title} class="uploaded-image-size" />
          <h3>{uploadedImage.title}</h3>
          <p>투표 수: {votes[uploadedImage.id] || 0}</p> <!-- 투표 수를 표시합니다 -->
          <p>투표율: {(votes[uploadedImage.id] / totalVotes * 100).toFixed(2) || 0}%</p> <!-- 투표율을 표시합니다 -->
        </div>
      {/each}
    </div>
    {#if selectedImage}
      <div class="selected-image">
        <h3>Selected: {selectedImage.title}</h3>
        <Button on:click={voteForImage} class="font-bold bg-green-600 text-white hover:bg-green-500 mt-4">
          <FontAwesomeIcon icon={faVoteYea} class="w-5 h-5 me-2" /> VOTE
        </Button>
      </div>
    {/if}
  </div>
{/if}

<style>
  .vote-page {
    margin-top: 2rem;
    text-align: center;
  }

  .uploaded-images-gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin-top: 2rem;
  }

  .uploaded-image-details {
    flex: 0 0 auto;
    width: 200px;
    text-align: center; 
    cursor: pointer;
    border: 2px solid transparent;
  }

  .uploaded-image-details.selected {
    border-color: blue;
  }

  .uploaded-image-size {
    width: 100%;
    height: 150px;
    object-fit: cover;
  }

  .selected-image {
    margin-top: 2rem;
  }
</style>