import { defineStore } from "pinia";
import axios from "axios";
import { useCookies } from "vue3-cookies";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
    isAuthenticated: false,
    loading: false,
    register_success: false,
  }),
  getters: {},
  actions: {
    async registerUser(data) {
      try {
        const res = await axios.post(
          `${import.meta.env.VITE_API_URL}/api/accounts/register/`,
          data,
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        this.register_success = true;
        return res.data;
      } catch (err) {
        this.register_success = false;
        return err.response;
      }
    },

    async loginUser(data) {
      try {
        const res = await axios.post(
          `${import.meta.env.VITE_API_URL}/api/token/`,
          data,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
        this.isAuthenticated = true;

        const { cookies } = useCookies();
        cookies.set("access", res.data.access, "1d", {
          path: "/api",
          httponly: true,
          secure: false,
        });

        return res.data;
      } catch (err) {
        console.log(err);
        this.isAuthenticated = false;
        return err.response;
      }
    },
  },
});
