<script setup lang="ts">
definePageMeta({
  layout: "default",
});

// to control the form tabs here
let tabCounter: number = ref(0);

// changing the tab counter
const handleToggleCounter = (index: number) => {
  tabCounter.value = index;
};
</script>

<template>
  <section class="grid grid-cols-1 md:grid md:grid-cols-1 lg:grid lg:grid-cols-2 place-content-center">
    <!-- for the side landing page -->
    <div>
      <div class="hidden lg:block bg-gray-100 h-screen px-5 py-5">
        <div>
          <div class="bg-primary-main-white w-32 rounded-full">hey</div>
        </div>

        <div>
          <img src="/images/maddox-furlong-1IRnESiBIU4-unsplash.jpg"/>
        </div>
      </div>
    </div>

    <!-- for the main login form here -->
    <div class="px-5 lg:px-10 py-10">
      <div class="flex items-center gap-2">
        <button @click="handleToggleCounter(0)" aria-label="button" title="Sign-Up" class="bg-gray-200 px-3 py-2 rounded-lg flex items-center gap-2 cursor-pointer">
          <span class="capitalize">sign in</span>
          <span class="icon-[material-symbols--sign-language-outline]"></span>
        </button>

        <button @click="handleToggleCounter(1)" aria-label="button" title="Sign-Up" class="bg-gray-200 px-3 py-2 rounded-lg flex items-center gap-2 cursor-pointer">
          <span class="capitalize">sign up</span>
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
