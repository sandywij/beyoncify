<script>
	import * as d3 from "d3";

	let svg;
	let width = 500;
	let height = 200;


	function loadData(){
		const data = d3.csv('data.csv').then((d)=>{

			const album = d3.nest()
											.key(function(d) { return d.album; })
											.entries(d);
			return album;
		})

		console.log(data);
		return data;
	}

	let promise = loadData();

	const qualities = ["danceability",
											"energy",
											"valence",
											"speechiness",
											"acousticness",
											"instrumentalness",
											]

	const colors = ["#d53e4f", "#fc8d59",
"#e6f598",
"#99d594",
"#3288bd",
"#756bb1"]

</script>

<style>

	.legend {
		align-items: baseline;
		position: -webkit-sticky; /* Safari */
		position: sticky;
		top: 0;
	}

	.key {
		background-color: #FEE290;
		width:100%;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
		text-align: center;

	}




	.viz-container {
		width:100%;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
		text-align: center;
	}

	line, rect {
		mix-blend-mode: multiply;
	}
</style>

<div class="main-container">
	<div class="legend">
		<p>key:</p>

		<div class="key">
			{#each qualities as q, qi}
			<div id=q>
				<svg width="10" height="10">
					<rect width="10" height="10" fill={colors[qi]}></rect>
				</svg>
				<p>{q}</p>
			</div>
			{/each}
		</div>

	</div>

	<div class="viz-container">
		{#await promise}
			<p>...loading</p>
		{:then data}
		{#each data as d, di}
		<div class="graphs">
		<svg width ="400" height="400">
		{#each d.values as v, i}
		<line x1="200" x2="200" y1="120" y2={120-v.duration_ms/3000} stroke-width="2" stroke="#A0A0A0" transform="rotate({i/d.values.length * 360}  200 200)"></line>
			{#each qualities as q, qi}
			<line x1={200 - v[q]*25} x2={200 + v[q]*25} y1={110-qi/6 * 3 * v.duration_ms/10000} y2={110-qi/6 * 3 * v.duration_ms/10000} stroke-width={v[q]*20} stroke={colors[qi]} transform="rotate({i/d.values.length * 360}  200 200)"></line>
			{/each}
		{/each}

		<defs>
				<clipPath id="img-{di}">
					 	<circle cx="200" cy="200" r="80"></circle>
				</clipPath>
		 </defs>

		 <image width="160" height="160" x="120" y="120" xlink:href="img/{d.values[0].slug}.png" clip-path="url(#img-{di})" />


		</svg>
			<p>{d.key}</p>
		</div>
		{/each}
		{:catch error}
			<p style="color: red">Didn't load :(</p>
		{/await}
	</div>

</div>
