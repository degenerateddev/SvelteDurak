<script>
    import "../app.css";
    import Navbar from "comps/Navbar.svelte"
    import Footer from "comps/Footer.svelte";

</script>

<div class="min-h-screen">
    <Navbar />

    <slot />

    <Footer />
</div>