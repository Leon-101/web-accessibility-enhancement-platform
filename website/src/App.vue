<script setup>
import { RouterLink, RouterView } from 'vue-router'
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
          <el-menu-item>
            <RouterLink to="/register">注册</RouterLink>
          </el-menu-item>
          <el-menu-item>
            <RouterLink to="/login">登录</RouterLink>
          </el-menu-item>
        </el-menu>
      </nav>
    </el-header>

    <RouterView />
  </el-container>
</template>
