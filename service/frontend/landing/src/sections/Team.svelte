<script>
  export let visible = false;
  import {fade} from 'svelte/transition'
</script>
<svelte:head>
  <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
</svelte:head>
<div class="section">
  {#if visible}
    <div in:fade="{{duration:2000}}">
      <h1>Команда</h1>
      <div class="content">
        <lottie-player class="lottie" src="person1.json" background="transparent" speed="1" loop autoplay/>
        <p>Наша команда </p>
      </div>
    </div>
  {/if}
</div>
<style>
  @media all and (max-width: 900px) {
    .content {
      flex-direction: column;
      width: 80%;
      margin: 0 auto;
    }

    .lottie {
      order: -1;
      width: 90%;
      height: auto;
      display: flex;
      justify-content: center;
      margin: 20px 0;
    }

    h1 {
      font-size: 13vw;
    }

    .content p {
      margin: 40px 0 20px 0;
    }
  }

  @media all and (min-width: 900px) {
    .section {
      height: 100vh;
    }

    .content {
      width: 100%;
    }

    .lottie {
      width: 500px;
    }

    h1 {
      font-size: 92px;
    }

    .content p {
      margin: 40px 40px 20px 10px;
    }
  }

  .section {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  h1 {
    font-family: Oswald, sans-serif;
    margin: 0;
    text-align: center;
    text-rendering: optimizeLegibility;
    color: #e0dfdc;
    letter-spacing: 0.1em;
    text-shadow: -1px -1px 1px #999999,
    2px 2px 1px #999999;
  }

  .content {
    height: calc(100% - 92px);
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

  .content p {
    font-family: 'Montserrat', sans-serif;
    font-size: 20px;
    color: #e0dfdc;
    padding: 10px 20px;
    border-left: 2px solid #FFFFFF;
    border-right: 2px solid #FFFFFF;
    max-width: 600px;
  }
</style>