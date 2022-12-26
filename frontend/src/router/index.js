import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/quote/:id',
    name: 'quote',
    component: () => import('../views/QuoteView.vue')
  },
  {
    path: '/create',
    name: 'create',
    component: () => import('../views/CreateQuoteView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
