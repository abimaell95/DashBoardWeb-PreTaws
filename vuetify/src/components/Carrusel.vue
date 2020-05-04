<template>
      <div>
        <v-carousel cycle height="15ñ0" hide-delimiter-background show-arrows-on-hover>
        <v-carousel-item v-for="(slide, i) in slides" :key="i">
          <v-sheet :color="colors[i]" height="100%">
            <v-row class="fill-height ml-5" justify="center">
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
          'pink darken-2',
          'deep-purple accent-4',
        ],
        slides: [
          'Ecuador',
          'Venezuela',
          'Mexico',

        ],
        amount:[
          '100',
          '200',
          '300',
        ]
      }
    },
  }
</script>
