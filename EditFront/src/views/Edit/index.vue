<template>
  <div class="EditMain" ref="filecont" >
    <img class="background" :src=currentImage />
    <div class="lefttools">
      <div class="lefttop">
        <img :src="misakaImg" alt="Misaka Mikoto">
        <h2 class="username-display">{{ store.username }}</h2>
      </div>
      <div class="leftlist">
        <svg @click="navigateTo('Catalog')" id="Catalog" t="1719471435071" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="18790" width="200" height="200"><path d="M867.995 459.647h-711.99c-27.921 0-52.353 24.434-52.353 52.353s24.434 52.353 52.353 52.353h711.99c27.921 0 52.353-24.434 52.353-52.353s-24.434-52.353-52.353-52.353z" p-id="18791" fill="#bfbfbf"></path><path d="M867.995 763.291h-711.99c-27.921 0-52.353 24.434-52.353 52.353s24.434 52.353 52.353 52.353h711.99c27.921 0 52.353-24.434 52.353-52.353s-24.434-52.353-52.353-52.353z" p-id="18792" fill="#bfbfbf"></path><path d="M156.005 260.709h711.99c27.921 0 52.353-24.434 52.353-52.353s-24.434-52.353-52.353-52.353h-711.99c-27.921 0-52.353 24.434-52.353 52.353s24.434 52.353 52.353 52.353z" p-id="18793" fill="#bfbfbf"></path>
          <desc class="tooltip">目录</desc>
        </svg>
        <svg @click="navigateTo('Outline')" id="Outline" t="1719471418244" class="icon" viewBox="0 0 1126 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2304" width="200" height="200"><path d="M142.234 0a142.234 142.234 0 0 1 56.883 272.589v210.944h113.715c15.718 0 28.467 12.8 28.467 28.467v56.883a28.467 28.467 0 0 1-28.467 28.467H199.168v263.117c0 16.538 3.43 31.488 8.704 42.087l2.048 3.686a34.1 34.1 0 0 0 1.894 2.918l0.87 1.024h100.148c15.718 0 28.467 12.8 28.467 28.468v56.883A28.467 28.467 0 0 1 312.832 1024H207.258c-72.807 0-119.399-73.267-121.856-156.774l-0.052-6.759V272.59A142.234 142.234 0 0 1 142.182 0z m886.988 853.35a51.2 51.2 0 0 1 51.2 51.2v68.25a51.2 51.2 0 0 1-51.2 51.2H562.79a51.2 51.2 0 0 1-51.2-51.2v-68.25a51.2 51.2 0 0 1 51.2-51.2h466.432z m0-398.233a51.2 51.2 0 0 1 51.2 51.2v68.25a51.2 51.2 0 0 1-51.2 51.2H562.79a51.2 51.2 0 0 1-51.2-51.2v-68.199a51.2 51.2 0 0 1 51.2-51.2h466.432z m0-398.234a51.2 51.2 0 0 1 51.2 51.2v68.25a51.2 51.2 0 0 1-51.2 51.2H562.79a51.2 51.2 0 0 1-51.2-51.2v-68.25a51.2 51.2 0 0 1 51.2-51.2h466.432z" fill="#bfbfbf" p-id="2305"></path>
          <title class="tooltip">大纲</title>
        </svg>
        <svg @click="navigateTo('OCR')" id="OCR" t="1719471387059" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2344" width="200" height="200"><path d="M1022.54 731.84v182.08c0 60.23-49.01 109.25-109.25 109.25H694.81c-20.14 0-36.42-16.28-36.42-36.42s16.28-36.42 36.42-36.42H913.3c20.1 0 36.42-16.31 36.42-36.41V731.84c0-20.14 16.27-36.42 36.42-36.42 20.13 0 36.4 16.28 36.4 36.42zM294.07 950.33H111.99c-20.06 0-36.41-16.31-36.41-36.41V731.84c0-20.14-16.31-36.42-36.42-36.42-20.1 0-36.41 16.28-36.41 36.42v182.08c0 60.23 49.01 109.25 109.24 109.25h182.08c20.1 0 36.42-16.28 36.42-36.42s-16.32-36.42-36.42-36.42zM38.16 328.1c20.1 0 36.42-16.31 36.42-36.41V109.61c0-20.07 16.35-36.42 36.41-36.42h182.08c20.1 0 36.42-16.31 36.42-36.41 0-20.1-16.31-36.42-36.42-36.42H110.99C50.76 0.36 1.75 49.38 1.75 109.61v182.08c0 20.1 16.31 36.41 36.41 36.41zM914.3 0.36H695.81c-20.14 0-36.42 16.31-36.42 36.42 0 20.1 16.28 36.41 36.42 36.41H914.3c20.1 0 36.42 16.35 36.42 36.42v182.08c0 20.1 16.27 36.41 36.42 36.41 20.14 0 36.41-16.31 36.41-36.41V109.61C1023.54 49.38 974.53 0.36 914.3 0.36zM383.4 509.78c0 97.6-55.2 156-136.4 156s-136.4-58.4-136.4-156 55.2-152.8 136.4-152.8 136.4 55.6 136.4 152.8z m-72.8 0c0-57.6-24.4-91.6-63.6-91.6s-63.2 34-63.2 91.6c0 58 24 94.4 63.2 94.4s63.6-36.4 63.6-94.4z m246.8 94.4c-42 0-69.2-34.4-69.2-93.6 0-58 31.6-92.4 70-92.4 21.2 0 36.8 9.6 51.6 23.2l37.6-45.6c-20.4-20.8-51.6-38.8-90.4-38.8-75.6 0-142 56.8-142 156 0 100.8 64 152.8 139.6 152.8 38.8 0 72-14.8 97.2-44l-37.6-44.8c-14 15.2-33.2 27.2-56.8 27.2z m302.4-62l66.4 118h-80l-54.8-104.8H757v104.8h-71.6v-297.6h109.2c63.6 0 116.4 21.6 116.4 93.6 0 43.6-20.4 71.6-51.2 86z m-18.8-86c0-28-18-37.2-52-37.2h-32v80h32c34 0 52-14.8 52-42.8z" p-id="2345" fill="#bfbfbf"></path>
          <title class="tooltip">图片识别</title>
        </svg>
        <svg @click="navigateTo('Voice')" id="Voice" t="1719471369078" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4166" width="200" height="200"><path d="M923.648 108.088889c21.902222 0 39.594667 15.815111 42.382222 36.920889l0.398222 5.859555V820.906667a42.325333 42.325333 0 0 1-36.977777 42.439111l-5.802667 0.341333H531.797333a35.555556 35.555556 0 0 1-5.233777-70.712889l5.233777-0.398222h330.695111c15.36 0 28.103111-11.207111 30.492445-25.884444l0.398222-4.949334V212.48a30.947556 30.947556 0 0 0-25.884444-30.435556l-5.006223-0.455111H532.764444a36.522667 36.522667 0 0 1-36.522666-36.522666c0-18.773333 13.312-33.962667 31.061333-36.579556l5.461333-0.398222h390.826667zM560.924444 354.076444c19.911111 0 36.465778 18.090667 36.465778 39.424 0 141.368889-94.435556 263.793778-221.809778 289.962667l-14.563555 2.503111v132.096c0 19.342222-13.653333 36.067556-31.118222 38.968889l-5.347556 0.398222c-18.204444 0-33.450667-14.961778-36.124444-33.678222l-0.398223-5.688889v-132.096l-2.503111-0.341333C155.875556 665.144889 57.344 546.360889 51.484444 406.641778L51.2 393.500444c0-21.617778 16.497778-39.424 36.977778-39.424 19.968 0 36.522667 18.090667 36.522666 39.424 0 119.239111 89.770667 216.177778 199.850667 216.177778 110.08 0 199.850667-96.938667 199.850667-216.177778 0-21.333333 16.497778-39.424 36.522666-39.424z m259.185778 259.413334c19.114667 0 35.100444 16.099556 35.100445 35.157333a33.564444 33.564444 0 0 1-9.784889 24.348445 35.157333 35.157333 0 0 1-19.626667 10.24l-5.688889 0.455111h-177.607111a35.441778 35.441778 0 0 1-35.043555-35.100445c0-17.351111 13.198222-32.142222 29.923555-34.702222l5.12-0.341333h177.607111zM324.835556 123.448889c65.592889 0 118.897778 53.304889 118.897777 118.897778v170.894222c0 65.536-53.304889 118.897778-118.897777 118.897778a119.523556 119.523556 0 0 1-119.864889-118.897778V242.346667c0-65.592889 53.76-118.897778 119.864889-118.897778z m495.331555 329.784889c19.114667 0 35.100444 16.042667 35.100445 35.157333a33.564444 33.564444 0 0 1-9.728 24.291556 35.271111 35.271111 0 0 1-19.683556 10.24l-5.688889 0.455111h-177.607111a35.498667 35.498667 0 0 1-35.043556-35.100445c0-17.294222 13.198222-32.085333 29.923556-34.702222l5.12-0.341333h177.607111z m0-159.288889c19.114667 0 35.100444 15.985778 35.100445 35.100444a33.564444 33.564444 0 0 1-9.728 24.291556 35.214222 35.214222 0 0 1-19.683556 10.24l-5.688889 0.455111h-177.607111a35.441778 35.441778 0 0 1-35.043556-35.043556c0-17.351111 13.198222-32.142222 29.923556-34.702222l5.12-0.398222h177.607111z" fill="#bfbfbf" p-id="4167"></path>
          <title class="tooltip">语音识别</title>
        </svg>
        <svg @click="navigateTo('Translate')" id="Translate" t="1719471340950" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="9962" width="200" height="200"><path d="M512 1024C230.4 1024 0 793.6 0 512S230.4 0 512 0s512 230.4 512 512-230.4 512-512 512z m0-960C265.6 64 64 265.6 64 512s201.6 448 448 448 448-201.6 448-448S758.4 64 512 64z m268.8 422.4c-60.8-6.4-118.4-22.4-169.6-51.2-54.4 25.6-115.2 44.8-172.8 57.6l-28.8-51.2c51.2-9.6 102.4-25.6 150.4-44.8-32-28.8-57.6-64-70.4-105.6H448V240h304v51.2c-19.2 44.8-48 83.2-86.4 112 44.8 16 89.6 28.8 134.4 32l-19.2 51.2z m-92.8-192H544c16 32 38.4 57.6 67.2 76.8 28.8-19.2 57.6-44.8 76.8-76.8zM265.6 265.6L307.2 224c38.4 28.8 70.4 57.6 102.4 92.8l-41.6 41.6c-28.8-35.2-64-67.2-102.4-92.8z m99.2 396.8c16-16 32-35.2 51.2-54.4l16 64c-35.2 38.4-73.6 76.8-115.2 108.8l-22.4-54.4c9.6-9.6 16-22.4 16-35.2v-227.2H224v-57.6h140.8v256z m214.4-83.2h-112v-54.4h112v-51.2h57.6v51.2h121.6v54.4h-121.6V640h150.4v57.6h-150.4V800h-57.6v-102.4h-137.6V640h137.6v-60.8z" p-id="9963" fill="#bfbfbf"></path>
          <title class="tooltip">翻译</title>
        </svg>
        <svg @click="navigateTo('Summarize')" id="Summarize" t="1719471303821" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2312" width="200" height="200"><path d="M841 315.6H641c-28.7 0-52-23.3-52-52V82h46v181.6c0 3.3 2.7 6 6 6h200v46z" fill="#bfbfbf" p-id="2313"></path><path d="M804 966H215c-29.2 0-53-23.8-53-53V119c0-29.2 23.8-53 53-53h41c12.7 0 23 10.3 23 23s-10.3 23-23 23h-41c-3.9 0-7 3.1-7 7v794c0 3.9 3.1 7 7 7h589c3.9 0 7-3.1 7-7V288.5L609.3 112H426c-12.7 0-23-10.3-23-23s10.3-23 23-23h192c5.6 0 11 2 15.1 5.7l216 189c5 4.4 7.9 10.7 7.9 17.3v635c0 29.2-23.8 53-53 53zM364.9 112h-39c-12.7 0-23-10.3-23-23s10.3-23 23-23h39c12.7 0 23 10.3 23 23s-10.3 23-23 23z" fill="#bfbfbf" p-id="2314"></path><path d="M307 372h413c8.3 0 15 6.7 15 15s-6.7 15-15 15H307c-8.3 0-15-6.7-15-15s6.7-15 15-15zM307 498h413c8.3 0 15 6.7 15 15s-6.7 15-15 15H307c-8.3 0-15-6.7-15-15s6.7-15 15-15zM307 624h413c8.3 0 15 6.7 15 15s-6.7 15-15 15H307c-8.3 0-15-6.7-15-15s6.7-15 15-15zM307 750h413c8.3 0 15 6.7 15 15s-6.7 15-15 15H307c-8.3 0-15-6.7-15-15s6.7-15 15-15zM307 246h231c8.3 0 15 6.7 15 15s-6.7 15-15 15H307c-8.3 0-15-6.7-15-15s6.7-15 15-15z" fill="#bfbfbf" p-id="2315"></path><path d="M610 481h71c7.7 0 14 6.3 14 14v35c0 7.7-6.3 14-14 14h-71c-7.7 0-14-6.3-14-14v-35c0-7.7 6.3-14 14-14zM346 734h71c7.7 0 14 6.3 14 14v35c0 7.7-6.3 14-14 14h-71c-7.7 0-14-6.3-14-14v-35c0-7.7 6.3-14 14-14zM346 230h71c7.7 0 14 6.3 14 14v35c0 7.7-6.3 14-14 14h-71c-7.7 0-14-6.3-14-14v-35c0-7.7 6.3-14 14-14z" fill="#bfbfbf" p-id="2316"></path>
          <title class="tooltip">摘要</title>
        </svg>
        <svg @click="navigateTo('Style_library')" id="Style_library" t="1719471218475" class="icon" viewBox="0 0 1026 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2347" width="200" height="200"><path d="M944.4 311.8c-32.7-2.3-63.4 3.5-101.5 54.3s-152.3 20.7-137.5-41c6.6-17.8 7.7-36.4 70.3-66.8 62.6-30.4 36.1-100.4 9.6-115 0 0-241.9-138.7-580.3 60.9-93 54-265.5 251.1-183.5 459.2C73.1 787.7 162.8 858.8 308.3 905c145.5 46.2 314.7 14.7 400.4-29.3 85.7-44 227.8-109.4 294.4-284.2 66.5-174.8-26-277.5-58.7-279.7z m-850 179.6c-3.8-26.8 24.3-53 62.9-58.5 38.5-5.5 72.9 11.8 76.7 38.6 3.8 26.8-24.3 53-62.9 58.5s-72.9-11.8-76.7-38.6z m121 203.6c-40.5 5.8-76.7-12.4-80.7-40.6-4-28.2 25.6-55.7 66.1-61.5 40.5-5.8 76.6 12.4 80.7 40.6 4.1 28.2-25.5 55.7-66.1 61.5z m18.4-325.2c-38.9 5.5-73.5-11.9-77.4-39-3.8-27.1 24.5-53.5 63.4-59s73.5 11.9 77.4 39-24.6 53.4-63.4 59z m172.9 468.8c-44.2 9.3-85.2-8.1-91.7-38.9-6.4-30.7 24.1-63.2 68.3-72.4 44.2-9.3 85.2 8.1 91.7 38.9 6.4 30.7-24.2 63.1-68.3 72.4z m28.9-582c-37 5.3-70-11.3-73.6-37.1-3.7-25.7 23.4-50.9 60.4-56.1 37-5.3 70 11.3 73.6 37.1 3.6 25.7-23.4 50.8-60.4 56.1z" p-id="2348" fill="#bfbfbf"></path>
          <title class="tooltip">样式库</title>
        </svg>
      </div>
      <div class="toolBar">
         <router-view></router-view>
      </div>
    </div>
    <div class="editor">
      <!-- <p>store.isShow: {{ store.isShow }}</p> -->
      <div v-if="store.isShow" class="editorcard">
        <div class="toptools">
          <EditorMenu :editor="editor" />
          <div class="topBtn">
          <button class="topButton" @click="toggleTheme()">昼夜切换</button>
          <button class="topButton" @click="autoFormat()">思维导图</button>
          <button class="topButton" @click="autoFormat()">格式化</button>
          <button class="topButton" @click="saveHTMLText()">Save</button>
        </div>
        </div>
        <div class="editcont">
          <Loading v-if="showLoading"/>
          <ContextMenu>
          <EditorContent @mousescroll="" @mousedown="" @mousemove=""
            @mouseup="selecttext($event)" style="padding: 8px; color: var(--textColor);" :editor="editor" />
          </ContextMenu>
        </div>

        <div class="bottomcount">
          字数统计:
          {{ editor?.storage.characterCount.characters() }}
        </div>
      </div>
      <div v-else-if="store.editorisShow">
        <Style_editor></Style_editor>
      </div>
      <div v-else>
        <Welcome></Welcome>
      </div>
    </div>


    <!-- <div class="righttools">
      
    </div> -->
  </div>
