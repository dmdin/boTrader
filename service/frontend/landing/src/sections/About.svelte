<script>
    export let visible = false;

    function typewriter(node, { speed = 30 }) {
		const valid = (
			node.childNodes.length === 1 &&
			node.childNodes[0].nodeType === Node.TEXT_NODE
		);

		if (!valid) {
			throw new Error(`This transition only works on elements with a single text node child`);
		}

		const text = node.textContent;
		const duration = text.length * speed;

		return {
			duration,
			tick: t => {
				const i = ~~(text.length * t);
				node.textContent = text.slice(0, i);
			}
		};
	}
</script>
<div class="section">
    <div class="info_block">
        {#if visible}
        <p in:typewriter>Предсказание курса акций происходит с помощью технологии машинного обучения,
            что обеспечивает максимальную точность прогноза. Модель постоянно учится на актульных данных,
            поэтому и стратегия бота будет изменяться, основываясь на последней информации.
            Все это позволит пользователю без каких бы то ни было усилий преумножать свой капитал.</p>
            {/if}
    </div>
</div>
<style>
    .section {
        width: 100%;
    }
    .info_block {
    }
</style>
