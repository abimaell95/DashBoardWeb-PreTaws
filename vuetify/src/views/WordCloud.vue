<template>
  <div>
  <v-container>
    
      
      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3"></h1>
      </v-col>
      <v-container>
        <v-row justify="center">     
          <v-col class="m-2 text-center" cols="12" >
            <h2 class="headline font-weight-bold mb-3">Word Cloud</h2>
          </v-col>
        </v-row>

        <v-row align="center" justify="center">
          <v-col cols="4">
         <v-expansion-panels focusable>
            <v-expansion-panel >
                <v-expansion-panel-header > 
                   <v-icon>mdi-map</v-icon> Select the Country
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-list>
                         
                        </v-list>
                </v-expansion-panel-content>
                </v-expansion-panel>
         </v-expansion-panels>

         </v-col>
        </v-row>
        <Foto/>
      </v-container>
      
  </v-container>
  </div>
</template>
<script>
  export default {
    data: () => ({
     items: [
        {
          text: 'Ecuador',
          rutas:'/bar'
          
        },
        {
          text: 'Mexico',
          rutas:'/pie'
        },
        {
          text: 'Venezuela',
          rutas:'/time'
        }
    ],
  })
}
</script>