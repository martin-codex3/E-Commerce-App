<script setup lang="ts">

const runtimeConfig = useRuntimeConfig()

// for the loading state and any errors
const isLoading: boolean = ref(false)
const formErrors: object = ref({})

// the reactive form state here
const form = reactive({
  first_name: "",
  last_name: "",
  username: "",
  email: "",
  password: "",
});

// function to submit the form data here
const handleSignUp = async () => {
  isLoading.value = true
  formErrors.value = {}

  try {
    await $fetch(`${runtimeConfig.public.apiBase}/api/create-account`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(form),
      onResponse(value) {
        if (!value.response.ok) {
          value.response._data.detail.forEach((error: any) => {
            formErrors.value[error.loc[1]] = error.msg
          })
        }

        if (value.response.ok) {
          // we will show the success message here
        }
      }
    })

  }catch (e) {
    return
  }finally {
    isLoading.value = false
  }
};
</script>

<template>
  <div class="space-y-5 pt-5">
    <div>
      <h1 class="capitalize font-semibold text-lg text-center">sign up</h1>
    </div>

    <div>
      <form @submit.prevent="handleSignUp" method="POST">
        <div class="form__wrapper flex flex-col gap-5">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
            <div>
              <label for="first_name" class="capitalize">first name</label>
              <input type="text" id="first_name" v-model="form.first_name"
                     :class="formErrors.first_name ? 'border border-red-500 ring ring-red-500' : ''"
                     class="w-full border rounded-lg py-2"/>
              <span v-if="formErrors.first_name" class="text-form-error text-sm flex items-center gap-1">
                <span class="icon-[material-symbols--error-outline-rounded]"></span>
                {{ formErrors.first_name }}
              </span>
            </div>

            <div>
              <label for="last_name" class="capitalize">last name</label>
              <input type="text" id="last_name" v-model="form.last_name" class="w-full border rounded-lg py-2" />
            </div>
          </div>

          <div>
            <label for="username" class="capitalize">username</label>
            <input type="text" id="username" v-model="form.username" class="w-full border rounded-lg py-2" />
          </div>

          <div>
            <label for="email" class="capitalize">email</label>
            <input type="email" placeholder="@user.com" v-model="form.email"
                   name="email" id="email" class="w-full border rounded-lg py-2" />
          </div>

          <div>
            <label for="password" class="capitalize">password</label>
            <input type="password" name="password" v-model="form.password"
                   id="password" class="w-full border rounded-lg py-2" />
          </div>

          <div>
            <button aria-label="button" type="submit" class="border-none bg-primary-main-blue transition
            hover:shadow-xl rounded-full cursor-pointer w-44 text-center py-2 flex items-center justify-center">
              <span v-if="isLoading" class="icon-[svg-spinners--180-ring] text-blue-100 text-xl"></span>
              <span v-else class="capitalize text-blue-100 font-semibold text-sm">sign up</span>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
