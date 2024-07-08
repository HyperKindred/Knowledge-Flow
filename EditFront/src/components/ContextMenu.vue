<template>
    <div class="container" @contextmenu="showMenu">
        <slot></slot>
        <Transition name="fade">
            <ul v-if="isVisible" class="menu" :style="menuStyle" ref="menu">
                <li class="menuitem" @click="handleTranslate">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path fill="currentColor" d="M4.076 4.216a5.04 5.04 0 0 1 2.844 0h.001c1.012.297 1.56.9 1.832 1.569c.253.62.253 1.27.253 1.661V12.5a.5.5 0 0 1-1 0v-.533a8 8 0 0 1-1.046.554c-.78.343-1.736.602-2.642.414a2.97 2.97 0 0 1-2.248-2.082c-.287-.97-.081-2.103.807-2.842c1.01-.84 2.171-1.046 3.207-1.003c.71.03 1.378.176 1.921.325c-.002-.375-.023-.791-.178-1.172c-.16-.392-.474-.776-1.187-.985a4.04 4.04 0 0 0-2.946.26a3 3 0 0 0-.208.117l-.007.005a.5.5 0 0 1-.565-.825l.002-.002l.002-.001l.006-.004l.02-.013l.065-.04q.083-.052.232-.128a5 5 0 0 1 .835-.329m1.966 3.79c-.873-.035-1.762.14-2.525.774c-.53.44-.682 1.132-.488 1.79a1.97 1.97 0 0 0 1.492 1.386c.606.126 1.332-.04 2.037-.35a7.6 7.6 0 0 0 1.448-.849V8.372c-.558-.163-1.242-.335-1.964-.365m8.428-1.339a.5.5 0 0 0-.942-.334a20 20 0 0 0-.472 1.643c-.492.032-.993.033-1.523-.002a.5.5 0 1 0-.068.997c.475.032.927.037 1.368.018a19 19 0 0 0-.249 1.551c-1.166.578-1.92 1.425-2.3 2.301c-.441 1.02-.395 2.164.25 2.853c.428.458 1.06.522 1.636.39c.42-.097.857-.304 1.277-.604q.045.099.087.205a.5.5 0 0 0 .93-.37a8 8 0 0 0-.236-.522c.792-.846 1.454-2.07 1.684-3.606c.765.262 1.275.797 1.493 1.387c.386 1.04-.035 2.547-2.109 3.47a.5.5 0 1 0 .406.913c2.426-1.078 3.255-3.072 2.64-4.73c-.364-.987-1.203-1.748-2.345-2.058L16 10a.5.5 0 1 0-1 0v.02a5.4 5.4 0 0 0-1.354.13q.083-.567.226-1.247c.739-.09 1.467-.237 2.24-.416a.5.5 0 0 0-.225-.974c-.62.144-1.199.263-1.769.348c.1-.384.232-.853.353-1.194m-3.267 6.572c.223-.517.64-1.057 1.297-1.498c-.01.633.04 1.159.13 1.612c.097.48.235.867.381 1.205c-.38.3-.754.48-1.065.551c-.384.088-.59.001-.683-.098c-.275-.295-.41-.967-.06-1.772m3.724-2.223c-.169 1.15-.612 2.08-1.147 2.764a5 5 0 0 1-.169-.623c-.097-.486-.145-1.102-.087-1.935q.06-.023.121-.043a4.6 4.6 0 0 1 1.282-.163"/></svg>
                    翻译
                </li>
                <span class="divider"></span>
                <li class="menuitem" @click="handleSummarize">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path fill="currentColor" d="M6 10.5a.5.5 0 1 1 1 0a.5.5 0 0 1-1 0m.5 1.5a.5.5 0 1 0 0 1a.5.5 0 0 0 0-1M6 14.5a.5.5 0 1 1 1 0a.5.5 0 0 1-1 0M8.5 10a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM8 12.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5m.5 1.5a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM6 2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V7.414a1.5 1.5 0 0 0-.44-1.06l-3.914-3.915A1.5 1.5 0 0 0 10.586 2zM5 4a1 1 0 0 1 1-1h4v3.5A1.5 1.5 0 0 0 11.5 8H15v8a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1zm9.793 3H11.5a.5.5 0 0 1-.5-.5V3.207z"/></svg>
                    摘要
                </li>
                <span class="divider"></span>
                <li class="menuitem" @click="handlePolish">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048"><path fill="currentColor" d="M1803 128q51 0 95 19t78 53t52 77t20 96q0 49-18 93t-54 80q-303 303-605 606t-606 606q-6 61-33 114t-69 92t-98 61t-117 23H192q-40 0-75-15t-61-41t-41-61t-15-75v-64h64q26 0 45-19t19-45q0-61 22-116t62-98t92-70t114-33q303-303 606-605t606-606q35-35 79-53t94-19M576 1435q55 24 98 67t67 98l116-116q-61-104-165-165zm-128 485q40 0 75-15t61-41t41-61t15-75t-15-75t-41-61t-61-41t-75-15t-75 15t-61 41t-41 61t-15 75q0 55-29 102t-80 71q18 19 45 19zM1886 456q34-34 34-83q0-24-9-45t-25-38t-37-25t-46-9q-49 0-83 34l-935 936q99 66 165 165z"/></svg>
                    润色
                </li>
                <span class="divider"></span>
                <li class="menuitem" @click="handleCorrect">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256"><path fill="currentColor" d="M225.91 74.79L181.22 30.1a14 14 0 0 0-19.8 0L38.1 153.41a13.94 13.94 0 0 0-4.1 9.9V208a14 14 0 0 0 14 14h168a6 6 0 0 0 0-12H110.49L225.91 94.59a14 14 0 0 0 0-19.8M93.52 210H48a2 2 0 0 1-2-2v-44.69a2 2 0 0 1 .59-1.41L136 72.49L183.52 120Zm123.9-123.9L192 111.52L144.49 64l25.41-25.41a2 2 0 0 1 2.83 0l44.69 44.68a2 2 0 0 1 0 2.83"/></svg>
                    修改病句
                </li>
                <span class="divider"></span>
                <li class="menuitem" @click="handleDelete">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path fill="currentColor" d="M5.92 2.228a.5.5 0 0 0-.84.544L9.405 9.43L7.48 12.39a3 3 0 1 0 .779.636L10 10.348l1.74 2.68a3 3 0 1 0 .779-.636zM14 17a2 2 0 1 1 0-4a2 2 0 0 1 0 4M4 15a2 2 0 1 1 4 0a2 2 0 0 1-4 0m7.192-6.489l-.596-.918l3.485-5.365a.5.5 0 0 1 .838.544z"/></svg>
                    剪切<span class="hotkey">Ctrl+X</span>
                </li>
                <li class="menuitem" @click="handleCopy">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"><path d="M16 3H4v13"/><path d="M8 7h12v12a2 2 0 0 1-2 2h-8a2 2 0 0 1-2-2z"/></g></svg>
                    复制<span class="hotkey">Ctrl+C</span>
                </li>
                <li class="menuitem" @click="handlePaste">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 2048"><path fill="currentColor" d="M1920 768v1280H896v-128H128V256h512q0-52 20-99t55-81t81-55T896 0q52 0 99 20t81 55t55 82t21 99h512v512zM512 384v128h768V384h-256v-33q0-17 1-36q0-34-3-67t-17-60t-39-43t-70-17q-44 0-69 16t-39 43t-17 60t-4 68v35q0 17 1 34zm384 1408V768h640V384h-128v256H384V384H256v1408zm896-896h-768v1024h768z"/></svg>
                    粘贴<span class="hotkey">Ctrl+V</span>
                </li>
            </ul>
        </Transition>
    </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import { mainStore } from '@/store/index.ts';

