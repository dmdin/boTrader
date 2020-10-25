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
		<p>Цель нашего сервиса - полная автоматизация трейдинга пользователя.
		Разработанный бот, используя выделенный капитал, будет самостоятельно вкладывать его в акции,
		сулящие наибольший доход</p>
        <p>Предсказание курса акций происходит с помощью технологии машинного обучения,
            что обеспечивает максимальную точность прогноза. Модель постоянно учится на актульных данных,
            поэтому и стратегия бота будет изменяться, основываясь на последней информации.
            Все это позволит пользователю без каких бы то ни было усилий преумножать свой капитал.</p>
			</div>
		<lottie-player class="lottie" src="https://assets6.lottiefiles.com/packages/lf20_eKikFJ.json"  background="transparent"  speed="1" loop  autoplay></lottie-player>
		</div>
    </div>
		{/if}
</div>
<style>
    .section {
        width: 100%;
    }
	.info_block {
	}
    .info_block h1 {
		font-family: Oswald, sans-serif;
		font-size: 92px;
		margin:0;
  text-align: center;
  text-rendering: optimizeLegibility;
		color: #e0dfdc;
    letter-spacing: .1em;
    text-shadow:
      -1px -1px 1px #999999,
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
	.text_block {
		width: 600px;
	}
	.info_block p {
		font-family: 'Montserrat', sans-serif;
		font-size: 20px;
		color: #e0dfdc;
		margin: 40px 0 20px 20px;
		padding: 10px 20px;
		border-left: 2px solid #FFFFFF;
		border-right: 2px solid #FFFFFF;
	}
	.lottie {
		width: 500px;
	}
</style>
