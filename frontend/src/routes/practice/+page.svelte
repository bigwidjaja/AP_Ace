<script>
    import { onMount } from 'svelte';
    
    // Currently only supporting Calculus AB
    const apClasses = [
      { id: 'calc_ab', name: 'AP Calculus AB' }
    ];
    
    // Units for Calculus AB
    const calcAbUnits = [
      { id: 'unit1', name: 'Unit 1: Limits and Continuity' },
      { id: 'unit2', name: 'Unit 2: Differentiation: Definition and Fundamental Properties' },
      { id: 'unit3', name: 'Unit 3: Differentiation: Composite, Implicit, and Inverse Functions' },
      { id: 'unit4', name: 'Unit 4: Contextual Applications of Differentiation' },
      { id: 'unit5', name: 'Unit 5: Analytical Applications of Differentiation' },
      { id: 'unit6', name: 'Unit 6: Integration and Accumulation of Change' },
      { id: 'unit7', name: 'Unit 7: Differential Equations' },
      { id: 'unit8', name: 'Unit 8: Applications of Integration' }
    ];
    
    let selectedClass = apClasses[0];
    let selectedUnit = null;
    let units = calcAbUnits;
    let isGenerating = false;
    
    function handleGenerateProblems() {
      if (!selectedUnit) return;
      
      isGenerating = true;
      // Here we would eventually call the API to generate problems
      console.log(`Generating problems for ${selectedClass.name}, ${selectedUnit.name}`);
      
      // Simulate API call completion
      setTimeout(() => {
        isGenerating = false;
      }, 1000);
    }
  </script>
  
  <div class="container mx-auto max-w-4xl p-6">
    <h1 class="text-3xl font-bold mb-6">AP Exam Practice Problems</h1>
    
    <div class="bg-white rounded-lg shadow-md p-6 mb-6">
      <div class="mb-4">
        <label for="ap-class" class="block text-sm font-medium text-gray-700 mb-2">Select AP Class</label>
        <select 
          id="ap-class" 
          class="w-full p-2 border border-gray-300 rounded-md" 
          bind:value={selectedClass}
        >
          {#each apClasses as apClass}
            <option value={apClass}>{apClass.name}</option>
          {/each}
        </select>
      </div>
      
      <div class="mb-6">
        <label for="unit" class="block text-sm font-medium text-gray-700 mb-2">Select Unit</label>
        <select 
          id="unit" 
          class="w-full p-2 border border-gray-300 rounded-md" 
          bind:value={selectedUnit}
        >
          <option value={null} disabled selected>Choose a unit</option>
          {#each units as unit}
            <option value={unit}>{unit.name}</option>
          {/each}
        </select>
      </div>
      
      <button 
        on:click={handleGenerateProblems}
        disabled={!selectedUnit || isGenerating}
        class="w-full py-2 px-4 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 disabled:bg-blue-300 disabled:cursor-not-allowed"
      >
        {#if isGenerating}
          Generating...
        {:else}
          Generate Practice Problems
        {/if}
      </button>
    </div>
    
    <div class="bg-white rounded-lg shadow-md p-6">
      <h2 class="text-xl font-semibold mb-4">Practice Problems</h2>
      
      {#if selectedUnit}
        <p class="text-gray-700">Problems for {selectedClass.name}: {selectedUnit.name} will appear here.</p>
      {:else}
        <p class="text-gray-500 italic">Select a unit to generate practice problems.</p>
      {/if}
    </div>
  </div>
  
  <style>
    /* Add any component-specific styles here */
  </style>