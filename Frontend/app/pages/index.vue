<script setup lang="ts">
definePageMeta({
  layout: "default",
});

// to controll the form tabs here
let tabCounter: number = ref(0);

// changing the tab counter
const handleToogleCounter = (index: number) => {
  tabCounter.value = index;
  console.log(tabCounter.value);
};
</script>

<template>
  <section class="grid grid-cols-1 md:grid md:grid-cols-1 lg:grid lg:grid-cols-2 gap-5 place-content-center">
    <!-- for the side landing page -->
    <div>
      <div class="hidden lg:block bg-gray-100 h-screen"></div>
    </div>

    <!-- for the main login form here -->
    <div class="px-10 py-10">
      <div class="flex items-center gap-2">
        <button @click="handleToogleCounter(0)" aria-label="button" title="Sign-Up" class="bg-gray-200 px-3 py-2 rounded-lg flex items-center gap-2 cursor-pointer">
          <span>sign in</span>
          <span class="icon-[material-symbols--sign-language-outline]"></span>
        </button>

        <button @click="handleToogleCounter(1)" aria-label="button" title="Sign-Up" class="bg-gray-200 px-3 py-2 rounded-lg flex items-center gap-2 cursor-pointer">
          <span>sign up</span>
          <span class="icon-[material-symbols--login]"></span>
        </button>
      </div>

      <div class="">
        <div v-if="tabCounter === 0">
          <SignIn />
        </div>

        <div v-else-if="tabCounter === 1">
          <SignUp />
        </div>
      </div>
    </div>
  </section>
</template>
