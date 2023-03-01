<script lang="ts">
  import Anchor from "./Anchor.svelte";
  import Button from "./Button.svelte";
</script>

<div class="container mx-auto bg-slate-900 mb-16">

      <div class="flex items-center border-b-2 border-gray-200 py-2">
        
        <div class="flex justify-start lg:w-0 lg:flex-1">
          <a href="/">
            <img class="object-cover h-24 w-84" src="/icon.png" alt="icon">
          </a>
        </div>

        <div class="hidden md:flex space-x-10">
  
          <Anchor text="Play Durak" to="/play"></Anchor>
          <Anchor text="How to play" to="/howto"></Anchor>

        </div>
        <div class="hidden md:flex items-center justify-end md:flex-1 gap-5">
          <Button title="Sign in"></Button>
          <Button title="Sign up"></Button>
        </div>
      </div>

</div>