<template>
  <div>
    <Toolbar />
    <h1>Linea de Tiempo</h1>
    <Carrusel />
  </div>
</template>


<script>
import Inicio from "@/components/Inicio.vue";
import Toolbar from "@/components/Toolbar.vue";
import Carrusel from "@/components/Carrusel.vue";
export default {
  name: "Home",
  components: {
    Toolbar,
    Carrusel,
    Inicio
  }
};
</script>