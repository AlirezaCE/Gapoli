<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Sign up</h1>

                <p class="mb-6 text-gray-600">
                    Welcome To Gapoli App 😉<br>
                    Create Your Account And Join Our Community.
                </p>
                <p class="font-bold">
                    Already have an account? <RouterLink to="/login" class="underline">Click in here</RouterLink> to log
                    in.
                </p>

            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Name</label><br>
                        <input v-model="form.name" type="text" placeholder="Your name"
                            class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Email</label><br>
                        <input v-model="form.email" type="email" placeholder="Your email"
                            class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Password</label><br>
                        <input v-model="form.password1" type="password" placeholder="Your password"
                            class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Repeat Password</label><br>
                        <input v-model="form.password2" type="password" placeholder="Repeat password"
                            class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-500 text-white p-6 rounded-lg">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>
                    
                    <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast' 

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.name === '') {
                this.errors.push('Your name could not be empty.')
            }

            if (this.form.email === '') {
                this.errors.push('Your email could not be empty.')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password could not be empty.')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('password1 and password2 are not match')
            }


            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(Response => {
                        if (Response.data.status === 'success') {
                            this.toastStore.showToast(5000, 'You registered in Gapoli successfuly 😊👌 now log in.', 'bg-emerald-500')

                            this.form.name = ''
                            this.form.email = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        }
                        else {
                            this.toastStore.showToast(5000, 'Something went wrong try again 😉', 'bg-red-500')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}


</script>