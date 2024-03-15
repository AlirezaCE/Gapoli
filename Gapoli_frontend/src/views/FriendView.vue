<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                    class="mb-6 rounded-full">

                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-between">
                    <p class="text-xs text-gray-500">
                        {{ user.friends_count }} {{ user.friends_count == 1 ? 'friend' : 'friends' }}
                    </p>
                    <p class="text-xs text-gray-500">23 posts</p>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">

            <div v-if="requests.length > 0" class="p-4 bg-white border border-gray-200 rounded-lg">
                <h1
                    class="text-center bg-gradient-to-r from-sky-300 to-blue-400 rounded-lg px-6 py-4 text-lg font-semibold text-white ">
                    Friendship requests</h1>
                <div class="p-4 bg-gray-200 border border-gray-300 text-center rounded-lg my-4"
                    v-for="(request, index) in requests" v-bind:key="request.id" v-show="!request.hide">
                    <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                        class="mb-6 rounded-full mx-auto w-[140px]">

                    <p><strong>
                            <RouterLink :to="{ 'name': 'profile', params: { 'id': request.sender.id } }">
                                {{ request.sender.name }}
                            </RouterLink>
                        </strong></p>

                    <div class="mt-6 flex space-x-8 justify-between">
                        <p class="text-xs text-gray-500">
                            {{ request.sender.friends_count }} {{ request.sender.friends_count == 1 ? 'friend' : 'friends' }}
                        </p>
                        <p class="text-xs text-gray-500">23 posts</p>
                    </div>

                    <div class="mt-6 space-x-4">
                        <button class="inline-block py-3 px-4 bg-purple-600 text-white rounded-lg"
                            @click="handleRequest('accepted', request.sender.id, request.sender.name, index)">
                            Accept
                        </button>
                        <button class="inline-block py-3 px-4 bg-red-500 text-white rounded-lg"
                            @click="handleRequest('rejected', request.sender.id, request.sender.name, index)">
                            Reject
                        </button>
                    </div>
                </div>
                <hr>
            </div>



            <div v-if="friends.length > 0"
                class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-3 gap-4">
                <div class="p-4 bg-gray-100 border border-gray-200 text-center rounded-lg" v-for="friend in friends"
                    v-bind:key="friend.id">
                    <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                        class="mb-6 rounded-full">

                    <p><strong>
                            <RouterLink :to="{ 'name': 'profile', params: { 'id': friend.id } }">
                                {{ friend.name }}
                            </RouterLink>
                        </strong></p>

                    <div class="mt-6 flex space-x-4 justify-between">
                        <p class="text-xs text-gray-500">
                            {{ friend.friends_count }} {{ friend.friends_count == 1 ? 'friend' : 'friends' }}
                        </p>
                        <p class="text-xs text-gray-500">23 posts</p>
                    </div>
                </div>
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
import { useToastStore } from '@/stores/toast' 

export default {
    name: 'FriendView',

    setup() {
        const toastStore = useToastStore()

        return {
            toastStore,
        }
    },

    components: {
        PeopleYouMayKnow,
        Trends,
    },

    data() {
        return {
            user: {},
            friends: [],
            requests: [],
        }
    },

    mounted() {
        this.getFriends()
    },

    methods: {
        getFriends() {
            axios
                .get(`/api/friends/${this.$route.params.id}/`)
                .then(Response => {
                    this.user = Response.data.user
                    this.friends = Response.data.friends
                    this.requests = Response.data.requests
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        handleRequest(status, sender_id, sender_name, index) {
            axios
                .post(`/api/friends/${sender_id}/${status}/`)
                .then(Response => {
                    if (Response.data.message === 'accepted') {
                        this.toastStore.showToast(5000, `${sender_name} is your friend now 😄`, 'bg-emerald-500')
                        this.friends.unshift(Response.data.sender)    
                    }
                    else {
                        this.toastStore.showToast(5000, 'request for friendship rejected', 'bg-red-500')
                    }

                    this.requests[index].hide = true // hide the buttons when it's clicked
                    this.requests.length = this.requests.length -1
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    },

}
</script>