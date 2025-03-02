<script>
    import { onMount } from 'svelte';
  
    // Define all AP classes
    const apClasses = [
        { 
            id: 'calc_ab', 
            name: 'AP Calculus AB',
            units: [
                { id: 'unit1', name: 'Unit 1: Limits and Continuity' },
                { id: 'unit2', name: 'Unit 2: Differentiation: Definition and Fundamental Properties' },
                { id: 'unit3', name: 'Unit 3: Differentiation: Composite, Implicit, and Inverse Functions' },
                { id: 'unit4', name: 'Unit 4: Contextual Applications of Differentiation' },
                { id: 'unit5', name: 'Unit 5: Analytical Applications of Differentiation' },
                { id: 'unit6', name: 'Unit 6: Integration and Accumulation of Change' },
                { id: 'unit7', name: 'Unit 7: Differential Equations' },
                { id: 'unit8', name: 'Unit 8: Applications of Integration' }
            ]
        },
       
        { 
            id: 'us_history', 
            name: 'AP United States History',
            units: [
                { id: 'unit1', name: 'Unit 1: Periods 1-2 (1491-1754)' },
                { id: 'unit2', name: 'Unit 2: Period 3 (1754-1800)' },
                { id: 'unit3', name: 'Unit 3: Period 4 (1800-1848)' },
                { id: 'unit4', name: 'Unit 4: Period 5 (1844-1877)' },
                { id: 'unit5', name: 'Unit 5: Period 6 (1865-1898)' },
                { id: 'unit6', name: 'Unit 6: Period 7 (1890-1945)' },
                { id: 'unit7', name: 'Unit 7: Period 8 (1945-1980)' },
                { id: 'unit8', name: 'Unit 8: Period 9 (1980-Present)' }
            ]
        },
        { 
            id: 'biology', 
            name: 'AP Biology',
            units: [
                { id: 'unit1', name: 'Unit 1: Chemistry of Life' },
                { id: 'unit2', name: 'Unit 2: Cell Structure and Function' },
                { id: 'unit3', name: 'Unit 3: Cellular Energetics' },
                { id: 'unit4', name: 'Unit 4: Cell Communication and Cell Cycle' },
                { id: 'unit5', name: 'Unit 5: Heredity' },
                { id: 'unit6', name: 'Unit 6: Gene Expression and Regulation' },
                { id: 'unit7', name: 'Unit 7: Natural Selection' },
                { id: 'unit8', name: 'Unit 8: Ecology' }
            ]
        },
        { 
            id: 'psychology', 
            name: 'AP Psychology',
            units: [
                { id: 'unit1', name: 'Unit 1: Biological Bases of Behavior' },
                { id: 'unit2', name: 'Unit 2: Cognition' },
                { id: 'unit3', name: 'Unit 3: Development and Learning' },
                { id: 'unit4', name: 'Unit 4: Social Psychology and Personality' },
                { id: 'unit5', name: 'Unit 5: Mental and Physical Health' },
            ]
        },
        { 
            id: 'comp_sci', 
            name: 'AP Computer Science A',
            units: [
                { id: 'unit1', name: 'Unit 1: Primitive Types' },
                { id: 'unit2', name: 'Unit 2: Using Objects' },
                { id: 'unit3', name: 'Unit 3: Boolean Expressions and if Statements' },
                { id: 'unit4', name: 'Unit 4: Iteration' },
                { id: 'unit5', name: 'Unit 5: Writing Classes' },
                { id: 'unit6', name: 'Unit 6: Array' }, 
                { id: 'unit7', name: 'Unit 7: ArrayList' } ,
                { id: 'unit8', name: 'Unit 8: 2D Array' } ,
                { id: 'unit9', name: 'Unit 9: Inheritance' } ,
                { id: 'unit10', name: 'Unit 10: Recursion' },
            ]
        }
    ];
  
    let selectedClass = apClasses[0];
    let selectedUnit = null;
    let units = selectedClass.units;
    let isGenerating = false;
  
    function handleClassChange() {
        // Reset unit selection when class changes
        selectedUnit = null;
        units = selectedClass.units;
    }
  
    async function handleGenerateProblems() {
        const userData = await fetch("http://localhost:5001/api/getClass", {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify([selectedClass.name, selectedUnit.name])
        });
    }
  </script>
  
  <div class="container">
    <h1 class="page-title">AP Exam Practice Problems</h1>
    
    <!-- Dropdown container with pink/purple background -->
    <div class="dropdown-container">
      <!-- Subject dropdown -->
      <div class="dropdown-box">
        <div class="dropdown-header">
          <svg xmlns="http://www.w3.org/2000/svg" class="icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
          </svg>
          <span class="dropdown-title">Subject</span>
        </div>
        <div class="select-wrapper">
          <select
            id="ap-class"
            class="select-input"
            bind:value={selectedClass}
            on:change={handleClassChange}
          >
            <option value={null} disabled>Any subject</option>
            {#each apClasses as apClass}
              <option value={apClass}>{apClass.name}</option>
            {/each}
          </select>
          <div class="select-arrow">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
              <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </div>
        </div>
      </div>
      
      <!-- Units dropdown -->
      <div class="dropdown-box">
        <div class="dropdown-header">
          <svg xmlns="http://www.w3.org/2000/svg" class="icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
          </svg>
          <span class="dropdown-title">Units</span>
        </div>
        <div class="select-wrapper">
          <select
            id="unit"
            class="select-input"
            bind:value={selectedUnit}
          >
            <option value={null} disabled selected>Choose a unit</option>
            {#each units as unit}
              <option value={unit}>{unit.name}</option>
            {/each}
          </select>
          <div class="select-arrow">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
              <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Generate button -->
    <button
      on:click={handleGenerateProblems}
      disabled={!selectedUnit || isGenerating}
      class="generate-button"
    >
      {#if isGenerating}
        Generating...
      {:else}
        Generate Practice Problems
      {/if}
    </button>
    
    <!-- Results section -->
    <div class="results-container">
      <h2 class="results-title">Practice Problems</h2>
      {#if selectedUnit}
        <p class="results-text">Problems for {selectedClass.name}: {selectedUnit.name} will appear here.</p>
      {:else}
        <p class="results-text-empty">Select a unit to generate practice problems.</p>
      {/if}
    </div>
  </div>
  
  <style>
    /* Global styles */
    :global(body) {
      background-color: #f3f4f6;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
      margin: 0;
      padding: 0;
    }
    
    /* Container styles */
    .container {
      max-width: 1000px;
      margin: 0 auto;
      padding: 24px;
    }
    
    /* Page title */
    .page-title {
      font-size: 1.875rem;
      font-weight: 700;
      margin-bottom: 24px;
    }
    
    /* Dropdown container */
    .dropdown-container {
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
      background-color: #0000001a;
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 24px;
    }
    
    @media (min-width: 768px) {
      .dropdown-container {
        grid-template-columns: 1fr 1fr;
      }
    }
    
    /* Dropdown box */
    .dropdown-box {
      background-color: #1f2937;
      border-radius: 8px;
      padding: 24px;
    }
    
    /* Dropdown header */
    .dropdown-header {
      display: flex;
      align-items: center;
      margin-bottom: 16px;
    }
    
    /* Icon */
    .icon {
      width: 24px;
      height: 24px;
      color: white;
      margin-right: 8px;
    }
    
    /* Dropdown title */
    .dropdown-title {
      color: white;
      font-size: 1.25rem;
      font-weight: 600;
    }
    
    /* Select wrapper */
    .select-wrapper {
      position: relative;
    }
    
    /* Select input */
    .select-input {
      width: 100%;
      padding: 12px 16px;
      padding-right: 40px;
      background-color: #374151;
      color: #d1d5db;
      border: none;
      border-radius: 6px;
      appearance: none;
      font-size: 1rem;
    }
    
    .select-input:focus {
      outline: none;
      box-shadow: 0 0 0 2px rgba(78, 108, 200, 0.339);
    }
    
    /* Select arrow */
    .select-arrow {
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      display: flex;
      align-items: center;
      padding-right: 12px;
      pointer-events: none;
    }
    
    .select-arrow svg {
      width: 20px;
      height: 20px;
      color: #9ca3af;
    }
    
    /* Generate button */
    .generate-button {
      width: 100%;
      padding: 12px 16px;
      background-color: #3a41cf;
      color: white;
      font-weight: 600;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      font-size: 1rem;
      margin-bottom: 24px;
      transition: background-color 0.2s;
    }
    
    .generate-button:hover {
      background-color: #121c74;
    }
    
    .generate-button:disabled {
      background-color: #6b76d796;
      cursor: not-allowed;
    }
    
    /* Results container */
    .results-container {
      background-color: white;
      border-radius: 8px;
      padding: 24px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    /* Results title */
    .results-title {
      font-size: 1.25rem;
      font-weight: 600;
      margin-bottom: 16px;
    }
    
    /* Results text */
    .results-text {
      color: #4b5563;
    }
    
    .results-text-empty {
      color: #9ca3af;
      font-style: italic;
    }
  </style>