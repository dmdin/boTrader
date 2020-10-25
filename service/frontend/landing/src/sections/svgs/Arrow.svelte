<script>
 import {draw} from 'svelte/transition';
 import {cubicOut} from 'svelte/easing';
 import {onMount} from 'svelte';

  let loaded = false;
 onMount(async () => {
        setTimeout(() => loaded = true, 4400)

    });

</script>
<div class="arrow">
<svg width="640" height="200" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">
 <g class="layer">
  {#if loaded}
<path in:draw d="m1.099987,2.500007c254.097696,9.867485 586.88371,13.567792 586.719776,12.951074c-0.163934,-0.616718 -524.424857,4.317025 -524.588791,3.700307c-0.163934,-0.616718 573.932924,16.651381 573.76899,16.034663c-0.163934,-0.616718 -632.621295,6.783896 -632.785229,6.167178c-0.163934,-0.616718 490.326586,10.484203 490.162652,9.867485c-0.163934,-0.616718 -245.737062,15.417946 -245.900996,14.801228c-0.163934,-0.616718 191.966711,12.951074 191.802777,12.334357c-0.163934,-0.616718 -103.114484,120.259976 -103.278418,119.643258c-0.163934,-0.616718 -1.475406,-0.616718 8.1967,-48.10399" fill="none" id="svg_18" stroke="#FFFFFF" stroke-dasharray="null" stroke-linecap="round" stroke-linejoin="round"/>
   {/if}
  </g>
</svg>
</div>
<style>
    @media all and (max-width: 900px) {
        .arrow {
            display: none;
        }
    }
 .arrow {
  margin: 50px auto;
 }
</style>