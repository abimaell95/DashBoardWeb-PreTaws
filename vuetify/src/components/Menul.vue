<template>
    <div>
        <p>
           Ecuador: <span id="ec"></span> <br> <br>
           Mexico : <span id="mex"></span> <br> <br>
           Venezuela : <span id="ve"></span>
    

        </p>

</div>
</template>

<script>
    
    const xlabels=[]
    const xvaluesEc=[];
    const xvaluesMe=[];
    const xvaluesVe=[];
    const url='https://raw.githubusercontent.com/abimaell95/DashBoardWeb-PreTaws/master/Radar/2015.json'
        getdata()
        async function getdata(){
            const response =await fetch (url)
            const datos= await response.json()
            console.log(datos)
            for (let key in datos){
                xlabels.push(key)
                if (key==="Ecuador"){
                    xvaluesEc.push(datos[key])
                }
                if (key==="Mexico"){
                    xvaluesMe.push(datos[key])
                }
                if (key==="Venezuela"){
                    xvaluesVe.push(datos[key])
                }
            /*const { polit, crime }=datos*/
            document.getElementById("ec").textContent= xvaluesEc;
            document.getElementById("mex").textContent= xvaluesMe;
            document.getElementById("ve").textContent= xvaluesVe;
            }            
        }
</script>