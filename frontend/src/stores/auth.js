import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    isAuthenticated: false,
    loading: false,
    register_success: false
  }),
  getters: {},
  actions: {
    async registerUser(data) {
      try {
        const res = axios.post(`${import.meta.env.VITE_API_URL}/api/accounts/register/`, data, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        console.log(res)
        return res
      } catch (err) {
        console.log(err)
      }
    }
  }
})
