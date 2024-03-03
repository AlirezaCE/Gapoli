<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-3 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="p-4 flex space-x-4">

                    <input type="search" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Search">
                    <a href="#" class="inline-block py-3 px-4 bg-purple-500 text-white rounded-full">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                        </svg>
                    </a>

                </div>
            </div>

            <div class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4">
                <div class="p-4 bg-gray-100 border border-gray-200 text-center rounded-lg">
                    <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg" class="mb-6 rounded-full">
                    
                    <p><strong>Hulk Smash</strong></p>
                    
                    <div class="mt-6 flex space-x-8 justify-between">
                        <p class="text-xs text-gray-500">125 friends</p>
                        <p class="text-xs text-gray-500">23 posts</p>
                    </div>
                </div>

                <div class="p-4 bg-gray-100 border border-gray-200 text-center rounded-lg">
                    <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg" class="mb-6 rounded-full">
                    
                    <p><strong>Hulk Smash</strong></p>
                    
                    <div class="mt-6 flex space-x-8 justify-between">
                        <p class="text-xs text-gray-500">125 friends</p>
                        <p class="text-xs text-gray-500">23 posts</p>
                    </div>
                </div>

                <div class="p-4 bg-gray-100 border border-gray-200 text-center rounded-lg">
                    <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg" class="mb-6 rounded-full">
                    
                    <p><strong>Hulk Smash</strong></p>
                    
                    <div class="mt-6 flex space-x-8 justify-between">
                        <p class="text-xs text-gray-500">125 friends</p>
                        <p class="text-xs text-gray-500">23 posts</p>
                    </div>
                </div>

                <div class="p-4 bg-gray-100 border border-gray-200 text-center rounded-lg">
                    <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg" class="mb-6 rounded-full">
                    
                    <p><strong>Hulk Smash</strong></p>
                    
                    <div class="mt-6 flex space-x-8 justify-between">
                        <p class="text-xs text-gray-500">125 friends</p>
                        <p class="text-xs text-gray-500">23 posts</p>
                    </div>
                </div>

                <div class="p-4 bg-gray-100 border border-gray-200 text-center rounded-lg">
                    <img src="https://img.favpng.com/8/7/15/hulk-superhero-icon-png-favpng-j7ZaifhXrReBKUiFaaMYQ22JJ.jpg" class="mb-6 rounded-full">
                    
                    <p><strong>Hulk Smash</strong></p>
                    
                    <div class="mt-6 flex space-x-8 justify-between">
                        <p class="text-xs text-gray-500">125 friends</p>
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
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'

export default{
    name: 'SearchView',
    components: {
        PeopleYouMayKnow,
        Trends,
    }
}
</script>