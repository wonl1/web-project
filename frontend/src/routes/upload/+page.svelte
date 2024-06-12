<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  let file;
  let fileName = '';
  let title = '';
  let description = '';
  let errorMessage = '';
  let isUploading = false;
  let imagePreview = '';
  let dateTaken = '';

  onMount(() => {
    resetForm();
  });

  function resetForm() {
    file = null;
    fileName = '';
    title = '';
    description = '';
    errorMessage = '';
    imagePreview = '';
    dateTaken = '';
  }

  function handleFileChange(event) {
    file = event.target.files[0];
    if (file) {
      fileName = file.name;
      const reader = new FileReader();
      reader.onload = (e) => {
        imagePreview = e.target.result;
      };
      reader.readAsDataURL(file);
    } else {
      resetForm();
    }
  }

  async function handleUpload() {
    if (!file || !title || !description || !dateTaken) {
      errorMessage = '모든 필드를 채워주세요.';
      return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('title', title);
    formData.append('description', description);
    formData.append('dateTaken', dateTaken);

    try {
      isUploading = true;
      const response = await fetch('http://127.0.0.1:8017/api/upload/', {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        const errorData = await response.json();
        const errorMessages = errorData.map(err => err.msg).join(', ');
        throw new Error(errorMessages);
      }

      const data = await response.json();
      // Return to the previous page after successful upload
      history.back();
    } catch (error) {
      console.error('파일 업로드 중 오류 발생:', error);
      errorMessage = error.message;
    } finally {
      isUploading = false;
    }
  }
</script>

<div class="upload-container">
  <h1 class="text-2xl font-bold mb-4">이미지 업로드</h1>
  <form on:submit|preventDefault={handleUpload}>
    {#if errorMessage}
      <p class="error-message">{errorMessage}</p>
    {/if}

    <div class="file-input-container">
      <label for="file-input" class="file-input-label">이미지 선택</label>
      {#if fileName}
        <span class="file-name">{fileName}</span>
      {/if}
    </div>
    <input id="file-input" type="file" accept="image/*" on:change={handleFileChange} class="file-input" />

    {#if imagePreview}
      <img src={imagePreview} alt="업로드된 이미지 미리보기" class="image-preview" />
    {/if}

    <label for="title-input" class="block mb-2 text-lg font-medium text-gray-700">
      제목
    </label>
    <input id="title-input" type="text" placeholder="제목을 입력하세요" bind:value={title} class="input-field" />
      
    <label for="date-input" class="block mb-2 text-lg font-medium text-gray-700">
      찍은 날짜
    </label>
    <input id="date-input" type="date" bind:value={dateTaken} class="input-field" />

    <label for="description-input" class="block mb-2 text-lg font-medium text-gray-700">
      설명
    </label>
    <textarea id="description-input" placeholder="설명을 입력하세요" bind:value={description} class="input-field" rows="4"></textarea>

    <button type="submit" class="font-bold bg-darkblue-600 text-lightyellow-100 hover:text-lightyellow-50 hover:bg-darkblue-500 px-4 py-2 rounded" disabled={isUploading}>
      {#if isUploading}
        <div class="loading-spinner"></div>
      {:else}
        업로드
      {/if}
    </button>
  </form>
</div>

<style>
  .upload-container {
    max-width: 1400px;
    margin: 30px 0;
    padding: 30px;
    border: 5px solid #1A2039;
    border-radius: 10px;
    background-color: #fffffb;
  }
  .input-field {
    display: block;
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .error-message {
    color: red;
    margin-bottom: 15px;
  }
  .loading-spinner {
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-left-color: #4A90E2;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    animation: spin 1s linear infinite;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
  .image-preview {
    max-width: 100%;
    max-height: 400px;
    margin-bottom: 15px;
    border-radius: 10px;
  }
  .file-input-container {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
  }
  .file-input-label {
    display: inline-block;
    font-weight: bold;
    background-color: #121832;
    color: #FFFFE0;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
  }
  .file-input-label:hover {
    background-color: #1A2039;
    color: #FFFFF3;
  }
  .file-input-label:disabled {
    background-color: #4A90E2;
    cursor: not-allowed;
  }
  .file-input {
    display: none;
  }
  .file-name {
    margin-left: 10px;
    font-size: 1rem;
    color: gray;
  }
</style>
