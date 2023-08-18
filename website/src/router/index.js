import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/scripts',
      name: 'scripts',
      component: () => import('../views/ScriptsView.vue'),
    },
    {
      path: '/needs',
      name: 'needs',
      component: () => import('../views/NeedsView.vue')
    },
    {
      path: '/user_center',
      name: 'user_center',
      component: () => import('../views/UserCenterView.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/reset_password',
      name: 'reset_password',
      component: () => import('../views/ResetPasswordView.vue')
    },
    {
      path: '/script_details/:script_id',
      name: 'script_detail',
      component: () => import('../views/ScriptDetailView.vue')
    },
    {
      path: '/script_upload',
      name: 'script_upload',
      component: () => import('../views/ScriptUploadView.vue')
    },
    {
      path: '/need_details/:script_id',
      name: 'need_detail',
      component: () => import('../views/NeedDetailView.vue')
    },
    {
      path: '/need_upload',
      name: 'need_upload',
      component: () => import('../views/NeedUploadView.vue')
    },
  ]
})

export default router
