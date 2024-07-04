import { h, ref, type Component } from 'vue'
import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import { defineStore} from 'pinia'

// 定义 useEditorStore
export const useEditorStore = defineStore('editor', () => {
  const headings = ref()
  const activeHeading = ref()
  const editorInstance = ref()
  
  const setHeadings = (data) => {
    headings.value = data
  }
  
  const setActiveHeading = (data) => {
    activeHeading.value = data
  }
  
  const setEditorInstance = (data) => {
    console.log(editorInstance.value)
    editorInstance.value = data
  }
  
  return {
    headings,
    setHeadings,
    activeHeading,
    setActiveHeading,
    editorInstance,
    setEditorInstance
  }
})

// 定义路由配置
const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'SignIn',
    component: () => import('../views/SignIn/index.vue')
  },
  {
    path: '/SignUp',
    name: 'SignUp',
    component: () => import('../views/SignUp/index.vue')
  },
  {
    path: '/Edit',
    name: 'Edit', 
    component: () => import('../views/Edit/index.vue'),
    redirect: '/Catalog',
    children: [
      {
        path: '/Catalog',
        name: "Catalog",
        component: () => import(`../views/Edit/Catalog/index.vue`)
      },
      {
        path: '/Outline',
        name: "Outline",
        component: () => import('../views/Edit/Outline/index.vue')
      },
      {
        path: '/OCR',
        name: "OCR",
        component: () => import('../views/Edit/OCR/index.vue')
      },
      {
        path: '/Voice',
        name: "Voice",
        component: () => import('../views/Edit/Voice/index.vue')
      },
      {
        path: '/Translate',
        name: "Translate",
        component: () => import('../views/Edit/Translate/index.vue')
      },
      {
        path: '/Summarize',
        name: "Summarize",
        component: () => import('../views/Edit/Summarize/index.vue')
      },
      {
        path: '/Style_library',
        name: "Style_library",
        component: () => import('../views/Edit/Style_library/index.vue')
      }
    ]
  }
]

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes: routes
})

export default router
