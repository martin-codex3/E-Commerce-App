<script setup lang="ts">
const runtimeConfig = useRuntimeConfig()

// for the toast notification here
const toast = useToast()
// for the loading state and any errors
const isLoading: boolean = ref(false);
const formErrors: object = ref({});
const emailError: string = ref("");

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
  emailError.value = ""

  try {
    await $fetch(`${runtimeConfig.public.apiBase}/api/create-account`, {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(form),
      onResponse(value) {
        // if the form is okay here//
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
        // errors will be caught here if the form has any errors
        if (!value.response.ok) {
          value.response._data.detail.forEach((error: any) => {
            formErrors.value[error.loc[1]] = error.msg
          })
          toast.add({
            severity: "error",
            summary: "Error",
            life: 10000,
            detail: "Correct the errors and try again!"
          })
        }


      },
    })

  }catch (e) {
    return
  }finally {
    isLoading.value = false
  }
};
</script>

<template>
  <Toast position="top-left"/>
  <div class="space-y-5 pt-5">
    <div>
      <h1 class="capitalize font-semibold text-lg text-center">sign up</h1>
    </div>

    <div>
      <form @submit.prevent="handleSignUp" method="POST">
        <div class="form__wrapper flex flex-col gap-5">
          <div class="grid grid-cols-2 lg:grid-cols-2 gap-5">
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
              <input type="text" id="last_name" v-model="form.last_name"
                     :class="formErrors.last_name ? 'border border-red-500 ring ring-red-500' : ''"
                     class="w-full border rounded-lg py-2" />
              <span v-if="formErrors.last_name" class="text-form-error text-sm flex items-center gap-1">
                <span class="icon-[material-symbols--error-outline-rounded]"></span>
                {{ formErrors.last_name }}
              </span>
            </div>
          </div>

          <div>
            <label for="username" class="capitalize">username</label>
            <input type="text" id="username" v-model="form.username"
                   :class="formErrors.username ? 'border border-red-500 ring ring-red-500' : ''"
                   class="w-full border rounded-lg py-2" />
            <span v-if="formErrors.username" class="text-form-error text-sm flex items-center gap-1">
                <span class="icon-[material-symbols--error-outline-rounded]"></span>
                {{ formErrors.username }}
            </span>
          </div>

          <div>
            <label for="email" class="capitalize">email</label>
            <input type="email" placeholder="@user.com" v-model="form.email"
                   name="email" id="email"
                   :class="formErrors.email || emailError ? 'border border-red-500 ring ring-red-500' : ''"
                   class="w-full border rounded-lg py-2" />
            <span v-if="formErrors.email" class="text-form-error text-sm flex items-center gap-1">
                <span class="icon-[material-symbols--error-outline-rounded]"></span>
                {{ formErrors.email }}
            </span>

            <span v-else-if="emailError" class="text-form-error text-sm flex items-center gap-1">
                <span class="icon-[material-symbols--error-outline-rounded]"></span>
                {{ emailError }}
            </span>
          </div>

          <div>
            <label for="password" class="capitalize">password</label>
            <input type="password" name="password" v-model="form.password"
                   id="password" class="w-full border rounded-lg py-2"
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
