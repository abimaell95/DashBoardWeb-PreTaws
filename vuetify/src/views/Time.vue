<template>
  <v-container>
    <v-col class="mb-4">
      <h1 class="display-2 font-weight-bold mb-3"></h1>
    </v-col>
    <v-row align="center" justify="center">
      <v-col class="d-flex text-center" cols="12" sm="6">
        <v-select
          v-model="select"
          v-on:change="fillData(Ecuador,Mexico,Venezuela)"
          :items="options"
          label="Select the topic"
        ></v-select>
        <p>{{select}}</p>
      </v-col>
    </v-row>
<p>{{loaded}}</p>
<p>{{Ecuador}}</p>
    <div class="small">
      <Timese :chart-data="datacollection"></Timese>
    </div>
  </v-container>
</template>

<script>
import Timese from "@/components/Timese";

export default {
  components: {
    Timese
  },
  data: () => {
    return {
      datacollection: {},
      Ecuador:[65, 76, 73, 80],
      Venezuela:[],
      Mexico:[],
      loaded:false,
      select: " ",
      options: [ "Crimen","Política","Corrupción",
    "Salud","Religion", 'Desempleo', 'Educación', "economi",
    "Deportes"
    ]
    }
  },
  async created(select) {
    let resp = await fetch(
      "https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/Series/economi.json"
      )
    let data = await resp.json();
    this.Ecuador = data.Ecuador;
    this.Mexico = data.Mexico;
    this.Venezuelas = data.newVsReturning;
    this.loaded = true;
  },

  methods: {
    fillData(Ecuador,Mexico,Venezuela) {
      this.datacollection = {
        labels: [
          "2015",
          "2016",
          "2017",
          "2018"
        ],
        datasets: [
            {
              label: 'Ecuador',
       
              //Data to be represented on y-axis
              data: Ecuador,
          },
           {
              label: 'Mexico',
              borderWidth: 2,
              backgroundColor: "transparent",
              borderColor: "rgba(00,200,0,0.6)",
              pointBorderColor: '#249EBF',
              data: Mexico
              },
          {
            label: 'Venezuela',
              borderWidth: 2,
              backgroundColor: "transparent",
              borderColor: "rgba(0,0,200,0.6)",
              pointBorderColor: '#250EBF',
              
              data: Venezuela
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
  max-width: 900px;
  margin: 150px auto;
}
</style>
