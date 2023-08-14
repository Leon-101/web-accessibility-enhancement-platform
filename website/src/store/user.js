import { reactive, computed } from 'vue';
import api from '../api';

const state = reactive({
	user: JSON.parse(sessionStorage.getItem("user") || localStorage.getItem("user")),
});

const getters = {
	user: () => state.user,
	loggedIn: () => !!state.user,
};

const actions = {
	login: (loginInfo) => {
		const { username, password, remember } = loginInfo;
		return api.post("/users/login", {
			username,
			password,
		}).then(({ data }) => {
			state.user = {
				username,
				token: data.access_token,
			};
			if (remember) {
				localStorage.setItem("user", store.user);
			}
			sessionStorage.setItem("user", store.user);
		});
	},
	logout: () => {
		localStorage.removeItem("user");
		sessionStorage.removeItem("user");
		state.user = null;
	},
	register: (registerInfo) => {
		const { username, email, password } = registerInfo;
		return api.post("/users/register", {
			username,
			email,
			password,
		}).then(({ data }) => {

		})
	},
};

for (const key in getters) {
	getters[key] = computed(getters[key]);
}

export function useUserStore() {
	return {
		...getters,
		...actions,
	}
}