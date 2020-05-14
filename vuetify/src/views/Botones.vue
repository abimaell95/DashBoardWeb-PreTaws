<template>
<v-container>
    <div id='app'></div>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum voluptates aliquid eum maxime perspiciatis voluptatem ex natus quibusdam fugiat culpa! Natus deleniti quia eius maiores expedita ipsum quas iusto neque!</p>
    </v-container>
    <!--<v-container>
      <br>
      <br>
      <br>
        <v-row>
            <v-col>
                <v-btn>Texto</v-btn>

                <v-btn dark color="primary">Texto</v-btn>
                <v-btn dark color="blue">Texto</v-btn>
                <v-btn text large color="warning" >Hola</v-btn>
                 <v-btn large  color="success">Normal</v-btn>

            </v-col>
        </v-row>

    </v-container>
        
    </div>-->
</template>
<script>
  var chart = c3.generate({
    bindto: 'app',
    data: {
      columns: [
        ['data1', 30, 200, 100, 400, 150, 250],
        ['data2', 50, 20, 10, 40, 15, 25]
      ]
    }
    })
</script>