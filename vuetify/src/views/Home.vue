<template>
  <div>
    <Toolbar />
    <Inicio />
    <Carrusel />
  </div>
</template>

<script>
// @ is an alias to /src
import Inicio from "@/components/Inicio.vue";
import Toolbar from "@/components/Toolbar.vue";
import Carrusel from "@/components/Carrusel.vue";
export default {
  name: "Home",
  components: {
    Toolbar,
    Carrusel,
    Inicio
  },
  data() {
    return {
      drawer: true
    };
  }
};
</script>
