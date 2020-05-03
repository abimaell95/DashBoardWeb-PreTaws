<template>
<div>
    <Toolbar/>
    <HelloWorld/>
        <Carrusel/>

</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Toolbar from '@/components/Toolbar.vue'
import Carrusel from '@/components/Carrusel.vue'
export default {
  name: 'Home',
  components: {
    Toolbar,Carrusel,HelloWorld
  },
   data () {
      return{
        drawer:true
      }
    }

}
</script>
