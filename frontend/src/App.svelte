<script>
	import Input from "./Input.svelte"
	import ResultWindow from "./ResultWindow.svelte";
	import Footer from "./Footer.svelte";

	let predictionSegments = "";

	function handleMessage(event){
		predictionSegments = event.detail.content;
	}

</script>

<div id="container">
	<h1>Secondary Structure Prediction 🧬</h1>
	<p>Insert a protein sequence below, and get the predicted secondary structures.</p>
	<Input on:message={handleMessage}/>
	<p id="message">☝️ Enter protein sequence!</p>
	<ResultWindow {predictionSegments}/>
	<Footer/>
</div>

<style>
	#container{
		display: flex;
		flex-direction: column;
		flex-wrap: nowrap;
		margin: auto;
		width: 50%;
		margin-top: 3em;
	}
	#message{
        background-color: #FFE3121A;
        color: #926C05;
        width: 25em;
        padding: 1em;
        margin: auto;
        margin-top: 2em;
    }
</style>



