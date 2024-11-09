<template>
  <div>
    <div class="tab">
      <button class="tablinks" @click="showChart('001')">春季旅游城市推荐</button>
      <button class="tablinks" @click="showChart('002')">夏季旅游城市推荐</button>
      <button class="tablinks" @click="showChart('003')">秋季旅游城市推荐</button>
      <button class="tablinks" @click="showChart('004')">冬季旅游城市推荐</button>
    </div>

    <div class="box">
      <div v-show="activeTab === '001'" class="chart-container">
        <div id="01" class="chart" style="height: 600px;"></div>
        <div id="02" class="chart" style="height: 600px;"></div>
      </div>

      <div v-show="activeTab === '002'" class="chart-container">
        <div id="03" class="chart" style="height: 600px;"></div>
        <div id="04" class="chart" style="height: 600px;"></div>
      </div>

      <div v-show="activeTab === '003'" class="chart-container">
        <div id="05" class="chart" style="height: 600px;"></div>
        <div id="06" class="chart" style="height: 600px;"></div>
      </div>

      <div v-show="activeTab === '004'" class="chart-container">
        <div id="07" class="chart" style="height: 600px;"></div>
        <div id="08" class="chart" style="height: 600px;"></div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import api from '../../api';
export default {
  name:'TourismRecommendation',
  data() {
    return {
      activeTab: "001", // Default active tab
      gone: [], // Data for the charts
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      api
        .post("/recommend/getData",{})
        //.post("/scrape/places")
        .then((response) => {
          this.gone = response.data;
          this.updateCharts();
        })
        .catch((error) => {
          console.error("Failed to fetch data", error);
        });
    },
    updateCharts() {
      this.updateChart("01", this.gone[0], "春季旅游景点推荐柱状图", "春季");
      this.updateChart("02", this.gone[0], "春季旅游景点推荐玫瑰图", "春季");
      this.updateChart("03", this.gone[1], "夏季旅游景点推荐柱状图", "夏季");
      this.updateChart("04", this.gone[1], "夏季旅游景点推荐玫瑰图", "夏季");
      this.updateChart("05", this.gone[2], "秋季旅游景点推荐柱状图", "秋季");
      this.updateChart("06", this.gone[2], "秋季旅游景点推荐玫瑰图", "秋季");
      this.updateChart("07", this.gone[3], "冬季旅游景点推荐柱状图", "冬季");
      this.updateChart("08", this.gone[3], "冬季旅游景点推荐玫瑰图", "冬季");
    },
    updateChart(id, data, title, season) {
      const chart = echarts.init(document.getElementById(id));
      const xAxisData = data.map((item) => item.name);
      const seriesData = data.map((item) => item.value);

      const option = {
        title: {
          text: title,
          subtext: `${season} tourist attractions`,
          x: "center",
          textStyle: {
            fontFamily: "Arial",
            fontSize: 20,
            fontWeight: "bolder",
          },
        },
        tooltip: { trigger: "item" },
        xAxis: {
          type: "category",
          data: xAxisData,
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            name: season,
            data: seriesData,
            type: "bar",
            itemStyle: {
              normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: "#91c7ae" },
                  { offset: 1, color: "rgba(22,75,247,0.1)" },
                ]),
              },
            },
            showBackground: true,
            backgroundStyle: {
              color: "rgba(180, 180, 180, 0.2)",
            },
          },
        ],
      };
      chart.setOption(option);
    },
    showChart(tabId) {
      this.activeTab = tabId;
    },
  },
};
</script>

<style scoped>
.chart-container {
  display: none;
}
.chart-container.active {
  display: block;
}
.tab button.active {
  background-color: #f1f1f1;
}
</style>
