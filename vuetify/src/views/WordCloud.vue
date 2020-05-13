<template>
   <v-container>
    
      
      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3"></h1>
      </v-col>
      <v-container>
        <v-row justify="center">     
          <v-col class="m-2 text-center" cols="12" >
            <h2 class="font-weight-bold mb-3 display-3">Word Cloud</h2>
          </v-col>
        </v-row>
      </v-container>
     <v-container fluid>
        <v-row align="center" justify="center">
          <v-col class="d-flex text-center" cols="12" sm="6">
            <v-select :items="items" label="Select the country" ></v-select>
          </v-col>
        </v-row>
        
      </v-container>
</v-container>


 
</template>
<script>
import Carrusel from '@/components/Carrusel.vue';

  export default {
     components: {
        Carrusel
      },
    data: () => ({
    itemsim: [
          { name : 'Ecuador',
            src: require('../assets/Ecuador.jpg')
           
          },
          {name : 'Mexico',
            src: require('../assets/Mexico.jpg',)
          },
          {name : 'Venezuela',
           src: require('../assets/Venezuela.jpg',)
          },
        ],
        model: 0,
        links: [
        'Home',
        'About Us',
        'Team',
        'Services',
        'Blog',
        'Contact Us',
      ],
       items: ['Ecuador', 'Mexico', 'Venezuela'],
  })
}
</script>