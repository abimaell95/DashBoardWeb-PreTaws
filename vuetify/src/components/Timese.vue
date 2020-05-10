<script>

  //Importing Line class from the vue-chartjs wrapper
  import { Line} from 'vue-chartjs'
  //Exporting this so it can be used in other components
  export default {
    extends: Line,

    data () {
      return {
        datacollection: {
          //Data to be represented on x-axis
        
          labels: [ "Crimen","Política","Corrupcion",
    "Salud","Religion", 'Desempleo', 'Educación','Deportes',
    'Economia'
    ],
          datasets: [
            {
              label: 'Ecuador',
              borderWidth: 2,
              backgroundColor: "transparent",
              borderColor: "rgba(200,0,0,0.6)",
              pointBorderColor: '#249EBF',
              //Data to be represented on y-axis
              data: [40, 20, 30, 50, 90, 10, 20, 40,80],
            },
            {
              label: 'Mexico',
              borderWidth: 2,
              backgroundColor: "transparent",
              borderColor: "rgba(00,200,0,0.6)",
              pointBorderColor: '#249EBF',
              data: [40, 39, 10, 40, 39, 80, 40,70,70]
              },
            {
              label: 'Venezuela',
              borderWidth: 2,
              backgroundColor: "transparent",
              borderColor: "rgba(0,0,200,0.6)",
              pointBorderColor: '#250EBF',
              
              data: [20, 10, 12, 33, 22, 25, 30,15,40]
            }
          ]
        },

        //Chart.js options that controls the appearance of the chart
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }],
            xAxes: [ {
              gridLines: {
                display: true
              }
            }]
          },
          
          responsive: true,
          maintainAspectRatio: false
        }
      }
    },
    mounted () {
      //renderChart function renders the chart with the datacollection and options object.
      this.renderChart(this.datacollection, this.options)
    }
  }
</script>

          
   