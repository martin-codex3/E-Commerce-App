<script setup lang="ts">
const isLoading: boolean = ref(false);
const formErrors: object = ref({});
const runtimeConfig = useRuntimeConfig();
const toast = useToast()

// the reactive form state here
const form = reactive({
  email: "",
  password: "",
});

// function to submit the form data here
const handleSignIn = async () => {
  isLoading.value = true
  formErrors.value = {}
  try {
    await $fetch(`${runtimeConfig.public.apiBase}/api/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(form),
      onResponse(value) {
        // checking if the response is okay here
        if (value.response.ok) {
          // we will show the success message here
          toast.add({
            severity: "success",
            summary: "Success",
            life: 10000,
            detail: "Account created successfully"
          })
        }
        // checking if the passed email already exists here
        if (value.response._data.detail.message) {
          emailError.value = value.response._data.detail.message;
          // for the already available email here
          toast.add({
            severity: "error",
            summary: "Error",
            life: 10000,
            detail: "Correct the errors and try again!"
          })
        }

        if (!value.response.ok) {
          value.response._data.detail.forEach((error: any) => {
            formErrors.value[error.loc[1]] = error.msg
          })
          // we will trigger the toast here
          toast.add({
            severity: "error",
            life: 10000,
            summary: "Error",
            detail: "Correct the errors and try again!"
          })
        }
      }
    })
  }catch (e) {
    return
  }
  finally {
    isLoading.value = false
  }
};
</script>

<template>
  <Toast position="top-left"/>
  <div class="space-y-5 pt-5">
    <div>
      <h1 class="capitalize font-semibold text-lg text-center">sign in</h1>
    </div>

    <div>
      <form @submit.prevent="handleSignIn" method="POST">
        <div class="form__wrapper flex flex-col gap-5">
          <div>
            <label for="email" class="capitalize">email</label>
            <input type="email" placeholder="@user.com" v-model="form.email" id="email"
                   class="w-full border rounded-lg py-2"
                   :class="formErrors.email ? 'border border-red-500 ring ring-red-500' : ''"/>
            <span v-if="formErrors.email" class="text-form-error text-sm flex items-center gap-1">
                <span class="icon-[material-symbols--error-outline-rounded]"></span>
                {{ formErrors.email }}
            </span>
          </div>

          <div>
            <label for="password" class="capitalize">password</label>
            <input type="password" id="password" v-model="form.password"
                   class="w-full border rounded-lg py-2"
                   :class="formErrors.password ? 'border border-red-500 ring ring-red-500' : ''"/>
            <span v-if="formErrors.password" class="text-form-error text-sm flex items-center gap-1">
                <span class="icon-[material-symbols--error-outline-rounded]"></span>
                {{ formErrors.password }}
            </span>
          </div>

          <div>
            <button aria-label="button" type="submit" :disabled="isLoading" class="border-none bg-primary-main-blue transition
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
