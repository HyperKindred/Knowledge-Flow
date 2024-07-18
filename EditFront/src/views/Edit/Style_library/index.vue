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
    @node-click="handleNodeClick"
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
          <svg t="1719995366880" @click="showStyleEditor(data)" class="editing" viewBox="0 0 1024 1024" version="1.1"
            xmlns="http://www.w3.org/2000/svg" p-id="3148" width="200" height="200">
            <path
              d="M880.288 232.48L560.192 45.12a95.648 95.648 0 0 0-96.64 0L143.68 232.48A96.64 96.64 0 0 0 96 315.904v397.664c0 34.784 18.624 66.88 48.736 84l320 181.92a95.52 95.52 0 0 0 94.496 0l320-181.92A96.576 96.576 0 0 0 928 713.568V315.904a96.64 96.64 0 0 0-47.712-83.424zM864 713.568c0 11.584-6.208 22.304-16.256 28l-320 181.92a31.776 31.776 0 0 1-31.488 0l-320-181.92A32.192 32.192 0 0 1 160 713.568V315.904c0-11.456 6.048-22.048 15.904-27.808l319.872-187.36a31.84 31.84 0 0 1 32.192 0l320.128 187.392c9.856 5.728 15.904 16.32 15.904 27.776v397.664z"
              p-id="3149" fill="#e6e6e6"></path>
            <path
              d="M512 320a192 192 0 1 0 0 384 192 192 0 0 0 0-384z m0 320a128 128 0 1 1 0-256 128 128 0 0 1 0 256z"
              p-id="3150" fill="#e6e6e6"></path>
          </svg>
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

const handleNodeClick = (data) => {
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