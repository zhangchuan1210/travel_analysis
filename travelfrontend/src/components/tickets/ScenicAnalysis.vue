<template>
  <div>
    <h1>景点门票分析</h1>

    <!-- Pie Chart -->
    <div class="chart-container" ref="chart1" style="height: 600px;"></div>
    <hr>

    <!-- Heat Map -->
    <div class="chart-container" ref="chart2" style="height: 700px;"></div>
    <hr>

    <!-- Scatter Chart -->
    <div class="chart-container" ref="chart3" style="height: 560px;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'ScenicAnalysis',
  props: {
    countList: Array,
    prices: Array,
    datalist: Array,
    cityJson: Object,
    priceNum: Array
  },
  mounted() {
    this.initCharts();
  },
  methods: {
    initCharts() {
      // Pie Chart
      const chart1 = echarts.init(this.$refs.chart1);
      const pieData = this.countList.map((item) => ({
        name: `${item.name}￥`,
        value: item.value
      }));
      const pieOption = {
        title: {
          text: '中国旅游景点平均门票占比饼图',
          subtext: 'Pie chart of average ticket share of Tourist attractions in China',
          left: 'center'
        },
        tooltip: { trigger: 'item' },
        legend: { orient: 'vertical', left: 'left' },
        series: [
          {
            name: '平均票价',
            type: 'pie',
            radius: '50%',
            data: pieData,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
      chart1.setOption(pieOption);

      // Heat Map
      const chart2 = echarts.init(this.$refs.chart2);
      const heatMapData = this.prices.map((item) => ({
        name: item.name,
        value: item.value
      }));
      const geoCoordMap = this.cityJson;

      const convertData = (data) =>
        data
          .map((item) => ({
            name: item.name,
            value: [...geoCoordMap[item.name], item.value]
          }))
          .filter((item) => item.value);

      const heatMapOption = {
        title: {
          text: '中国热门旅游城市平均旅游门票热力图',
          subtext: 'Average ticket heat map of popular tourist cities in China',
          left: 'center'
        },
        tooltip: {},
        visualMap: {
          min: 40000,
          max: 900000,
          left: 'left',
          bottom: 'bottom',
          text: ['High', 'Low'],
          inRange: { color: ['#e0ffff', '#006edd'] },
          calculable: true
        },
        geo: {
          map: 'china',
          roam: true
        },
        series: [
          {
            type: 'scatter',
            coordinateSystem: 'geo',
            data: convertData(heatMapData),
            symbolSize: 10,
            itemStyle: { color: '#F06C00' }
          }
        ]
      };
      chart2.setOption(heatMapOption);

      // Scatter Chart
      const chart3 = echarts.init(this.$refs.chart3);
      const scatterData = this.priceNum.map((item) => [
        item.avg_price,
        item.avg_price
      ]);

      const scatterOption = {
        title: {
          text: '中国热门旅游城市平均旅游门票散点图',
          subtext: 'Scatter chart of average ticket price of popular tourist cities in China',
          left: 'center'
        },
        tooltip: {
          formatter: (params) =>
            `${params.value[1]}￥`
        },
        xAxis: { type: 'value', scale: true },
        yAxis: { type: 'value', scale: true },
        series: [
          {
            name: '平均票价',
            type: 'scatter',
            data: scatterData,
            markLine: {
              data: [{ type: 'average', name: 'AVG' }]
            }
          }
        ]
      };
      chart3.setOption(scatterOption);
    }
  }
};
</script>

<style scoped>
.chart-container {
  margin-top: 20px;
}
</style>
