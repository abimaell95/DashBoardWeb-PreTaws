
<script>
import { Bar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  
  extends: Bar,
  mixins: [reactiveProp],
  props: ['options'],
  mounted () {

    this.renderChart(this.chartData, this.options)
  }
}
</script>













fetch('https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/datos.json')
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    console.log(myJson);
  });
  async function cargarJSON(){
    const response= await fetch('https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/datos.json');
    const myJson= await response.json;
 
  }
  
  //Importing Line class from the vue-chartjs wrapper
  import { Bar } from 'vue-chartjs'
  //Exporting this so it can be used in other components
  export default {
    extends: Bar,

    data () {
      return {
        datacollection: {
          //Data to be represented on x-axis
        
          labels: [ this.valor,"Política","Corrupcion",
    "Salud","Religion", 'Desempleo', 'Educación','Deportes',
    'Economia'
    ],
          datasets: [
            {
              label: 'Positivo',
              backgroundColor: '#249EBF',
              pointBackgroundColor: 'white',
              borderWidth: 2,
              pointBorderColor: '#249EBF',
              //Data to be represented on y-axis
              data: [40, 20, 30, 50, 90, 10, 20, 40,80],
            },
            {
              label: 'Neutro',
              backgroundColor: '#746A68',
              pointBackgroundColor: 'white',
              borderWidth: 2,
              pointBorderColor: '#249EBF',
              data: [40, 39, 10, 40, 39, 80, 40,70,70]
              },
            {
              label: 'Negativo',
              backgroundColor: '#ff8000',
              pointBackgroundColor: 'white',
              borderWidth: 2,
              pointBorderColor: '#249EBF',
              data: [20, 10, 12, 33, 22, 25, 30,15,40]
            }
          ]
        },

        //Chart.js options that controls the appearance of the chart
        options: {
          scales: {
             yAxes: [{
          stacked: true
        }],
             xAxes: [{
          stacked: true,
          categoryPercentage: 0.5,
          barPercentage: 1
          }]
          },
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
        }
      }
    },*/
  /*  mounted () {
      //renderChart function renders the chart with the datacollection and options object.
      this.renderChart(this.datacollection, this.options)
      console.log(this.valor)
     /*document.getElementById('user').addEventListener('change',(event)=> console.log(event))*/
    
   /* props: ['valor'],
    updated() {
      console.log(this.valor)
    },*/

</script>

          
   -->