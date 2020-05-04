<template>
  <div>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img :src="require('../assets/taws.png')" class="my-3" contain height="200" />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3"></h1>

      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">BAR CHART</h2>
      	
        <v-row justify="center">     
      <a
            v-for="(link, i) in paises"
            :key="i"
            :href="link.href"
            class="subheading mx-3"
            target="_blank"
          >{{ link.text }}</a>
      
        </v-row>
      </v-col>


      
    </v-row>
  </v-container>
  
  </div>
</template>
