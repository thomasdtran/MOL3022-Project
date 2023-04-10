<script>
    import { createEventDispatcher } from "svelte";
    import {predicted} from './stores';

    let proteinSequence = "MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPRVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVHVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALSNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD";
    let predictionSegments = ""

    const dispatch = createEventDispatcher()

    async function sendProteinSequence(){
        
        proteinSequence = proteinSequence.replaceAll('\n', '')

        const res = await fetch('http://127.0.0.1:5000/prediction', {
			method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
			body: JSON.stringify({
                proteinSequence
			})
		})

        const json = await res.json()
        predictionSegments = json

        predicted.update(n => true);
        
        sendPrediction();
    }

    function sendPrediction(){
    
        dispatch('message', {
            content: predictionSegments
        });
    }
</script>

<div id="container">
    <p id="title">Protein sequence</p>
    <textarea rows="8" cols="50" bind:value={proteinSequence}></textarea>
    <button on:click={sendProteinSequence}>Predict</button>
</div>

<style>
    #container{
        display: flex;
        flex-direction: column;
        border: 2px solid #e9e9e9;
        padding: 1em;
        border-radius: 5px;
    }
    #title{
        color: #5d5d5d;
    }
    textarea{
        resize: none;
    }
    button{
        width: 5em;
    }
</style>