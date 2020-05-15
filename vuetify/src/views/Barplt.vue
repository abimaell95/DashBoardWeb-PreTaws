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
<p>{{select}}</p>
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
      select: "Ecuador",
      options: [
    "Ecuador", "México", "Venezuela"
      ]
    };
  },
async mounted() {
    let resp = await fetch(
      "https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/Bar/" +
        this.select +
        ".json"
    );
    let data = await resp.json();
    this.datacollection = {
        labels: [
        "Politic",
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
            label: "Positivo",
            backgroundColor: "#249EBF",
            pointBackgroundColor: "white",
            borderWidth: 2,
            pointBorderColor: "#249EBF",
            data: data.Positivo
          },
          {
            label: "Neutro",
            backgroundColor: "#746A68",
            pointBackgroundColor: "white",
            borderWidth: 2,
            pointBorderColor: "#249EBF",
            data: data.Neutro
          },
          {
            label: "Negativo",
            backgroundColor: "#ff8000",
            pointBackgroundColor: "white",
            borderWidth: 2,
            pointBorderColor: "#249EBF",
            data: data.Negativo
          }
        ]
      };
  },
async updated()  {
    let resp = await fetch(
      "https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/Bar/" +
        this.select +
        ".json"
    );
    let data = await resp.json();
    this.datacollection = {
        labels: [
        "Politic",
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
            label: "Positivo",
            backgroundColor: "#249EBF",
            pointBackgroundColor: "white",
            borderWidth: 2,
            pointBorderColor: "#249EBF",
            data: data.Positivo
          },
          {
            label: "Neutro",
            backgroundColor: "#746A68",
            pointBackgroundColor: "white",
            borderWidth: 2,
            pointBorderColor: "#249EBF",
            data: data.Neutro
          },
          {
            label: "Negativo",
            backgroundColor: "#ff8000",
            pointBackgroundColor: "white",
            borderWidth: 2,
            pointBorderColor: "#249EBF",
            data: data.Negativo
          }
        ]
      };
  }
}
</script>

<style>
.small {
  max-width: 500px;
  margin: 150px auto;
}
 
</style>






