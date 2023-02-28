<script lang="ts">
    import Button from "../components/Button.svelte"
    import Navbar from "../components/Navbar.svelte"
    import type { PageData } from './$types';
    import type { BotGame } from "../lib/types";

    export let data: PageData;

    let games: Array<BotGame> = data.games;
    
    console.log(games)
</script>

<Navbar></Navbar>

<div class="container mx-auto text-center h-screen">
    <h1 class="text-3xl font-bold underline">
        Play Durak!
    </h1>

    <div class="result">
        {#if games !== undefined}
            {#each games as game}
                <h5>Game no. {game.id}</h5>
                <h5>{game.winner}</h5>
                <h5>{game.play_date}</h5>
            {/each}
        {/if}
    </div>
</div>