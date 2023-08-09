<script setup>
import { ref, reactive, onMounted } from 'vue'
import { API_host } from '../config'
import { simulatedScriptData } from '../simulatedScriptData'

const scriptData = ref([]);
const searchQuery = ref('');
const sortOption = ref('releaseTime');
const currentPage = ref(1);
const pageSize = ref(10);

// 过滤、排序、分页后的脚本列表
const displayedScripts = ref([]);

// 总脚本数量
const totalScripts = ref(scriptData.length);

// 搜索脚本
const searchScripts = () => {
  alert('功能开发中……');
};

// 处理当前页变化
const handleCurrentChange = (newPage) => {
  currentPage.value = newPage;
  fetchScripts();
};

const fetchScripts = async () => {
  scriptData.value = simulatedScriptData;
  totalScripts.value = scriptData.value.length;
  displayedScripts.value = scriptData.value;
};

// 初始化时获取脚本列表数据
onMounted(fetchScripts);

</script>

<template>
  <div>
    <!-- 搜索区 -->
    <el-row class="search-area">
      <el-col :span="12">
        <el-input v-model="searchQuery" placeholder="请输入脚本名称或目标网址" />
      </el-col>
      <el-col :span="2">
        <el-button type="primary" @click="searchScripts">搜索</el-button>
      </el-col>
    </el-row>

    <!-- 排序选择区 -->
    <el-radio-group v-model="sortOption" class="sort-area">
      <el-radio label="releaseTime">发布时间</el-radio>
      <el-radio label="downloads">下载量</el-radio>
      <el-radio label="rating">评分</el-radio>
    </el-radio-group>
    <!-- 脚本列表 -->
    <el-card v-for="script in displayedScripts" :key="script.id" class="script-card">
      <div class="script-info">
        <h3>{{ script.title }}</h3>
        <p>{{ script.description }}</p>
        <p>作者：{{ script.author }}</p>
        <p>创建时间：{{ script.create_time }}</p>
        <p>下载量：{{ script.downloads }}</p>
        <!-- <p>评分：{{ script.rating }}</p> -->
      </div>
      <div class="details-link">
        <!-- <router-link :to="`/scripts/${script.id}`">查看详情</router-link> -->
        <el-link href="test.user.js">安装</el-link>
      </div>
    </el-card>

    <!-- 分页控件 -->
    <!-- <el-pagination layout="prev, pager, next" :total="totalScripts" v-model:current-page="currentPage"></el-pagination> -->

  </div>
</template>