</template>
<script lang="ts" setup>
import { Brush, EditPen, } from '@element-plus/icons-vue'
import { defineComponent, onMounted, onBeforeUnmount, ref, watch, computed } from 'vue';
import { Editor, EditorContent, useEditor, BubbleMenu } from '@tiptap/vue-3';
import { storeToRefs } from 'pinia'
import Underline from '@tiptap/extension-underline'
import ContextMenu from '../../components/ContextMenu.vue'
import Loading from '../../components/Loading.vue'
// 列表
import ListItem from '@tiptap/extension-list-item'
import OrderedList from '@tiptap/extension-ordered-list'
import BulletList from '@tiptap/extension-bullet-list'
// 左侧
import misakaImg from '../../assets/images/Misaka Mikoto.webp'
import Catalog from './Catalog/index.vue'
import Outline from './Outline/index.vue'
import OCR from './OCR/index.vue'
import Voice from './Voice/index.vue'
import Style_library from './Style_library/index.vue'
// 代码
import CodeBlockLowlight from '@tiptap/extension-code-block-lowlight'
import css from 'highlight.js/lib/languages/css'
import js from 'highlight.js/lib/languages/javascript'
import ts from 'highlight.js/lib/languages/typescript'
import html from 'highlight.js/lib/languages/xml'
import { common, createLowlight } from 'lowlight'
// 字数统计
import CharacterCount from '@tiptap/extension-character-count'
import Heading from '@tiptap/extension-heading'
import StarterKit from '@tiptap/starter-kit'
import Placeholder from '@tiptap/extension-placeholder'
import { UndoRound, MoreHorizOutlined } from '@vicons/material'
import TaskItem from '@tiptap/extension-task-item'
import TaskList from '@tiptap/extension-task-list'
import Welcome from './Welcome/index.vue'
import Style_editor from './Style_editor/index.vue'
import { Paragraph } from '@tiptap/extension-paragraph';
// 使用Pinia
import { useEditorStore } from '../../router/index.ts'
import EditorMenu from './EditorMenu/index.vue'
import { defineStore } from 'pinia'
import { ElMessage } from 'element-plus';
import axios from 'axios'
import { useRouter } from 'vue-router';
import { mainStore } from '../../store/index.ts';
import { Extension } from '@tiptap/core'

