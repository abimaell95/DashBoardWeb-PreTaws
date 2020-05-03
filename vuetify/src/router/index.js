import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home

  },  
  {
    path: '/botones',
    name: 'botones',
   component: () => import('../views/Botones.vue')
  },
  {
    path: '/bar',
    name: 'Bar',
   component: () => import('../views/Bar.vue')
  },
  {
    path: '/pie',
    name: 'radar',
   component: () => import('../views/Radar.vue')
  },
  {
    path: '/time',
    name: 'time',
   component: () => import('../views/Time.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
