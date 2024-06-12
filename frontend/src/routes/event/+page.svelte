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
  let totalVotes = 0; // 전체 득표 수를 저장

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

              // 이미지에 대한 투표 수를 저장
              votes[uploadedImage.id] = uploadedImage.votes;
              totalVotes += uploadedImage.votes; // 전체 득표 수를 계산
          }

          // 득표 수가 높은 순서대로 이미지를 정렬
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

  async function voteForImage(image) {
    const response = await fetch(`http://127.0.0.1:8017/api/posts/${image.id}/vote/`, {
        method: 'PUT',
    });
    if (!response.ok) {
        throw new Error('Error voting for image');
    }
    const data = await response.json();
    votes[image.id] = data.votes;
    totalVotes += 1; // 전체 득표 수를 업데이트

    // 득표 수가 높은 순서대로 이미지를 다시 정렬
    uploadedImages.sort((a, b) => votes[b.id] - votes[a.id]);

    // 투표 후에 이미지 목록을 다시 불러옴
    await fetchUploadedImages();

    // 총 득표 수를 업데이트
    totalVotes = 0;
    for (let uploadedImage of uploadedImages) {
        totalVotes += votes[uploadedImage.id];
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
        <div class="uploaded-image-details" role="button" tabindex="0" on:click={() => selectImage(uploadedImage)} on:keydown={(event) => handleKeydown(event, uploadedImage)}>
          <img src={uploadedImage.image} alt={uploadedImage.title} class="uploaded-image-size" />
          <h3>{uploadedImage.title}</h3>
          <p>vote: {votes[uploadedImage.id] || 0}</p> 
          <p>voter turnout : {(votes[uploadedImage.id] / totalVotes * 100).toFixed(2) || 0}%</p> 
          <Button on:click={() => voteForImage(uploadedImage)} class="font-bold bg-green-600 text-white hover:bg-green-500 mt-4">
            <FontAwesomeIcon icon={faVoteYea} class="w-5 h-5 me-2" /> VOTE
          </Button>
        </div>
      {/each}
    </div>
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

  .uploaded-image-size {
    width: 100%;
    height: 150px;
    object-fit: cover;
  }

  h2 {
    font-size: 35px;
    font-weight: bold;
  }

  h3 {
    font-size: 20px;
    font-weight: bold;
  }

  .vote-page {
    margin-top: 2rem;
    margin-bottom: 2rem;
    text-align: center;
  }

</style>