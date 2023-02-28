<script lang="ts">
    import Button from "../components/Button.svelte"
    import Navbar from "../components/Navbar.svelte"
    import type { PageData } from './$types';

    export let data: PageData;

    let games = data.games;
</script>

<Navbar></Navbar>

<div class="container mx-auto text-center h-screen">
    <h1 class="text-3xl font-bold underline">
        Play Durak!
    </h1>

    <div class="result">
        {#each games as game}
            <h5>Game no. {game.pk}</h5>
            <h5>{game.fields.winner}</h5>
            <h5>{game.fields.uuid}</h5>
            <h5>{game.fields.play_date}</h5>
        {/each}
    </div>
</div>