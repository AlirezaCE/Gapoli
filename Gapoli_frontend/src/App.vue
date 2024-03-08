<template>

	<nav class="py-10 px-8 border-b border-gray-200" style="box-shadow: 0 2px 4px 0 rgba(112, 8, 98, 0.106)">
		<div class="max-w-7xl mx-auto">
			<div class="flex items-center justify-between">
				<div class="menu-left">
					<a href="#" class="text-xl">Gapoli</a>
				</div>

				<div class="menu-center flex space-x-12" v-if="userStore.user.isAuthenticated">
					<a href="#" class="text-purple-700">
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
							stroke="currentColor" class="w-6 h-6">
							<path stroke-linecap="round" stroke-linejoin="round"
								d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
						</svg>
					</a>

					<a href="#">
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
							stroke="currentColor" class="w-6 h-6">
							<path stroke-linecap="round" stroke-linejoin="round"
								d="M8.625 12a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 0 1-2.555-.337A5.972 5.972 0 0 1 5.41 20.97a5.969 5.969 0 0 1-.474-.065 4.48 4.48 0 0 0 .978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25Z" />
						</svg>
					</a>

					<a href="#">
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
							stroke="currentColor" class="w-6 h-6">
							<path stroke-linecap="round" stroke-linejoin="round"
								d="M14.857 17.082a23.848 23.848 0 0 0 5.454-1.31A8.967 8.967 0 0 1 18 9.75V9A6 6 0 0 0 6 9v.75a8.967 8.967 0 0 1-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 0 1-5.714 0m5.714 0a3 3 0 1 1-5.714 0" />
						</svg>
					</a>

					<a href="#">
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
							stroke="currentColor" class="w-6 h-6">
							<path stroke-linecap="round" stroke-linejoin="round"
								d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
						</svg>
					</a>
				</div>

				<div class="menu-right">
				
					<template v-if="userStore.user.isAuthenticated">
						<RouterLink :to="{'name': 'profile', params:{'id': userStore.user.id}}">
							<img style="width: 50px;"
								src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
								class="rounded-full">
						</RouterLink>
					</template>

					<template v-else>
						<RouterLink to="/login" class="mr-4 py-4 px-6 text-white bg-sky-600 rounded-lg">Login</RouterLink>
						<RouterLink to="/signup" class="py-4 px-6 text-white bg-purple-600 rounded-lg">SignUp</RouterLink>
					</template>
				
				</div>
			</div>
		</div>
	</nav>

	<main class="px-8 py-6 bg-gray-100">
		<RouterView />
	</main>

	<Toast />
</template>

<script>
import axios from 'axios';
import Toast from '@/components/Toast.vue'
import { useUserStore } from '@/stores/user';

export default {
	setup() {
		const userStore = useUserStore()

		return {
			userStore
		}
	},

	components: {
		Toast
	},

	beforeCreate() {
		this.userStore.initStore()

		const token = this.userStore.user.access
		if (token) {
			axios.defaults.headers.common["Authorization"] = "Bearer " + token;
		}
		else {
			axios.defaults.headers.common["Authorization"] = "";
		}
	}
}
</script>