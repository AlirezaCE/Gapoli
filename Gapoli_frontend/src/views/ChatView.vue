<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="space-y-4">
                    <div v-for="conversation in conversations" v-bind:key="conversation.id"
                        class="flex items-center justify-between hover:bg-gray-100 transition duration-300 ease-in-out">
                        <div class="flex items-center space-x-2">
                            <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                                class="rounded-full w-10 h-10">
                            <div>
                                <p v-for="user in conversation.users" v-bind:key="user.id" class="text-xs">
                                    <strong v-on:click="setActiveConversation(conversation)"
                                        v-if="userStore.user.id !== user.id" class="cursor-pointer">
                                        <div v-if="this.active_conversation.id === conversation.id"
                                            class="text-purple-500">
                                            {{ user.name }}
                                        </div>
                                        <div v-else class="text-blue-500">
                                            {{ user.name }}
                                        </div>
                                    </strong>
                                </p>
                                <p class="text-xs text-gray-500">{{ conversation.users.length }} participants</p>
                            </div>
                        </div>
                        <span class="text-xs text-gray-500">{{ conversation.since_modified }} ago</span>
                    </div>
                </div>
            </div>
        </div>


        <div class="main-center col-span-3 space-y-4">

            <div class="bg-white border border-gray-200 rounded-lg">
                <div class="flex flex-col flex-grow p-4">
                    <div v-if="active_conversation.messages && active_conversation.messages.length === 0">
                        <p class="flex justify-center items-center">say hi 👋😊</p>
                    </div>
                    <div v-else>
                        <div v-for="message in this.active_conversation.messages" v-bind:key="message.id">
                            <div v-if="message.sender.id === userStore.user.id"
                                class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                                <div>
                                    <div class="bg-blue-600 text-white p-4 rounded-l-lg rounded-br-lg">
                                        <p class="text-sm">
                                            {{ message.body }}
                                        </p>
                                    </div>
                                    <span class="text-xs text-gray-500 leading-none">{{ message.since_created }}
                                        ago</span>
                                </div>
                                <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                    <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                                        class="rounded-full w-[40px]">
                                </div>
                            </div>

                            <div v-else class="flex w-full mt-2 space-x-3 max-w-md">
                                <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                    <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg"
                                        class="rounded-full w-[40px]">
                                </div>
                                <div>
                                    <div class="bg-purple-400 p-4 rounded-r-lg rounded-bl-lg">
                                        <p class="text-sm">
                                            {{ message.body }}
                                        </p>
                                    </div>
                                    <span class="text-xs text-gray-500 leading-none">{{ message.since_created }}
                                        ago</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


            <div class="p-2 bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="sendMessage()" method="post">
                    <div class="p-4 max-w-7xl mx-auto grid grid-cols-10 gap-4">
                        <div class="col-span-9">
                            <textarea v-model="text"
                                class="p-4 w-full bg-gray-100 rounded-lg border border-gray-300 focus:outline-none focus:border-purple-500"
                                placeholder="Message"></textarea>
                        </div>
                        <div class="col-span-1 flex items-center justify-center">
                            <button type="submit"
                                class="inline-block py-2 px-4 bg-blue-500 text-white rounded-full hover:bg-blue-600 focus:outline-none focus:bg-blue-600">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </form>
            </div>

        </div>
    </div>
</template>


<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import { useToastStore } from '@/stores/toast'

export default {
    name: 'ChatView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore,
        }
    },

    data() {
        return {
            conversations: [],
            active_conversation: {},
            text: '',
        }
    },

    mounted() {
        this.getConversations()
    },

    methods: {
        getConversations() {
            axios
                .get(`/api/chat/`)
                .then(Response => {
                    this.conversations = Response.data;

                    if (this.conversations.length) {
                        this.active_conversation = this.conversations[0]
                        this.getMessages(this.active_conversation.id)
                    }
                })
                .catch(error => {
                    console.log(error);
                })
        },

        getMessages() {
            let id_type = 'conversation'

            if (this.$route.params.reciver_id){
                this.active_conversation.id = this.$route.params.reciver_id
                id_type = 'reciver'
            }

            axios
                .get(`/api/chat/${this.active_conversation.id}/${id_type}/`)
                .then(Response => {
                    console.log('aaaaaaaa', Response.data);
                    this.active_conversation = Response.data;
                })
                .catch(error => {
                    console.log(error);
                })
        },

        sendMessage() {
            if (this.active_conversation.id) {
                axios
                    .post(`/api/chat/send/${this.active_conversation.id}/`, { 'body': this.text })
                    .then(Response => {
                        console.log(Response.data);
                        this.active_conversation.messages.push(Response.data)
                        this.text = ''
                    })
                    .catch(error => {
                        console.log(error);
                    })
            }
            else{
                this.toastStore.showToast(5000, 'There is no active conversation', 'bg-emerald-500')
            }
        },

        setActiveConversation(conversation) {
            this.active_conversation = conversation
            this.getMessages()
        },
    }
}
</script>