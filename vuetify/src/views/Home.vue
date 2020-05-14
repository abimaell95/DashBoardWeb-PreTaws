<template>
  <v-container >
    <v-row class="text-center">
      <v-col cols="12">
        <br>
        <br>
        <br>
      </v-col>

      <v-col class="mb-4" cols="12" sm="6" offset-sm="3">
        <h1 class="display-2 font-weight-bold mb-3"></h1>

        <h2 class="subheading font-weight-regular">
          Bienvenido al dashboard  de noticias relevantes en algunos
          países de America Latina
        </h2>
      </v-col>

      <v-col class="mb-0" cols="6" sm="6" offset-sm="3">
        <h2 class="headline font-weight-bold mb-3">Países</h2>
         <v-row justify="center" >
              <v-col v-for="(item,i) in paises" :key="i"  sm="4">
                <v-img :src="item.src" :alt="item.text" class="my-3" contain height="100">
                </v-img>
                    <p class="display-1 " v-text="item.text"></p>
              </v-col>
         </v-row>
      </v-col>
      <br>
      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">Tópicos</h2>
    <br>
        <v-row justify="center">
          <a v-for="(link, i) in temas" :key="i" class="grey--text mx-3">{{ link}}</a>
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
        src: require('../assets/Ecuador.png')
      },
      {
        text: "Mexico",
        src: require('../assets/Mexico.png')
      },
      {
        text: "Venezuela",
        src: require('../assets/Venezuela.png')
      }
    ]
  })
};
</script>
