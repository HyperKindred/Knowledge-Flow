import { defineStore } from 'pinia';
import { useEditor } from '@tiptap/vue-3';
import StarterKit from '@tiptap/starter-kit';
import Paragraph from '@tiptap/extension-paragraph';
import TaskList from '@tiptap/extension-task-list';
import TaskItem from '@tiptap/extension-task-item';
import Placeholder from '@tiptap/extension-placeholder';
import OrderedList from '@tiptap/extension-ordered-list';
import BulletList from '@tiptap/extension-bullet-list';
import ListItem from '@tiptap/extension-list-item';
import CharacterCount from '@tiptap/extension-character-count';
import { Extension } from '@tiptap/core';
import { Highlight } from '@tiptap/extension-highlight'
import { Italic } from '@tiptap/extension-italic'
import { Markdown } from 'tiptap-markdown';

export const mainStore = defineStore('main', {
  state: () => ({
    ipAddress: 'http://123.57.215.19:5000',
    isShow: false,
    editorisShow: false,
    openStyleID: null,
    openNoteID: null,
    usedStyleID: null,
    htmlContent: null,
    editor: null,
    username: null,
    content: null,
    select: null,
    isLoading: false,
    headings: [],
    background: "night_background",
    theme: localStorage.getItem('theme') || 'dark',
    stylesConfig: {
      heading: {
        1: {
          'font-size': '30px',
          'font-family': 'Arial, sans-serif',
          'color': 'white',
          'margin-top': '10px',
          'margin-bottom': '10px',
        },
        2: {
          'font-size': '25px',
          'font-family': 'Arial, sans-serif',
          'color': 'white',
          'margin-top': '8px',
          'margin-bottom': '8px',
        },
        3: {
          'font-size': '20px',
          'font-family': 'Arial, sans-serif',
          'color': 'white',
          'margin-top': '5px',
          'margin-bottom': '5px',
        },
        4: {
          'font-size': '16px',
          'font-family': 'Arial, sans-serif',
          'color': 'white',
          'margin-top': '5px',
          'margin-bottom': '5px',
        },
      },
      paragraph: {
        'font-size': '16px',
        'font-family': 'Arial, sans-serif',
        'color': 'white',
        'margin-top': '5px',
        'margin-bottom': '5px',
      },
      bulletList: {
        'font-size': '16px',
        'font-family': 'Arial, sans-serif',
        'color': 'white',
        'margin-top': '5px',
        'margin-bottom': '5px',
      },
      orderedList: {
        'font-size': '16px',
        'font-family': 'Arial, sans-serif',
        'color': 'white',
        'margin-top': '5px',
        'margin-bottom': '5px',
      },
    },
  }),
  getters: {},
  actions: {
    updateStyleConfig(group, style, key, value) {
      if (style) {
        this.stylesConfig[group][style][key] = value;
      } else {
        this.stylesConfig[group][key] = value;
      }
    },
    setOpenNoteID(id) {
      this.openNoteID = id;
    },
    setUsedStyleID(id) {
      this.usedStyleID = id;
    },
    setOpenStyleID(id) {
      this.openStyleID = id;
    },
    setHTMLContent(newContent) {
      this.htmlContent = newContent;
    },
    setStyleConfig(newStylesConfig) {
      this.stylesConfig = newStylesConfig;
    },
    initializeEditor() {
      this.editor = useEditor({
        content: ``,
        extensions: [
          StarterKit.configure({
            heading: {
              levels: [1, 2, 3, 4, 5],
            },
          }),
          Markdown,
          Highlight.configure({
            multicolor: true,  // 可选，允许多种颜色高亮
            color: '#ffeb3b', // 可选，设置默认高亮颜色
          }),
          Italic,
          ExtendedStyle,
          Paragraph,
          TaskList,
          TaskItem,
          Placeholder.configure({
            placeholder: '开启知识之旅~',
          }),
          OrderedList,
          BulletList,
          ListItem,
          CharacterCount.configure({
            limit: 10000,
          }),
        ],
        onUpdate: ({ editor }) => {
          this.loadHeadings(editor);
          this.setEditorInstance(editor);
        },
        onCreate: ({ editor }) => {
          this.loadHeadings(editor);
          this.setEditorInstance(editor);
        },
        injectCSS: false,
      });
    },
    setEditorInstance(editorInstance) {
      this.editor = editorInstance;
    },
    setElementStyle(style) {
      if (this.editor) {
        this.editor.chain().focus().setElementStyle(style).run();
      }
    },
    setAllElementsStyle(type, level, style) {
      if (this.editor) {
        this.editor.chain().focus().setAllElementsStyle(type, level, style).run();
        this.isLoading = true;
      } else {
        alert('editor is not ready');
      }
    },
    loadHeadings(editor) {
      const headings = [];
      editor.state.doc.descendants((node, pos) => {
        if (node.type.name === 'heading') {
          headings.push({
            text: node.textContent,
            level: node.attrs.level,
            pos,
          });
        }
      });
      this.headings = headings;
    },
    applyStylesFromConfig() {
      const styleGroups = Object.keys(this.stylesConfig);
      styleGroups.forEach(group => {
        const styles = this.stylesConfig[group];
        if (group === 'heading') {
          const levels = Object.keys(styles);
          levels.forEach(level => {
            const styleObj = styles[level];
            const styleString = Object.entries(styleObj)
              .map(([key, value]) => `${key}: ${value}`)
              .join('; ');
            this.setAllElementsStyle(group, parseInt(level), styleString);
          });
        } else {
          const styleString = Object.entries(styles)
            .map(([key, value]) => `${key}: ${value}`)
            .join('; ');
          this.setAllElementsStyle(group, null, styleString);
        }
      });
    },
    setContent(content: string) {
      this.content = content
    },
    setSelect(select: string) {
      this.select = select
    },
    setUsername(username: string) {
      this.username = username
    },
    toggleTheme() {
      this.theme = this.theme === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('theme', this.theme);
      localStorage.setItem('theme', this.theme);
    },

    setTheme(theme: string) {
      this.theme = theme;
      document.documentElement.setAttribute('theme', theme);
      localStorage.setItem('theme', theme);
    },
    initializeTheme() {
      document.documentElement.setAttribute('theme', this.theme);
    },

  },
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
      setElementStyle: style => ({ commands }) => {
        const types = ['heading', 'paragraph', 'bulletList', 'orderedList'];
        let updated = false;
        types.forEach(type => {
          updated = commands.updateAttributes(type, { style }) || updated;
        });
        return updated;
      },
      setAllElementsStyle: (type, level, style) => ({ state, dispatch }) => {
        const { tr } = state;
        state.doc.descendants((node, pos) => {
          if (node.type.name === type && (level === null || node.attrs.level === level)) {
            let newStyle = (node.attrs.style || '').split(';').filter(Boolean);

            // Convert the style string to a key-value map
            const styleMap = {};
            newStyle.forEach(s => {
              const [key, value] = s.split(':').map(str => str.trim());
              styleMap[key] = value;
            });

            // Add new styles to the map
            style.split(';').filter(Boolean).forEach(s => {
              const [key, value] = s.split(':').map(str => str.trim());
              styleMap[key] = value;
            });

            // Convert the style map back to a string
            newStyle = Object.entries(styleMap).map(([key, value]) => `${key}: ${value}`).join('; ');

            const newAttrs = {
              ...node.attrs,
              style: newStyle,
            };

            tr.setNodeMarkup(pos, undefined, newAttrs);
          }
        });

        if (tr.docChanged) {
          dispatch(tr);
        }

        return true;
      },

    };
  },
});
