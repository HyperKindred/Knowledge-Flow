import { Extension } from '@tiptap/core'
import MarkdownIt from 'markdown-it'

export const Markdown = Extension.create({
  name: 'markdown',

  addOptions() {
    return {
      markdownIt: {},
    }
  },

  addStorage() {
    return {
      parser: null,
    }
  },

  addCommands() {
    return {
      setMarkdownContent: (markdown) => ({ commands }) => {
        const html = this.storage.parser.render(markdown)
        commands.setContent(html, true)
      },
    }
  },

  onCreate() {
    this.storage.parser = new MarkdownIt(this.options.markdownIt)
  },

  addProseMirrorPlugins() {
    return []
  },
})
