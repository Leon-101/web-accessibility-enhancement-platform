<script setup>
import { ref } from 'vue';
import api from '../api';
import { ElMessage, ElSpace } from 'element-plus';
import { useRouter } from "vue-router"
import { useUserStore } from '../store/user';

const router = useRouter();
const userStore = useUserStore();

const needName = ref("");
const needDesc = ref('');

async function submit(e) {
	api.post('/needs/upload', {
		name: needName.value,
		description: needDesc.value,
		author: userStore.user.value?.username,
	})
		.then(() => {
			ElMessage.success("发布成功！");
			router.push("/needs");
		})
		.catch(({ response }) => {
			if (response) {
				ElMessage.error("发布失败，请检查您输入的内容。");
			}
		});

}

</script>
  
<template>
	<el-main>
		<div class="script-upload">
			<el-space size="default" fill>
				<h2>发布需求</h2>
				<el-input placeholder="在这里填写需求标题" v-model="needName"></el-input>
				<el-input type="textarea" :rows="10" placeholder="在这里填写需求描述" v-model="needDesc"></el-input>
				<div>
					<el-button type="primary" @click="submit">发布</el-button>
				</div>
			</el-space>
		</div>
	</el-main>
</template>
  
<style scoped>
h2 {
	font-weight: bold;
	font-size: 1.5em;
	margin-bottom: 1em;
}

.script-upload {
	margin: 20px;
}
</style>
  