<script setup>
import { ref, reactive, watch, onMounted } from 'vue'
import api from '../api'
import { ElMessage, ElText } from 'element-plus'

const sortOptions = ref([
  { value: "create_time", label: "发布时间" },
  { value: "votes", label: "热度" },
]);
const form = ref({
  keyword: '',
  sortBy: 'create_time',
});

const submitForm = () => {
  fetchNeeds();
};

const needData = ref([]);
const currentPage = ref(1);
const pageSize = ref(10);
const displayedNeeds = ref([]);
const totalNeeds = ref(0);

// 处理页面切换
watch(currentPage, () => {
  fetchNeeds();
});

const fetchNeeds = async () => {
  const queryParams = {
    q: form.value.keyword,
    sort_by: form.value.sorBy,
    order: "desc",
    limit: 10,
    offset: (currentPage.value - 1) * pageSize.value + 1,
  };
  api.get("/needs", {
    params: queryParams,
  })
    .then(({ data }) => {
      needData.value = data.data;
      totalNeeds.value = data.total;
      displayedNeeds.value = needData.value;
      ElMessage.success("加载成功");
    }).catch(({ response, request }) => {
      if (response) {
        ElMessage.error(`需求列表加载失败，状态码：${response.status}`);
      }
    });
}

const votes = (id) => {
  //todo
}

onMounted(fetchNeeds);

</script>

<template>
  <el-main>
    <el-row>
      <el-col :span="22">
        <!-- 列表筛选区 -->
        <el-form :model="form" :inline="true" @submit.native.prevent="submitForm">
          <el-form-item label="搜索">
            <el-input v-model="form.keyword" placeholder="请输入需求名称或目标网址"></el-input>
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
        <el-button @click="$router.push('/need_upload')">发布需求</el-button>
      </el-col>
    </el-row>

    <el-row justify="center" align="middle">
      <el-col :span="18">
        <el-card class="script-card" v-for="need in displayedNeeds" :key="need.id">
          <template #header>
            <h3 class="script-name">
              <router-link :to="`/need_details/${need.id}`">{{ need.name }}</router-link>
            </h3>
          </template>
          <div class="script-info">
            <el-text tag="p" class="mx-1">{{ need.description }}</el-text>
            <div class="script-metadata">
              <el-text tag="p">发布者：{{ need.author }}</el-text>
              <el-text tag="p">{{ new Date(need.create_time).toLocaleDateString() }}</el-text>
              <el-text tag="p">得票数：{{ need.votes || 0 }}</el-text>
              <el-button type="primary" @click="votes(need.id)">投票</el-button>
            </div>
          </div>
        </el-card>
        <!-- 分页控件 -->
        <el-pagination layout="prev, pager, next" :total="totalNeeds" v-model:current-page="currentPage" prev-text="上一页"
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

.script-metadata {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}
</style>