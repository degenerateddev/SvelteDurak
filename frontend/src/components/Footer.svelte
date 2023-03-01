<script lang="ts">
    import Anchor from "./Anchor.svelte";
</script>

<div class="container mx-auto border-t-2 py-10">
    <div class="flex justify-center">
        <ul class="text-center space-y-2">
            <li>
                <Anchor text="Legal Disclosure" to="/legal"></Anchor>
            </li>
            <li>
                <Anchor text="Privacy Policy" to="/privacy"></Anchor>
            </li>
            <li>
                <Anchor text="Contact" to="/contact"></Anchor>
            </li>
        </ul>
    </div>
</div>