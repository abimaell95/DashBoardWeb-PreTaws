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
          label="Select the country"
        ></v-select>

      </v-col>
    </v-row>

    <div class="small">
      <Chart :chart-data="datacollection"></Chart>
    </div>
  </v-container>
</template>

<script>
import Chart from "@/components/Chart";

export default {
  components: {
    Chart
  },
  data: () => {
    return {
      datacollection: {},
      select: [],
      options: [
        { value: 20, text: "Ecuador" },
        { value: 60, text: "Venezuela" },
        { value: 50, text: "México" }
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
            label: "Positivo",
            backgroundColor: "#249EBF",
            pointBackgroundColor: "white",
            borderWidth: 2,
            pointBorderColor: "#249EBF",
            //Data to be represented on y-axis
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






