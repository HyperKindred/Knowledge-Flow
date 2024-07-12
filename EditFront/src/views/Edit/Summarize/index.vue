<template>
    <div class="container">
        <div class="title">
            <h2>文本摘要</h2>
        </div>
        <div class="text-item">
            <div class="loadingarea">
                <Loading v-if="showLoading"/>
                <textarea class="textarea" v-model="res" placeholder="摘要结果"></textarea>
            </div>
            <button class="button" @click="copy">复制</button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { mainStore } from '@/store/index.ts';
import Loading from '../../../components/Loading.vue'

const res = ref('');
const store = mainStore();
const theme = ref('')
const showLoading = ref(false);

// 对选中文本进行摘要
const summarizeSelected = (text) => {
    let formData = new FormData();
    formData.append('text', text);

    axios({
        method: 'post', 
        url: `${store.ipAddress}/api/summarize`, 
        data: formData, 
        headers:{'Content-Type': 'multipart/form-data'}}
    )
    .then(response => {
        let responseData = response.data;
        if (responseData.ret === 0) {
            res.value = responseData.res;
        } else {
            ElMessage({message: '摘要失败：' + responseData.msg, type: 'error', duration: 5 * 1000, grouping: true});
        }
    })
    .catch(error => {
        console.error('Error posting data:', error);
        ElMessage({message: '摘要失败：网络错误，请稍后重试！', type: 'error', duration: 5 * 1000, grouping: true});
    })
    .finally(() => {
        stopLoading();
    });
}

// 监听摘要事件
watch(() => store.select, (select) => {
    if (select === 'summarize') {
        loading();
        summarizeSelected(store.content);
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
    display: flex;
    flex-direction: column;
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: var(--backgroudColor);
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
    height: 90%;
}
.loadingarea {
    position: relative;
    display: flex;
    resize: none;
    outline: none;
    background-color: #333333;
    color: #ffffff;
    border: none;
    width: 80%;
    height: 90%;
}
.textarea {
    resize: none;
    outline: none;
    background-color: var(--btnColor);
    color:var(--textColor);
    border: none;
    padding: 10px;
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    font-size: 20px;
    font-family: 'Arial';
}
.button {
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
.button:hover {
    background-color: #b2b2b2;
    color: var(--textColor);
}
</style>
