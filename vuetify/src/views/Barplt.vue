<template>
  <v-container>
  <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3"></h1>
      </v-col>
      <br>
     <v-row align="center" justify="center">
          <v-col class="d-flex text-center" cols="12" sm="6">
            <v-select @click="fillData()" v-model='selected' :options="options" label="Select the year" ></v-select>
          </v-col>
        </v-row>
        <div>
    <b-form-select @click="fillData()" v-model="selected" :options="options"></b-form-select>
    <div class="mt-3">Selected: <strong @click="fillData()">{{ selected }}</strong></div>
  </div>
  <div class="small">

    <Chart :chart-data="datacollection"></Chart>
    <button @click="fillData()">Randomize</button>
  </div>
   

  </v-container>
</template>

<script>
  import Chart from '@/components/Chart'

  export default {
    components: {
      Chart
    },
    data: ()  => {
      return {
        datacollection: null,
        selected: null,
        options: [
          { value: null, text: 'Please select some item' },
          { value: 'a', text: 'This is First option' },
          { value: 'b', text: 'Default Selected Option' },
          { value: 'c', text: 'This is another option' },
          { value: 'd', text: 'This one is disabled', disabled: true }
        ]
      } 
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
        this.datacollection = {
         labels: [ 'Crime',"Política","Corrupcion","Salud","Religion", 'Desempleo', 'Educación','Deportes','Economia'],
          datasets: [
            {
              label: 'Positivo',
              backgroundColor: '#249EBF',
              pointBackgroundColor: 'white',
              borderWidth: 2,
              pointBorderColor: '#249EBF',
              //Data to be represented on y-axis
              data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(),this.getRandomInt()],
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
        }

        //Chart.js options that controls the appearance of the chart
    
        },
    
      getRandomInt () {
        return Math.floor(Math.random()*(40-2) )
      }
    }
  }
</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
<<<<<<< HEAD
=======
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
        <h3 class="text-center">Bar Plot</h3>
        <v-row align="center" justify="center">
      <v-col class="d-flex text-center" cols="12" sm="6">
        <v-select v-model='select' :items="items" label="Select the country" ></v-select>
      </v-col>
        </v-row>
      </div>
      <br><br>
       <Chart/>

    </div>
  </section>
</template>-->

<!--<script>
  import Chart from '@/components/Chart'

  export default {
    name: 'VueChartJS',
    components: {
      Chart
    }, data: () => ({
      items: ['Ecuador', 'Mexico', 'Venezuela'],select
    }),
>>>>>>> da2ebfd76f93a28f0f87917d03eec0f020a4199a
  }
</style>

