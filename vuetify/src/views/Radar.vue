<template>
  <section class="container">
    <h1>Demo examples of vue-chartjs</h1>
    <div class="columns">
      <div class="column">
        <h3>Line Chart</h3>
      </div>
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