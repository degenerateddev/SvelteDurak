<script lang="ts">
    import type { GameCard } from "$lib/types";

    export let suit : string;
    export let value : number | string;
    export let small = false;
    export let field: Array<GameCard> = []; // via bind:field connected to field_cards in 'play' route so field_cards can be updated
</script>

<a class="card-container shadow-lg shadow-black w-fit" on:click>
    <img alt="card" class:card={!small} class:card-small={small} class="card-small rounded" src="/assets/cards/single/{suit.slice(0, -1).toUpperCase()}-{value}.svg" />
</a>

<style>
    .card-container {
        float: left;
        margin-bottom: 20px;
        max-width: 200px;
        margin: 2px;
        transition-duration: 0.2s;
    }

    .card-container:hover {
        transform: scale(1.1);
        transition-duration: 0.2s;
    }

    .card {
        object-fit: contain;
        height: 220px;
    }

    .card-small {
        object-fit: contain;
        height: 150px;
    }
</style>