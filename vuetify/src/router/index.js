import Vue from 'vue'
import VueRouter from 'vue-router'
import Radar from '@/views/Radar'
Vue.use(VueRouter)

  const routes = [{
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/wc',
    name: 'WordCloud',
   component: () => import('../views/WordCloud.vue')
  },
{
    path: '/barplt',
    name: 'barplt',
   component: () => import('../views/Barplt.vue')
  },
  {
    path: '/time',
    name: 'time',
   component: () => import('../views/Time.vue')
  },
  {
    path: '/radar',
    name: 'radar',
   component: () => import('../views/Radar.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
