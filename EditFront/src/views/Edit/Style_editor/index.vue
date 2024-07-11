<template>
  <div class="main">
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
                  <label>{{ getLabel(key) }}:</label>
                  <el-select v-if="key === 'font-size'" v-model="style[key]" placeholder="请选择字体大小" class="style-select">
                    <el-option
                      v-for="size in fontSizes"
                      :key="size"
                      :label="size + 'px'"
                      :value="size + 'px'"
                    ></el-option>
                  </el-select>
                  <el-select v-else-if="key === 'font-family'" v-model="style[key]" placeholder="请选择字体样式" class="style-select">
                    <el-option
                      v-for="font in fonts"
                      :key="font"
                      :label="font"
                      :value="font"
                    ></el-option>
                  </el-select>
                  <el-select v-else-if="key === 'margin-top' || key === 'margin-bottom'" v-model="style[key]" placeholder="请选择行间距" class="style-select">
                    <el-option
                      v-for="space in lineHeights"
                      :key="space"
                      :label="space + 'px'"
                      :value="space + 'px'"
                    ></el-option>
                  </el-select>
                  <input
                    v-else-if="key === 'color'"
                    type="color"
                    :value="value"
                    @input="updateStyle(groupName, styleName, key, $event.target.value)"
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
                <label>{{ getLabel(key) }}:</label>
                <el-select v-if="key === 'font-size'" v-model="styleGroup[key]" placeholder="请选择字体大小" class="style-select">
                  <el-option
                    v-for="size in fontSizes"
                    :key="size"
                    :label="size + 'px'"
                    :value="size + 'px'"
                  ></el-option>
                </el-select>
                <el-select v-else-if="key === 'font-family'" v-model="styleGroup[key]" placeholder="请选择字体样式" class="style-select">
                  <el-option
                    v-for="font in fonts"
                    :key="font"
                    :label="font"
                    :value="font"
                  ></el-option>
                </el-select>
                <el-select v-else-if="key === 'margin-top' || key === 'margin-bottom'" v-model="styleGroup[key]" placeholder="请选择行间距" class="style-select">
                  <el-option
                    v-for="space in lineHeights"
                    :key="space"
                    :label="space + 'px'"
                    :value="space + 'px'"
                  ></el-option>
                </el-select>
                <input
                  v-else-if="key === 'color'"
                  type="color"
                  :value="value"
                  @input="updateStyle(groupName, null, key, $event.target.value)"
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
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { ElMessage, ElMessageBox, ElSelect, ElOption } from 'element-plus';
import { useEditorStore } from '../../../router/index.ts';
import axios from 'axios';
import { mainStore } from '@/store/index.ts';
const store = mainStore();
const theme = ref('')
const stylesConfig = computed(() => store.stylesConfig);

const fontSizes = ['12', '14', '16', '18', '20', '22', '24', '26', '28', '30'];
const fonts = ['Arial', 'Helvetica', 'Times New Roman', 'Courier New', 'Verdana', 'Microsoft YaHei', 'SimSun', 'SimHei'];
const lineHeights = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50'];

const updateStyle = (group, style, key, value) => {
    store.updateStyleConfig(group, style, key, value);
};

const getLabel = (key) => {
  switch (key) {
    case 'font-size':
      return '字体大小';
    case 'font-family':
      return '字体样式';
    case 'color':
      return '字体颜色';
    case 'margin-top':
      return '上行间距';
    case 'margin-bottom':
      return '下行间距';
    default:
      return key;
  }
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
  background-color: rgba(121, 121, 121, 0.685);
  margin-top: 5px;
  height: 70px;
  position: relative;
}

.saveStyle {
  background-color: var(--btnColor);
  color: var(--titleColor);
  border: 1.5px solid var(--titleColor);
  margin-right: 20px;
  margin-left: auto;
}
.top_tool h2 {
  flex: 2;
  text-align: center;
}

.main {
  padding-left: 0.2%;
}
.main_editor {
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
  height: 700px;
  background-color: var(--editorColor);
}

.editor-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
  padding-left: 5%;
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
  gap: 20px;
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

.style-select {
  width: 200px;
}
</style>
