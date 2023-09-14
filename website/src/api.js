import axios from 'axios'
import { ElMessage } from 'element-plus';
import testDataOfNeeds from "./test_data/needs"

const useTestData = true; // 请求错误时是否返回测试数据

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
		//返回模拟数据
		if (useTestData && response.config.url === "/needs") {
			return {
				status: 200,
				data: testDataOfNeeds,
			};
		}

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
