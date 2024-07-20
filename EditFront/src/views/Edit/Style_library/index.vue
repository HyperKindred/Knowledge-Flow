<template>
  <div class="file-manager">
    <div class="add-style">
      <h2>样式库</h2>
      <svg class="icon" viewBox="0 0 1024 1024" width="50" height="50" @click="newStyle">
        <path
          d="M925.696 384q19.456 0 37.376 7.68t30.72 20.48 20.48 30.72 7.68 37.376q0 20.48-7.68 37.888t-20.48 30.208-30.72 20.48-37.376 7.68l-287.744 0 0 287.744q0 20.48-7.68 37.888t-20.48 30.208-30.72 20.48-37.376 7.68q-20.48 0-37.888-7.68t-30.208-20.48-20.48-30.208-7.68-37.888l0-287.744-287.744 0q-20.48 0-37.888-7.68t-30.208-20.48-20.48-30.208-7.68-37.888q0-19.456 7.68-37.376t20.48-30.72 30.208-20.48 37.888-7.68l287.744 0 0-287.744q0-19.456 7.68-37.376t20.48-30.72 30.208-20.48 37.888-7.68q39.936 0 68.096 28.16t28.16 68.096l0 287.744 287.744 0z"
          fill="#8a8a8a"></path>
      </svg>
    </div>
    <div class="content">
      <Loading2 v-if="showLoading"/>
      <el-tree
    :data="treeData"
    :props="defaultProps"
    :highlight-current="true"
    node-key="id"
    ref="fileTree"
    empty-text=""
    @node-drop="handleNodeDrop"
  >
    <template #default="{ node, data }">
      <div class="file-item">
        <span v-if="editingNode !== data.id">{{ data.label }}</span>
        <el-input
          v-else
          v-model="data.label"
          size="mini"
          maxlength="20"
          @blur="finishEditing(data)"
          @keyup.enter.native="finishEditing(data)"
        />
        <div class="file-icon" v-if="data.id > 1">
          <svg t="1719995366880" @click="applyStyle(data)" class="editing" viewBox="0 0 1024 1024" version="1.1"
            xmlns="http://www.w3.org/2000/svg" p-id="3148" width="200" height="200">
            <path
              d="M880.288 232.48L560.192 45.12a95.648 95.648 0 0 0-96.64 0L143.68 232.48A96.64 96.64 0 0 0 96 315.904v397.664c0 34.784 18.624 66.88 48.736 84l320 181.92a95.52 95.52 0 0 0 94.496 0l320-181.92A96.576 96.576 0 0 0 928 713.568V315.904a96.64 96.64 0 0 0-47.712-83.424zM864 713.568c0 11.584-6.208 22.304-16.256 28l-320 181.92a31.776 31.776 0 0 1-31.488 0l-320-181.92A32.192 32.192 0 0 1 160 713.568V315.904c0-11.456 6.048-22.048 15.904-27.808l319.872-187.36a31.84 31.84 0 0 1 32.192 0l320.128 187.392c9.856 5.728 15.904 16.32 15.904 27.776v397.664z"
              p-id="3149" fill="#e6e6e6"></path>
            <path
              d="M512 320a192 192 0 1 0 0 384 192 192 0 0 0 0-384z m0 320a128 128 0 1 1 0-256 128 128 0 0 1 0 256z"
              p-id="3150" fill="#e6e6e6"></path>
          </svg>
          <svg t="1721450187890" @click="showStyleEditor(data)" class="editing" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="8453" width="200" height="200"><path d="M1001.2672 800.8704a22.70208 22.70208 0 0 1 0-41.1648 24.4736 24.4736 0 0 0 13.312-27.7504c-9.3184-38.0928-29.2864-72.704-57.6512-99.7376-8.3968-7.9872-21.1968-9.0112-30.72-2.4576-7.2704 5.0176-16.6912 5.4272-24.3712 1.024a22.6816 22.6816 0 0 1-11.264-21.504c1.024-11.5712-6.2464-22.3232-17.408-25.6a205.9776 205.9776 0 0 0-115.2 0c-11.1616 3.2768-18.432 13.824-17.5104 25.3952 0.3072 3.4816-0.2048 6.9632-1.4336 10.24-2.56 6.4512-7.9872 11.3664-14.6432 13.4144-6.656 2.048-13.9264 0.9216-19.6608-3.072-9.5232-6.5536-22.3232-5.5296-30.72 2.4576a204.98432 204.98432 0 0 0-57.6512 99.7376c-2.7648 11.264 2.8672 22.8352 13.312 27.7504 7.9872 3.7888 13.0048 11.776 13.0048 20.5824 0 8.8064-5.12 16.7936-13.0048 20.5824a24.4224 24.4224 0 0 0-13.312 27.8528c9.3184 38.0928 29.3888 72.704 57.7536 99.7376 8.3968 7.9872 21.1968 9.0112 30.72 2.3552 7.2704-5.0176 16.7936-5.4272 24.3712-0.9216 7.68 4.4032 11.9808 12.9024 11.264 21.7088-0.9216 11.5712 6.3488 22.1184 17.5104 25.3952H757.76c37.5808 10.9568 77.6192 10.9568 115.2 0a24.20736 24.20736 0 0 0 17.5104-25.3952c-0.3072-3.4816 0.2048-6.9632 1.4336-10.1376 2.56-6.4512 7.9872-11.3664 14.6432-13.4144 6.656-2.048 13.9264-0.9216 19.6608 3.072 9.5232 6.5536 22.3232 5.5296 30.6176-2.4576 28.3648-27.0336 48.4352-61.7472 57.7536-99.84 2.7648-11.264-2.8672-22.9376-13.312-27.8528z m-66.7648 80.4864a71.72096 71.72096 0 0 0-57.0368 6.2464c-17.3056 9.9328-29.696 26.7264-33.9968 46.2848a159.40608 159.40608 0 0 1-55.9104 0 71.50592 71.50592 0 0 0-34.0992-46.1824 71.33184 71.33184 0 0 0-57.0368-6.3488c-12.1856-14.336-21.7088-30.72-28.0576-48.4352a71.54688 71.54688 0 0 0 23.04-52.5312c0-19.968-8.3968-39.0144-23.04-52.5312a157.2864 157.2864 0 0 1 28.0576-48.4352c19.0464 5.9392 39.7312 3.584 57.0368-6.3488 17.3056-9.9328 29.696-26.7264 33.9968-46.1824 18.5344-3.2768 37.376-3.2768 55.9104 0 4.4032 19.456 16.7936 36.1472 34.0992 46.1824 17.3056 9.9328 37.9904 12.288 57.0368 6.3488 12.1856 14.2336 21.7088 30.72 28.0576 48.4352a71.63904 71.63904 0 0 0-23.1424 52.5312c0 19.968 8.3968 39.1168 23.1424 52.6336-6.3488 17.5104-15.872 33.8944-28.0576 48.3328z" fill="#dbdbdb" p-id="8454"></path><path d="M815.3088 691.2c-48.2304 1.2288-86.7328 40.7552-86.7328 89.088s38.5024 87.8592 86.8352 89.088a89.2928 89.2928 0 0 0 79.1552-43.9296c16.384-27.9552 16.384-62.5664 0-90.4192a89.45664 89.45664 0 0 0-79.2576-43.8272z m0 129.4336a40.32512 40.32512 0 1 1 0-80.5888c21.7088 0.8192 38.8096 18.6368 38.8096 40.3456s-17.1008 39.424-38.8096 40.2432zM858.5216 38.912h-819.2c-16.9984 0-30.72 13.7216-30.72 30.72v860.16c0 16.9984 13.7216 30.72 30.72 30.72h450.56c16.9984 0 30.72-13.7216 30.72-30.72s-13.7216-30.72-30.72-30.72h-419.84v-798.72h757.76v317.44c0 16.9984 13.7216 30.72 30.72 30.72s30.72-13.7216 30.72-30.72v-348.16c0-16.9984-13.7216-30.72-30.72-30.72z" fill="#dbdbdb" p-id="8455"></path><path d="M552.7552 701.5424H400.7936c-9.6256-35.5328-41.5744-62.0544-80.1792-62.976-40.1408-1.024-74.4448 25.9072-84.5824 62.976H137.216c-13.6192 0-24.576 10.9568-24.576 24.576 0 13.6192 10.9568 24.576 24.576 24.576h98.816c9.6256 35.5328 41.5744 62.0544 80.1792 62.976 40.1408 1.024 74.4448-25.9072 84.5824-62.976h151.9616a24.576 24.576 0 0 0 0-49.152z m-197.7344 26.4192a36.58752 36.58752 0 0 1-37.4784 35.6352c-20.1728-0.512-36.2496-17.3056-35.6352-37.4784v-2.048a36.58752 36.58752 0 0 1 37.4784-35.6352c20.1728 0.512 36.1472 17.3056 35.6352 37.4784v2.048zM735.8464 465.2032H406.9376c-9.6256-35.5328-41.5744-62.0544-80.1792-62.976-40.1408-1.024-74.4448 25.9072-84.5824 62.976H137.216c-13.6192 0-24.576 10.9568-24.576 24.576s10.9568 24.576 24.576 24.576h104.8576c9.6256 35.5328 41.5744 62.0544 80.1792 62.976 40.1408 1.024 74.4448-25.9072 84.5824-62.976h329.0112a24.576 24.576 0 0 0 0-49.152z m-374.784 26.7264a36.61824 36.61824 0 1 1-73.216-2.1504v-1.9456a36.61824 36.61824 0 1 1 73.216 1.9456v2.1504zM137.216 278.016h328.9088c9.6256 35.5328 41.5744 62.0544 80.1792 62.976 40.1408 1.024 74.4448-25.9072 84.5824-62.976h104.8576c13.6192 0 24.576-10.9568 24.576-24.576s-10.9568-24.576-24.576-24.576H630.9888c-9.6256-35.5328-41.5744-62.0544-80.1792-62.976-40.1408-1.024-74.4448 25.9072-84.5824 62.976H137.216c-13.6192 0-24.576 10.9568-24.576 24.576s10.9568 24.576 24.576 24.576z m374.784-26.624a36.61824 36.61824 0 1 1 73.216 2.1504v1.9456a36.61824 36.61824 0 1 1-73.216-1.9456v-2.1504z" fill="#dbdbdb" p-id="8456"></path></svg>
          <svg class="delete" viewBox="0 0 1024 1024" width="20" height="20" @click="deleteStyle(data)">
            <path
              d="M607.897867 768.043004c-17.717453 0-31.994625-14.277171-31.994625-31.994625L575.903242 383.935495c0-17.717453 14.277171-31.994625 31.994625-31.994625s31.994625 14.277171 31.994625 31.994625l0 351.94087C639.892491 753.593818 625.61532 768.043004 607.897867 768.043004z"
              fill="#bfbfbf"></path>
            <path
              d="M415.930119 768.043004c-17.717453 0-31.994625-14.277171-31.994625-31.994625L383.935495 383.935495c0-17.717453 14.277171-31.994625 31.994625-31.994625 17.717453 0 31.994625 14.277171 31.994625 31.994625l0 351.94087C447.924744 753.593818 433.647573 768.043004 415.930119 768.043004z"
              fill="#bfbfbf"></path>
            <path
              d="M928.016126 223.962372l-159.973123 0L768.043004 159.973123c0-52.980346-42.659499-95.983874-95.295817-95.983874L351.94087 63.989249c-52.980346 0-95.983874 43.003528-95.983874 95.983874l0 63.989249-159.973123 0c-17.717453 0-31.994625 14.277171-31.994625 31.994625s14.277171 31.994625 31.994625 31.994625l832.032253 0c17.717453 0 31.994625-14.277171 31.994625-31.994625S945.73358 223.962372 928.016126 223.962372zM319.946246 159.973123c0-17.545439 14.449185-31.994625 31.994625-31.994625l320.806316 0c17.545439 0 31.306568 14.105157 31.306568 31.994625l0 63.989249L319.946246 223.962372 319.946246 159.973123 319.946246 159.973123z"
              fill="#bfbfbf"></path>
            <path
              d="M736.048379 960.010751 288.123635 960.010751c-52.980346 0-95.983874-43.003528-95.983874-95.983874L192.139761 383.591466c0-17.717453 14.277171-31.994625 31.994625-31.994625s31.994625 14.277171 31.994625 31.994625l0 480.435411c0 17.717453 14.449185 31.994625 31.994625 31.994625l448.096758 0c17.717453 0 31.994625-14.277171 31.994625-31.994625L768.215018 384.795565c0-17.717453 14.277171-31.994625 31.994625-31.994625s31.994625 14.277171 31.994625 31.994625l0 479.231312C832.032253 916.835209 789.028725 960.010751 736.048379 960.010751z"
              fill="#bfbfbf"></path>
          </svg>
          <svg class="rename" viewBox="0 0 1024 1024" width="20" height="20" @click="renameStyle(data)">
            <path
              d="M775.84 392.768l-155.2-172.352L160.768 643.264l-38.368 187.936 190.56-12.832zM929.952 229.952l-131.2-150.944-0.288-0.32a16 16 0 0 0-22.592-0.96l-131.168 120.576 155.168 172.352 128.832-118.464a15.936 15.936 0 0 0 1.248-22.24zM96 896h832v64H96z"
              fill="#bfbfbf"></path>
          </svg>
        </div>
      </div>
    </template>
  </el-tree>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick, onBeforeMount, onMounted, defineComponent, computed } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { useEditorStore } from '../../../router/index.ts'
