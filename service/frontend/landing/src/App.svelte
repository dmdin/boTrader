<link href="https://fonts.googleapis.com/css2?family=Montserrat@1&display=swap" rel="stylesheet">
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


    onMount(async () => {

    });


</script>


<main>
	<Header/>
	<Hero/>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>

<style>

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