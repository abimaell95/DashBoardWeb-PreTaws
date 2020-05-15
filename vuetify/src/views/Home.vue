<template>
<v-container>
  <v-section>
    <v-row class="text-center">
      <v-col cols="12">
        <br>
        <br>
        <br>
      </v-col>

      <v-col class="mb-4" cols="12" sm="6" offset-sm="3">
        <h1 class="display-2 font-weight-bold mb-3"></h1>

        <h1 class="subheading font-weight-regular">
    Welcome to the relevant news Dashboard at
           Latin American countries
        </h1>
      </v-col>

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
        <h1 class="headline font-weight-bold mb-3">Topics</h1>
    <br>
        <v-row justify="center" class="mb-5" cols="12">
          <p v-for="(link, i) in temas" :key="i" class="grey--text mx-3">{{ link}}</p>
        </v-row>
      </v-col>

      
    </v-row>
    
  </v-section>
   <v-card max-width="1000" class="mx-auto" >
    <v-container class="pa-1">
      <v-item-group v-model="selected" multiple >
        <v-row>
          <v-col v-for="(item, i) in items" :key="i" cols="12" md="4" >
            <v-item v-slot:default="{ active, toggle }">
              <v-img :src="`https://cdn.vuetifyjs.com/images/${item.src}`" height="150"  class="text-right pa-2" @click="toggle" >
                <v-btn icon dark >
                  <v-icon>
                    {{ active ? 'mdi-heart' : 'mdi-heart-outline' }}
                  </v-icon>
                </v-btn>
              </v-img>
            </v-item>
          </v-col>
        </v-row>
      </v-item-group>
    </v-container>
  </v-card>
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
          src: 'backgrounds/bg.jpg',
        },
        {
          src: 'backgrounds/md.jpg',
        },
        {
          src: 'backgrounds/bg-2.jpg',
        },
       
      ],
      selected: [],
  })
};
</script>
