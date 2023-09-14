<script setup>
import { ref } from 'vue'
import { RouterLink, useRoute, useRouter } from 'vue-router'
import { useUserStore } from '../store/user';
import { ElMessage, ElMessageBox } from 'element-plus';

const router = useRouter();
const route = useRoute();
const userStore = useUserStore();

const registerForm = ref({
  username: '',
  email: '',
  password: '',
  confirmPassword: '',
});

const handleRegister = () => {
  userStore.register(registerForm.value)
    .then(() => {
      const { username, password } = registerForm.value;
      ElMessageBox({
        boxType: "alert",
        title: "注册成功",
        message: `您的用户名是：${username}`,
        confirmButtonText: "立即登录",
        type: "success",
      })
        .then(() => {
          return userStore.login({
            username,
            password,
            remember: true,
          });
        })
        .then(() => {
          ElMessage.success("登录成功！");
          router.push(route.query.redirect || "/");
        });
    })
    .catch(({ response, request }) => {
      if (response) {
        const errors = response.data.errors;
        try {
          Object.values(errors).forEach(messages => {
            ElMessage.error(messages.join("\n"));
          });
        } catch (err) {
          console.error(err);
          ElMessage("注册失败，请检查您的输入。");
        }
      }
    })
};
</script>

<template>
  <el-main>
    <el-row justify="center" align="middle">
      <el-col :span="12">
        <h2 class="form-title">注册</h2>
        <el-form :model="registerForm" label-width="auto">
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