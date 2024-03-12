<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-3 space-y-4">
            <form v-on:submit.prevent="submitForm" class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="p-4 flex space-x-4">

                    <input v-model="query" type="search" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Search">
                    <button href="#" class="inline-block py-3 px-4 bg-purple-500 text-white rounded-full">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                        </svg>
                    </button>

                </div>
            </form>

            <div 
                v-if="users.length > 0"
                class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4"
            >
                <div 
                    class="p-4 bg-gray-100 border border-gray-200 text-center rounded-lg"
                    v-for="user in users"
                    v-bind:key="user.id"  
                >
                    <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                        class="mb-6 rounded-full">

                    <p><strong>
                        <RouterLink :to="{'name': 'profile', params:{'id': user.id}}">
                            {{ user.name }}
                        </RouterLink>
                    </strong></p>

                    <div class="mt-6 flex space-x-8 justify-between">
                        <p class="text-xs text-gray-500">
                            {{ user.friends_count }} {{ user.friends_count == 1 ? 'friend' : 'friends' }}
                        </p>
                        <p class="text-xs text-gray-500">23 posts</p>
                    </div>
                </div>
            </div>




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

export default {
    name: 'SearchView',

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
    },

    data() {
        return {
            query: '',
            users: [],
            posts: [],
        }
    },

    methods: {
        submitForm() {
            console.log('submitform', this.query) 

            axios
                .post('/api/search/', { query: this.query })
                .then(Response => {
                    console.log('response is', Response.data)
                    
                    this.users = Response.data.users
                    this.posts = Response.data.posts
                })
                .catch(error => {
                    console.log("error: ", error)
                })

        }
    },
}
</script>