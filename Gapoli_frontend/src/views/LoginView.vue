<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Log in</h1>

                <p class="mb-6 text-gray-600">
                    Welcome back! 👋😊<br>
                    Please enter your credentials to log in.
                </p>
                <p class="font-bold">
                    Don't have an account? <RouterLink to="/signup" class="underline">Click in here</RouterLink> to
                    create one.
                </p>

            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Email</label><br>
                        <input v-model="form.email" type="email" placeholder="Your email"
                            class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Password</label><br>
                        <input v-model="form.password" type="password" placeholder="Your password"
                            class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Log in</button>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-500 text-white p-6 rounded-lg">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            errors: [],
        }
    },

    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your email could not be empty.')
            }

            if (this.form.password === '') {
                this.errors.push('Your password could not be empty.')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/login/', this.form)
                    .then(Response => {
                        this.userStore.setToken(Response.data)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + Response.data.access
                    })
                    .catch(error => {
                        console.log('error', error)
                    })

                await axios
                    .get('/api/detail/')
                    .then(Response => {
                        this.userStore.setUserInfo(Response.data)

                        this.$router.push('/feed')
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}


</script>