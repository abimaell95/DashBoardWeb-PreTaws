import pandas as pd
import numpy as np
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt
import json

df = pd.read_csv("/Users/User/Desktop/proyecto/PYTHON/news_latam.csv", sep=",")
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
    if elem not in d:
        d[elem] = {}
    for tipos in df.cnn_prediction.unique():
        if tipos not in d[elem]:
            d[elem][tipos] = {}
            negativo = df.polaridad[(df.polaridad < 0) & (
                df.country == elem) & (df.cnn_prediction == tipos)].size
            positivo = df.polaridad[(df.polaridad > 0) & (
                df.country == elem) & (df.cnn_prediction == tipos)].size
            neutro = df.polaridad[(df.polaridad == 0) & (
                df.country == elem) & (df.cnn_prediction == tipos)].size
            d[elem][tipos]["positivo"] = positivo
            d[elem][tipos]["neutro"] = neutro
            d[elem][tipos]["negativo"] = negativo
            a = [positivo, neutro, negativo]
            m.append(a)
# print(d)
matriz = np.array(m)
transpuesta = matriz.transpose()
#ARCHIVO JSON
feelings=['positivo','neutro','negativo']
datos={}
datos['topicos']=list(titulos)

N=3 #NUMERO DE PAISES
F=3 #NUMERO DE SENTIMIENTO
for i in range(N):
    matrizPais= transpuesta[:,9*(i):9*(i+1)]
    totalPais= np.sum(matrizPais,axis=0)
    datos['total%s'%(paises[i])]=totalPais
    for j in range(F):
        fPaisP= (matrizPais[j]*100)/totalPais
        datos['%s%s'%(paises[i],feelings[j])]=list(np.around(fPaisP,decimals= 3))
    
# datosJson= json.dumps(datos)
# print(type(datosJson))
print(type(datos))

print(datos)
        


# N = 9

# ind = np.arange(N)    # the x locations for the groups
# width = 0.30       # the width of the bars: can also be len(x) sequence

# positivo = plt.bar(ind, ecuadorPositivo, width)
# neutro = plt.bar(ind, ecuadorNeutro, width, bottom=ecuadorPositivo)
# negativo = plt.bar(ind, ecuadorNegativo, width,bottom= ecuadorNeutro+ecuadorPositivo)

# plt.ylabel('Scores')
# plt.title('Scores by feelings')
# plt.xticks(ind, tuple([tipo for tipo in titulos]))
# plt.yticks(np.arange(0, 100, step=10))
# plt.legend((positivo[0], neutro[0],negativo[0]), ('Positivo', 'Neutro','Negativo'))

# plt.show()
