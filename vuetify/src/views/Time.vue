<template>
  <v-container>
    <v-col class="mb-4">
      <h1 class="display-2 font-weight-bold mb-3"></h1>
    </v-col>
    <v-row align="center" justify="center">
      <v-col class="d-flex text-center" cols="12" sm="6">
        <v-select
          v-model="select"
          v-on:change="fillData(`${select}`)"
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
      datacollection: {},
      select: [],
      options: [
        { value: 20, text: "Economía" },
         {value:10,  text: "Crimen"},
          {value:25 ,text:"Política"},
         {value:30 , text:"Corrupción"},
         {value:35 , text:"Salud"},
          {value:40 ,text:"Religion"},
          {value:80 ,text:"Desempleo"},
         { value:50 ,text:"Educación"},
         { value:70,text:"Deportes"},
   
      ]
    };
  },

  methods: {
    fillData(valor) {
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
              data: [40, 20, 60, 50, 90, 10, 20, 40,80],
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
              
              data: [valor,
              valor,
              valor,
              valor,
              valor,
              valor,
              valor,
              valor,
              valor]
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
