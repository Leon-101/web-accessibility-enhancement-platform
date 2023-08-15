import axios from 'axios'

export default axios.create({
	baseURL: '/api',
	timeout: 30000,
	headers: {
		'Content-Type': 'application/json',
	}
});
