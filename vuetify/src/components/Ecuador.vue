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
            <v-select  class="form-option"  :items="items" label="Select the country" v-on:change="changeRoute"></v-select>
            
          </v-col>
        </v-row>

      </v-container>
</v-container>
