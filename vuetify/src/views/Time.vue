<template>
  <section class="container">
     <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3"></h1>
      </v-col>
      <br>
    <div class="columns">
      <div class="column">

        <h3 class="text-center">Line Chart</h3>
      </div>
      <br><br>
       <Chart/>

        <h3 class="text-center">Time series Chart</h3>
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
    }
  }
</script>

