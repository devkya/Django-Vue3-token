<script setup>
import { computed, ref } from "vue";
import { useRoute } from "vue-router";

const tab = ref(null);
const routeName = computed(() => useRoute().name);
console.log(routeName);
</script>

<template>
  <v-app>
    <v-app-bar elevation="0" app>
      <v-row align="center">
        <v-col cols="auto">
          <h3 class="mx-5">DevKya's Blog / Vue & Django</h3>
        </v-col>
        <v-col cols="auto">
          <v-tabs
            v-model="tab"
            color="deep-purple-accent-4"
            class="self-justify-center"
            align-tabs="center"
          >
            <v-tab :value="1" to="/register">REGISTER</v-tab>
            <v-tab :value="2" to="/">LOGIN</v-tab>
            <v-tab :value="3" to="/dashboard">DASHBOARD</v-tab>
          </v-tabs>
        </v-col>
      </v-row>
    </v-app-bar>
    <v-container>
      <div class="appBar pa-5 bg-grey-lighten-3 d-flex">
        <div class="align-self-center">
          <h4 class="text-h4 font-weight-bold ma-3">{{ routeName }} Page</h4>
          <h5 class="font-weight-regular ma-3">
            JWT Tutorial with Http Only Cookies
          </h5>
        </div>
      </div>
      <div>
        <router-view />
      </div>
    </v-container>
  </v-app>
</template>

<style scoped>
.appBar {
  height: 15vh;
  min-height: 80px;
}
</style>
