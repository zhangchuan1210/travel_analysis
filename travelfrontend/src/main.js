import { createApp } from 'vue';
import IndexApp from './Index.vue';
import { createRouter, createWebHistory } from 'vue-router';

// Import your components
import HotSpot from './components/hotspot/HotSpot.vue';
import Tickets from './components/tickets/ScenicAnalysis.vue';
import Recommend from './components/recommend/TourismRecommendation.vue';
import Emotion from './components/emotion/EmotionAnalysis.vue';

const routes = [
  { path: '/hotspot', component: HotSpot },
  { path: '/tickets', component: Tickets },
  { path: '/recommend', component: Recommend },
  { path: '/emotion', component: Emotion },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

const app = createApp(IndexApp);
app.use(router);
app.mount('#app');
