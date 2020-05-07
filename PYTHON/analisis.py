import pandas as pd
import numpy as np
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/User/Desktop/proyecto/PYTHON/news_latam.csv", sep=",")
titulos=df.cnn_prediction.unique()

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
ecuadorTotal= np.sum(transpuesta[:, 0:9],axis=0)
ecuadorPositivo =((transpuesta[:, 0:9][0])*100/ecuadorTotal)
ecuadorNeutro = (transpuesta[:, 0:9][1])*100
ecuadorNegativo =(transpuesta[:, 0:9][2])*100

print(ecuadorPositivo)

mexicoPositivo = transpuesta[:, 9:18][0]
mexicoNeutro = transpuesta[:, 9:18][1]
mexicoPositivo = transpuesta[:, 9:18][2]

venezuelaPositivo = transpuesta[:, 18:][0]
venezuelaNeutro = transpuesta[:, 18:][1]
venezuelaPositivo = transpuesta[:, 18:][2]
N = 9

ind = np.arange(N)    # the x locations for the groups
width = 0.30       # the width of the bars: can also be len(x) sequence

positivo = plt.bar(ind, ecuadorPositivo, width)
neutro = plt.bar(ind, ecuadorNeutro, width, bottom=ecuadorPositivo)
negativo = plt.bar(ind, ecuadorNegativo, width,bottom= ecuadorNeutro+ecuadorPositivo)

plt.ylabel('Scores')
plt.title('Scores by feelings')
plt.xticks(ind, tuple([tipo for tipo in titulos]))
plt.yticks(np.arange(0, 1000, step=100))
plt.legend((positivo[0], neutro[0],negativo[0]), ('Positivo', 'Neutro','Negativo'))

plt.show()
