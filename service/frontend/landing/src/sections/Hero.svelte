<script>
  import HeroTitle from './svgs/HeroTitle.svelte';
  import Arrow from './svgs/Arrow.svelte';
</script>

<div class="section">
  <HeroTitle/>
  <Arrow/>
</div>

<style>
  @media all and (min-width: 900px) {
    .section {
      padding: 130px 0 0 0;
    }
  }

  .section {
    z-index: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 80vh;
  }
</style>