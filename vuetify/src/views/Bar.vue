<template>
  <div>
    <Toolbar />

    <Carrusel />
  </div>
</template>

<script>
export default {
  name: "Bar",

  data: () => ({
    importantLinks: [
      {
        text: "Documentation",
        href: "https://vuetifyjs.com"
      },
      {
        text: "Chat",
        href: "https://community.vuetifyjs.com"
      },
      {
        text: "Made with Vuetify",
        href: "https://madewithvuejs.com/vuetify"
      },
      {
        text: "Twitter",
        href: "https://twitter.com/vuetifyjs"
      },
      {
        text: "Articles",
        href: "https://medium.com/vuetify"
      }
    ],
    paises: [
      {
        text: "Explore components",
        href: "https://vuetifyjs.com/components/api-explorer"
      },
      {
        text: "Select a layout",
        href: "https://vuetifyjs.com/layout/pre-defined"
      },
      {
        text: "Frequently Asked Questions",
        href: "https://vuetifyjs.com/getting-started/frequently-asked-questions"
      }
    ]
  })
};
</script>





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