<template>
  <div class="file-manager">
    <div class="add-file">
      <h2>OCR图片识别</h2>
      <svg @click="triggerFileInput" t="1719546222308" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3650" width="200" height="200">
        <path d="M576 928H192c-52.992 0-96-43.093333-96-96V192c0-52.992 43.093333-96 96-96h640c52.992 0 96 43.093333 96 96v384.064c0 17.706667-14.293333 32-32 32s-32-14.293333-32-32V192.021333c0-17.706667-14.4-32-32-32H192c-17.706667 0-32 14.378667-32 32v639.957334c0 17.706667 14.4 32 32 32h384c17.706667 0 32 14.314667 32 32 0 17.706667-14.293333 32.021333-32 32.021333zM128 693.312a32.064 32.064 0 0 1-22.613333-54.698667l159.402666-159.338666a95.786667 95.786667 0 0 1 110.72-17.984l173.589334 86.805333c12.309333 6.186667 27.093333 3.797333 36.8-5.994667l287.402666-287.445333a32.042667 32.042667 0 0 1 45.290667 45.312L631.210667 587.392a95.786667 95.786667 0 0 1-110.72 18.005333l-173.589334-86.826666a31.616 31.616 0 0 0-36.8 6.016l-159.509333 159.317333c-6.186667 6.314667-14.4 9.386667-22.592 9.386667z m320-277.376c-52.906667 0-96-43.093333-96-96s43.093333-96.021333 96-96.021333 96 43.093333 96 96-43.093333 96.021333-96 96.021333z m0-128c-17.6 0-32 14.378667-32 32 0 17.6 14.4 32 32 32s32-14.4 32-32c0-17.621333-14.4-32-32-32zM768 928c-17.706667 0-32-14.293333-32-32v-192.021333c0-17.706667 14.293333-32 32-32s32 14.293333 32 32v192c0 17.706667-14.293333 32.021333-32 32.021333z m128-128c-7.893333 0-15.701333-2.922667-21.909333-8.725333L768 691.669333l-106.090667 99.712a31.936 31.936 0 0 1-45.226666-1.408 31.957333 31.957333 0 0 1 1.408-45.205333l112.213333-105.386667A48.554667 48.554667 0 0 1 768 621.44c14.72 0 28.501333 6.613333 37.696 17.92l112.213333 105.386667A31.957333 31.957333 0 0 1 896 800z" fill="#8a8a8a" p-id="3651"></path>
      </svg>
    </div>
    <input type="file" ref="fileInput" @change="handleFileChange" multiple hidden />
  </div>
  <div class="loadingarea">
    <Loading2 v-if="showLoading"/>
    <div class="content">
      <ul v-if="responseText.length > 0">
        <li v-for="(item, index) in responseText" :key="index">{{ item }}</li>
      </ul>
      <p v-else>没有识别到内容</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { mainStore } from '@/store';
import Loading2 from '../../../components/Loading2.vue'

const theme = ref('');
const store = mainStore();
const fileList = ref<File[]>([]);
const fileInput = ref<HTMLInputElement | null>(null);
const responseText = ref<string[]>([]); // 修改为字符串数组类型
const showLoading = ref(false);

const triggerFileInput = () => {
  fileInput.value?.click();
};

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files) {
    fileList.value = Array.from(target.files);
    uploadimg();
  }
};

const uploadimg = () => {
  showLoading.value = true;

  let formData = new FormData();
  formData.append("username", store.username);
  fileList.value.forEach((file) => {
    formData.append("img", file, "img.png");
    console.log('Added file to formData:', file);
  });

  axios({
    method: 'post',
    url: `${store.ipAddress}/api/img2word`,
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
    console.log('Response received:', res);

    if (res.data && res.data.ret === 1) {
      alert("上传失败");
    } else if (res.data && Array.isArray(res.data.res)) {
      responseText.value = res.data.res;
      console.log('Parsed response data.res:', responseText.value);
    } else {
      console.error('Unexpected response format:', res.data);
      responseText.value = [];
    }
  }).catch(error => {
    console.error('Error during image upload:', error);
    alert('上传过程中发生错误');
  }).finally(() => {
    showLoading.value = false;
  });
};

onMounted(() => {
  store.initializeTheme();
  theme.value = store.theme;
});
</script>

<style scoped>
.add-file {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
}

.add-file h2 {
  flex: 2;
  text-align: center;
  color: var(--titleColor);
}

.add-file svg {
  max-width: 8%;
  max-height: 8%;
  width: auto;
  height: auto;
  object-fit: contain;
  margin-left: auto;
  margin-right: 20px;
  cursor: pointer;
  filter: invert(var(--invert));
}
.content {
  width: auto;
  height: auto;
  padding-left: 15px;
  padding-right: 15px;
  object-fit: contain;  
  border-radius: 10px;
  background-color: rgba(134, 134, 134, 0);
}
.loadingarea {
  position: relative;
  width: auto;
  height: calc(100% - 85.84px);
  overflow-y: auto;
  max-height: 100%;
}
</style>
