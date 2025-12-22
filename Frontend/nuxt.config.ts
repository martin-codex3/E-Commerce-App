// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";
import Aura from "@primeuix/themes/aura";
import ToastService from 'primevue/toastservice';

// the toast service to be used within the app her
export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  css: ["./app/assets/css/main.css"],
  modules: ["@pinia/nuxt", '@primevue/nuxt-module', "@nuxt/image"],
  primevue: {
    options: {
      theme: {
        preset: Aura,
        options: {
          darkModeSelector: false
        }
      }
    }
  },
  vite: {
    plugins: [tailwindcss(), ToastService],
  },
  runtimeConfig: {
    public: {
      apiBase: process.env.BACKEND_URL
    },
  },
});