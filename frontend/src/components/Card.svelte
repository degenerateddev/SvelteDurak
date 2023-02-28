<script lang="ts">
    export let suit;
    export let value;
    export let small = false;
    export let field = []; // via bind:field connected to field_cards in 'play' route so field_cards can be updated
</script>

{#if small}
    <a class="card-container" on:click>
        <img class="card-small rounded" src="/assets/cards/single/{suit.slice(0, -1).toUpperCase()}-{value}.svg" />
    </a>
{:else}
    <a class="card-container" on:click>
        <img class="card rounded" src="/assets/cards/single/{suit.slice(0, -1).toUpperCase()}-{value}.svg" />
    </a>
{/if}

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