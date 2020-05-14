<template>
  <v-container>
    <v-col class="mb-4">
      <h1 class="display-2 font-weight-bold mb-3"></h1>
    </v-col>
    <br />
    <v-row align="center" justify="center">
      <v-col class="d-flex text-center" cols="12" sm="6">
        <v-select
          v-model="select"
          v-on:change="fillData(`${select}`)"
          :items="options"
          label="Select the year"
        ></v-select>

      </v-col>
    </v-row>

    <div class="small">
      <Radar :chart-data="datacollection"></Radar>
    </div>
  </v-container>
</template>

<script>
import Radar from "@/components/Radar";

export default {
  components: {
    Radar
  },
  data: () => {
    return {
      datacollection: {},
      select: [],
      options: [
        { value: 20, text: "2015" },
        { value: 60, text: "2016" },
        { value: 50, text: "2017" },
        { value: 80, text: "2018" }
      ]
    };
  },

  methods: {
    fillData(valor) {
      this.datacollection = {
        labels: [
          "Crime",
          "Política",
          "Corrupcion",
          "Salud",
          "Religion",
          "Desempleo",
          "Educación",
          "Deportes",
          "Economia"
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
            label: "Neutro",
            backgroundColor: "#746A68",
            pointBackgroundColor: "white",
            borderWidth: 2,
            pointBorderColor: "#249EBF",
            data: [
              valor,
              valor,
              valor,
              valor,
              valor,
              valor,
              valor,
              valor,
              valor
            ]
          },
          {
            label: "Negativo",
            backgroundColor: "#ff8000",
            pointBackgroundColor: "white",
            borderWidth: 2,
            pointBorderColor: "#249EBF",
            data: [
              valor,
              valor,
              valor,
              valor,
              valor,
              valor,
              valor,
              valor,
              valor
            ]
          }
        ]
      };

      //Chart.js options that controls the appearance of the chart
    }
  }
};
</script>

<style>
.small {
  max-width: 500px;
  margin: 150px auto;
}
 
</style>



























<!--<template>
  <section class="container">
     <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3"></h1>
      </v-col>
      <br>
    <div class="columns">
      <div class="column">
        <h3 class="text-center">Radar Chart</h3>
        <v-row align="center" justify="center">
          <v-col class="d-flex text-center" cols="12" sm="6">
            <v-select v-model='select' :items="items" label="Select the year" ></v-select>
          </v-col>
        </v-row>


      </div>
      <br><br>
       <Radar/>

    </div>
  </section>
</template>

<script>
  import Radar from '@/components/Radar'

  export default {
    name: 'VueChartJS',
    components: {
      Radar
    },  data(){
      return{
        select:null,
   
        items: [
          { text : 2015,
            value:Ecuador      
          },
          {text : 2016,
            value:require('../assets/Mexico.jpg',)
          },
          {text : 2017,
           value: require('../assets/Venezuela.jpg',)
          },
          {text : 2018,
           value: require('../assets/Venezuela.jpg',)
          }

          ]}  
          
    },
  }
</script>-->

