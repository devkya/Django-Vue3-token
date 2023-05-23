<script setup>
import { ref } from "vue";
import { useAuthStore } from "../stores/auth";
import router from "@/router/index";
import { storeToRefs } from "pinia";

const authStore = useAuthStore();
const { isAuthenticated } = storeToRefs(authStore);
const username = ref("");
const password = ref("");

async function onSubmit() {
  const data = new FormData();
  data.append("username", username.value);
  data.append("password", password.value);
  const res = await authStore.loginUser(data);

  console.log(isAuthenticated.value);

  if (authStore.isAuthenticated) {
    router.push("/dashboard");
  } else {
    console.log("로그인 실패");
  }
}
</script>
<template>
  <div>
    <v-card>
      <v-card-text>
        <v-form @submit.prevent="onSubmit">
          <div class="px-5">
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="username"
                  class="mb-2"
                  label="User Name*"
                  placeholder="Enter your User Name"
                  variant="underlined"
                >
                </v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="password"
                  label="Password*"
                  placeholder="Enter your password"
                  variant="underlined"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col col="12" class="text-right">
                <v-btn
                  color="deep-purple-accent-4"
                  size="large"
                  type="submit"
                  variant="elevated"
                >
                  Sign In
                </v-btn>
              </v-col>
            </v-row>
          </div>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>
