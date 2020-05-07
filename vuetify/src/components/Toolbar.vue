<template >
<div >
  
  <v-app id="inspire">
     <router-view></router-view>  
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
                            <v-list-item v-for="(item, i) in itemssm" :key="i" >
                            <v-list-item-icon>
                                <v-icon v-text="item.icon"></v-icon>
                            </v-list-item-icon>
                            <v-list-item-content>
                                <v-list-item-title>
                                  <router-link class="white--text" :to="item.rutas" > {{item.text}}</router-link>
                                </v-list-item-title>
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

   
  </v-app>
</div>
  
</template>



<script>
  export default {

   data: () => ({
    drawer: null,
    itemssm: [
        {
          icon: 'mdi-facebook',
          text: 'Facebook',
          rutas: 'https://www.facebook.com/'
         
        },
        {
          icon: 'mdi-twitter',
          text: 'Twitter',
          rutas: 'https://www.facebook.com/'

        },
        {
          icon: 'mdi-instagram',
          text: 'Instagram',
          rutas: '/time'

        }
      ],
      items: [
        
        {
          icon: 'mdi-chart-pie',
          text: 'Bar Plot',
          rutas:'/barplt'
        },
         {
          icon: 'mdi-radar',
          text: 'Radar',
          rutas:'/radar'

        },
        {
          icon: 'mdi-chart-timeline-variant',
          text: 'Timeseries',
          rutas:'/time'

        },
       
        {
          icon: 'mdi-wordpress',
          text: 'WordCloud',
          rutas:'/wc'
          
        },
    ],
      names : 
      [ 
        {texto: 'Typs of Chart',icono:'mdi-graph'},
        {texto:"Social Media" ,icono:'mdi-account-group'}
      ],
          paises: [
      {
        text: "Ecuador",
        href: "../assets/taws.png"
      },
      {
        text: "Venezuela",
        href: "../assets/taws.png"
      },
      {
        text: "México",
        href: "../assets/taws.png"
      }
    ],
     model:1,
    })
  
  }
</script>