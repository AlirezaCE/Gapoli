<template>
    <div class="max-w-7xl mx-auto grid grid-cols-12 gap-4">

        <div class="main-center col-span-8 space-y-4">
            <div v-if="post.id" class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="mb-6 flex items-center justify-between">

                    <div class="flex items-center space-x-6">
                        <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                            class="w-[40px] rounded-full">

                        <p><strong>
                                <RouterLink :to="{ 'name': 'profile', params: { 'id': post.created_by.id } }">
                                    {{ post.created_by.name }}
                                </RouterLink>
                            </strong></p>
                    </div>

                    <div class="text-gray-600">{{ post.since_created }} ago</div>

                </div>

                <p>{{ post.body }}</p>

                <div class="my-6 flex justify-between">
                    <div class="flex space-x-6">
                        <div class="flex items-center space-x-2">

                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6" @click="like_post(post.id)">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                            </svg>
                            <span class="text-gray-500 text-xs">{{ post.like_count }} {{ post.like_count <= 1 ? 'Like'
                : 'Likes' }}</span>

                        </div>

                        <div class="flex items-center space-x-2">
                            <RouterLink :to="{ 'name': 'post_detail', params: { 'id': post.id } }">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 0 1-.923 1.785A5.969 5.969 0 0 0 6 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337Z" />
                                </svg>
                            </RouterLink>
                            <span class="text-gray-500 text-xs">{{ post.comment_count }} {{ post.comment_count <= 1
                ? 'Comment' : 'Comments' }}</span>

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
            </div>
        </div>

        <div class="main-center col-span-4 space-y-4">
            <div class="p-2 bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="comment" method="post">
                    <div class="p-4 flex items-center justify-between space-x-3">
                        <textarea v-model="text" class="p-4 w-full h-14 bg-gray-100 rounded-br-lg rounded-tl-lg"
                            placeholder="Comment">
                        </textarea>

                        <button class="p-1 bg-purple-500 rounded-l-lg rounded-br-lg ">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6 text-gray-100">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M15.75 17.25 12 21m0 0-3.75-3.75M12 21V3" />
                            </svg>
                        </button>
                    </div>
                </form>
                <div class='mx-4 my-2 ' v-for="(comment, index) in post.comment" v-bind:key="comment.id"
                    v-show="!comment.hide">
                    <div class="mx-auto flex">
                        <div class="w-full ">
                            <p class="p-4 bg-white border border-gray-200 rounded-br-lg rounded-l-lg">{{ comment.text }}
                            </p>
                            <div class="flex justify-between text-xs text-gray-400">
                                <p>{{ comment.since_created }}</p>
                                <p>{{ comment.created_by.name }}</p>
                            </div>
                        </div>
                        <button v-if="userStore.user.id === comment.created_by.id" class="rounded-full ml-3 mt-3 bg-red-500 w-10 h-10 items-center flex justify-center">
                            <svg @click="delete_comment(comment.id, index)" xmlns="http://www.w3.org/2000/svg"
                                fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                                class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
                            </svg>
                        </button>
                    </div>
                </div>

            </div>
        </div>

        <div class="main-right col-span-3 space-y-4">
            <!-- <PeopleYouMayKnow />
            <Trends /> -->

        </div>
    </div>
</template>

<script>
import axios from 'axios'
// import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
// import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import { useUserStore } from '@/stores/user';

export default {
    name: 'PostDetailView',

    setup() {
        const userStore = useUserStore()

        return {
            userStore,
        }
    },

    components: {
        // PeopleYouMayKnow,
        // Trends,
        FeedItem,
    },

    data() {
        return {
            post: {},
            text: '',
        }
    },

    mounted() {
        this.getPostDetail()
    },

    methods: {
        getPostDetail() {
            axios
                .get(`/api/post/detail/${this.$route.params.id}/`)
                .then(Response => {
                    this.post = Response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        comment() {
            console.log('comment is ', this.text)

            axios
                .post(`/api/post/comment/${this.$route.params.id}/`, { 'text': this.text })
                .then(Response => {
                    console.log('data from back', Response.data)
                    if (Response.data.comment.text === this.text) {
                        this.post.comment.unshift(Response.data.comment)
                        this.post.comment_count += 1
                        this.text = ''
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        delete_comment(comment_id, index) {
            axios
                .post(`/api/post/comment/delete/${this.$route.params.id}/${comment_id}/`)
                .then(Response => {
                    console.log('data from back', Response.data)
                    if (Response.data.message === "deleted") {
                        this.post.comment[index].hide = true
                        this.post.comment_count -= 1
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>