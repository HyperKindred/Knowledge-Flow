<template>
    <div class="container">
        <div class="title">
            <h2>文本摘要</h2>
        </div>
        <div class="text-item">
            <textarea class="textarea" v-model="res" placeholder="摘要结果"></textarea>
            <button class="button" @click="copy">复制</button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { mainStore } from '@/store/index.ts';

const res = ref('');
const store = mainStore();

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
    });
}

// 监听摘要事件
watch(() => store.select, (select) => {
    if (select === 'summarize') {
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
.text-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: 90%;
}
.textarea {
    resize: none;
    outline: none;
    background-color: #333333;
    color: #767676;
    border: none;
    padding: 10px;
    width: 80%;
    height: 90%;
    font-size: 20px;
    font-family: 'Arial';
}
.button {
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
.button:hover {
    background-color: #b2b2b2;
    color: #818181;
}
</style>
