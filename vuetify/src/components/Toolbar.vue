<template>
  <v-card flat height="50px" tile >
    <v-toolbar dense>
      
      <v-app-bar-nav-icon  @click="drawer =! drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      
    </v-toolbar>
    <v-navigation-drawer app v-model="drawer" dark temporary>
        <v-row class="mb-3 mt-3 ml-3" >
            <v-avatar color="indigo">
              <v-icon dark>mdi-account-circle</v-icon>
            </v-avatar>
        </v-row>





        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header>
               <v-icon>mdi-graph</v-icon>
               Types of Chart</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-list>
                  <v-list-item-group v-model="model">
                    <v-list-item
                      v-for="(item, i) in items"
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


                <v-list>
                          <v-list-item-group >
                            <v-list-item>
                              <v-list-item-icon>
                                <v-icon>mdi-chart-bar</v-icon>
                              </v-list-item-icon>
                              <v-list-item-content>
                                  <v-list-item-title> 
                                <router-link to="/about" class="white--text" >Bar Chart</router-link>
                                  </v-list-item-title>
                              </v-list-item-content>
                            </v-list-item>
                            <v-list-item>
                              <v-list-item-icon>
                                <v-icon>mdi-chart-pie</v-icon>
                              </v-list-item-icon>
                              <v-list-item-content>
                                <v-list-item-title>                     
                                  <router-link to="/about" class="white--text" >Pie Chart</router-link>
                        </v-list-item-title>
                              </v-list-item-content>
                            </v-list-item>
                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-chart-timeline-variant</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>                      
                            <router-link to="/about" class="white--text" >Timeseries Chart</router-link>
                      </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                      <v-list-item>
                        <v-list-item-icon>
                          <v-icon>mdi-radar</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>  
                            <router-link to="/botones" class="white--text" >Radar Chart</router-link>
                      </v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                </v-list>
              </v-expansion-panel-content>
          </v-expansion-panel>

            <v-expansion-panel>
                    <v-expansion-panel-header>
                      <v-icon>mdi-account-group</v-icon>Social Media</v-expansion-panel-header>
                    <v-expansion-panel-content>
              <v-list>
                  <v-list-item-group >
                    <v-list-item>
                      <v-list-item-icon>
                        <v-icon>mdi-facebook</v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Facebook</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-icon>
                        <v-icon>mdi-twitter</v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Twitter</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-icon>
                        <v-icon>mdi-instagram</v-icon>
                      </v-list-item-icon>
                      <v-list-item-content>
                        <v-list-item-title>Instagram</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>
              </v-expansion-panel-content>
          
          </v-expansion-panel>
        </v-expansion-panels>

  </v-navigation-drawer>
  </v-card>
  
</template>

<script>
  export default {
    
    data () {
      return{
        drawer:true
      }
    }
  }
</script>

