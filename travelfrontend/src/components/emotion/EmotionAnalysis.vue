<template>
  <div id="emotion">
    <h1>旅游舆情分析</h1>
    <!-- 词云图 -->
    <div ref="wordCloudChart" style="height: 800px; width: 100%;"></div>
    <br />

    <!-- 情感分析图 (考虑因素) -->
    <div ref="sentimentFactorsChart" style="height: 600px; width: 650px; float: left"></div>

    <!-- 情感分析图 (景点类型) -->
    <div ref="sentimentAttractionChart" style="height: 600px; width: 600px; float: left"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'EmotionAnalysis',
  data() {
    return {
      datalist: [
        { name: '景点1', value: 100 },
        { name: '景点2', value: 80 },
        // 更多数据...
      ],
      words: ['风景', '价格', '服务', '交通', '人文', '设施', '卫生', '餐饮', '住宿', '安全', '娱乐', '舒适度'],
      positive: [80, 70, 60, 90, 85, 70, 60, 65, 75, 80, 90, 70],
      neutral: [10, 20, 30, 10, 10, 20, 25, 20, 15, 10, 5, 20],
      negative: [10, 10, 10, 0, 5, 10, 15, 15, 10, 10, 5, 10]
    };
  },
  mounted() {
    this.initWordCloudChart();
    this.initSentimentFactorsChart();
    this.initSentimentAttractionChart();
  },
  methods: {
    // 初始化词云图
    initWordCloudChart() {
      const chart = echarts.init(this.$refs.wordCloudChart);
      const option = {
        title: {
          text: '旅游评论数据词云图',
          subtext: 'Tourism review data word cloud',
          textStyle: { fontSize: 20 }
        },
        series: [
          {
            type: 'wordCloud',
            shape: 'star',
            gridSize: 2,
            sizeRange: [10, 50],
            rotationRange: [-90, 90],
            textStyle: {
              color: () =>
                `rgb(${Math.round(Math.random() * 160)}, ${Math.round(Math.random() * 160)}, ${Math.round(Math.random() * 160)})`
            },
            data: this.datalist
          }
        ]
      };
      chart.setOption(option);
    },
    // 初始化情感分析图 - 考虑因素
    initSentimentFactorsChart() {
      const chart = echarts.init(this.$refs.sentimentFactorsChart);
      const option = {
        title: { text: '旅游考虑因素情感分析图', textStyle: { fontSize: 16 } },
        tooltip: { trigger: 'axis' },
        legend: {},
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: { type: 'value' },
        yAxis: { type: 'category', data: this.words.slice(0, 10) },
        series: [
          { name: '积极', type: 'bar', stack: 'total', data: this.positive.slice(0, 10) },
          { name: '中性', type: 'bar', stack: 'total', data: this.neutral.slice(0, 10) },
          { name: '消极', type: 'bar', stack: 'total', data: this.negative.slice(0, 10) }
        ]
      };
      chart.setOption(option);
    },
    // 初始化情感分析图 - 景点类型
    initSentimentAttractionChart() {
      const chart = echarts.init(this.$refs.sentimentAttractionChart);
      const option = {
        title: { text: '旅游景点类型情感分析图', textStyle: { fontSize: 16 } },
        tooltip: { trigger: 'axis' },
        legend: {},
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: { type: 'category', data: this.words.slice(10) },
        yAxis: { type: 'value' },
        series: [
          { name: '积极', type: 'bar', stack: 'total', data: this.positive.slice(10) },
          { name: '中性', type: 'bar', stack: 'total', data: this.neutral.slice(10) },
          { name: '消极', type: 'bar', stack: 'total', data: this.negative.slice(10) }
        ]
      };
      chart.setOption(option);
    }
  }
};
</script>

<style scoped>
#wordCloudChart, #sentimentFactorsChart, #sentimentAttractionChart {
  margin-bottom: 20px;
}
</style>
