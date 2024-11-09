<template>
  <div>
    <div class="result-wrap">
      <!-- City Dropdown -->
      <div class="label" style="float: left;">
        <label class="city"> 城 市 ：</label>
      </div>
      <div class="field">
        <select v-model="selectedCity" class="input w50" style="height: 20px">
          <option v-for="(city, index) in cities" :key="index" :value="city">
            {{ city }}
          </option>
        </select>
      </div>

      <!-- Sights Table -->
      <div id="thscfx" style="height: 600px; float: left;">
        <div id="thscfx2" style="height: 600px; width: 400px; float: left;">
          <table class="fl-table">
            <thead>
              <tr>
                <th>景点名称</th>
                <th>评    分</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, index) in sightList" :key="index">
                <td>{{ row.sight }}</td>
                <td>{{ row.score }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Echarts Map -->
        <div id="thscfx3" style="height: 600px; width: 750px; float: left;"></div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name:'DashBoard',
  data() {
    return {
      ctx: window.location.pathname, // Assuming the ctx is the current page's path
      selectedCity: '', // Store selected city from the dropdown
      cities: [], // List of cities to be passed in
      sightList: [] // List of sights data
    };
  },
  mounted() {
    // Initialize ECharts chart
    this.initializeChart();
    // Simulate data fetching from server
    this.fetchCitiesAndSights();
  },
  methods: {
    fetchCitiesAndSights() {
      // Simulate a backend response
      // In real life, you would fetch this data from the server using something like axios
      this.cities = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']; // Example cities
      this.sightList = [
        { sight: 'Great Wall of China', score: 4.8 },
        { sight: 'Forbidden City', score: 4.9 },
        { sight: 'Summer Palace', score: 4.7 }
      ]; // Example sights
    },
    initializeChart() {
      const myChartFjHf3 = echarts.init(document.getElementById('thscfx3'));

      const randomValue = () => Math.round(Math.random() * 200);

      const option = {
        tooltip: {
          formatter: function (params) {
            return `<p style="font-size:18px">${params.data.name}</p>`;
          },
          backgroundColor: "#ff7f50",
          textStyle: { color: "#fff" }
        },
        visualMap: {
          show: true,
          x: 'left',
          y: 'center',
          inRange: {
            color: ['#e0ffff', '#006edd']
          }
        },
        series: [
          {
            name: '中国',
            type: 'map',
            mapType: 'china',
            label: {
              normal: {
                show: true
              },
              emphasis: {
                show: true
              }
            },
            data: [
              { name: '北京', value: randomValue() },
              { name: '上海', value: randomValue() },
              { name: '广东', value: randomValue() },
              // Add more provinces as needed
            ]
          }
        ]
      };

      myChartFjHf3.setOption(option);
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
.fl-table {
  margin: 20px;
  border-radius: 5px;
  font-size: 12px;
  border: none;
  border-collapse: collapse;
  max-width: 100%;
  white-space: nowrap;
  word-break: keep-all;
}

.fl-table th {
  text-align: left;
  font-size: 20px;
}

.fl-table tr:hover td {
  background: #00d1b2;
  color: #F8F8F8;
}

.fl-table td, .fl-table th {
  border-style: none;
  border-top: 1px solid #dbdbdb;
  border-left: 1px solid #dbdbdb;
  border-bottom: 3px solid #dbdbdb;
  border-right: 1px solid #dbdbdb;
  padding: .5em .55em;
  font-size: 15px;
}

.fl-table td {
  vertical-align: center;
  height: 30px;
}

.city option {
  font-size: 15px;
  height: 30px;
}

.fl-table tr:nth-child(even) {
  background: #F8F8F8;
}

.input {
  width: 200px;
}
</style>
