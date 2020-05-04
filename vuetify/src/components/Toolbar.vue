<template >
<div id="app">
  <v-app id="inspire">
    <v-navigation-drawer dark v-model="drawer" app>
        <v-row class="mb-3 mt-3 ml-3" >
           <v-avatar size=150>
                 <img
                src="../assets/taws.png"  alt="Taws" height="150" >
            </v-avatar>
        </v-row>

        <v-expansion-panels focusable>
            <v-expansion-panel >
                <v-expansion-panel-header > 
                    <v-icon >mdi-graph</v-icon> Types of Graph
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
                                      <router-link class="white--text" :to="item.rutas" > {{item.text}}</router-link>

                                   </v-list-item-title>
                            </v-list-item-content>
                            </v-list-item>
                        </v-list-item-group>
                        </v-list>

                </v-expansion-panel-content>
                </v-expansion-panel>
                <v-expansion-panel >
                <v-expansion-panel-header > 
                    <v-icon >mdi-account-group</v-icon>
                    Social Media
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-list>
                        <v-list-item-group v-model="model">
                            <v-list-item
                            v-for="(item, i) in itemssm"
                            :key="i"
                            >
                            <v-list-item-icon>
                                <v-icon v-text="item.icon"></v-icon>
                            </v-list-item-icon>
                            <v-list-item-content>
                                <v-list-item-title v-text="item.text"></v-list-item-title>
                            </v-list-item-content>
                            </v-list-item>
                        </v-list-item-group>
                        </v-list>

                </v-expansion-panel-content>
                </v-expansion-panel>
        </v-expansion-panels>
    </v-navigation-drawer>

    <v-app-bar app color="indigo" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-content>
     <Inicio/>
     <Carrusel/>
     
    </v-content>
    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; 2019</span>
    </v-footer>
  </v-app>
</div>
  
</template>







<script>
import Inicio from '@/components/Inicio.vue'
import Carrusel from '@/components/Carrusel.vue'

  export default {
      components: {
          Inicio,Carrusel
      },
    
   data: () => ({
    drawer: null,
    itemssm: [
        {
          icon: 'mdi-facebook',
          text: 'Facebook',
         
        },
        {
          icon: 'mdi-twitter',
          text: 'Twitter',
          
        },
        {
          icon: 'mdi-instagram',
          text: 'Instagram',
        }
      ],
      items: [
        {
          icon: 'mdi-chart-bar',
          text: 'Bar',
           rutas:'/bar'
          
        },
        {
          icon: 'mdi-chart-pie',
          text: 'Pie',
          rutas:'/pie'
        },
        {
          icon: 'mdi-chart-timeline-variant',
          text: 'Timeseries',
          rutas:'/time'

        },
        {
          icon: 'mdi-radar',
          text: 'Radar',
          rutas:'/radar'

        },
      ],
      names : [ {texto: 'Types of Chart',
                icono:'mdi-graph'},{texto:"Social Media" ,icono:'mdi-account-group'}],
      model: 1,
    }),
  
  }
</script>