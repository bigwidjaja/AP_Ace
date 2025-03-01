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
          id: 'eng_lang', 
          name: 'AP English Language and Composition',
          units: [
              { id: 'unit1', name: 'Unit 1: Rhetorical Analysis' },
              { id: 'unit2', name: 'Unit 2: Argument Writing' },
              { id: 'unit3', name: 'Unit 3: Synthesis Writing' },
              { id: 'unit4', name: 'Unit 4: Research and Source Analysis' },
              { id: 'unit5', name: 'Unit 5: Style and Tone in Writing' },
              { id: 'unit6', name: 'Unit 6: Critical Reading Strategies' }
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
              { id: 'unit1', name: 'Unit 1: Scientific Foundations of Psychology' },
              { id: 'unit2', name: 'Unit 2: Biological Bases of Behavior' },
              { id: 'unit3', name: 'Unit 3: Sensation and Perception' },
              { id: 'unit4', name: 'Unit 4: Learning' },
              { id: 'unit5', name: 'Unit 5: Cognitive Psychology' },
              { id: 'unit6', name: 'Unit 6: Developmental Psychology' },
              { id: 'unit7', name: 'Unit 7: Motivation, Emotion, and Personality' },
              { id: 'unit8', name: 'Unit 8: Clinical Psychology' }
          ]
      },
      { 
          id: 'comp_sci', 
          name: 'AP Computer Science Principles',
          units: [
              { id: 'unit1', name: 'Unit 1: Digital Information' },
              { id: 'unit2', name: 'Unit 2: The Internet' },
              { id: 'unit3', name: 'Unit 3: Algorithms and Programming' },
              { id: 'unit4', name: 'Unit 4: Data and Information' },
              { id: 'unit5', name: 'Unit 5: Working with Data' },
              { id: 'unit6', name: 'Unit 6: The Impact of Computing' }
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
              on:change={handleClassChange}
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