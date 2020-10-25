<script>
    import HeroTitle from './svgs/HeroTitle.svelte';
    import Arrow from './svgs/Arrow.svelte';
</script>

<div class="section">
    <HeroTitle/>
    <Arrow/>
</div>

<style>
    .section {
        z-index: 100;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin: 200px 0;
    }
</style>