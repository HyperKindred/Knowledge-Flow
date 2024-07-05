<template>
    <div class="container">
        <div class="title">
            <h2>文本翻译</h2>
        </div>
        <div class="language-switcher">
            <span class="left-language">中文</span>
            <button class="switch-button" @click="switchLanguages">
                <el-icon><Switch /></el-icon>
            </button>
            <span class="right-language">英文</span>
        </div>
        <div class="text-item">
            <textarea class="textarea" v-model="textarea" placeholder="输入文本"></textarea>
            <button class="translate-button" @click="translate">翻译</button>
            <textarea class="textarea" v-model="res" placeholder="翻译结果"></textarea>
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

const textarea = ref('');
const res = ref('');
const store = mainStore();
const mode = ref('0');

const switchLanguages = () => {
    if (mode.value === '0') {
        document.querySelector('.left-language').style.left = 'calc(65% - 30px)';
        document.querySelector('.right-language').style.left = '35%';
        mode.value = '1';
    } else {
        document.querySelector('.left-language').style.left = '35%';
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
</script>

<style scoped>
.container {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #222222;
}
.title {
    color: #ffffff;
    position: relative;
    display: flex;
    align-items: center;
    padding-bottom: 10px;
}

.title h2 {
  flex: 2;
  text-align: center;
}
.language-switcher {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 7%;
}
.left-language {
    position: absolute;
    left: 35%;
    font-size: 15px;
    color: #ffffff;
    transition: left 0.3s ease;
}
.right-language {
    position: absolute;
    left: calc(65% - 30px);
    font-size: 15px;
    color: #ffffff;
    transition: left 0.3s ease;
}
.text-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: 80%;
}
.textarea {
    resize: none;
    outline: none;
    background-color: #333333;
    color: #ffffff;
    border: none;
    padding: 10px;
    width: 70%;
    height: 40%;
    font-size: 20px;
    font-family: 'Arial';
}
.switch-button {
    margin: 15px;
    padding: 0;
    width: 50px;
    height: 15px;
    background-color: #222222;
    color: #919191;
    border: none;
    border-radius: 10px;
    outline: none;
    cursor: pointer;
}
.switch-button:hover {
    background-color: #222222;
    color: #6d6d6d;
}
.translate-button {
    margin: 10px;
    background-color: #303030;
    color: #919191;
    border: none;
    border-radius: 10px;
    outline: none;
    cursor: pointer;
    position: relative;
    left: 29%;
}
.translate-button:hover {
    background-color: #b2b2b2;
    color: #818181;
}
</style>