import lightImage from '@/assets/images/light_background.jpg';
import darkImage from '@/assets/images/dark_background.jpg';
const router = useRouter();
const lowlight = createLowlight()
lowlight.register({ html, ts, css, js })
const editorStore = useEditorStore()
const store = mainStore();
const aipolish = ref("")
const filecont = ref(null);
const aicontinuation = ref("")
const visiblemenu = ref(false)
const position = ref({
  top: 0,
  left: 0
})
const theme = ref('')
const editorContent = ref('');
const showLoading = ref(false);


function navigateTo(componentName) {
  router.push({ name: componentName });

  let currentIcon = document.getElementById(componentName);
  const svgIcons = document.querySelectorAll('.icon');
  currentIcon.querySelectorAll('path').forEach(path => {
    path.style.fill = '#ffffff';
  });
  svgIcons.forEach(svgIcon => {
    if (svgIcon.id !== componentName) {
      svgIcon.querySelectorAll('path').forEach(path => {
        path.style.fill = '';
      });
    }
  });
}
onMounted(() => {
  store.initializeTheme();
  theme.value = store.theme;
});

const currentImage = computed(() => {
  return store.theme === 'light' ? lightImage : darkImage;
});

const ExtendedStyle = Extension.create({
  name: 'extendedStyle',
  addGlobalAttributes() {
    return [
      {
        types: ['heading', 'paragraph', 'bulletList', 'orderedList'],
        attributes: {
          style: {
            default: '',
            parseHTML: element => {
              const style = element.getAttribute('style') || '';
              return style;
            },
            renderHTML: attributes => {
              return { style: attributes.style };
            },
          },
        },
      },
    ];
  },
  addCommands() {
    return {
      setElementStyle: (style) => ({ commands }) => {
        return commands.updateAttributes('heading', { style }) ||
               commands.updateAttributes('paragraph', { style }) ||
               commands.updateAttributes('bulletList', { style }) ||
               commands.updateAttributes('orderedList', { style });
      },
    };
  },
});







