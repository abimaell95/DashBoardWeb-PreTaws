<template>
  <v-container dark>
    <v-col class="mb-4">
      <h1 class="display-2 font-weight-bold mb-3"></h1>
    </v-col>
      <v-row justify="center">     
          <v-col class="m-1 text-center" cols="12" >
            <h2 class="font-weight-bold mb-3 display-3">Radar</h2>
          </v-col>
        </v-row>
    <v-row align="center" justify="center">
      <v-col class="d-flex text-center" cols="12" sm="6">
        <v-select 
          v-model="select"
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
          label: "Ecuador",
          backgroundColor: "#f6f578",
          pointRadius: 0,
          borderColor: "#fcbf1e",
          borderWidth: 2,

          data: data.Ecuador
        },
        {
          label: "México",
          backgroundColor: "#b2ebf2",
          pointRadius: 0,
          borderColor: "#00bcd4",
          borderWidth: 2,

          data: data.Mexico
        },
        {
          label: "Venezuela",
          backgroundColor: "#fc7e2f",
          pointRadius: 0,
          borderColor: "#dd2c00",
          borderWidth: 2,

          data: data.Venezuela
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
          label: "Ecuador",
          backgroundColor: "#f6f578",
          pointRadius: 0,
          borderColor: "#fcbf1e",
          borderWidth: 2,

          data: data.Ecuador
        },
        {
          label: "México",
          backgroundColor: "#b2ebf2",
          pointRadius: 0,
          borderColor: "#00bcd4",
          borderWidth: 2,

          data: data.Mexico
        },
        {
          label: "Venezuela",
          backgroundColor: "#fc7e2f",
          pointRadius: 0,
          borderColor: "#dd2c00",
          borderWidth: 2,

          data: data.Venezuela
        }
      ]
    };
  }
  //Chart.js options that controls the appearance of the chart
};
</script>

<style>
.small {
  max-width: 700px;
  margin: 20px 350px;
}
 
</style>

