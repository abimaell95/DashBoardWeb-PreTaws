import pandas as pd
import numpy as np
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt
import json

df = pd.read_csv("/Users/User/Desktop/prueba/new.csv", sep=",")
titulos=df.cnn_prediction.unique()
paises=df.country.unique()

df['polaridad'] = df['title_trans'].apply(
    lambda x: TextBlob(x).sentiment.polarity)

df['subj'] = df['title_trans'].apply(
    lambda x: TextBlob(x).sentiment.subjectivity)
array = np.array(["positivo", "neutro", "negativo"])
d = {}
m = []
for elem in df.country.unique():
    # if elem not in d:
    #     d[elem] = {}
    # d[elem]["Positivo"]=[]
    # d[elem]["Neutro"] =[]
    # d[elem]["Negativo"] =[]
    a=0;b=0;c=0
    for tipos in df.cnn_prediction.unique():
        negativo = df.polaridad[(df.polaridad < 0) & (df.country == elem) & (df.cnn_prediction == tipos)].size
        positivo = df.polaridad[(df.polaridad > 0) & (df.country == elem) & (df.cnn_prediction == tipos)].size
        neutro = df.polaridad[(df.polaridad == 0) & (df.country == elem) & (df.cnn_prediction == tipos)].size
        # d[elem]["Positivo"].append(positivo)
        # d[elem]["Neutro"].append(neutro)
        # d[elem]["Negativo"].append(negativo)
        a = [positivo, neutro, negativo]
        m.append(a)
print(d)
matriz = np.array(m)
transpuesta = matriz.transpose()
#ARCHIVO JSON
feelings=['Positivo','Neutro','Negativo']
d2={}

N=3 #NUMERO DE PAISES
F=3 #NUMERO DE SENTIMIENTO
for i,elem in enumerate(paises) :
    matrizPais= transpuesta[:,9*(i):9*(i+1)]
    totalPais= np.sum(matrizPais,axis=0)
    for j,senti in enumerate(feelings):
        if senti not in d2:
            d2[senti]=0
        fPaisP= (matrizPais[j]*100)/totalPais
        d2[senti]=list(np.around(fPaisP,decimals= 3))
        with open(elem+'.json','w') as f:
            json.dump(d2,f)