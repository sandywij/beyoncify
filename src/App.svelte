<script>
	import * as d3 from "d3";
	import Graph from './Graph.svelte';

	let spotifyUri = "5IVuqXILoxVWvWEPm82Jxr";
	let svg;
	let width = 500;
	let height = 200;
	let playing = "Crazy in Love";

	function loadData(){
		const data = d3.csv('data.csv').then((d)=>{

			const album = d3.nest()
											.key(function(d) { return d.album; })
											.entries(d);
			return album;
		})
		return data;
	}

	let promise = loadData();

	const qualities = [
	{ id: 'danceability',   color: "#d53e4f"   },
	{ id: 'energy', color: "#fc8d59" },
	{ id: 'valence',  color: "#e6f598"  },
	{ id: 'speechiness',   color: "#99d594"   },
	{ id: 'acousticness', color: "#3288bd" },
	{ id: 'instrumentalness',  color: "#756bb1" }
];


</script>

<style>

	.legend {
		width: 100%;
		background-color: #FEE290;
		position: -webkit-sticky; /* Safari */
		position: sticky;
		top: 0;
		display: flex;
		align-items: baseline;
		justify-content: space-around;
		font-size: 0.8em;
	}

	.key {
		width:80%;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
		text-align: center;
	}

	.sub-key{
		display: inline-flex;
		align-items: baseline;
		flex-wrap: nowrap;
	}

	.sub-key > *{
		padding-left: 1em;
	}

	rect {
		mix-blend-mode: multiply;
	}

	.viz-container {
		width:100%;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
		text-align: center;
	}

	#music-player {
		position:fixed;
				 left:0px;
				 bottom:0px;
				 height: auto;
				 width: auto;
	}

	#music-player p{
		font-size: 0.8em;
	}


</style>

<div class="main-container">
	<div class="legend">
		<div>
			<h1>B</h1>
		</div>
		<div>
			<p>Key:</p>
		</div>


		<div class="key">
			{#each qualities as q}
			<div class="sub-key" id=q>
				<svg width="10" height="10">
					<rect width="10" height="10" fill={q.color}></rect>
				</svg>
				<p>{q.id}</p>
			</div>
			{/each}
		</div>
	</div>

	<div class="viz-container">
		{#await promise}
			<p>...loading</p>
		{:then data}
		{#each data as d}
		<Graph data={d} qualities={qualities} bind:spotifyUri bind:playing/>
		{/each}
		{:catch error}
			<p style="color: red">Didn't load :(</p>
		{/await}
	</div>


	<div id="music-player">

	<iframe src="https://open.spotify.com/embed/track/{spotifyUri}" width="80" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
		<p>Track: {playing}</p>
	</div>
</div>
