<template>
    <v-container>
        <v-row>
            <v-col>
                <v-btn>Texto</v-btn>

                <v-btn dark color="primary">Texto</v-btn>
                <v-btn dark color="blue">Texto</v-btn>
                <v-btn text large color="warning" >Hola</v-btn>
                 <v-btn large  color="success">Normal</v-btn>

            </v-col>
        </v-row>

    <Menul/>
    </v-container>
        
    
</template>
<script>
  import Menul from '@/components/Menul'

  export default {
    name: 'VueChartJS',
    components: {
      Menul
    }
  }
</script>