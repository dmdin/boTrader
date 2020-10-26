 <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;1,300&display=swap" rel="stylesheet">
 <script>
  let about_visible = false;
  let team_visible = false;
  let drown = false;
  window.addEventListener("scroll", scroll_flag, false);

  function scroll_flag(e) {
    if (window.pageYOffset > 300) {
      about_visible = true;
    }
    if (window.pageYOffset > 700) {
      team_visible = true;
    }
  }

  import Hero from './sections/Hero.svelte';
  import Header from "./sections/Header.svelte";
  import About from "./sections/About.svelte";
  import Team from "./sections/Team.svelte";
  import {onMount} from "svelte";


  onMount(async () => {

  });

  let height;
</script>

<svelte:window bind:outerHeight={height}/>
<body>
  <main>
    <Header/>
    <Hero/>
    <About visible={about_visible}/>

  </main>
<!--  <Team visible={team_visible}/>-->
</body>
<style>
  :root {
    background: black;
  }
  @media all and (min-width: 900px) {
    main {
      /*height: calc(100vh - 60px);*/
      padding: 60px 0 0 0;
    }
  }

  body {
    background-color: #000000;
  }

  main {
    /*height: calc(100vh - 60px);*/
    text-align: center;
    margin: 0 auto;
    max-width: 1000px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

</style>