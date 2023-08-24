import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { useUserStore } from '../store/user'

const userStore = useUserStore();

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
      component: () => import('../views/UserCenterView.vue'),
      meta: { requiresAuth: true },
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
      component: () => import('../views/ScriptUploadView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/need_details/:script_id',
      name: 'need_detail',
      component: () => import('../views/NeedDetailView.vue')
    },
    {
      path: '/need_upload',
      name: 'need_upload',
      component: () => import('../views/NeedUploadView.vue'),
      meta: { requiresAuth: true },
    },
  ]
})


// 守卫需要登录的路由
router.beforeEach((to, from) => {
  if (
    to.meta.requiresAuth &&
    !userStore.loggedIn.value &&
    to.name != "login"
  ) {
    // 重定向到登录页面
    return {
      path: '/login',
      query: { redirect: to.fullPath }, // 保存目标位置，用于登录后的跳转
    }
  }
})

export default router
