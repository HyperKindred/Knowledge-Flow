<template>
    <div class="loader-wrapper" v-if="isVisible">
        <div class="loader1"></div>
        <div class="loader2">
            <span class="loader-inner"></span>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { mainStore } from '../store/index.ts';


const isVisible = ref(false);
const store = mainStore();

if (store.isOpen) {
    isVisible.value = true;
}

setTimeout(() => {
    if (!store.isOpen) {
        isVisible.value = false;
    }
    watch(() => store.isOpen, (newVal) => {
        if (!newVal) {
            isVisible.value = false;
        }
    });
}, 2000);
</script>

<style scoped>
.loader-wrapper {
    height: 100%;
    width: 100%;
    position: fixed;
    left: 0;
    top: 0;
    background-color: var(--openbackColor);
    z-index: 2;
}

.loader1 {
    display: inline-block;
    width: 50px;
    height: 50px;
    position: fixed;
    border: 4px solid var(--openColor);
    left: 47%;
    top: 48%;
    transform: translate(-50%, -50%);
    animation: loader 2s infinite ease;
}

.loader2 {
    display: inline-block;
    width: 50px;
    height: 50px;
    position: fixed;
    border: 4px solid var(--openColor);
    left: 48.5%;
    top: 51%;
    transform: translate(-50%, -50%);
    animation: loader 2s infinite ease;
    background-color: var(--openbackColor);
}

.loader-inner {
    vertical-align: top;
    display: inline-block;
    width: 100%;
    background-color: var(--openColor);
    animation: loader-inner 2s infinite ease-in;
}

@keyframes loader {
    0% {
        transform: rotate(0deg);
    }
    
    25% {
        transform: rotate(180deg);
    }
    
    50% {
        transform: rotate(180deg);
    }
    
    75% {
        transform: rotate(360deg);
    }
    
    100% {
        transform: rotate(360deg);
    }
}

@keyframes loader-inner {
    0% {
        height: 0%;
    }
    
    25% {
        height: 0%;
    }
    
    50% {
        height: 100%;
    }
    
    75% {
        height: 100%;
    }
    
    100% {
        height: 0%;
    }
}
</style>