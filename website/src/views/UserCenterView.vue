<script setup>
import UnderConstruction from '../components/UnderConstruction.vue';
import { ElMessage, ElText, ElButton } from 'element-plus'
import { RouterLink, useRouter } from 'vue-router';
import { useUserStore } from '../store/user';
const router = useRouter();
const userStore = useUserStore();

const logout = e => {
  userStore.logout().then(() => {
    ElMessage.success("退出成功！");
    router.push("/");
  })
}
</script>

<template>
  <el-main>
    <el-text tag="p">用户名：{{ userStore.user.value?.username }}</el-text>
    <el-button @click="logout">退出登录</el-button>
    <UnderConstruction />
  </el-main>
</template>
