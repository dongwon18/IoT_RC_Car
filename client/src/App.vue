<template>
  <div id="app">
    <div>
      <h1 class="Title">🚗 RED Explorer</h1>
    </div>    
    <div class="charts">
      <div class="temp">
      <h2>temperature[C]</h2>
      <apexchart width="350" :options="options_temp" :series="series_temp"/>
      </div>
      <div class="humi">
        <h2>humidity[%]</h2>
        <apexchart width="350" :options="options_humi" :series="series_humi"/>
      </div>
      <div class="distance">
        <h2>distance[cm]</h2>
        <apexchart width="350" :options="options_distance" :series="[distance[0]]"/>
      </div>
    </div>
    
    
  </div>
</template>

<script>
import moment from "moment";
export default {
  name: "App",
  created() {
    this.$socket.on("getData", (data)=>{
      console.log(data);
      this.times = data.map((data)=> data.time);
      this.times = this.times.map((time) => moment(time).format("HH:mm:ss"));
      this.temperatures = data.map((data)=> data.num1 *100);
      this.humidities = data.map((data) => data.num2 * 100);
      this.distance = data.map((data)=> data.num3 * 100);
      this.options_temp ={
        chart:{
          type: 'bar',
          toolbar:{
            show: true,
             toolbar: {
              show: true,
              offsetX: 50,
              offsetY: 50,
              tools: {
                download: true,
                selection: true,
                zoom: true,
                zoomin: true,
                zoomout: true,
                pan: true,
                reset: true | '<img src="/static/icons/reset.png" width="20">',
                customIcons: []
              },
              export: {
                csv: {
                  filename: undefined,
                  columnDelimiter: ',',
                  headerCategory: 'category',
                  headerValue: 'value',
                  dateFormatter(timestamp) {
                    return new Date(timestamp).toDateString()
                  }
                },
                svg: {
                  filename: undefined,
                },
                png: {
                  filename: undefined,
                }
              },
              autoSelected: 'zoom' 
            },
          },
        },
        xaxis: {
          categories: this.times,
        },
        yaxis:{
          decimalsInFloat: 3,
          min: -10,
          max: 100,
        },
        plotOptions:{
          bar:{
            colors: {
              ranges:[
                {
                  from: 0,
                  to: 10,
                  color: '#0033FF'
                },
                {
                  from: 10,
                  to: 40,
                  color: '#33CC33'
                },
                {
                  from: 40,
                  to: 100,
                  color: '#FF3300'
                },
              ],
            },
            dataLabels:{
              position: 'top',
              maxItems: 100,
              hideOverflowingLabels: false,
              orientation: 'horizontal',
            },
          },
        },
        stroke:{
          show: false,
        },
        dataLabels:{
          enabled:false,
        },
        legend:{
          show: true,
        },
        
      };

      this.options_humi ={
        xaxis: {
          categories: this.times,
        },
        yaxis:{
          decimalsInFloat: 3,
          min: 0,
          max: 100,
        },
        plotOptions:{
          bar:{
            barHeight: '100%',
            columnWidth: '70%',
            colors:{
              ranges: [
                {
                  from: 0,
                  to: 40,
                  color: '#FFCC00',
                  name: 'dry',
                }, 
                {
                  from: 40,
                  to: 60,
                  color: '66CC33',
                  name: 'proper',
                },
                {
                  from: 60,
                  to: 100,
                  color: '336699',
                  name: 'humid',
                },
              ],              
            },
           
          },
        },
        stroke:{
            show: false,
          },
      };
      
      this.options_distance={  
        chart: {
          height: 280,
          type: "radialBar",
        },
        series: [this.distance[0]],
        color: ["#FF3300"],
        plotOptions: {
          radialBar: {
            startAngle: -90,
            endAngle: 90,
            track: {
              background: '#333',
              startAngle: -90,
              endAngle: 90,
            },
            dataLabels: {
              name: {
                show: false,
              },
              value: {
                fontSize: "30px",
                show: true,
                formatter: function(val){
                  return (val).toFixed(2);
                },
              }
            }
          }
        },
        fill: {
          type: "gradient",
          gradient: {
            shade: "dark",
            type: "horizontal",
            gradientToColors: ["#FF3300", "#0000FF"],
            opacityFrom: 1,
            opacityTo: 1,  
            inverseColors: true,
            stops: [0, 100],
          }
        },
        stroke: {
          lineCap: "butt"
        },
        labels: ["distance"]
      },
      this.series_temp = [
        {
          name:"temperature[C]",
          type: 'bar',
          data: this.temperatures,
        },
      ];
      this.series_humi = [
        {
          name:"humidity[%]",
          type: 'bar',
          data: this.humidities,
        },
      ];
    });
  },
  data(){
    return {
      times: [],
      temperatures: [],
      humidities: [],
      distance: [],
      options_temp:{},
      options_humi: {},
      options_distance: {},
      series_temp: [],
      series_humi: [],
      options: {
        chart: {
          id: "vuechart-example",
        },
        xaxis:{
          categories: [1991, 1992, 3, 4, 5, 6, 7, 8],
        },
      },
      options_humi:{
        chart: {
          id: "vuechart-example",
        },
        xaxis:{
          categories: [1991, 1992, 3, 4, 5, 6, 7, 8],
        },
      },
      series: [
        {
          name: "series-1",
          data: [30, 40, 50, 45, 49, 60, 91, 20],
        },
        {
          name: "series-2",
          data: [20, 50, 40, 65, 30, 65, 93, 27],
        },
      ],
      
    };
  },
};
</script>

<style scoped>
#app{
  max-width: 100%;
}
.charts{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding-top: 50px;
}

.Title {
  text-align: center;
  padding-bottom: 20px;
  border-bottom: solid rgb(192, 104, 104) 10px;
}
.humi {
  margin-left: 100px;
  margin-right: 100px;
  padding-right: 30px;
  padding-left: 30px;
  background-color: beige;
  border: solid black 1px;
}
.temp {
  padding-right: 30px;
  padding-left: 30px;
  background-color: beige;
  border: solid black 1px;
}
.distance {
  margin-top: 50px;
}

</style>
