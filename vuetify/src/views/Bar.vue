<template>
    <div>
        <Toolbar/>
          <h1>Bar Chart</h1>





          
       <Carrusel/>
    </div>
</template>


<script>
import HelloWorld from '@/components/HelloWorld.vue'
import Toolbar from '@/components/Toolbar.vue'
import Carrusel from '@/components/Carrusel.vue'
export default {
  name: 'Home',
  components: {
    Toolbar,Carrusel,HelloWorld
  }
}
</script>