store.initializeEditor();
const { editor } = storeToRefs(store);

const saveHTMLText = () => {
  if (editor.value) {
    editorContent.value = editor.value.getHTML();
  }
  let styleid = 1;
  if(store.usedStyleID){
    styleid = store.usedStyleID;
  }
  let formdata = new FormData();
  formdata.append("username", store.username);
  formdata.append("id", store.openNoteID);
  formdata.append("note", editorContent.value);
  formdata.append("styleId", styleid);
  axios({
    method: 'post',
    url: `${store.ipAddress}/api/saveNote`,
    data: formdata,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
    if(res.data.ret == 0) alert("保存成功");
  }).catch(error => {
    console.error("There was an error!", error);
  });
};


const autoFormat = () => {
  if (editor.value) {
    editorContent.value = editor.value.getHTML();
  }
  let formdata = new FormData();
  formdata.append("text", editorContent.value);
  axios({
    method: 'post',
    url: `${store.ipAddress}/api/autoFormat`,
    data: formdata,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
    const htmlContent = res.data.msg;
    store.setHTMLContent(htmlContent);
  })
}

const autoMindmap = () => {
  if (editor.value) {
    editorContent.value = editor.value.getHTML();
  }
  let formdata = new FormData();
  formdata.append("text", editorContent.value);
  formdata.append("username", store.username);
  axios({
    method: 'post',
    url: `${store.ipAddress}/api/autoMindmap`,
    data: formdata,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
    if(res.data.ret){
      alert(res.data.msg);
    }
  })
}

