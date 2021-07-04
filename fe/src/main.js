import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.use(Vuex);  

const store = new Vuex.Store({
  state: {
    waypoints: [],
    wpTable: {
      currentPage: 1,
      itemsPerPage: 10,
      totalRows: 0
    },
  },
  mutations: {
    updateWaypoints(state, waypoints) {
      state.waypoints = waypoints;
    },
    updateRows(state, totalItems) {
      state.wpTable.totalRows = totalItems;
    },
    updateTablePage(state, page){
      state.wpTable.currentPage = page;
    }
  }
});

new Vue({
  render: h => h(App),
  store
}).$mount('#app')
