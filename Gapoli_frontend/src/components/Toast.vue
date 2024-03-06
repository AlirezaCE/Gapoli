<script setup>
import { useToastStore } from '@/stores/toast'

const store = useToastStore()


</script>

<template>
    <div 
        v-if="store.isVisible"
        class="transition ease-in-out delay-500 duration-500 px-6 py-7 fixed top-full right-8 rounded-lg"
        :class="store.classes"    
    >
        {{ store.message }}   
    </div>
</template>