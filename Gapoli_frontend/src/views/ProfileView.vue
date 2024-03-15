<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                    class="mb-6 rounded-full">

                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-between">
                    <RouterLink :to="{ 'name': 'friends', params: { id: user.id } }" class="text-xs text-gray-500">
                        {{ user.friends_count }} {{ user.friends_count == 1 ? 'friend' : 'friends' }}
                    </RouterLink>
                    <p class="text-xs text-gray-500">23 posts</p>
                </div>
                <div v-if="userStore.user.id !== user.id" class="mt-6">
                    <button
                        class="inline-block py-3 px-4 bg-purple-600 text-white rounded-lg"
                        @click="sendFriendshipRequest">
                        {{ friendshipButtonText }}
                    </button>
                </div>
            </div>
            <div class="mt-4">
                    <button v-if="userStore.user.id === user.id"
                        class="w-full py-3 px-4 bg-red-600 text-white rounded-lg"
                        @click="logout">
                        Logout
                    </button>
                </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div v-if="userStore.user.id === user.id" class="p-2 bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">
                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="What are you looking for today?"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <a href="#" class="inline-block py-4 px-6 bg-sky-600 text-white rounded-lg">Attach</a>
                        <button href="#"
                            class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
            </div>

            <!-- <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="mb-6 flex items-center justify-between">

                    <div class="flex items-center space-x-6">
                        <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                            class="w-[40px] rounded-full">
                        <p><strong>Hulk Smash</strong></p>
                    </div>

                    <div class="text-gray-600">2 minutes ago</div>

                </div>

                <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                    class="rounded-lg w-full">

                <div class="my-6 flex justify-between">
                    <div class="flex space-x-6">
                        <div class="flex items-center space-x-2">

                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                            </svg>
                            <span class="text-gray-500 text-xs">11111 likes</span>

                        </div>

                        <div class="flex items-center space-x-2">

                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 0 1-.923 1.785A5.969 5.969 0 0 0 6 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337Z" />
                            </svg>
                            <span class="text-gray-500 text-xs">122 comments</span>

                        </div>
                    </div>

                    <div>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" />
                        </svg>
                    </div>

                </div>
            </div> -->


            <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" v-bind:key="post.id">
                <FeedItem v-bind:post="post" />
            </div>

        </div>

        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />
            <Trends />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import { useUserStore } from '@/stores/user';
import { useToastStore } from '@/stores/toast' 

export default {
    name: 'ProfileView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore,
        }
    },

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
    },

    data() {
        return {
            posts: [],
            body: '',
            user: '',
            friendshipButtonText: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: {
        "$route.params.id": {
            handler: function () {
                this.getFeed()
            },
            deep: true,
            immediate: true,
        },
    },

    methods: {

        sendFriendshipRequest() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`)
                .then(Response => {
                    if (Response.data.message === 'canceled') { //when you send a request and you are sender of it
                        this.friendshipButtonText = 'friendship request'
                        this.toastStore.showToast(5000, 'you canceled sending friendship request', 'bg-emerald-500')
                    }
                    else if (Response.data.message === 'canceled_friendship') { //when you send a request and you are sender of it
                        this.friendshipButtonText = 'friendship request'
                        this.toastStore.showToast(5000, 'you canceled friendship', 'bg-emerald-500')
                    }
                    else if(Response.data.message === 'accepted'){ // when second user also request for the friendship
                        this.friendshipButtonText = 'cancel friendship request'
                        this.toastStore.showToast(5000, 'You are friends now 🤩', 'bg-emerald-500')
                    }
                    else { //when there is not any request between the user
                        this.friendshipButtonText = 'cancel friendship request'
                        this.toastStore.showToast(5000, 'your friendship reqeust has been sent 👌', 'bg-emerald-500')
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getFeed() {
            axios
                .get(`/api/post/profile/${this.$route.params.id}/`)
                .then(Response => {
                    this.posts = Response.data.post
                    this.user = Response.data.user
                    this.friendshipButtonText = Response.data.friendshipButtonText
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        submitForm() {
            console.log('body is ', this.body)

            axios
                .post('/api/post/create/', { 'body': this.body })
                .then(Response => {
                    console.log('data from back', Response.data)
                    this.posts.unshift(Response.data)
                    this.body = ''
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        logout() {
            this.userStore.removeToken()
            this.$router.push('/login')
        }
    }
}
</script>