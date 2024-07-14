<template>
  <div>
    <template v-for="(item, index) in items">
      <div class="divider" v-if="item.type === 'divider'" :key="`divider${index}`" />
      <MenuItem v-else :key="index" v-bind="item" />
    </template>
  </div>
</template>

<script setup lang="ts">
import { Editor } from '@tiptap/vue-3'
import { mainStore } from '@/store';
import MenuItem from '@/views/Edit/MenuItem/index.vue'



const store = mainStore();


const items = [
  {
    icon: 'bold',
    title: 'Bold',
    action: () => store.editor?.chain().focus().toggleBold().run(),
    isActive: () => store.editor?.isActive('bold'),
    iconType: 'remix'
  },
  {
    icon: 'italic',
    title: 'Italic',
    action: () => store.editor?.chain().focus().toggleItalic().run(),
    isActive: () => store.editor?.isActive('italic'),
    iconType: 'remix'
  },
  {
    icon: 'strikethrough',
    title: 'Strike',
    action: () => store.editor?.chain().focus().toggleStrike().run(),
    isActive: () => store.editor?.isActive('strike'),
    iconType: 'remix'
  },
  {
    icon: 'code-view',
    title: 'Code',
    action: () => store.editor?.chain().focus().toggleCode().run(),
    isActive: () => store.editor?.isActive('code'),
    iconType: 'remix'
  },
  {
    icon: 'mark-pen-line',
    title: 'Highlight',
    action: () => store.editor?.chain().focus().toggleHighlight().run(),
    isActive: () => store.editor?.isActive('highlight'),
    iconType: 'remix'
  },
  {
    type: 'divider'
  },
  {
    icon: 'h-1',
    title: 'Heading 1',
    action: () => {
      store.editor.chain().focus().toggleHeading({ level: 1 }).run();
      store.applyStylesFromConfig();
      // alert(JSON.stringify(store.stylesConfig, null, 2));
    },
    isActive: () => store.editor.isActive('heading', { level: 1 }),
    iconType: 'remix'
  },
  {
    icon: 'h-2',
    title: 'Heading 2',
    action: () => {
      store.editor?.chain().focus().toggleHeading({ level: 2 }).run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor?.isActive('heading', { level: 2 }),
    iconType: 'remix'
  },
  {
    icon: 'h-3',
    title: 'Heading 3',
    action: () => {
      store.editor?.chain().focus().toggleHeading({ level: 3 }).run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor?.isActive('heading', { level: 3 }),
    iconType: 'remix'

  },
  {
    icon: 'h-4',
    title: 'Heading 4',
    action: () => {
      store.editor?.chain().focus().toggleHeading({ level: 4 }).run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor?.isActive('heading', { level: 4 }),
    iconType: 'remix'
  },
  {
    icon: 'paragraph',
    title: 'Paragraph',
    action: () => {
      store.editor.chain().focus().setParagraph().run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor.isActive('paragraph'),
    iconType: 'remix'
  },
  {
    icon: 'list-unordered',
    title: 'Bullet List',
    action: () => {
      store.editor.chain().focus().toggleBulletList().run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor.isActive('bulletList'),
    iconType: 'remix'
  },
  {
    icon: 'list-ordered',
    title: 'Ordered List',
    action: () => {
      store.editor.chain().focus().toggleOrderedList().run();
      store.applyStylesFromConfig();
    },
    isActive: () => store.editor.isActive('orderedList'),
    iconType: 'remix'
  },
  {
    icon: 'list-check-2',
    title: 'Task List',
    action: () => store.editor?.chain().focus().toggleTaskList().run(),
    isActive: () => store.editor?.isActive('taskList'),
    iconType: 'remix'
  },
  {
    icon: 'code-box-line',
    title: 'Code Block',
    action: () => store.editor?.chain().focus().toggleCodeBlock().run(),
    isActive: () => store.editor?.isActive('codeBlock'),
    iconType: 'remix'
  },
  {
    icon: 'custom-icon',
    title: 'Convert to Markdown',
    iconType: 'custom',
    action: () => {
      if (store.convertSelectionToMarkdown) {
        store.convertSelectionToMarkdown(); // 调用方法
      } else {
        console.error('convertSelectionToMarkdown 方法不存在');
      }
    },
    isActive: () => false,
  },
  {
    type: 'divider'
  },
  {
    icon: 'double-quotes-l',
    title: 'Blockquote',
    action: () => store.editor?.chain().focus().toggleBlockquote().run(),
    isActive: () => store.editor?.isActive('blockquote'),
    iconType: 'remix'
  },
  {
    icon: 'separator',
    title: 'Horizontal Rule',
    action: () => store.editor?.chain().focus().setHorizontalRule().run(),
    iconType: 'remix'
  },
  {
    type: 'divider'
  },
  {
    icon: 'text-wrap',
    title: 'Hard Break',
    action: () => store.editor?.chain().focus().setHardBreak().run(),
    iconType: 'remix'
  },
  {
    icon: 'format-clear',
    title: 'Clear Format',
    action: () =>
      store.editor?.chain().focus().clearNodes().unsetAllMarks().run(),
    iconType: 'remix'
  },
  {
    type: 'divider'
  },
  {
    icon: 'arrow-go-back-line',
    title: 'Undo',
    action: () => store.editor?.chain().focus().undo().run(),
    iconType: 'remix'
  },
  {
    icon: 'arrow-go-forward-line',
    title: 'Redo',
    action: () => store.editor?.chain().focus().redo().run(),
    iconType: 'remix'
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
