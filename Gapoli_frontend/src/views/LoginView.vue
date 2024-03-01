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
                   Don't have an account? <RouterLink to="/signup" class="underline">Click in here</RouterLink> to create one. 
                </p>

            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6">
                    <div>
                        <label>Email</label><br>
                        <input type="email" placeholder="Your email" class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Password</label><br>
                        <input type="password" placeholder="Your password" class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Log in</button>
                </form>
            </div>
        </div>
    </div>
</template>