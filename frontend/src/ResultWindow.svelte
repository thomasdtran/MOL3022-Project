<script>
    import Dialog, { Header, Title, Content, Actions } from '@smui/dialog';
    import IconButton from '@smui/icon-button';
    import {predicted} from './stores';

    export let predictionSegments;

    let open;

    predicted.subscribe(value => {
        open = value;
    })

    function closeHandler(event){
        predicted.update(n => false);
    }

</script>


<Dialog
        bind:open
        fullscreen
        aria-labelledby="fullscreen-title"
        aria-describedby="fullscreen-content"
        on:SMUIDialog:closed={closeHandler}
>
    <Header>
        <Title id="fullscreen-title">Secondary Structure</Title>
        <IconButton action="close" class="material-icons">x</IconButton>
    </Header>
    
    <Content id="fullscreen-content">
        {#each predictionSegments as prediction}

            <div id="resultContainer">
                <p class="resultText">
                    Query:  {prediction.start}  {prediction.query}  {prediction.end}
                </p>
                <p class="resultText">
                    Struc:  {prediction.start}  {@html prediction.struc.join('').toUpperCase().replace(/E/g, '<span style="color:green">E</span>').replace(/C/g, '<span style="color:#e39e19">C</span>').replace(/H/g, '<span style="color:red">H</span>')}  {prediction.end}
                </p>
            </div>
        {/each}
    </Content>
</Dialog>

<style>
    

    #resultContainer{
        margin-bottom: 2em;
    }
    .resultText{
        white-space: nowrap;
        font-size: large;
        font-family: monospace;
    }
</style>