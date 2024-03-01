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
                   Already have an account? <RouterLink to="/login" class="underline">Click in here</RouterLink> to log in. 
                </p>

            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6">
                    <div>
                        <label>Name</label><br>
                        <input type="text" placeholder="Your name" class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Email</label><br>
                        <input type="email" placeholder="Your email" class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Password</label><br>
                        <input type="password" placeholder="Your password" class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Repeat Password</label><br>
                        <input type="password" placeholder="Repeat password" class="w-full mt-2 px-6 py-4 border border-gray-200 rounded-lg">
                    </div>
                    <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</button>
                </form>
            </div>
        </div>
    </div>
</template>