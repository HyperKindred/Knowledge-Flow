<template>
  <div class="main"></div>
  <div class="top_tool">
    <h2>样式编辑</h2>
    <button class="saveStyle" @click="saveStyleConfig()">Save</button>
  </div>
  <div class="main_editor">
    <div v-for="(styleGroup, groupName) in store.stylesConfig" :key="groupName" class="editor-group">
      <div v-if="groupName !== 'heading'" class="editor-heading">
        <h3>{{ groupName }}</h3>
      </div>
      <div class="editor">
        <div v-if="groupName === 'heading'">
          <div v-for="(style, styleName) in styleGroup" :key="styleName">
            <h3>{{ groupName }} {{ styleName }}</h3>
            <div class="style-options">
              <div v-for="(value, key) in style" :key="key" class="style-item">
                <label>{{ key }}:</label>
                <input
                  v-if="key === 'color'"
                  type="color"
                  :value="value"
                  @input="updateStyle(groupName, styleName, key, $event.target.value)"
                />
                <input
                  v-else-if="key === 'font-size'"
                  type="number"
                  :value="parseInt(value)"
                  @input="updateStyle(groupName, styleName, key, $event.target.value + 'px')"
                />
                <input
                  v-else
                  type="text"
                  :value="value"
                  @input="updateStyle(groupName, styleName, key, $event.target.value)"
                />
              </div>
            </div>
          </div>
        </div>
        <div v-else>
          <div class="style-options">
            <div v-for="(value, key) in styleGroup" :key="key" class="style-item">
              <label>{{ key }}:</label>
              <input
                v-if="key === 'color'"
                type="color"
                :value="value"
                @input="updateStyle(groupName, null, key, $event.target.value)"
              />
              <input
                v-else-if="key === 'font-size'"
                type="number"
                :value="parseInt(value)"
                @input="updateStyle(groupName, null, key, $event.target.value + 'px')"
              />
              <input
                v-else
                type="text"
                :value="value"
                @input="updateStyle(groupName, null, key, $event.target.value)"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { useEditorStore } from '../../../router/index.ts';
import axios from 'axios';
import { mainStore } from '@/store/index.ts';
const store = mainStore();

const stylesConfig = computed(() => store.stylesConfig);

const updateStyle = (group, style, key, value) => {
    store.updateStyleConfig(group, style, key, value);
};
const saveStyleConfig = () => {
  let jsonString = JSON.stringify(store.stylesConfig, null, 2);
  let formdata = new FormData();
  formdata.append("username", store.username);
  formdata.append("id", store.openStyleID);
  formdata.append("style", jsonString);
  axios({
    method: 'post',
    url: `${store.ipAddress}/api/saveStyle`,
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
</script>

<style scoped>
.top_tool {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgba(207, 220, 245, 0.199);
  border-bottom: 1px dashed #9ca19f65;
  margin-top: 5px;
  height: 70px;
  position: relative;
}



.saveStyle {
  background-color: rgba(173, 212, 247, 0.813);
  color: beige;
}

.top_tool h2 {
  flex: 2;
  text-align: center;
}

.main_editor {
  display: flex;
  flex-direction: column;
  margin-top: 5px;
  overflow-y: scroll;
  height: 700px;
}

.editor-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.editor-heading {
  margin-bottom: 10px;
}

.editor {
  display: flex;
  flex-direction: column;
}

.style-options {
  display: flex;
  flex-wrap: wrap;
}

.style-item {
  display: flex;
  flex-direction: column;
  margin-right: 20px;
  margin-bottom: 10px;
}

.style-item label {
  margin-bottom: 5px;
}
</style>
