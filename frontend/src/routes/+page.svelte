<script lang="ts">
    import Button from "../components/Button.svelte"
    import type { PageData } from './$types';
    import type { BotGame } from "$lib/types";
    import Game from "comps/Game.svelte";

    export let data: PageData;

    let games: Array<BotGame> = data.games;
</script>

<div class="container mx-auto text-center h-screen space-y-10">
    <h1 class="text-3xl font-bold underline text-zinc-200">
        Recent Games
    </h1>

    <div class="w-1/2 mx-auto space-y-2">
        {#if games !== undefined}
            {#each games as game}
                <Game game={game}></Game>
            {/each}
        {/if}
    </div>
</div>