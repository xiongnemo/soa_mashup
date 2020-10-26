// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueAMap from 'vue-amap'
import ElementUI from 'element-ui'
import XMLJS from 'xml-js'
import 'element-ui/lib/theme-chalk/index.css'
import soa_search_everything from './assets/js/soa_search_everything';
Vue.use(soa_search_everything);//将全局函数当做插件来进行注册
Vue.use(XMLJS)
Vue.use(VueAMap)
Vue.use(ElementUI)

VueAMap.initAMapApiLoader({
  // 高德的key
  key: '0b3ff1027bd08cf297f4c31163aa456f',
  // 插件集合
  plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor'],
  // 高德 sdk 版本，默认为 1.4.4
  v: '1.4.4'
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  render: h => h(App)
})
