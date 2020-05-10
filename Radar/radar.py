import pandas as pd
import numpy as np
import json
dataf=pd.read_csv( "/Users/User/Desktop/Python/new.csv",sep=",")
ide=dataf.id_news;country=dataf.country ;tipos=dataf.cnn_prediction;dates=dataf.time;titles=dataf.title_trans;news=dataf.news
tipos_uni=tipos.unique() #tipos de noticias sin repetir
country_uni=country.unique()#paises sin repetir
#Extraccion de los años 
fechas=np.zeros((len(dates),), dtype=int)
for ind,fecha in enumerate(dates):
        año=fecha.split("-")[0]
        fechas[ind]=int(año)
dataf["fechas"]=fechas
#Años sin repetir#
fechasunicas=dataf.fechas.unique()
c=0
for paises in country_uni:
    d={}
    for tipos in tipos_uni:
        if tipos not in d:
            d[tipos]=0
        condicion= ((dataf.cnn_prediction==tipos) & (dataf.country==paises))
        cant=dataf.cnn_prediction[condicion].size
        d[tipos]+=cant
        c+=cant
        with open(paises+'.json','w') as f:
                json.dump(d,f)
print(c)

### Graficos de Serie de Tiempo ###
"""for topics in tipos_uni:
        d={}
        if topics not in d:
                d[topics]={}
        for paises in country_uni:
                if paises not in d[topics]:
                        d[topics][paises]=[]
                for años in fechasunicas:
                        condi=(fechas==años) & (country==paises) & (tipos==topics)
                        canti=fechas[condi].size     
                        d[topics][paises].append(canti)
        with open(topics+'.json','w') as f:
                json.dump(d,f)
print(d)"""

