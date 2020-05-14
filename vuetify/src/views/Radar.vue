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
      Ecuador: [],
      Venezuela: [],
      Mexico: [],
      select: "2015",
      options: ["2015", "2016", "2017", "2018"]
    };
  },
  async mounted() {
    let resp = await fetch(
      "https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/Radar/" +
        this.select +
        ".json"
    );
    let data = await resp.json();
    this.Ecuador = data.Ecuador;
    this.Mexico = data.Mexico;
    this.Venezuela = data.Venezuela;
    this.loaded = true;
    this.datacollection = this.datacollection = {
      labels: [
        "Política",
        "Salud",
        "Economia",
        "Crimen",
        "Corrupcion",
        "Educación",
        "Deportes",
        "Desempleo",
        "Religion"
      ],
      datasets: [
        {
          label: "Ecuador",
          backgroundColor: "#ffd31d",
          pointRadius: 0,
          borderWidth: 1,

          data: this.Ecuador
        },
        {
          label: "México",
          backgroundColor: "#00bcd4",
          pointRadius: 0,
          borderWidth: 1,

          data: this.Mexico
        },
        {
          label: "Venezuela",
          backgroundColor: "#fc7e2f",
          pointRadius: 0,
          borderWidth: 1,

          data: this.Venezuela
        }
      ]
    };
  },
  async updated() {
    let resp = await fetch(
      "https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/Radar/" +
        this.select +
        ".json"
    );
    let data = await resp.json();
    this.Ecuador = data.Ecuador;
    this.Mexico = data.Mexico;
    this.Venezuela = data.Venezuela;
    this.loaded = true;
    this.datacollection = this.datacollection = {
      labels: [
        "Política",
        "Salud",
        "Economia",
        "Crimen",
        "Corrupcion",
        "Educación",
        "Deportes",
        "Desempleo",
        "Religion"
      ],
      datasets: [
        {
          label: "Ecuador",
          backgroundColor: "#ffd31d",
          pointRadius: 0,
          borderWidth: 1,

          data: this.Ecuador
        },
        {
          label: "México",
          backgroundColor: "#00bcd4",
          pointRadius: 0,
          borderWidth: 1,

          data: this.Mexico
        },
        {
          label: "Venezuela",
          backgroundColor: "#fc7e2f",
          pointRadius: 0,
          borderWidth: 1,

          data: this.Venezuela
        }
      ]
    };
  }
  //Chart.js options that controls the appearance of the chart
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

