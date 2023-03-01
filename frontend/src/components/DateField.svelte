<script lang="ts">
    export let date: string;

    let formatted: Array<string> = date.split("#")   
</script>

{formatted[0]} at {formatted[1]}