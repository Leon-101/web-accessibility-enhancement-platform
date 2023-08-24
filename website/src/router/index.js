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
      component: HomeView,
      meta: {
        title: '首页',
      },
    },
    {
      path: '/scripts',
      name: 'scripts',
      component: () => import('../views/ScriptsView.vue'),
      meta: {
        title: '脚本库',
      },
    },
    {
      path: '/needs',
      name: 'needs',
      component: () => import('../views/NeedsView.vue'),
      meta: {
        title: '需求趋',
      },
    },
    {
      path: '/user_center',
      name: 'user_center',
      component: () => import('../views/UserCenterView.vue'),
      meta: {
        title: '个人中心',
        requiresAuth: true,
      },
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
      meta: {
        title: '关于我们',
      },
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue'),
      meta: {
        title: '注册',
      },
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
      meta: {
        title: '登录',
      },
    },
    {
      path: '/reset_password',
      name: 'reset_password',
      component: () => import('../views/ResetPasswordView.vue'),
      meta: {
        title: '忘记密码',
      },
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
      meta: {
        title: '上传脚本',
        requiresAuth: true,
      },
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
      meta: {
        title: '发布需求',
        requiresAuth: true,
      },
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

// 路由切换后更改页面标题
router.afterEach((to, from) => {
  const baseTitle = "无障碍优化平台";
  const pageTitle = to.meta.title || "";
  document.title = pageTitle ? `${pageTitle} - ${baseTitle}` : baseTitle;
});

export default router