watch(() => store.htmlContent, (newContent) => {
  if (editor.value) {
    editor.value.commands.setContent(newContent, 'html');
  }
  stopLoading();
});

watch(() => store.openNoteID, () => {
  loading();
});


// 获取选中的文字
const selecttext = (e: MouseEvent) => {
    const { from, to } = editor.value.state.selection;
    if (from !== to) {
        const selection = window.getSelection().toString();
        store.setContent(selection);
    }
    else {
        store.setContent('');
    }
}

// 润色函数
const polishSelected=(text)=>{
    var formData = new FormData();
    formData.append('text', text);

    axios({
        method: 'post', 
        url: `${store.ipAddress}/api/polish`, 
        data: formData, 
        headers:{'Content-Type': 'multipart/form-data'}}
    )
    .then(response => {
        let responseData = response.data;
        if (responseData.ret === 0) {
            editor.value.chain().focus().deleteSelection().insertContent(responseData.res).run();
        } else {
            ElMessage({message: '润色失败：' + responseData.msg, type: 'error', duration: 5 * 1000, grouping: true});
        }
    })
    .catch(error => {
        console.error('Error posting data:', error);
        ElMessage({message: '润色失败：网络错误，请稍后重试！', type: 'error', duration: 5 * 1000, grouping: true});
    })
    .finally(() => {
        stopLoading();
    });
}

