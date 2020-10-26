import Vue from 'vue'
import Router from 'vue-router'
import SOAMashup from '@/components/SOAMashup'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SOAMashup',
      component: SOAMashup
    }
  ]
})
