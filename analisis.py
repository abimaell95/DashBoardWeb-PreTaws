import pandas as pd
import numpy as np
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv( "/Users/User/Desktop/Python/new.csv",sep=",")
df['polaridad']=df['title_trans'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['subj']=df['title_trans'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
df.to_csv(r"C:/Users/User/Desktop/Python/exportados.csv")
#Ecuador=[];Mexico=[];Venezuela=[]
array=np.array(["positivo","neutro","negativo"])
d={};m=[]
for elem in df.country.unique():
    if elem not in d:
        d[elem]={}
    for tipos in df.cnn_prediction.unique():
        if tipos not in d[elem]:
            d[elem][tipos]={}
            negativo=df.polaridad[(df.polaridad<0) & (df.country==elem) &(df.cnn_prediction==tipos)].size
            positivo=df.polaridad[(df.polaridad>0) & (df.country==elem) &(df.cnn_prediction==tipos)].size 
            neutro=df.polaridad[(df.polaridad==0) & (df.country==elem) &(df.cnn_prediction==tipos)].size
            d[elem][tipos]["positivo"]=positivo
            d[elem][tipos]["neutro"]=neutro
            d[elem][tipos]["negativo"]=negativo
            a=[positivo,neutro,negativo]
            m.append(a)
#print(d)
matriz=np.array(m)
transpuesta=matriz.transpose()
ecuador=transpuesta[:,0:9]
mexico=transpuesta[:,9:18]
venezuela=transpuesta[:,18:]
print(ecuador )
print(mexico)