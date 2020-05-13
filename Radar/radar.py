import pandas as pd
import numpy as np
import json
dataf = pd.read_csv("PYTHON/news_latam.csv", sep=",")
# DATOS COMPLETOS POR ENCABEZADO

country = dataf.country
types = dataf.cnn_prediction
dates = dataf.time

# AÑOS, TIPOS Y PAISES SIN REPETIR
tipos = types.unique()  # types de noticias sin repetir
paises = country.unique()  # paises sin repetir
fecha = dates.unique()


yearsAll=np.array(([i.split('-')[0]  for i in dates]))
years= np.unique(yearsAll)

for year in list(years):
    myJSON={}
    for pais in paises:
        topicos=[]
        for tipo in tipos:
            condicion=(((yearsAll==year)&(np.array(country)==pais))&(np.array(types)==tipo))
            topicos.append(int(condicion.sum()))
        porcentajes= np.array(topicos)/sum(topicos)*100
        topicos=list(np.around(porcentajes,decimals= 3))
        myJSON[pais]=topicos
    with open('Radar/'+str(year)+'.json', 'w') as f:
        try:
            json.dump(myJSON, f)
        except UnicodeEncodeError:
                pass
