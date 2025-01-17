<template>
    <div class="container">
        <div class="title">
            <h2>文本翻译</h2>
        </div>
        <div class="text-item">
            <div class="language-switcher">
                <span class="left-language">中文</span>
                <button class="switch-button" @click="switchLanguages">
                    <el-icon><Switch /></el-icon>
                </button>
                <span class="right-language">英文</span>
            </div>
            <textarea class="inputarea" v-model="textarea" placeholder="输入文本"></textarea>
            <button class="translate-button" @click="translate">翻译</button>
            <div class="loadingarea">
                <Loading v-if="showLoading"/>
                <textarea class="resultarea" v-model="res" placeholder="翻译结果"></textarea>
            </div>
            <button class="translate-button" @click="copy">复制</button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { Switch } from '@element-plus/icons-vue';
import { mainStore } from '@/store/index.ts';
import Loading from '../../../components/Loading.vue'

const textarea = ref('');
const res = ref('');
const store = mainStore();
const mode = ref('0');
const theme = ref('')
const showLoading = ref(false);

const switchLanguages = () => {
    if (mode.value === '0') {
        // @ts-ignore
        document.querySelector('.left-language').style.left = 'calc(65% - 30px)';
        // @ts-ignore
        document.querySelector('.right-language').style.left = '35%';
        mode.value = '1';
    } else {
        // @ts-ignore
        document.querySelector('.left-language').style.left = '35%';
        // @ts-ignore
        document.querySelector('.right-language').style.left = 'calc(65% - 30px)';
        mode.value = '0';
    }
}
 
// 点击翻译按钮翻译
const translate = () => {
    if (textarea.value === '') {
        ElMessage({message: '请输入文本', type: 'error', duration: 5 * 1000, grouping: true});
        return;
    }

    loading();

    let formData = new FormData();
    formData.append('text', textarea.value);
    formData.append('mode', mode.value);

    axios({
        method: 'post', 
        url: `${store.ipAddress}/api/translate`, 
        data: formData, 
        headers:{'Content-Type': 'multipart/form-data'}}
    )
    .then(response => {
        let responseData = response.data;
        if (responseData.ret === 0) {
            res.value = responseData.res;
        } else {
            ElMessage({message: '翻译失败：' + responseData.msg, type: 'error', duration: 5 * 1000, grouping: true});
        }
    })
    .catch(error => {
        console.error('Error posting data:', error);
        ElMessage({message: '翻译失败：网络错误，请稍后重试！', type: 'error', duration: 5 * 1000, grouping: true});
    })
    .finally(() => {
        stopLoading();
    });
}

// 对选中文本进行翻译
const translateSelected = (text) => {
    textarea.value = text;
}

// 监听翻译事件
watch(() => store.select, (select) => {
    if (select === 'translate') {
        translateSelected(store.content);
    }
});

// 复制到剪切板
const copy = async () => {
    try {
        await navigator.clipboard.writeText(res.value);
        ElMessage({message: '内容已复制到剪切板! ', type: 'success', duration: 5 * 1000, grouping: true});
    } catch (err) {
        ElMessage({message: '复制失败，请重试! ', type: 'error', duration: 5 * 1000, grouping: true});
    }
};

onMounted(() => {
  store.initializeTheme();
  theme.value = store.theme;
});

const loading = () => {
    showLoading.value = true;
}

const stopLoading = () => {
    showLoading.value = false;
}
</script>

<style scoped>
.container {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: var(--backgroundColor);
}
.title {
    color: var(--titleColor);
    position: relative;
    display: flex;
    align-items: center;
    padding-bottom: 10px;
}

.title h2 {
  flex: 2;
  text-align: center;
}
.text-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: calc(100% - 85.83px); 
}
.language-switcher {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 10%;
    padding-bottom: 4%;
    padding: relative;
}
.left-language {
    position: absolute;
    left: 35%;
    font-size: 15px;
    color: var(--textColor);
    transition: left 0.3s ease;
}
.right-language {
    position: absolute;
    left: calc(65% - 30px);
    font-size: 15px;
    color:  var(--textColor);
    transition: left 0.3s ease;
}
.inputarea {
    resize: none;
    outline: none;
    background-color: var(--btnColor);
    color:  var(--textColor);
    border: none;
    padding: 10px;
    width: 70%;
    height: 40%;
    font-size: 20px;
    font-family: 'Arial';
    border-radius: 10px;
}
.switch-button {
    margin: 15px;
    padding: 0;
    width: 50px;
    height: 15px;
    background-color: rgba(0,0,0,0);
    color: var(--textColor);
    border: none;
    border-radius: 10px;
    outline: none;
    cursor: pointer;
}
.switch-button:hover {
    background-color: rgba(0,0,0,0);
    color: #6d6d6d;
}
.translate-button {
    margin: 10px;
    background-color: var(--btnColor);
    color: var(--textColor);
    border: none;
    border-radius: 10px;
    outline: none;
    cursor: pointer;
    position: relative;
    left: 29%;
    border: 1.5px solid var(--titleColor);
}
.translate-button:hover {
    background-color: #b2b2b2;
    color: var(--textColor);
}
.loadingarea {
    position: relative;
    display: flex;
    resize: none;
    outline: none;
    background-color: #33333300;
    border: none;
    width: calc(70% + 20px);
    height: calc(40% + 20px);
}
.resultarea {
    resize: none;
    outline: none;
    background-color: var(--btnColor);
    color:  var(--textColor);
    border: none;
    padding: 10px;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    font-size: 20px;
    font-family: 'Arial';
    border-radius: 10px;
}
</style>