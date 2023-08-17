import axios from 'axios'
import { ElMessage } from 'element-plus';

const api = axios.create({
	baseURL: '/api',
	timeout: 30000,
	headers: {
		'Content-Type': 'application/json',
		// 'Content-Type': 'application/x-www-form-urlencoded',
	}
});

// 添加响应拦截器
api.interceptors.response.use(function (response) {
	return Promise.resolve(response);
}, function (error) {
	console.error(error);
	const { response, request } = error;
	if (response) {
		if (response.status >= 500) {
			ElMessage.error(`服务器错误：${response.status}`);
		}
	} else if (request) {
		ElMessage.error("无法连接到服务器");
	} else {
		ElMessage.error("请求出错");
	}
	return Promise.reject(error);
});

export default api;
