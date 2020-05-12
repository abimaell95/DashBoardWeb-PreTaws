<template>
      <div>
        <v-carousel cycle height="15ñ0" hide-delimiters hide-delimiter-background show-arrows-on-hover dark>
        <v-carousel-item v-for="(slide, i) in slides" :key="i">
          <v-sheet :color="colors[i]" height="100%">
            <v-row class="fill-height ml-5" justify="center">
              <div >
                <p class="display-2 text-right">
                {{ slide }} 
                </p>
              <p class="display-2 text-right"  >{{ amount[i]}}</p>
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
          'blue lighten-3',
          'teal lighten-3 ',
          'deep-purple lighten-3',
        ],
        slides: [
          'Ecuador',
          'Venezuela',
          'Mexico',

        ],
        amount:[
          'Crime',
          'Health',
          'Sport',
        ]
      }
    },
  }
</script>
