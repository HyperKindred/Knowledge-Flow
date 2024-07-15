<template>
  <div>
    <template v-for="(item, index) in items" :key="item.key">
      <div class="divider" v-if="item.type === 'divider'" />
      <!-- @ts-ignore -->
      <MenuItem v-else :key="item.key" v-bind="item" />
    </template>
  </div>
</template>

<script setup lang="ts">
import { mainStore } from '@/store';
import MenuItem from '@/views/Edit/MenuItem/index.vue'

const store = mainStore();

// 定义 MenuItem 的 Props 类型
interface MenuItemProps {
  icon: string;
  title: string;
  action: () => void;
  isActive: () => boolean;
  iconType: string;
  type: 'normal';
  key: number;
}

// 定义 Divider 类型的 Props
interface DividerProps {
  type: 'divider';
  key: number;
}

// 确保 `items` 数组的类型满足 `MenuItem` 组件的 Props 和 Divider 类型
const items: (MenuItemProps | DividerProps)[] = [
  {
    icon: 'bold',
    title: 'Bold',
    action: () => store.editor?.chain().focus().toggleBold().run(),
    isActive: () => store.editor?.isActive('bold'),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 1,
  },
  {
    icon: 'italic',
    title: 'Italic',
    action: () => store.editor?.chain().focus().toggleItalic().run(),
    isActive: () => store.editor?.isActive('italic'),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 2,
  },
  {
    icon: 'strikethrough',
    title: 'Strike',
    action: () => store.editor?.chain().focus().toggleStrike().run(),
    isActive: () => store.editor?.isActive('strike'),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 3,
  },
  {
    icon: 'code-view',
    title: 'Code',
    action: () => store.editor?.chain().focus().toggleCode().run(),
    isActive: () => store.editor?.isActive('code'),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 4,
  },
  {
    icon: 'mark-pen-line',
    title: 'Highlight',
    action: () => store.editor?.chain().focus().toggleHighlight().run(),
    isActive: () => store.editor?.isActive('highlight'),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 5,
  },
  {
    type: 'divider',
    key: 6,
  },
  {
    icon: 'h-1',
    title: 'Heading 1',
    action: () => {
      store.editor.chain().focus().toggleHeading({ level: 1 }).run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor.isActive('heading', { level: 1 }),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 7,
  },
  {
    icon: 'h-2',
    title: 'Heading 2',
    action: () => {
      store.editor?.chain().focus().toggleHeading({ level: 2 }).run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor?.isActive('heading', { level: 2 }),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 8,
  },
  {
    icon: 'h-3',
    title: 'Heading 3',
    action: () => {
      store.editor?.chain().focus().toggleHeading({ level: 3 }).run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor?.isActive('heading', { level: 3 }),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 9,
  },
  {
    icon: 'h-4',
    title: 'Heading 4',
    action: () => {
      store.editor?.chain().focus().toggleHeading({ level: 4 }).run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor?.isActive('heading', { level: 4 }),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 10,
  },
  {
    icon: 'paragraph',
    title: 'Paragraph',
    action: () => {
      store.editor.chain().focus().setParagraph().run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor.isActive('paragraph'),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 11,
  },
  {
    icon: 'list-unordered',
    title: 'Bullet List',
    action: () => {
      store.editor.chain().focus().toggleBulletList().run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor.isActive('bulletList'),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 12,
  },
  {
    icon: 'list-ordered',
    title: 'Ordered List',
    action: () => {
      store.editor.chain().focus().toggleOrderedList().run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor.isActive('orderedList'),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 13,
  },
  {
    icon: 'list-check-2',
    title: 'Task List',
    action: () => store.editor?.chain().focus().toggleTaskList().run(),
    isActive: () => store.editor?.isActive('taskList'),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 14,
  },
  {
    icon: 'code-box-line',
    title: 'Code Block',
    action: () => store.editor?.chain().focus().toggleCodeBlock().run(),
    isActive: () => store.editor?.isActive('codeBlock'),  // 添加 isActive 函数
    iconType: 'remix',
    type: 'normal',
    key: 15,
  },
  {
    icon: 'custom-icon',
    title: 'Convert to Markdown',
    iconType: 'custom',
    action: () => {
      if (store.convertSelectionToMarkdown) {
        store.convertSelectionToMarkdown();
      }
    },
    isActive: () => false,  // 添加 isActive 函数
    key: 16,
    type: 'normal',
  },
  {
    icon: 'align-left',
    title: 'Align Left',
    action: () => store.editor?.chain().focus().setTextAlign('left').run(),
    iconType: 'remix',
    type: 'normal',
    isActive: () => store.editor?.isActive({ textAlign: 'left' }),  // 添加 isActive 函数
    key: 17,
  },
  {
    icon: 'align-center',
    title: 'Align Center',
    action: () => store.editor?.chain().focus().setTextAlign('center').run(),
    iconType: 'remix',
    type: 'normal',
    isActive: () => store.editor?.isActive({ textAlign: 'center' }),  // 添加 isActive 函数
    key: 18,
  },
  {
    icon: 'align-right',
    title: 'Align Right',
    action: () => store.editor?.chain().focus().setTextAlign('right').run(),
    iconType: 'remix',
    type: 'normal',
    isActive: () => store.editor?.isActive({ textAlign: 'right' }),  // 添加 isActive 函数
    key: 19,
  },
  {
    // @ts-ignore
    icon: 'separator',
    title: 'Separator',
    iconType: 'remix',
    type: 'divider',
    key: 20,
  },
  {
    icon: 'text-wrap',
    title: 'Wrap Text',
    action: () => store.editor?.chain().focus().setHardBreak().run(),
    iconType: 'remix',
    type: 'normal',
    isActive: () => false,  // 添加 isActive 函数
    key: 21,
  },
  {
    icon: 'format-clear',
    title: 'Clear Format',
    action: () => store.editor?.chain().focus().clearNodes().unsetAllMarks().run(),
    iconType: 'remix',
    type: 'normal',
    isActive: () => false,  // 添加 isActive 函数
    key: 22,
  },
  {
    type: 'divider',
    key: 23,
  },
  {
    icon: 'arrow-go-back-line',
    title: 'Undo',
    action: () => store.editor?.chain().focus().undo().run(),
    iconType: 'remix',
    type: 'normal',
    isActive: () => false,  // 添加 isActive 函数
    key: 24,
  },
  {
    icon: 'arrow-go-forward-line',
    title: 'Redo',
    action: () => store.editor?.chain().focus().redo().run(),
    iconType: 'remix',
    type: 'normal',
    isActive: () => false,  // 添加 isActive 函数
    key: 25,
  }
]

</script>

<style lang="scss">
.divider {
  background-color: rgba(#fff, 0.25);
  height: 1.25rem;
  margin-left: 0.5rem;
  margin-right: 0.75rem;
  width: 1px;
  display: inline-block;
}
</style>
