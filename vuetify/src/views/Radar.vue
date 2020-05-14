<template>
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
</script>

