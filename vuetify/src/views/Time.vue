<template>
  <section class="container">
     <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3"></h1>
      </v-col>
      <br>
    <div class="columns">
        <h3 class="text-center">Time series Chart</h3>

        <v-row align="center" justify="center">
          <v-col class="d-flex text-center" cols="12" sm="6">
            <v-select :items="items" label="Select the topic" ></v-select>
          </v-col>
        </v-row>

      </div>
      <br><br>
       <Timese/>


  </section>
</template>

<script>
  import Timese from '@/components/Timese'

  export default {
    name: 'VueChartJS',
    components: {
      Timese
    }, data: () => ({
      items:[ "Crimen","Política","Corrupcion",
    "Salud","Religion", 'Desempleo', 'Educación', 'Deportes',
    'Economia'],
    }),
  }
</script>

