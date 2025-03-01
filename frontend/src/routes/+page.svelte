
<!-- start: this is for testing backend to front end-->
<script> 

    import { goto } from '$app/navigation';

    function navigateToPractice() {
        goto('/practice');
    }   

    import { onMount } from 'svelte';
    let message = 'Loading...';
    let isConnected = false;
    let errorDetails = '';
    
    onMount(async () => {
      try {
        console.log("Attempting to connect to backend at http://localhost:5001/api/hello");
        const response = await fetch('http://localhost:5001/api/hello');
        console.log("Response received:", response.status);
        const data = await response.json();
        console.log("Data received:", data);
        message = data.message;
        isConnected = true;
      } catch (error) {
        message = 'Error connecting to backend';
        errorDetails = error.toString();
        console.error("Connection error:", error);
      }
    });

  </script>
  
  <div class="container">
    <h1>Frontend-Backend Connection Test</h1>
    {#if isConnected}
      <p class="success">✅ Connected to backend successfully!</p>
    {:else}
      <p class="error">❌ {message}</p>
      {#if errorDetails}
        <p class="error-details">Error details: {errorDetails}</p>
      {/if}
    {/if}
    <p>Message from backend: <strong>{message}</strong></p>
  </div>


  <style>
    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 2rem;
    }
    .success {
      color: green;
      font-weight: bold;
    }
    .error {
      color: red;
      font-weight: bold;
    }
    .error-details {
      font-family: monospace;
      background: #ffeeee;
      padding: 10px;
      border-radius: 4px;
      word-break: break-all;
    }
  </style> 

<!-- end: this is for testing backend to front end-->

[]
<button 
  on:click={navigateToPractice}
  class="bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors"
>
  Practice Problems
</button>