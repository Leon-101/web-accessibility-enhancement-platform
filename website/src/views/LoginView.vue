<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router';
import { ElMessage } from 'element-plus';
import { API_BASE_URL } from '../config'

const router = useRouter();

const loginForm = ref({
  username: '',
  password: '',
});

const remember = ref(true);

const handleLogin = async (e) => {
  try {
    const response = await fetch(API_BASE_URL + '/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(loginForm.value),
    });

    const responseBody = response.json();
    if (response.ok) {
      if (remember) {
        localStorage.setItem("access_token", responseBody.access_token);
      }
      sessionStorage.setItem("access_token", responseBody.access_token);
      ElMessage("登陆成功！");
      router.push('/');
    } else {
      ElMessage("登陆失败，请检查您的用户名和密码。");
    }
  } catch (error) {
    ElMessage("网络请求出错");
    console.error('登录请求出错', error);
  }
};
</script>

<template>
  <el-main>
    <el-row justify="center" align="middle">
      <el-col :span="12">
        <h2 class="form-title">登录</h2>
        <el-form :model="loginForm" label-width="auto">
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

<style scoped>
.form-title {
  font-weight: bold;
  font-size: 1.5em;
  margin-bottom: 1em;
}

.el-form-item {
  margin-bottom: 1em;
}

.el-input {
  width: 60%;
}
</style>