<script setup>
import { ref, reactive, watch, onMounted } from 'vue'
import { API_BASE_URL } from '../config'
import { simulatedScriptData } from '../simulatedScriptData'

const sortOptions = ref([
  { value: "create_time", label: "发布时间" },
  { value: "stars", label: "收藏数" },
]);
const form = ref({
  keyword: '',
  sortBy: 'create_time',
});

const submitForm = () => {
  alert("功能开发中……");
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
  scriptData.value = simulatedScriptData;
  totalScripts.value = scriptData.value.length;
  displayedScripts.value = scriptData.value;
};

// 初始化时获取脚本列表数据
onMounted(fetchScripts);

</script>

<template>
  <!-- 列表筛选区 -->
  <el-main>
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

    <!-- 脚本列表 -->
    <el-row justify="center" align="middle">
      <el-col :span="12">
        <el-card v-for="script in displayedScripts" :key="script.id" class="script-card">
          <template #header>
            <h3><el-link>{{ script.title }}</el-link></h3>
          </template>
          <div class="script-info">
            <p>{{ script.description }}</p>
            <p>作者：{{ script.author }}</p>
            <p>创建时间：{{ script.create_time }}</p>
            <p>下载量：{{ script.downloads }}</p>
          </div>
          <div class="details-link">
            <!-- <router-link :to="`/scripts/${script.id}`">查看详情</router-link> -->
            <el-link href="test.user.js">安装</el-link>
          </div>
        </el-card>

        <!-- 分页控件 -->
        <el-pagination layout="prev, pager, next" :total="100" v-model:current-page="currentPage" prev-text="上一页"
          next-text="下一页"></el-pagination>
      </el-col>
    </el-row>

  </el-main>
</template>
