<template>
  <div class="about">

    <Toolbar/>
    <HelloWorld/>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae debitis laudantium nisi quia voluptates ipsa? Doloremque doloribus, fuga beatae ea assumenda nam debitis eaque quaerat ullam consequatur impedit temporibus asperiores!</p>
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
  }
}
</script>
