<script setup>
import { ref } from 'vue';
import api from '../api';
import { ElMessage } from 'element-plus';

const scriptCode = ref('');

scriptCode.value = `// ==UserScript==
// @name         XXX网站无障碍优化
// @namespace    http://a11y.org/
// @version      0.1
// @description  优化XXX网站的无障碍问题
// @author       YYY
// @match        https://xxx.com/*
// @grant        none
// ==/UserScript==

(function() {
    // Your code here...
})();
`;

async function submitScript(e) {
	const blob = new Blob([scriptCode.value], { type: 'text/plain' });
	const formData = new FormData();
	formData.append('script_file', blob, 'script.js'); // 'script_file' 是后端接受文件的字段名

	api.post('/scripts/upload', formData, {
		headers: {
			'Content-Type': 'multipart/form-data',
		},
	})
		.then(() => {
			ElMessage.success("上传成功！");
		})
		.catch(({ response, request }) => {
			if (response) {
				ElMessage.error("上传失败，请检查您的代码格式。");
			}
		});

}

</script>
  
<template>
	<el-main>
		<div class="script-upload">
			<h2>上传脚本</h2>
			<el-input type="textarea" :rows="20" placeholder="在这里输入你的脚本代码" v-model="scriptCode"></el-input>
			<el-button type="primary" @click="submitScript">上传</el-button>
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
  