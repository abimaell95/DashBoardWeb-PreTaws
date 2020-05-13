<template>
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
        <v-select id='user' :items="items" label="Select the country" @change="printselect" ></v-select>
      </v-col>
      </v-row>
      </div>
      <br><br>
      <Chart :valor="value"  />

    </div>
  </section>
</template>

<script>
  import Chart from '@/components/Chart'
  export default {
    name: 'VueChartJS',
    components: {
      Chart
    }, data: () => ({
      items: ['Ecuador', 'Mexico', 'Venezuela'],
      value: 'kjwajasasj',
    }),

     methods: {
            printselect(value) {
              this.value=value
/*this.$router.push({path:'/educationOption/' + this.id })*/
            }
        },
      updated() {
        console.log(this.value)
      },
  }

  
</script>



