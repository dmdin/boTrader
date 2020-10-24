<script>
	export let name;
	let drown = false;
	window.addEventListener("scroll", scroll_flag, false);

	function scroll_flag(e) {
		if (window.pageYOffset > 700) {
			drown = true;
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
            shape: {
                image: {
                    width: 100,
                    height: 300
                }
            }
        },
    };

    let onParticlesLoaded = (event) => {
        const particlesContainer = event.detail.particles;
        document.getElementById('tsparticles').style.position = "fixed";
        document.getElementById('tsparticles').style.height = 100 +"%";
        document.getElementById('tsparticles').style.width = 100 +"%";
        document.getElementById('tsparticles').style.zIndex= "0";
        document.getElementById('tsparticles').style.marginTop= 60 + "px";
        // you can use particlesContainer to call all the Container class
        // (from the core library) methods like play, pause, refresh, start, stop
    };
    let height;
</script>

<svelte:window bind:outerHeight={height}/>
<svelte:component
    this={ParticlesComponent}
    id="tsparticles"
    options={particlesConfig}
    height = "200px"
    on:particlesLoaded={onParticlesLoaded}
/>

<main>
	<Header/>
	<Hero/>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>

<style>
    #tsparticles {
        height: 100px;
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