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
        padding: 130px 0 0 0;
    }
</style>