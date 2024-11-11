<template>
  <div id="hotspot">
    <h1>热门景点分析</h1>

    <!-- 中国各省旅游热度热力图 -->
    <div ref="heatMapChart" style="height: 600px; width: 100%;"></div>
    <hr />

    <!-- 国内城市热门景点数柱状图 -->
    <div ref="barChart" style="height: 600px; width: 100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import api from "@/api";

export default {
  name: 'HotSpot',
  data() {
      return {
        localData: {
         datalist: { type: Array, default: () => [] },
         maps: { type: Array, default: () => [] },
        },
      };
  },
  mounted() {

  },
  methods: {
      fetchData() {
      api
        .get("/hotspot/listhotspot")
        .then((response) => {
          this.localData.datalist = response.data.datalist;
          this.localData.maps = response.data.maps;
          this.initHeatMapChart();
          this.initBarChart();
        })
        .catch((error) => {
          console.error("Failed to fetch data", error);
        });
    },
    // 初始化中国各省旅游热度热力图
    initHeatMapChart() {
      const heatMapChart = echarts.init(this.$refs.heatMapChart);
      const heatMapOption = {
        title: {
          text: '中国各省旅游热度热力图',
          subtext: "China's provincial tourism heat map",
          textAlign: 'left',
          x: 'center',
          textStyle: { fontFamily: 'Arial', fontSize: 20, fontWeight: 'normal' }
        },
        tooltip: {
          formatter: (params) => `<p style="font-size:18px">${params.data.name}</p><p style="font-size:14px">${params.data.value}</p>`,
          backgroundColor: "#007f50",
          textStyle: { color: "#fff" }
        },
        visualMap: {
          show: true,
          x: 'left',
          y: 'center',
          splitList: [
            { start: 600000, end: 900000 },
            { start: 500000, end: 700000 },
            { start: 300000, end: 500000 },
            { start: 200000, end: 300000 },
            { start: 100000, end: 200000 },
            { start: 10000, end: 100000 }
          ],
          color: ['#5475f5', '#9feaa5', '#85daef', '#74e2ca', '#e6ac53', '#9fb5ea']
        },
        series: [
          {
            name: '中国',
            type: 'map',
            mapType: 'china',
            label: {
              normal: { show: true },
              emphasis: { show: true }
            },
            data: this.localData.datalist.map((item) => ({ name: item.name, value: item.value }))
          }
        ]
      };
      heatMapChart.setOption(heatMapOption);
    },

    // 初始化国内城市热门景点数柱状图
    initBarChart() {
      const barChart = echarts.init(this.$refs.barChart);
      const filteredMaps = this.localData.maps.filter(item => item.value >= 16);
      const barChartOption = {
        title: {
          text: '国内城市热门景点数柱状图',
          subtext: 'Bar chart of popular scenic spots in Chinese cities',
          textAlign: 'left',
          x: 'center',
          textStyle: { fontFamily: 'Arial', fontSize: 20, fontWeight: 'normal' }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: { type: 'shadow' }
        },
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: { type: 'value', boundaryGap: [0, 0.01] },
        yAxis: {
          type: 'category',
          data: filteredMaps.map((item) => item.name)
        },
        series: [
          {
            name: '热门景点数',
            type: 'bar',
            data: filteredMaps.map((item) => item.value),
            itemStyle: {
              normal: {
                color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [
                  { offset: 0, color: '#248ff7' },
                  { offset: 1, color: 'rgba(22,75,247,0.1)' }
                ])
              }
            }
          }
        ]
      };
      barChart.setOption(barChartOption);
    }
  }
};
</script>

<style scoped>
#app {
  text-align: center;
}

#heatMapChart, #barChart {
  margin-bottom: 20px;
}
</style>
