import Vue from "vue";
import App from "./App.vue";
import io from "socket.io-client";
import VueApexCharts from "vue-apexcharts";

Vue.use(VueApexCharts);
Vue.component("apexchart", VueApexCharts);

Vue.config.productionTip = false;
const socket = io.connect("http://localhost:8081", {
	transport: ["websocket"],
});
Vue.prototype.$socket = socket;

new Vue({
	render: (h) => h(App),
}).$mount("#app");