import axios from 'axios';
import { mainStore } from '@/store/index.ts';
import Loading2 from '../../../components/Loading2.vue';

const treeData = ref([

]);
const theme = ref('')
const defaultProps = {
  children: 'children',
  label: 'label'
};
const editorStore = useEditorStore()
const newNodeId = ref(1);
const editingNode = ref(null);
const selectedNode = ref(null);
const store = mainStore();
const showLoading = ref(true);
const username = localStorage.getItem('username');

store.setUsername(username);

const addStyle = (styleId, styleName) => {
  const newStyle = { id: styleId, label: styleName };
  treeData.value.push(newStyle);
  editingNode.value = newStyle.id;
  nextTick(() => {
    const node = document.querySelector(`[node-key="${newStyle.id}"] input`);
    if (node) {
      node.focus();
    }
  });
};


const hasStyle = computed(() => {
      return treeData.value.length > 1;
    });

const newStyle = () => {
  let username = new FormData();
  username.append('username', store.username);
  axios({
    method: 'post',
    url: `${store.ipAddress}/api/createStyle`,
    data: username,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
    if (res.data.ret == 0) {
      let name = '未命名样式';
      addStyle(res.data.id, name);
    }
  });

};

const deleteStyle = (data) => {
  ElMessageBox.confirm('确定删除此样式吗?', '提示', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning',
  }).then(() => {
    let styleId = new FormData();
    styleId.append('id', data.id);
    styleId.append('username', store.username);
    axios({
      method: 'post',
      url: `${store.ipAddress}/api/delStyle`,
      data: styleId,
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }).then(res => {
    });
    const index = treeData.value.findIndex(style => style.id === data.id);
    if (index !== -1) {
      treeData.value.splice(index, 1);
      if(!hasStyle.value){
    store.openStyleID = null;
    store.usedStyleID = 1;
    store.editorisShow = false;
  }
    }
  });

};

