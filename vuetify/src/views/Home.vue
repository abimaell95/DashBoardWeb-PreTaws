<template>
<v-container>
  <v-section>
    <v-row class="text-center">
      <v-col cols="12">
        <br>
      </v-col>

      <v-row class="mb-4" cols="12" sm="6" offset-sm="3">

        <h1 class="subheading font-weight-regular">
    Welcome to the relevant news Dashboard at
           Latin American countries
        </h1>
      </v-row>

      <v-col class="mb-1" cols="6" sm="6" offset-sm="3">
        <h1 class="headline font-weight-bold mb-3">Countries</h1>
         <v-row justify="center" >
              <v-col v-for="(item,i) in paises" :key="i"  sm="4">
                <v-img :src="item.src" :alt="item.text" class="my-2" contain height="80">
                </v-img>
                    <p v-text="item.text"></p>
              </v-col>
         </v-row>
      </v-col>
      <br>
      <v-col class="mb-5" cols="12">
        <h1 class="display-2 font-weight-bold mb-3">Topics</h1>
        <v-row justify="center" class="mb-5" cols="12">
          <h5 v-for="(link, i) in temas" :key="i" class="grey--text mx-3">{{ link}}</h5>
        </v-row>
      </v-col>

      
    </v-row>
    
  </v-section>
  <v-row>
  <v-card v-for="(item,i) in items" :key="i" class="mx-auto " max-width="350" outlined >
    <v-list-item :class="item.color">
      <v-list-item-content  >
             <div> <v-icon dark>{{item.icon}}</v-icon></div>
        <v-list-item-title class="display-2 mb-1 white--text" align="right" > {{item.label}}</v-list-item-title>
        <v-list-item-subtitle align="right" class="white--text">More Publication</v-list-item-subtitle>
        <v-list-item-subtitle align="right" class="display-1 white--text">{{item.text}} </v-list-item-subtitle>

      </v-list-item-content>

    </v-list-item>
  </v-card>
  </v-row>
</v-container>
</template>

<script>
export default {
  name: "Home",

  data: () => ({
    temas: ["Crime", "Politics", "Corruption",
     "Health", "Religion", 'Unemployment', 'Education', "Economy",
     "Sports"
    ],
    paises: [
      {
        text: "Ecuador",
        src: require('../assets/Ecuador.png')
      },
      {
        text: "México",
        src: require('../assets/Mexico.png')
      },
      {
        text: "Venezuela",
        src: require('../assets/Venezuela.png')
      }
    ],
    items: [
        {
          label :'Country ',
          text: 'Mexico',
          icon: 'mdi-google-maps',
          color: 'blue-grey darken-3'
        },
        {
          label :'Month',
          text: 'August - 489 ',
          icon: 'mdi-calendar',
          color: 'blue-grey darken-2'
        },
        {
          label :'Year',
          text: '2017 - 1347',
          icon: 'mdi-newspaper',
          color: 'blue-grey darken-3'
        },
       
      ]
  })
};
</script>
