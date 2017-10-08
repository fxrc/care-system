// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import routes from './router/index'
import store from './vuex/store'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import Vuex from 'vuex'
import 'element-ui/lib/theme-default/index.css'
import 'font-awesome/css/font-awesome.min.css'
import axios from 'axios'
import $ from 'jquery'

Vue.prototype.$http = axios
export const myAxios = axios

Vue.config.productionTip = false

Vue.use(Vuex)
Vue.use(VueRouter)
Vue.use(ElementUI)
Vue.use(VueResource)

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path == '/login') {
    store.commit("delUserId");
  }
  let user = store.state.userid
  if (user == "" && to.path != '/login') {
    next({ path: '/login' })
  } else {
    switch(to.path){
      case '/indexMajor':
        if(store.state.pagePower['indexMajor'] != true){
          next({path: '/login'});
        }
        break;

      case '/indexStudents':
        if(store.state.pagePower['indexStudents'] != true){
          next({path: '/login'});
        }
        break;

      case '/person':
        if(store.state.pagePower['person'] != true){
          next({path: '/login'});
        }
        break;

      case '/officeDataExpore':
        if(store.state.pagePower['officeDataExpore'] != true){
          next({path: '/login'});
        }
        break;

      case '/officeSuggestions':
        if(store.state.pagePower['officeSuggestions'] != true){
          next({path: '/login'});
        }
        break;

      case '/systemUserTeam':
        if(store.state.pagePower['systemUserTeam'] != true){
          next({path: '/login'});
        }
        break;

      case '/systemUsers':
        if(store.state.pagePower['systemUsers'] != true){
          next({path: '/login'});
        }
        break;

      case '/systemRoleTeam':
        if(store.state.pagePower['systemRoleTeam'] != true){
          next({path: '/login'});
        }
        break;

      case '/dataUpdateBasic':
        if(store.state.pagePower['dataUpdateBasic'] != true){
          next({path: '/login'});
        }
        break;

      case '/dataUpdateScore':
        if(store.state.pagePower['dataUpdateScore'] != true){
          next({path: '/login'});
        }
        break;

      case '/dataFilter':
        if(store.state.pagePower['dataFilter'] != true){
          next({path: '/login'});
        }
        break;
    
      case '/dataUpdateFocus':
        if(store.state.pagePower['dataUpdateFocus'] != true){
          next({path: '/login'});
        }
        break;
    }
     next()
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
