<template>
    <body>
        
        <p>
           politica : <span id="polit"></span>
    
            latitude : <span id="crime"></span>

        </p>
    </body>

</template>

<script>
    


    const xlabels=[];
    const xvalues=[];

    async function chart () {
    const url='https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/Radar/""+.json'
        getdata()
        async function getdata(){
            const response =await fetch (url)
            const datos= await response.json()
            for (let key in datos){
                xlabels.push(key)
                xvalues.push(datos[key])
            }
            /*const { polit, crime }=datos*/
            console.log(xvalues)
            document.getElementById("polit").textContent= xvalues;
            /*document.getElementById("crime").textContent= "world";*/
            
        }
    }
</script>