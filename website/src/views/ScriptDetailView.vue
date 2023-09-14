<script setup>
import { ref, onMounted } from "vue";
import { ElText } from "element-plus";
import { useRoute } from "vue-router";
import api from "../api";

const route = useRoute();

const script = ref({});
const scriptCode = ref("");

const fetchScriptDetail = () => {
  api.get(`/scripts/detail?script_id=${route.params.script_id}`)
    .then(({ data }) => {
      script.value = data;
    })
    .then(() => {
      return api.get(`${script.value.script_url}`);
    })
    .then(({ data }) => {
      scriptCode.value = data;
    });
}

const installScript = (scriptID) => {
  window.location.href = "api/" + script.value.script_url;
}

onMounted(fetchScriptDetail);
</script>

<template>
  <el-main>
    <el-row justify="center" align="middle">
      <el-col :span="18">
        <el-card class="script-card">
          <template #header>
            <h2 class="script-title">
              {{ script.name }}
            </h2>
          </template>
          <div class="script-info">
            <el-text tag="p" class="mx-1">{{ script.description }}</el-text>
            <div class="script-metadata">
              <el-text tag="p">作者：{{ script.author }}</el-text>
              <el-text tag="p">{{ new Date(script.create_time).toLocaleDateString() }}</el-text>
              <el-text tag="p">收藏数：{{ script.stars || 0 }}</el-text>
              <el-button type="primary" @click="installScript(script.id)">安装</el-button>
            </div>
            <br />
            <h3>脚本代码</h3>
            <el-input type="textarea" :rows="20" v-model="scriptCode" readonly></el-input>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </el-main>
</template>

<style scoped>
.script-card {
  margin-bottom: 20px;
  border: 1px solid #ebeef5;
}

.script-title {
  font-weight: bold;
  font-size: 1.2em;
}

/* .script-info {
  padding: 15px;
} */

.script-metadata {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}
</style>