import { defineStore } from "pinia";

export const useCreateUserStore = defineStore("create-account-store", async () => {
    // we will define all the required tooling here
    const isLoading: boolean = ref(false);
    const errors: object = ref({});

    // function to create the user here
    const runtimeConfig = useRuntimeConfig();

    const handleCreateAccount = async (user_data: any) => {
        try {
            isLoading.value = true;

            // we will attempt to register the client here
            await $fetch(`${runtimeConfig.public}/create-account`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify(user_data),
                onResponse(value) {
                    console.log(value)
                }
            });

        } catch (error) {
            errors.value = error.message;
        } finally {
            isLoading.value = false;
        }
    }

    // we will export the values here
    return { isLoading, errors, handleCreateAccount }
});
