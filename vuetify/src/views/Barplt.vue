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

    </div>
  </section>
</template>

<script>
  import Chart from '@/components/Chart'

  export default {
    name: 'VueChartJS',
    components: {
      Chart
    }
  }
</script>



