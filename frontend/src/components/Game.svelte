<script lang="ts">
    import type { BotGame } from "$lib/types";
    import DateField from "./DateField.svelte";

    export let game: BotGame;
</script>

<div class="container text-zinc-200 bg-slate-800 p-5">
    <div class="flex justify-between text-xl">
        <div>
            Game no. {game.id}
        </div>
        <div>
            {game.winner}
        </div>
        <div>
            <DateField date={game.play_date}></DateField>
        </div>
    </div>
</div>