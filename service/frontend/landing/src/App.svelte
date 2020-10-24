<script>
    import Hero from './sections/Hero.svelte';
    import {onMount} from "svelte";
    import * as module from 'svelte-particles';
    let ParticlesComponent = module.default;


    onMount(async () => {
        // const module = await import("svelte-particles");
        // ParticlesComponent = module.default;
    });

    let particlesConfig = {
        particles: {
            number: {
              value: 30,
              density: {
                  enable: true,
                  value_area: 200
              }
            },
            color: {
                value: "#939393",
            },
            links: {
                enable: true,
                color: "#CCCCCC",
            },
            move: {
                enable: true,
            },
        },
    };

    let onParticlesLoaded = (event) => {
        const particlesContainer = event.detail.particles;

        // you can use particlesContainer to call all the Container class
        // (from the core library) methods like play, pause, refresh, start, stop
    };
    let height;
</script>

<svelte:window bind:outerHeight={height}/>
<svelte:component
    this="{ParticlesComponent}"
    id="tsparticles"
    options="{particlesConfig}"
    height="1000px"
    on:particlesLoaded="{onParticlesLoaded}"
/>

<main>
    <Hero/>


</main>

<style>
    #tsparticles {
        height: 100vh;
    }
    main {
        text-align: center;
        padding: 1em;
        margin: 0 auto;
        max-width: 1000px;
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