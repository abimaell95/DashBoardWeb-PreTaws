<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img :src="require('../assets/taws.png')" class="my-3" contain height="200" />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3"></h1>

        <p class="subheading font-weight-regular">
          Bienvenido al dashboar de noticias relevantes en algunos
          <br />países de America Latina
        </p>
      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">Países</h2>
      	
        <v-row justify="center">     
      <a
            v-for="(link, i) in paises"
            :key="i"
            :href="link.href"
            class="subheading mx-3"
            target="_blank"
          >{{ link.text }}</a>
      
        </v-row>
      </v-col>
      <br>
      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">Tópicos</h2>
    <br>
        <v-row justify="center">
          <a
            v-for="(link, i) in temas"
            :key="i"
            class="subheading mx-3"
            target="_blank"
          >{{ link}}</a>
        </v-row>
      </v-col>

      
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Home",

  data: () => ({
    temas: [ "Crimen","Política","Corrupcion",
    "Salud","Religion", 'Desempleo', 'Educación'
    ],
    paises: [
      {
        text: "Ecuador",
        href: "../assets/ecuador.png"
      },
      {
        text: "Venezuela",
        href: "../assets/venezuela.png"
      },
      {
        text: "México",
        href: "../assets/ecuador.png"
      }
    ]
  })
};
</script>
