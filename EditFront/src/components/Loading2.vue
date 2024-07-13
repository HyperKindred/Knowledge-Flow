<template>
    <div class="loading-wrapper">
        <svg>
            <circle cx="45" cy="45" r="20"></circle>
        </svg>
        <div class="loading-text">正在加载中...</div>
    </div>
</template>

<style scoped>
.loading-wrapper {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: 100%;
    background-color: var(--loadingColor2);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    color: var(--titleColor);
    font-size: 15px;
    z-index: 1;
    animation: easein 0.5s;
}
@keyframes easein {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}
svg {
    position: relative;
    width: 100px;
    height: 100px;
    animation: rotate 2s linear infinite;
}
@keyframes rotate {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}
svg circle {
    width: 100%;
    height: 100%;
    fill: none;
    stroke-width: 3px;
    stroke: var(--titleColor);
    transform: translate(5px,5px);
    stroke-dasharray: 110;
    stroke-dashoffset: 110;
    animation: animate 4s linear infinite;
}
@keyframes animate {
    0%,100% {
        stroke-dashoffset: 110;
    }
    50% {
        stroke-dashoffset: 0;
    }
    50.1% {
        stroke-dashoffset: 220;
    }
}
</style>