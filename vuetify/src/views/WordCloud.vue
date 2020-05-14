<template>
   <v-container>
    
      
      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3"></h1>
      </v-col>
        <v-row justify="center">     
          <v-col class="m-1 text-center" cols="12" >
            <h2 class="font-weight-bold mb-3 display-3">Word Cloud</h2>
          </v-col>
        </v-row>
        <v-row align="center" justify="center">
          <v-col class="d-flex text-center" cols="12" sm="6">
            <v-select v-model='select' :items="items" label="Select the country" ></v-select>         
          </v-col>   
    
        </v-row>   
      
    <v-img :src=select alt="km" class="my-1" contain height="500" />
</v-container>


 
</template>
<script>
import Ecuador from  "../assets/Ecuador.jpg"
  export default {
    name: 'WordCloud',

    data(){
      return{
        select:Ecuador, //este es el primer valor del select
   
        items: [
          { text : 'Ecuador',
            value:Ecuador      
          },
          {text : 'Mexico',
            value:require('../assets/Mexico.jpg',)
          },
          {text : 'Venezuela',
           value: require('../assets/Venezuela.jpg',)
          }
          ]}  
          
  },
    updated(){
    console.log(this.select)
  }
}
</script>