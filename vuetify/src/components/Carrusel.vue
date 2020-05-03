<template>
      <div>
    <router-view></router-view>

    <v-carousel cycle height="15ñ0" hide-delimiter-background show-arrows-on-hover>
    <v-carousel-item v-for="(slide, i) in slides" :key="i">
      <v-sheet :color="colors[i]" height="100%">
        <v-row class="fill-height ml-5" align="center">
          <div >
            <p class="display-2 text-right">
            {{ slide }} 
            </p>
          <p class="display-2 text-right"> {{ amount[i] }} </p>
          </div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
            </div>

</template>

<script>
  export default {
    name:'Carrusel',
    data () {
      return {
        colors: [
          'indigo',
          'warning',
          'pink darken-2',
          'red lighten-1',
          'deep-purple accent-4',
        ],
        slides: [
          'Publications',
          'Second',
          'Third',
          'Fourth',
          'Fifth',
        ],
        amount:[
          '100',
          '200',
          '300',
          '400',
          '500',

        ]
      }
    },
  }
</script>
