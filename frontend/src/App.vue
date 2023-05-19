<script setup></script>

<template>
  <v-app>
    <v-main>
      <v-tabs v-model="tab" bg-color="primary">
        <v-tab to="/">Login</v-tab>
        <v-tab to="/dashboard">Dashboard</v-tab>
      </v-tabs>

      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>
