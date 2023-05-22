<script setup>
import { ref } from 'vue'
const email = ref('')
const password = ref('')
async function onSubmit() {
  console.log('onSubmit()...')
}
</script>
<template>
  <div>
    <v-card>
      <v-card-text>
        <h3 class="text-h5 text-center font-weight-bold">로그인</h3>
        <v-form v-model="form" @submit.prevent="onSubmit">
          <div class="pa-5">
            <v-text-field
              v-model="email"
              :readonly="loading"
              class="mb-2"
              clearable
              label="Email"
              placeholder="Enter your Email"
              variant="underlined"
            >
            </v-text-field>

            <v-text-field
              v-model="password"
              :readonly="loading"
              clearable
              label="Password"
              placeholder="Enter your password"
              variant="underlined"
            ></v-text-field>
          </div>

          <v-btn
            :disabled="!form"
            :loading="loading"
            block
            color="deep-purple-accent-4"
            size="large"
            type="submit"
            variant="elevated"
          >
            Sign In
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>
