<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  function goToPrac() {
      goto('/practice');
  }
</script>

<body>
  <div style="background-image: url('/gradient.jpg')" class='bg-no-repeat w-screen min-h-screen bg-cover'>
    <div style='font-family: "Instrument Serif"; display: flex; justify-content: space-between;'>
      <p class='white-text' style='font-size: 2.5em; margin: 0.5em 0.75em;'>
        AP<span class='italic'> ace</span>
      </p>

      <button class='italic' style='font-size: 1.5em; margin: 0.75em 1.25em; padding: 0em 1.5em; border-radius: 2em; background-color: transparent; color: white; font-family: "Instrument Serif"; border: 2px solid white;' on:click = {goToPrac}>
        Get Started
      </button>
    </div>

    <div style='margin: 10svh 12.5em; font-family: "Instrument Serif"; display: flex; justify-content: space-between;'>
      <p class='white-text' style='font-size: 5em; margin: 0em 0.75em; line-height: 1.1em;'>
        Elevate your<br>
        Study Sessions,<br>
        and Score 5s<br>
        on AP Exams
      </p>

      <ul style='background-color: black; border: 2px white solid; border-radius: 0.5em; color: white; padding: 1em 2em; font-size: 1.75em; font-family: "Figtree"; inline-size: min-content; width: 12em; margin: -1em 1em 0 0;'> 
        <li>Create Practice AP Exam Problems tailored for you.</li>
        <li>Pick Between Essential STEM & Humanities courses.</li>
        <li style='padding-bottom: 0.25em;'>Our AI will Generate AP-Based Questions with answer choices and solutions!</li>
      </ul>
    </div>
  </div>
</body>

<style global>
  * {
    margin: 0px;
  }

  body {
    background-color: black;
    margin: 0px;
    padding: 0px;
  }

  li {
    padding-bottom: 1.5em;
  }

  .white-text {
    color: white;
  }


</style>