const renameStyle = (data) => {
  // store.isShow = false;
  editingNode.value = data.id;
  nextTick(() => {
    const node = document.querySelector(`[node-key="${data.id}"] input`);
    if (node) {
      node.focus();
    }
  });
};

const finishEditing = (data) => {
  editingNode.value = null;
  if (!data.label.trim()) {
    ElMessage.error('样式名不能为空');
    data.label = '未命名样式';
  }
  let formData = new FormData();
  formData.append('id', data.id);
  formData.append('styleName', data.label);
  formData.append('username', store.username);
  axios({
    method: 'post',
    url: `${store.ipAddress}/api/renameStyle`,
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
  });
};


const handleNodeDrop = (draggingNode, dropNode, dropType) => {
  const draggingNodeIndex = treeData.value.findIndex(style => style.id === draggingNode.data.id);
  const dropNodeIndex = treeData.value.findIndex(style => style.id === dropNode.data.id);

  if (dropType === 'before') {
    treeData.value.splice(dropNodeIndex, 0, ...treeData.value.splice(draggingNodeIndex, 1));
  } else if (dropType === 'after') {
    treeData.value.splice(dropNodeIndex + 1, 0, ...treeData.value.splice(draggingNodeIndex, 1));
  }
};

const applyStyle = (data) => {
  if(store.isShow){
  store.setUsedStyleID(data.id);

  let formdata = new FormData();
  formdata.append("username", store.username);

  axios({
    method: 'post',
    url: `${store.ipAddress}/api/pullStyleList`,
    data: formdata,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
    let styleConfig = null;

    for (let i = 0; i < res.data.styleList.length; i++) {
      if (res.data.styleList[i][0] === store.usedStyleID) {
        styleConfig = JSON.parse(res.data.styleList[i][2]);
        break;
      }
    }

    if (styleConfig) {
      store.setStyleConfig(styleConfig);
      store.applyStylesFromConfig();
    } else {
      console.error("No matching style configuration found");
    }
  }).catch(error => {
    console.error("Error fetching style list:", error);
  });
}
}

