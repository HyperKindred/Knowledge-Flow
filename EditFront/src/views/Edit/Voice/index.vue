<template>
  <div class="file-manager">
      <div class="add-file">
        <h2>语音识别转文字</h2>
          <svg @click="triggerFileInput" t="1719556568075" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4835" width="200" height="200"><path d="M774.73792 110.1568H249.25696c-102.4256 0-185.46688 83.04128-185.46688 185.46688v432.75264c0 102.4256 83.04128 185.46688 185.46688 185.46688h387.328s17.92512-0.98304 17.92512-22.21056c0-23.36256-18.87232-24.15616-18.87232-24.15616H249.25696c-76.83072 0-139.10016-62.26944-139.10016-139.10016V295.62368c0-76.8256 62.26944-139.10016 139.10016-139.10016h525.48096c76.83072 0 139.10016 62.27456 139.10016 139.10016v293.6576s1.46432 14.73024 23.86432 13.9264c20.91008-0.74752 22.50752-13.97248 22.50752-13.97248V295.62368c0-102.4256-83.0464-185.46688-185.472-185.46688z" fill="#707070" p-id="4836"></path><path d="M661.79072 286.4896l-108.53888 29.24032c-15.1552 2.45248-26.51136 14.02368-26.2144 26.25536h-0.04096v208.3584c-19.42528-7.808-42.88512-9.6-66.41664-3.5584-49.95072 12.84608-81.26464 56.10496-69.9392 96.64 11.33056 40.52992 61.0048 62.98624 110.95552 50.16064 46.14656-11.86816 76.35456-49.6896 71.76192-87.35232V357.93408l93.25568-25.12384c15.76448-2.54976 27.47904-14.99136 26.14784-27.78624-1.32096-12.78464-15.20128-21.08416-30.97088-18.5344zM825.84576 638.21312l-109.47584 116.30592h79.69792v113.5104c0 16.43008 13.3376 29.76768 29.7728 29.76768s29.76768-13.3376 29.76768-29.76768v-113.5104h79.70304l-109.4656-116.30592z" fill="#707070" p-id="4837"></path></svg>
      </div>   
      <input type="file" ref="fileInput" @change="handleFileChange" multiple hidden /> 
  </div>
  <div class="loadingarea">
    <Loading v-if="showLoading"/>
    </div>
  <div class="content">
    {{ responseText }}
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { mainStore } from '@/store';
import Loading from '../../../components/Loading.vue'

const store = mainStore();
const fileList = ref<File[]>([]);
const fileInput = ref<HTMLInputElement | null>(null);
const responseText = ref<string | null>(null);
const triggerFileInput = () => {
fileInput.value?.click();
};
const theme = ref('')
const showLoading = ref(false);

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
  formData.append("voice", file);
  console.log(file);
});
axios({
  method: 'post',
  url: `${store.ipAddress}/api/voice2word`,
  data: formData,
  headers: {
    'Content-Type': 'multipart/form-data'
  }
}).then(res => {
  if (res.data.ret == 1) {
    alert("上传失败");
  } else {
    responseText.value = res.data.res;
  }
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
color: var(--titleColor)
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
background-color: rgba(134, 134, 134, 0.683);
}
.loadingarea {
  position: relative;
  width: auto;
  height: calc(100% - 85.84px);
}
</style>
