<script>

import { Radar } from 'vue-chartjs'
  //Exporting this so it can be used in other components
  export default {
    extends: Radar,

    data () {
      return {
        datacollection: {
          //Data to be represented on x-axis
        
          labels: [ "Crimen","Política","Corrupcion",
    "Salud","Religion", 'Desempleo', 'Educación', 'Deportes',
    'Economia'
    ],
          datasets: [
            {
                label: 'Ecuador',
                backgroundColor: "transparent",
                borderColor: "rgba(200,0,0,0.6)",
                fill: false,
                radius: 6,
                pointRadius: 6,
                pointBorderWidth: 3,
                pointBackgroundColor: "orange",
                pointBorderColor: "rgba(200,0,0,0.6)",
                pointHoverRadius: 10,
                        //Data to be represented on y-axis
              data: [40, 20, 30, 50, 90, 10, 20, 40,80],
            },
            {
              label: 'Mexico',
                backgroundColor: "transparent",
                borderColor: "rgba(00,200,0,0.6)",
                fill: false,
                radius: 6,
                pointRadius: 6,
                pointBorderWidth: 3,
                pointBackgroundColor: "orange",
                pointBorderColor: "rgba(200,0,0,0.6)",
                pointHoverRadius: 10,
              data: [40, 39, 10, 40, 39, 80, 40,70,70]
              },
            {
               label: "Venezuela",
                backgroundColor: "transparent",
                borderColor: "rgba(0,0,200,0.6)",
                fill: false,
                radius: 6,
                pointRadius: 6,
                pointBorderWidth: 3,
                pointBackgroundColor: "cornflowerblue",
                pointBorderColor: "rgba(0,0,200,0.6)",
                pointHoverRadius: 10,
              data: [20, 10, 12, 33, 22, 25, 30,15,40]
            }
          ]
        },

        //Chart.js options that controls the appearance of the chart
      options : {
    scale: {
        angleLines: {
            display: false
        },
        ticks: {
            suggestedMin: 50,
            suggestedMax: 90
        }
    }
     }
      }
    },
    mounted () {
      //renderChart function renders the chart with the datacollection and options object.
      this.renderChart(this.datacollection, this.options)
    }
  }
</script>
