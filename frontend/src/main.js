import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import { createPinia } from "pinia";
import { globalCookiesConfig } from "vue3-cookies";
import VueCookies from "vue3-cookies";
globalCookiesConfig({
  httponly: true,
  path: "/api/",
  secure: false,
});

loadFonts();
const app = createApp(App);
app.use(VueCookies);
app.use(router);
app.use(vuetify);
app.use(createPinia());
app.mount("#app");
