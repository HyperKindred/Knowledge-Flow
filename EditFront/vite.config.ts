import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  css: {
  },
  server: {
    proxy: {
      '/api': {
        ws: true,
        target: 'https://ban2qdz2qaqbp8w5.aistudio-hub.baidu.com/api/', //这里填入你要请求的接口的前缀
        changeOrigin: true,   //是否跨域
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
  build: {
    outDir: 'dist', // 构建输出目录
    assetsDir: 'assets', // 静态资源目录
  }
})