// 修改病句函数 
const correctSelected=(text)=>{
    var formData = new FormData();
    formData.append('text', text);

    axios({
        method: 'post', 
        url: `${store.ipAddress}/api/correct`, 
        data: formData, 
        headers:{'Content-Type': 'multipart/form-data'}}
    )
    .then(response => {
        let responseData = response.data;
        if (responseData.ret === 0) {
            editor.value.chain().focus().deleteSelection().insertContent(responseData.res).run();
        } else {
            ElMessage({message: '修改失败：' + responseData.msg, type: 'error', duration: 5 * 1000, grouping: true});
        }
    })
    .catch(error => {
        console.error('Error posting data:', error);
        ElMessage({message: '修改失败：网络错误，请稍后重试！', type: 'error', duration: 5 * 1000, grouping: true});
    })
    .finally(() => {
        stopLoading();
    });
}

// 剪切函数
const deleteSelected = () => {
    editor.value.chain().focus().deleteSelection().run();
}

// 复制函数
const copySelected = () => {
    navigator.clipboard.writeText(store.content);
}

// 粘贴函数
const pasteSelected = (text) => {
    navigator.clipboard.readText().then(clipText => {
        editor.value.chain().focus().deleteSelection().insertContent(clipText).run();
    });
}
const toggleTheme = () => {
  store.toggleTheme();
};

