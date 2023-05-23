import { createRouter, createWebHistory } from "vue-router";
import LoginView from "@/views/LoginView.vue";
import DashboardView from "@/views/DashboardView.vue";
import RegisterView from "@/views/RegisterView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "",
      component: () => import("@/layouts/DefaultLayout.vue"),
      children: [
        {
          path: "",
          name: "Login",
          component: LoginView,
        },
        {
          path: "/register",
          name: "Register",
          component: RegisterView,
        },
        {
          path: "/dashboard",
          name: "Dashboard",
          component: DashboardView,
        },
      ],
    },
  ],
});

export default router;
