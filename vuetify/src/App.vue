<template>

  <v-app>
    <div> 
           
              <Toolbar />              
                   
              <Carrusel />
      
    </div>
  </v-app>
 

</template>

<script>
import Toolbar from './components/Toolbar';
import Carrusel from './components/Carrusel';

export default {
  name: 'App',

  components: {
  Toolbar,Carrusel
  },

  data: () => ({
    
  })
};
</script>
