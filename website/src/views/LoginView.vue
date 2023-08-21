<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router';
import { ElMessage } from 'element-plus';
import { useUserStore } from '../store/user';

const router = useRouter();
const userStore = useUserStore();

const loginForm = ref({
  username: '',
  password: '',
  remember: true,
});

const handleLogin = async e => {
  userStore.login(loginForm.value)
    .then(() => {
      ElMessage.success("登陆成功！");
      router.push('/needs');
    })
    .catch(({ response, request }) => {
      if (response) {
        ElMessage.error(response.data.msg ?? "登录失败！");
      } else if (request) {
        ElMessage.error("网络请求出错");
      }
    });
}

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
                <el-checkbox v-model="loginForm.remember">记住我</el-checkbox>
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