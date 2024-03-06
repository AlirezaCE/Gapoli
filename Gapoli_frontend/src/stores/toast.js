import { defineStore } from "pinia"

export const useToastStore = defineStore({
    id: 'toast',

    state: () => ({
        ms: 0,
        message: '',
        classes: '',
        isVisible: false 
    }),

    actions: {
        showToast(ms, message, classes){
            this.ms = parseInt(ms)
            this.message = message
            this.classes = classes
            this.isVisible = true

            setTimeout(() => {
                console.log('11111111111')
                this.classes += ' -translate-y-28'
            }, 10)

            setTimeout(() => {
                console.log('222222222222')
                this.classes = this.classes.replace(' -translate-y-28',' -translate-y-88')
            }, this.ms -1500)

            setTimeout(() => {
                console.log('222222222222')
                this.classes = this.classes.replace('-translate-y-88','')
            }, this.ms -50)
            
            setTimeout(() => {
               this.isVisible = false 
            }, this.ms);
        }
    }
})