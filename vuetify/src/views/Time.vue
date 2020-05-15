<template>
  <v-container>
    <v-col class="mb-4">
      <h1 class="display-2 font-weight-bold mb-3"></h1>
    </v-col>
       <v-row justify="center">     
          <v-col class="m-1 text-center" cols="12" >
            <h2 class="font-weight-bold mb-3 display-3">Time Series</h2>
          </v-col>
        </v-row>
    <v-row align="center" justify="center">
      <v-col class="d-flex text-center" cols="12" sm="6">
        <v-select
          v-model="select"
          :items="options"
          label="Select the topic"
        ></v-select>
      </v-col>
    </v-row>

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
      datacollection:{},
      loaded:false,
      select: "Crimen",
      options:[{value: "Crimen",text:"Crime"}, {value: "Política",text:"Politic"}, {value: "Corrupción",text:"Corruption"},
     {value: "Salud",text:"Health"},{value: "Religion",text: "Religion"}, {value: "Desempleo",text:'Unemployment'}, 
{value: "Educación",text:'Education'}, {value: "Economia",text:"Economy"},
     {value: "Deportes",text:"Sports"}]
    }
  },
 
   async mounted()  {
    let resp = await fetch(
      "https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/Series/"+this.select+".json"
      )
    let data = await resp.json();
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
              backgroundColor: "transparent",
              borderColor: "#ffd31d",
              data: data.Ecuador,
          },
           {
              label: 'Mexico',
              borderWidth: 2,
              backgroundColor: "transparent",
              borderColor: "rgba(00,200,0,0.6)",
              pointBorderColor: '#249EBF',
              data: data.Mexico
              },
          {
            label: 'Venezuela',
              borderWidth: 2,
              backgroundColor: "transparent",
              borderColor: "rgba(0,0,200,0.6)",
              pointBorderColor: '#250EBF',
              
              data: data.Venezuela
          }
        ]
      };
  }, 
  async updated()  {
    let resp = await fetch(
      "https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/Series/"+this.select+".json"
      )
    let data = await resp.json();
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
              backgroundColor: "transparent",
              borderColor: "#ffd31d",
              data: data.Ecuador,
          },
           {
              label: 'Mexico',
              borderWidth: 2,
              backgroundColor: "transparent",
              borderColor: "rgba(00,200,0,0.6)",
              pointBorderColor: '#249EBF',
              data: data.Mexico
              },
          {
            label: 'Venezuela',
              borderWidth: 2,
              backgroundColor: "transparent",
              borderColor: "rgba(0,0,200,0.6)",
              pointBorderColor: '#250EBF',
              
              data: data.Venezuela
          }
        ]
      };
  }

};
</script>

<style>
.small {
  width: 500px;
  height: 200px;
  margin: 10px 350px;
}
 
</style>
