<script>
  export let visible = false;
  import {fade} from 'svelte/transition'
</script>
<svelte:head>
  <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
</svelte:head>
<div class="section">
  {#if visible}
    <div in:fade="{{duration:2000}}" class="info_block">
      <h1>О boTrade</h1>
      <div class="content">
        <div class="text_block">
          <p>Проект сфокусирован на полной автоматизации торговли акциями.
            Наша цель - создать бота, который будет самостоятельно адаптироваться к изменяющимся
            условиям на рынке и извлекать максимальную выгоду из сделок</p>
          <p>Предсказание динамики цен происходит благодяря машинному обучению и аугментации
            данных. Такие техники дают максимальную эффективность в принятии решений.
            Все это позволит клиенту без каких-либо усилий преумножать свой капитал.</p>
        </div>
        <lottie-player class="lottie" src="https://assets6.lottiefiles.com/packages/lf20_eKikFJ.json"
                       background="transparent" speed="1" loop autoplay></lottie-player>
      </div>
    </div>
  {/if}
</div>
<style>
  @media all and (max-width: 900px) {
    .content {
      flex-direction: column;
    }

    .lottie {
      order: -1;
      width: 70%;
      height: auto;
      display: flex;
      justify-content: center;
      margin: 20px 0;
    }

    .info_block h1 {
      font-size: 13vw;
    }

    .text_block {
      width: 80%;
      margin: 10px 0 40px 0;
    }

    .info_block p {
      margin: 40px 0 20px 0;
    }
  }

  @media all and (min-width: 900px) {
    .section {
      height: 100vh;
    }

    .lottie {
      flex-basis: 500px;
      flex-shrink: 1;
    }

    .info_block h1 {
      font-size: 92px;
    }

    .text_block {
      width: 600px;
    }

    .info_block p {
      margin: 40px 0 20px 20px;
    }
  }

  .section {
    width: 100%;
  }

  .info_block h1 {
    font-family: Oswald, sans-serif;
    margin: 0;
    text-align: center;
    text-rendering: optimizeLegibility;
    color: #e0dfdc;
    letter-spacing: .1em;
    text-shadow: -1px -1px 1px #999999,
    2px 2px 1px #999999;
  }

  .content {
    width: 100%;
    max-width: 1500px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 0 auto;
  }

  .info_block p {
    font-family: 'Montserrat', sans-serif;
    font-size: 20px;
    color: #e0dfdc;
    padding: 10px 20px;
    border-left: 2px solid #FFFFFF;
    border-right: 2px solid #FFFFFF;
  }
</style>
