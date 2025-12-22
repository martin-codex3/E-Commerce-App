// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";
import Aura from "@primeuix/themes/aura";

export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  css: ["./app/assets/css/main.css"],
  modules: ["@pinia/nuxt", '@primevue/nuxt-module'],
  primevue: {
    options: {
      theme: {
        preset: Aura
      }
    }
  }
  vite: {
    plugins: [tailwindcss()],
  },
  runtimeConfig: {
    public: {
      apiBase: process.env.BACKEND_URL
    },
  },
});
