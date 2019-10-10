<script>
  import * as d3 from "d3";
  import Graph from "./Graph.svelte";

  let spotifyUri = "5IVuqXILoxVWvWEPm82Jxr";
  let svg;
  let width = 500;
  let height = 200;
  let playing = "Crazy in Love";

  function loadData() {
    const data = d3.csv("data.csv").then(d => {
      const album = d3
        .nest()
        .key(function(d) {
          return d.album;
        })
        .entries(d);
      return album;
    });
    return data;
  }

  let promise = loadData();

  const qualities = [
    { id: "danceability", color: "#d53e4f" },
    { id: "energy", color: "#fc8d59" },
    { id: "valence", color: "#e6f598" },
    { id: "speechiness", color: "#99d594" },
    { id: "acousticness", color: "#3288bd" },
    { id: "instrumentalness", color: "#756bb1" }
  ];
</script>

<style>
  .center {
	  width: 100%;
	  max-width: 600px;
	  margin: auto;
    text-align: center;
    padding: 1em 0em;
  }

  .analysis {
	font-family: "Open Sans", Arial, Helvetica, sans-serif;
	max-width: 600px;
	width: 100%;
	margin: auto;
	line-height: 2em;
  }

  .legend {
    width: 100%;
    background-color: #fee290;
    position: -webkit-sticky; /* Safari */
    position: sticky;
    top: 0;
    display: flex;
    align-items: center;
    justify-content: space-around;
	font-size: 0.8em;
	height: 100px;
  }

  .key {
    width: 80%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    text-align: center;
  }

  .sub-key {
    display: inline-flex;
    align-items: baseline;
    flex-wrap: nowrap;
  }

  .sub-key > * {
    padding-left: 1em;
  }

  @media screen and (min-width: 600px) {
    rect {
      mix-blend-mode: multiply;
    }
  }

  @media screen and (max-width: 600px) {
    rect {
      opacity: 0.9;
    }
  }

  .viz-container {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    text-align: center;
    margin-bottom: 100px;
  }

  #music-player {
    position: fixed;
    left: 0px;
    bottom: 0px;
    height: auto;
    width: auto;
  }

  #music-player p {
    font-size: 0.8em;
  }
</style>

<div class="main-container">



  <div class="center">
        
    <h1>Beyoncify</h1>
  <a style="font-size:12px; font-family:'Open Sans';" href="https://www.sandywij.com/">Sandy Guberti Ng</a>
      </div>

  <div class="center">

    <p>Patiently waiting for my demise</p>

    <p>'Cause my success can't be quantified</p>

    <p>If I gave two fucks, two fucks about streaming numbers</p>

    <p>Would have put Lemonade up on Spotify</p>
  </div>

<div class="analysis">
    <p>
      Since Lemonade’s release on April 23 2016, it had been exclusively
      available on Tidal. Three years after its release, it is now finally
      available on other streaming platforms — including Spotify.
	  </p>

	  <p>
	   For every
      track in Spotify’s catalog, runs a suite of audio analysis algorithms.
      These extract about a dozen high-level acoustic attributes from the audio.
	  </p>

	  <p>
	  In this visualization shows seven attributes that were available on Spotify’s API: Duration,
      Danceability, Energy, Valence, Speechiness, Acousticness,
      Instrumentalness. With the exception of Duration, all the attributes are
      measures from 0.0 to 1.0.
    </p>
  </div>

  
  <div class="legend">

    <div>
      <p>Key:</p>
    </div>

    <div class="key">
      {#each qualities as q}
        <div class="sub-key" id="q">
          <svg width="10" height="10">
            <rect width="10" height="10" fill={q.color} />
          </svg>
          <p>{q.id}</p>
        </div>
      {/each}
    </div>
  </div>

<div>

<div class="center">    <p><strong>Click to play track.</strong></p>
</div>

  <div class="viz-container">
    {#await promise}
      <p>...loading</p>
    {:then data}
      {#each data as d}
        <Graph data={d} {qualities} bind:spotifyUri bind:playing />
      {/each}
    {:catch error}
      <p style="color: red">Didn't load :(</p>
    {/await}
  </div>
</div>
  <div id="music-player">

    <iframe
      src="https://open.spotify.com/embed/track/{spotifyUri}"
      width="80"
      height="80"
      frameborder="0"
      allowtransparency="true"
      allow="encrypted-media" />
    <p>Track: {playing}</p>
  </div>
</div>

