<script setup>
import { reactive, ref } from "vue";
import { useAuthStore } from "../stores/auth";
const authStore = useAuthStore();
const userData = reactive({
  first_name: "",
  last_name: "",
  username: "",
  password: "",
  re_password: "",
});

async function onSubmit() {
  console.log("submit()...");
  const data = new FormData();
  for (const [key, value] of Object.entries(userData)) {
    data.append(key, value);
  }

  const res = await authStore.registerUser(data);
  console.log(res);
}
</script>

<template>
  <div>
    <!-- form validate 는 생략 -->
    <v-card>
      <v-card-text>
        <v-form @submit.prevent="onSubmit">
          <div class="px-5">
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="userData.username"
                  label="User Name*"
                  placeholder="Enter your User Name*"
                  variant="underlined"
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="6">
                <v-text-field
                  v-model="userData.first_name"
                  label="First Name*"
                  placeholder="Enter your First Name*"
                  variant="underlined"
                >
                </v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  v-model="userData.last_name"
                  label="Last Name*"
                  placeholder="Enter your Last Name"
                  variant="underlined"
                ></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="6">
                <v-text-field
                  v-model="userData.password"
                  label="Password*"
                  placeholder="Enter your Password"
                  variant="underlined"
                ></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  v-model="userData.re_password"
                  label="Re Password*"
                  placeholder="Enter your Re Password"
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
                  Sign Up
                </v-btn>
              </v-col>
            </v-row>
          </div>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>
