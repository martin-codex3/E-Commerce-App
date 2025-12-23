<script setup lang="ts">
import image1 from "../assets/images/maddox-furlong-1IRnESiBIU4-unsplash.jpg";
import image2 from "@/assets/images/ryan-waring-164_6wVEHfI-unsplash.jpg";
import image3 from "@/assets/images/tom-brunberg-D4ZtZX1UeAI-unsplash.jpg";
import image4 from "@/assets/images/tuananh-blue-2QSK4kFoVZE-unsplash.jpg";
import image5 from "@/assets/images/engin-akyurt-Y5n8mCpvlZU-unsplash.jpg";



definePageMeta({
  layout: "default",
});

// to control the form tabs here
let tabCounter: number = ref(0);

// changing the tab counter
const handleToggleCounter = (index: number) => {
  tabCounter.value = index;
};

// for all the images here
const all_images: any[] = reactive([
    image1, image2, image3, image4, image5
]);

const currentIndex: number = ref(0)

// function to change the images
const handleChangeImages = (index: number) => {
  all_images.forEach((item: any, index) => {
    console.log(item)
    console.log(index)
  })
}

</script>

<template>
  <section class="grid grid-cols-1 md:grid md:grid-cols-1 lg:grid lg:grid-cols-2 place-content-center">
    <!-- for the side landing page -->
    <div>
      <div class="hidden lg:block bg-gray-100 h-screen px-5 py-5 space-y-7">
        <div class="flex items-center justify-between">
          <div class="bg-primary-main-white py-2 w-32 rounded-full flex items-center justify-center">
            <h1 class="capitalize text-sm">shoes</h1>
          </div>

          <div class="bg-primary-main-white py-2 w-32 rounded-full flex items-center justify-center gap-3">
            <div class="h-3 w-3 rounded-full bg-primary-main-blue"></div>
            <div class="h-3 w-3 rounded-full bg-primary-main-blue"></div>
            <div class="h-3 w-3 rounded-full bg-primary-main-blue"></div>
            <div class="h-3 w-3 rounded-full bg-primary-main-blue"></div>
          </div>
        </div>

        <div class="">
          <NuxtImg :src="image1" placegolder class="rounded-3xl"/>
        </div>

        <div class="flex items-center gap-3">
          <button @click="handleChangeImages(1)" aria-label="button" class="bg-primary-main-blue flex cursor-pointer
           text-blue-100 items-center justify-center p-2 rounded-full">
            <span class="icon-[material-symbols--chevron-left] text-xl"></span>
          </button>

          <button aria-label="button" class="bg-primary-main-blue flex cursor-pointer
           text-blue-100 items-center justify-center p-2 rounded-full">
            <span class="icon-[material-symbols--chevron-right] text-xl"></span>
          </button>
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
