<script setup>
import { ref, reactive, watch, onMounted } from 'vue'
import api from '../api'
import { simulatedScriptData } from '../test_data/scripts'
import { ElMessage, ElText } from 'element-plus'

const sortOptions = ref([
  { value: "create_time", label: "发布时间" },
  { value: "stars", label: "收藏数" },
]);
const form = ref({
  keyword: '',
  sortBy: 'create_time',
});

const submitForm = () => {
  fetchScripts();
};

const scriptData = ref([]);
const currentPage = ref(1);
const pageSize = ref(10);
const displayedScripts = ref([]);
const totalScripts = ref(0);

// 处理页面切换
watch(currentPage, () => {
  fetchScripts();
});

const fetchScripts = async () => {
  const queryParams = {
    q: form.value.keyword,
    sort_by: form.value.sorBy,
    order: "desc",
    limit: 10,
    offset: (currentPage.value - 1) * pageSize.value + 1,
  };
  api.get("/scripts", {
    params: queryParams,
  })
    .then(({ data }) => {
      scriptData.value = data.data;
      totalScripts.value = data.total;
      displayedScripts.value = scriptData.value;
      ElMessage.success("加载成功");
    }).catch(({ response, request }) => {
      if (response) {
        ElMessage.warning(`脚本列表加载失败，状态码：${response.status}`);
      } else if (request) {
        ElMessage.error("网络请求出错，显示填充数据");
        scriptData.value = simulatedScriptData;
        totalScripts.value = scriptData.value.length;
        displayedScripts.value = scriptData.value;
      }
    });
}

const installScript = (scriptID) => {
  api.get(`/scripts/detail?script_id=${scriptID}`)
    .then(({ data }) => {
      window.location.href = "api/" + data.script_url;
    })
    .catch(err => ElMessage.error("安装失败"));
}

// 初始化时获取脚本列表数据
onMounted(fetchScripts);

</script>

<template>
  <el-main>
    <el-row>
      <el-col :span="22">
        <!-- 列表筛选区 -->
        <el-form :model="form" :inline="true" @submit.native.prevent="submitForm">
          <el-form-item label="搜索">
            <el-input v-model="form.keyword" placeholder="请输入脚本名称或目标网址"></el-input>
          </el-form-item>
          <el-form-item label="排序方式">
            <el-select v-model="form.sortBy" placeholder="请选择排序方式">
              <el-option v-for="opt in sortOptions" :label="opt.label" :value="opt.value"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" native-type="submit">查询</el-button>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="2">
        <el-button @click="$router.push('/script_upload')">上传脚本</el-button>
      </el-col>
    </el-row>

    <el-row justify="center" align="middle">
      <el-col :span="18">
        <!-- 脚本列表 -->
        <el-card class="script-card" v-for="script in displayedScripts" :key="script.id">
          <template #header>
            <h3 class="script-name">
              <router-link :to="`/script_details/${script.id}`">{{ script.name }}</router-link>
            </h3>
          </template>
          <div class="script-info">
            <el-text tag="p" class="mx-1">{{ script.description }}</el-text>
            <div class="script-metadata">
              <el-text tag="p">作者：{{ script.author }}</el-text>
              <el-text tag="p">{{ new Date(script.create_time).toLocaleDateString() }}</el-text>
              <el-text tag="p">收藏数：{{ script.stars || 0 }}</el-text>
              <!-- <el-link href="test.user.js">安装</el-link> -->
              <el-button type="primary" @click="installScript(script.id)">安装</el-button>
            </div>
          </div>
        </el-card>
        <!-- 分页控件 -->
        <el-pagination layout="prev, pager, next" :total="totalScripts" v-model:current-page="currentPage" prev-text="上一页"
          next-text="下一页"></el-pagination>
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