// 监听菜单事件
watch(() => store.select, (select) => {
    if (select === 'polish') {
        loading();
        polishSelected(store.content);
    }
    if (select === 'correct') {
        loading();
        correctSelected(store.content);
    }
    if (select === 'delete') {
        deleteSelected();
    }
    if (select === 'copy') {
        copySelected();
    }
    if (select === 'paste') {
        pasteSelected(store.content);
    }
});

const loading = () => {
    showLoading.value = true;
}

const stopLoading = () => {
    showLoading.value = false;
}
</script>
<style>
.EditMain {
  position: relative;
  width: 100w;
  height: 98.5vh;

  display: grid;
  grid-template-columns: 25% 75%;

}

.background {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
        position: fixed;
        z-index: -1;
    }

.lefttools {
  position: relative;
  display: flex;
  background-color: rgba(255, 255, 255, 0);
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-rows: 10% 10% 80%;
}

.lefttop {
  position: relative;
  display: flex;
  align-items: center;
  background-color: var(--backgroundColor);
  width: 95%;
  height: 90%;
  left: 2.5%;
  top: 5%;
  border-radius: 5px;

}

.icon{
  position: relative;
  max-width: 40%;
  max-height: 40%;
  object-fit: contain;
  cursor: pointer;
}

.icon:hover path{
  fill: #ffffff
}

.username-display {
  padding-left: 5%;
  margin: 0; 
  color: var(--titleColor);
}
.leftlist{
  position: relative;
  display: flex;
  align-items: center; 
  justify-content: center; 
  background-color: var(--backgroundColor);
  width: 95%;
  height: 100%;
  left: 2.5%;
  top: 2.5%;
  object-fit: contain;
  border-radius: 5px;
}

.leftlist svg{
  position: relative;
  max-width: 40%;
  max-height: 40%;
  object-fit: contain;
  cursor: pointer;
  filter: invert(var(--invert));
}



.toolBar {
  position: relative;
  background-color: var(--backgroundColor);
  width: 95%;
  height: 100%;
  left: 2.5%;
  bottom: 2.5%;
  top: 1%;
  border-radius: 5px;
}



