import axios from 'axios'

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
	return response;
}, function (error) {
	console.error(error);
	return Promise.reject(error);
});

export default api;