const addStyleWithoutRename = (styleId, styleName) => {
  const newStyle = { id: styleId, label: styleName };
  treeData.value.push(newStyle);
  nextTick(() => {
    const node = document.querySelector(`[node-key="${newStyle.id}"] input`);
    if (node) {
      node.focus();
    }
  });
};
onBeforeMount(() => {
  let username = new FormData();
  username.append('username', store.username);
  axios({
    method: 'post',
    url: `${store.ipAddress}/api/pullStyleList`,
    data: username,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
    for (let i = 0; i < res.data.styleList.length; i++) {

      addStyleWithoutRename(res.data.styleList[i][0], res.data.styleList[i][1]);
    }
  }).finally(() => {
    showLoading.value = false;
  });
});

onMounted(() => {
  store.initializeTheme();
  theme.value = store.theme;
});

function showStyleEditor(data) {
  store.setOpenStyleID(data.id);
  let formdata = new FormData();
  formdata.append("username", store.username);
  axios({
    method: 'post',
    url: `${store.ipAddress}/api/pullStyleList`,
    data: formdata,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(res => {
    for (let i = 0; i < res.data.styleList.length; i++) {
    if (res.data.styleList[i][0] == store.openStyleID) {
    const StyleConfig = res.data.styleList[i][2];
    store.setStyleConfig(JSON.parse(StyleConfig));
    }
    }
  });
  store.isShow = false;
  store.setOpenNoteID(null);
  store.editorisShow = true;
}

</script>

<style scoped>
.file-manager {
  height: 100%;
}

.add-style {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
  background-color: var(--backgroudColor);
}


.add-style h2 {
  flex: 2;
  text-align: center;
  color: var(--titleColor);
}
.add-style svg {
  max-width: 6%;
  max-height: 6%;
  width: auto;
  height: auto;
  object-fit: contain;
  margin-left: auto;
  margin-right: 20px;
  cursor: pointer;
  filter: invert(var(--invert));
}

.content {
  position: relative;
  width: auto;
  height: calc(100% - 85.84px);
  object-fit: contain;
  /* background-color: rgba(134, 134, 134, 0.683); */
}

.el-tree {
  border: 1px solid var(--treeColor);
  background-color: var(--treeColor);
  color: var(--titleColor);
  border-radius: 10px;
  padding: 10px;
  max-height: 100%;

  overflow-y: auto;
}

:deep().el-tree>.el-tree-node>.el-tree-node__content:hover {
  background-color: var(--hoverColor);
  border-radius: 5px;
}

:deep().el-tree>.el-tree-node.is-current>.el-tree-node__content {
  background-color: var(--currentColor);
  border-radius: 5px;

}



.el-input {
  width: auto;
  height: 25px;
  background-color: #cce5ff6b;
}

:deep().el-input>.el-input__wrapper {
  background-color: #abababc6;
  border-radius: 5px;
}

:deep().el-input>.el-input__wrapper>.el-input__inner {
  color: var(btnColor);
}




.file-item {
  display: flex;
  flex: 1;
  align-items: center;
  justify-content: space-between;
  padding-right: 8px;
  width: auto;
}

.file-item span {
  display: inline-block;
  max-width: 300px;
  /* Adjust this value as needed */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  vertical-align: middle;
}


.file-icon {
  padding-right: 0pxs;
  display: flex;
  margin-right: 0px;
}

.delete {
  width: 20px;
  height: 20px;
  margin-right: 5px;
  margin-left: 0px;
  cursor: pointer;
  filter: invert(var(--invert));
}

.rename {
  width: 20px;
  height: 20px;
  margin-right: 0px;
  margin-left: 0px;
  cursor: pointer;
  filter: invert(var(--invert));
}

.editing {
  width: 20px;
  height: 20px;
  margin-right: 6px;
  margin-left: 0px;
  cursor: pointer;
  filter: invert(var(--invert));
}
</style>
