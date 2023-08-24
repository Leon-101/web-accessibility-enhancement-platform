<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from './store/user'

const userStore = useUserStore();
</script>

<template>
  <el-container>
    <el-header>
      <nav>
        <el-menu mode="horizontal" menu-trigger="click">
          <el-menu-item>
            <RouterLink to="/">首页</RouterLink>
          </el-menu-item>
          <el-menu-item>
            <RouterLink to="/scripts">脚本库</RouterLink>
          </el-menu-item>
          <el-menu-item>
            <RouterLink to="/needs">需求区</RouterLink>
          </el-menu-item>
          <el-menu-item>
            <RouterLink to="/about">关于我们</RouterLink>
          </el-menu-item>
          <template v-if="userStore.loggedIn.value">
            <el-menu-item>
              <RouterLink to="/user_center">个人中心</RouterLink>
            </el-menu-item>
          </template>
          <template v-else>
            <el-menu-item>
              <RouterLink to="/register">注册</RouterLink>
            </el-menu-item>
            <el-menu-item>
              <RouterLink to="/login">登录</RouterLink>
            </el-menu-item>
          </template>
        </el-menu>
      </nav>
    </el-header>
    <br>
    <router-view v-slot="{ Component }">
      <transition name="fade">
        <component :is="Component" />
      </transition>
    </router-view>
  </el-container>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>