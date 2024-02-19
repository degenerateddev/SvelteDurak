<script lang="ts">
    import type { PageData } from './$types';
    import type { BotGame } from "$lib/types";
    import DateField from "comps/DateField.svelte";

    export let data: PageData;

    let games: Array<BotGame> = data.games;
</script>

<div class="container mx-auto text-center h-screen space-y-10">
    <h1 class="text-3xl font-bold underline text-zinc-200">
        Recent Games
    </h1>

    <table class="container mx-auto max-w-5xl table-auto text-zinc-200 rounded-md">
        <thead>
            <tr>
                <th>Game no.</th>
                <th>Winner</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody>
            {#if games !== undefined}
                {#each games as game, index}
                    {#if index % 2 == 0}
                        <tr class="bg-slate-800">
                            <td>
                                {game.id}
                            </td>
                            <td>
                                {game.winner}
                            </td>
                            <td>
                                <DateField date={game.play_date}></DateField>
                            </td>
                        </tr>
                    {:else}
                        <tr class="bg-slate-700">
                            <td>
                                {game.id}
                            </td>
                            <td>
                                {game.winner}
                            </td>
                            <td>
                                <DateField date={game.play_date}></DateField>
                            </td>
                        </tr>
                    {/if}
                {/each}
            {/if}
        </tbody>
    </table>
</div>