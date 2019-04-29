<script>
  import * as d3 from "d3";

  export let spotifyUri;
  export let playing;
  export let data;
  export let qualities;

  const r = 80;

  const width = 360;
  const height = 360;
  const midPoint = {x: width/2, y:height/2};
  const circleEdge = width/2 - r;

  $: albumData = data.values;


  function tooltip(node, text) {
		const tooltip = document.createElement('div');
		tooltip.textContent = text;

		Object.assign(tooltip.style, {
			position: 'absolute',
			background: 'black',
			color: 'white',
			padding: '0.5em 1em',
			fontSize: '12px',
			pointerEvents: 'none',
			transform: 'translate(5px, -50%)',
			borderRadius: '2px',
			transition: 'opacity 0.4s'
		});


		function append(event) {
			document.body.appendChild(tooltip);
			tooltip.style.opacity = 0;
			setTimeout(() => tooltip.style.opacity = 1);
      tooltip.style.top = `${event.pageY}px`;
      tooltip.style.left = `${event.pageX}px`;
		}

		function remove() {
			tooltip.remove();
		}

		node.addEventListener('mouseenter', append);
		node.addEventListener('mouseleave', remove);

		return {
			update(text) {
				tooltip.textContent = text;
				position();
			},

			destroy() {
				tooltip.remove();
				node.removeEventListener('mouseenter', append);
				node.removeEventListener('mouseleave', remove);
			}
		};
	}





</script>

<style>
  line {
    mix-blend-mode: multiply;
  }


</style>

<div class="graphs">
  <p>{data.key}</p>

<svg width ={width} height={height}>

{#each albumData as d, di}
<g on:click={()=>{spotifyUri = d.id; playing = d.songtitle;}} use:tooltip={d.songtitle} >
  <line x1={midPoint.x} x2={midPoint.x} y1={circleEdge} y2={circleEdge-d.duration_ms/3000} stroke-width="2" stroke="#A0A0A0" transform="rotate({di/albumData.length * 360} {midPoint.x} {midPoint.y})"></line>
  {#each qualities as q, qi}
  <line x1={midPoint.x - d[q.id]*25} x2={midPoint.x + d[q.id]*25} y1={0.9*circleEdge -qi/6 * 3 * d.duration_ms/10000} y2={0.9*circleEdge -qi/6 * 3 * d.duration_ms/10000} stroke-width={d[q.id]*20} stroke={q.color} transform="rotate({di/albumData.length * 360} {midPoint.x} {midPoint.y})"></line>
  {/each}
  </g>
{/each}

<defs>
    <clipPath id="img-{data.values[0].id}">
        <circle cx={midPoint.x} cy={midPoint.y} r={r}></circle>
    </clipPath>
 </defs>

 <image width={r*2} height={r*2} x={midPoint.x-r} y={midPoint.y-r} xlink:href="img/{data.values[0].slug}.png" clip-path="url(#img-{data.values[0].id}" />


</svg>
</div>
