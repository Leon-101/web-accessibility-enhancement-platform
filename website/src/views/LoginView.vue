<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router';
import { API_BASE_URL } from '../config'

const router = useRouter();

const loginForm = ref({
  username: '',
  password: '',
});

const remember = ref(true);

const handleLogin = async () => {
  try {
    const response = await fetch(API_BASE_URL + '/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(loginForm.value),
    });

    if (response.ok) {
      if (remember) {
        // 存储access_token
      }
      router.push('/');
    } else {
      alert('登录失败');
    }
  } catch (error) {
    console.error('登录请求出错', error);
  }
};
</script>

<template>
  <el-main>
    <el-row justify="center" align="middle">
      <el-col :span="8">
        <h2>登录</h2>
        <el-form :model="loginForm" label-width="120px">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="loginForm.username"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input type="password" v-model="loginForm.password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-row>
              <el-col :span="12">
                <el-checkbox v-model="remember">记住我</el-checkbox>
              </el-col>
              <el-col :span="12">
                <router-link to="/reset_password">忘记密码</router-link>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="handleLogin">登录</el-button>
          </el-form-item>
        </el-form>
        <div class="register-link">
          没有账号？<router-link to="/register">立即注册</router-link>
        </div>
      </el-col>
    </el-row>
  </el-main>
</template>
