<template>
  <div class="outline__list" style="display: flex; flex-direction: column;">
    <h2 class="text-gray-400">大纲</h2>
    <template v-for="(heading, index) in headings" :key="index">
      <el-popover trigger="click" placement="right">
        <template #reference>
          <el-button @click="handleHeadingClick(heading.text)" text class="outline__item"
            :class="`outline__item--${heading.level}`">
            {{ heading.text }}
            <el-icon v-if="heading.icon">
              <component :is="heading.icon" />
            </el-icon>
          </el-button>
        </template>
        <!-- 如果需要弹出内容，请在这里添加 -->
      </el-popover>
    </template>
  </div>
</template>

<script setup lang="ts">
import { mainStore } from '@/store'; // Import from correct path
import { storeToRefs } from 'pinia';
import { onMounted, ref } from 'vue';

const store = mainStore();
const { headings } = storeToRefs(store);
const theme = ref('')
/**
 * 左侧区域
 */
const setActiveHeading = (data: string) => {
  // Your logic for handling the active heading
  console.log('Active heading:', data);
}

const handleHeadingClick = (data: string) => {
  setActiveHeading(data);
}

onMounted(() => {
  store.initializeTheme();
  theme.value = store.theme;
});
</script>

<style scoped lang="scss">
.outline {
  position: relative;
  opacity: 0.75;
  border-radius: 0.5rem;
  padding: 0.75rem;
  background: var(--backgroundColor);

  &__list {
    list-style: none;
    font-size: 18px;
    padding: 0;
  }

  &__item {
    a:hover {
      opacity: 0.5;
    }

    &--1 {
      font-size: 23px;
    }

    &--3 {
      padding-left: 1rem;
    }

    &--4 {
      padding-left: 2rem;
    }

    &--5 {
      padding-left: 3rem;
    }

    &--6 {
      padding-left: 4rem;
    }
  }
}

.text-gray-400 {
  position: relative;
  display: flex;
  align-items: center; 
  justify-content: center; 
  color: var(--titleColor);
}

.el-button {
  max-width: 100%;
  white-space: normal; // Allow text to wrap
  overflow-wrap: break-word; // Break long words
  word-wrap: break-word; // Support for older browsers
}
.outline__item{
  display: flex;
  justify-content: left;
  color: var(--titleColor);
}
</style>
