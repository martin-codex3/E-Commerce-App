<script setup lang="ts">
// the reactive form state here
const form = reactive({
  email: "",
  password: "",
});

// function to submit the form data here
const handleSignIn = () => {
  console.log(form);
};
</script>

<template>
  <div class="space-y-5 pt-5">
    <div>
      <h1 class="capitalize font-semibold text-lg text-center">sign in</h1>
    </div>

    <div>
      <form @submit.prevent="handleSignIn" method="POST">
        <div class="form__wrapper flex flex-col gap-5">
          <div>
            <label for="email" class="capitalize">email</label>
            <input type="email" placeholder="@user.com" name="email" id="email" class="w-full border rounded-lg py-2" />
          </div>

          <div>
            <label for="password" class="capitalize">password</label>
            <input type="password" name="password" id="password" class="w-full border rounded-lg py-2" />
          </div>

          <div>
            <button arial-label="button" type="submit" class="border-none bg-primary-main-blue transition hover:shadow-xl rounded-full cursor-pointer w-44 text-center py-2">
              <span class="capitalize text-blue-100 font-semibold">sign in</span>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
