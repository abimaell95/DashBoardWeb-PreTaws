<template >
<div >
  
  <v-app >
     <router-view></router-view>  
    <v-navigation-drawer dark v-model="drawer" app>
        <v-row class="ml-3" justify="center" >
            <img
                src="../assets/taws.png"  alt="Taws" width="150" height="150">
        
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
                                        <li>
        <a class="text-white"
          :href= 'item.rutas'
          target="_blank"
          rel="noopener"
          >{{item.text}}</a
        >
      </li>

                                </v-list-item-title>
                            </v-list-item-content>
                            </v-list-item>
                        </v-list-item-group>
                        </v-list>

                </v-expansion-panel-content>
              
              </v-expansion-panel>
            </v-expansion-panels>
        
    </v-navigation-drawer>

    <v-app-bar app color="black" dark>
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
          rutas: 'https://www.facebook.com/tawsespol/'
         
        },
        {
          icon: 'mdi-twitter',
          text: 'Twitter',
          rutas: 'https://twitter.com/TawsEspol'

        },
        {
          icon: 'mdi-instagram',
          text: 'Instagram',
          rutas: 'https://www.instagram.com/taws_espol/'

        }
      ],
      items: [
        
        {
          icon: 'mdi-chart-bar-stacked',
          text: 'Bar',
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
     model:1,
     

    })
  
  }
  
</script>
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}

</style>