const store = mainStore();
const router = useRouter();

// 处理翻译
const handleTranslate = () => {
    router.push({ name: 'Translate' })
    .then(() => {
        store.setSelect('');
        nextTick(() => {
            store.setSelect('translate');
        });
    });
};
// 处理摘要
const handleSummarize = () => {
    router.push({ name: 'Summarize' })
    .then(() => {
        store.setSelect('');
        nextTick(() => {
            store.setSelect('summarize');
        });
    });
};
// 处理润色
const handlePolish = () => {
    store.setSelect('');
    nextTick(() => {
        store.setSelect('polish');
    });
};
// 处理修改病句
const handleCorrect = () => {
    store.setSelect('');
    nextTick(() => {
        store.setSelect('correct');
    });
};
// 处理剪切
const handleDelete = () => {
    store.setSelect('');
    nextTick(() => {
        store.setSelect('delete');
    });
};
// 处理复制
const handleCopy = () => {
    store.setSelect('');
    nextTick(() => {
        store.setSelect('copy');
    });
};
// 处理粘贴
const handlePaste = () => {
    store.setSelect('');
    nextTick(() => {
        store.setSelect('paste');
    });
};

// 定义菜单样式和菜单引用
const menuStyle = reactive({
    left: '0px',
    top: '0px',
});

const isVisible = ref(false);
const menu = ref<HTMLElement | null>(null);

// 右键点击时显示菜单
const showMenu = (e: MouseEvent) => {
    if (store.content !== '') {
        e.preventDefault();

        const { clientX, clientY } = e;

        isVisible.value = true;
        menuStyle.left = `${e.clientX}px`;
        menuStyle.top = `${e.clientY}px`;

    }
};

// 隐藏菜单
const hideMenu = () => {
    isVisible.value = false;
};

// 监听全局点击事件以隐藏菜单
onMounted(() => {
    document.addEventListener('click', hideMenu);
    // document.addEventListener('scroll', showMenu);
});
</script>
  
<style scoped>
    .container {
        display: inline-block;
        width: 100%;
        height: 100%;
    }
    .fade-enter-from, .fade-leave-to {
        opacity: 0;
    }
    .fade-enter-active {
        transition: opacity 0.2s ease;
    }
    .fade-enter-to, .fade-leave-from {
        opacity: 1;
    }
    .menu {
        position: fixed;
        width: 300px;
        height: auto;
        background-color: #2c2c2c;
        padding: 3px;
        margin: 0;
        color: #fff;
        border: 1px solid #494949;
        border-radius: 10px;
        z-index: 999;
        list-style-type: none;
    }
    .menuitem {
        padding-left: 0px;
        padding-top: 4px;
        padding-bottom: 4px;
        margin: 2px 1px;
        height: 25px;
        border-radius: 4px;
        font-size: 15.5px;
        user-select: none;
        display: flex;
        align-items: center;
    }
    .menuitem:hover {
        background-color: #484848;
    }
    .icon {
        margin-left: 10px;
        margin-right: 13px;
        width: 20px;
        height: 25px;
    }
    .divider {
        display: block;
        width: 307.47px;
        height: 1px;
        transform: translateX(-3.741px);
        background-color: #494949;
        margin: 5px 0;
    }
    .hotkey {
        margin-left: 150px;
        font-size: 14px;
        color: #d2d2d2;
        user-select: none;
    }
</style>
