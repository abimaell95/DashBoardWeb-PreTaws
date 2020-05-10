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
            <v-select :items="items" label="Select the country" ></v-select>
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
    }, data: () => ({
      items: ['Ecuador', 'Mexico', 'Venezuela'],
    }),
  }
</script>

