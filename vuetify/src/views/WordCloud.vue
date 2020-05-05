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
                        <v-list-item-group v-model="model">
                          <v-list-item v-for="(item, i) in items" :key="i">
                            <v-list-item-icon>
                                <v-icon v-text="item.icon"></v-icon>
                            </v-list-item-icon>
                            <v-list-item-content>
                                   <v-list-item-title >
                                      <router-link :to="{ name: 'Fotos', params: {id : item}}" 
                                        v-for="(item,index) of fotosArreglo" :key="index">
                                      </router-link>
                                      <Foto></Foto>
        <button @click="home">Home</button>
        <button @click="anterior">Anterior</button>
        <button @click="siguiente">Siguiente</button>
                                   </v-list-item-title>
                            </v-list-item-content>
                            </v-list-item>
                        </v-list-item-group>
                        </v-list>

                </v-expansion-panel-content>
                </v-expansion-panel>
         </v-expansion-panels>
         </v-col>
        </v-row>
      </v-container>
      
  </v-container>
  </div>
</template>
<script>
import Foto from "@/components/Fotos.vue"

  export default {
    components:{
        Foto
     },
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
     fotosArreglo: [1,2,3]
    }),
      methods: {
         home() {
             this.$router.push('/')
         },
         anterior() {
             this.$router.back()
         },
         siguiente() {
             this.$router.back()
         }
     }
  }
</script>