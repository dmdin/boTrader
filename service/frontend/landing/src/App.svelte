<script>
    import About from "./sections/About.svelte";

    let about_visible = false;
    let drown = false;
    window.addEventListener("scroll", scroll_flag, false);

    function scroll_flag(e) {
        if (window.pageYOffset > 400) {
            about_visible = true;
        }
    }

    import Hero from './sections/Hero.svelte';
    import Header from "./sections/Header.svelte";
    import {onMount} from "svelte";
    import * as module from 'svelte-particles';

    let ParticlesComponent = module.default;


    onMount(async () => {
        // const module = await import("svelte-particles");
        // ParticlesComponent = module.default;
    });

    let height;
</script>

<svelte:window bind:outerHeight={height}/>
<div class="window">
<main>
	<Header/>
	<Hero/>
</main>
<About visible={about_visible}/>
</div>
<style>
    .window {
        height: 3000px;
        background-color: #000000;
    }
    main {
        height: 100vh;
        text-align: center;
        padding: 1em;
        margin: 0 auto;
        max-width: 1000px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>