.editor {
  position: relative;
}

.editorcard {
  position: relative;
  width: 95%;
  height: 95%;
  left: 2.5%;
  top: 2.5%;
  display: grid;
  grid-template-rows: 5% 91% 4%;
  border-radius: 5px;
}



.toptools {
  display: flex;
  background-color: var(--toptools);
  border-bottom: 1px dashed #9ca19f65;
}


.topBtn {
  position: relative;
  display: flex;
  margin-right: 0px;
  margin-left: auto;
}
.topButton {
  background-color: var(--btnColor);
  color: var(--titleColor);
  border: 1.5px solid var(--titleColor);
  max-height: 100%;
  margin-right: 5px;
}



.bottomcount {
  background-color: var(--countColor);
  border-top: 5px;
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: 100%;
  grid-template-rows: 100%;
  justify-items: center;
  align-items: center;
}

.editcont {
  position: relative;
  max-height: 88vh;
  width: 100%;
  overflow-y: auto;
  object-fit: contain;
  background-color: var(--editorColor);
}


.ProseMirror {
  overflow: hidden !important;
}
</style>

<style lang="scss">
b {
  font-weight: bold;
}

.ProseMirror {
  overflow-y: scroll;
}

.ProseMirror p {
  margin: 0;
}

.ProseMirror:focus {
  outline: none;
}

.tiptap p.is-editor-empty:first-child::before {
  color: #adb5bd;
  content: attr(data-placeholder);
  float: left;
  height: 0;
  pointer-events: none;
}


.tiptap {
  >*+* {
    margin-top: 0.75em;
  }

  ul {
    padding: 0 2rem;
    list-style: square;
  }

  ol {
    padding: 0 2rem;
    list-style: decimal;
  }

  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 100%;
    margin: 0;
    overflow: hidden;

    td,
    th {
      min-width: 1em;
      border: 2px solid #ced4da;
      padding: 3px 5px;
      vertical-align: top;
      box-sizing: border-box;
      position: relative;

      >* {
        margin-bottom: 0;
      }
    }

    th {
      font-weight: bold;
      text-align: left;
      background-color: #f1f3f5;
    }

    .selectedCell:after {
      z-index: 2;
      position: absolute;
      content: '';
      left: 0;
      right: 0;
      top: 0;
      bottom: 0;
      background: rgba(200, 200, 255, 0.4);
      pointer-events: none;
    }

    .column-resize-handle {
      position: absolute;
      right: -2px;
      top: 0;
      bottom: -2px;
      width: 4px;
      background-color: #adf;
      pointer-events: none;
    }

    p {
      margin: 0;
    }
  }

  pre {
    background: #0d0d0d;
    color: #fff;
    font-family: 'JetBrainsMono', monospace;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;

    code {
      color: inherit;
      padding: 0;
      background: none;
      font-size: 0.8rem;
    }

    .hljs-comment,
    .hljs-quote {
      color: #616161;
    }

    .hljs-variable,
    .hljs-template-variable,
    .hljs-attribute,
    .hljs-tag,
    .hljs-name,
    .hljs-regexp,
    .hljs-link,
    .hljs-name,
    .hljs-selector-id,
    .hljs-selector-class {
      color: #f98181;
    }

    .hljs-number,
    .hljs-meta,
    .hljs-built_in,
    .hljs-builtin-name,
    .hljs-literal,
    .hljs-type,
    .hljs-params {
      color: #fbbc88;
    }

    .hljs-string,
    .hljs-symbol,
    .hljs-bullet {
      color: #b9f18d;
    }

    .hljs-title,
    .hljs-section {
      color: #faf594;
    }

    .hljs-keyword,
    .hljs-selector-tag {
      color: #70cff8;
    }

    .hljs-emphasis {
      font-style: italic;
    }

    .hljs-strong {
      font-weight: 700;
    }
  }
}

.tableWrapper {
  overflow-x: auto;
}

.resize-cursor {
  cursor: ew-resize;
  cursor: col-resize;
}
</style>