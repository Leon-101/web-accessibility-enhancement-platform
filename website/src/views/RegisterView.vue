<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { API_BASE_URL } from '../config';

const registerForm = ref({
  username: '',
  email: '',
  password: '',
  confirmPassword: '',
});

const handleRegister = () => {
  //todo
};
</script>

<template>
  <el-main>
    <el-row justify="center" align="middle">
      <el-col :span="8">
        <h2>注册</h2>
        <el-form :model="registerForm">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="registerForm.username"></el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input v-model="registerForm.email"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input type="password" v-model="registerForm.password"></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="confirmPassword">
            <el-input type="password" v-model="registerForm.confirmPassword"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="handleRegister">注册</el-button>
          </el-form-item>
        </el-form>
        <div class="login-link">
          已有账号？<RouterLink to="/login">立即登录</RouterLink>
        </div>
      </el-col>
    </el-row>
  </el-main>
</template>
