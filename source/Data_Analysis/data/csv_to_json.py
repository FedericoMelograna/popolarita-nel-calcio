import pandas as pd
from unidecode import unidecode
import json

df = pd.read_csv('full_df.csv')
df.nome=df.nome.apply(unidecode)
cols=['nome','eta','ruolo_dettaglio','squadra','Germania', 'Francia',
       'Italia', 'Spagna', 'Inghilterra', 'Internazionale','SOCIAL','MEDIA', 'GOOGLE',
       'WIKIPEDIA','IPOP']

df1 = df[cols]
df1.index=df1.nome
df1=df1.drop('nome',axis=1)
diz = df1.T.to_dict()

with open('data_full.json', 'w') as outfile:
    json.dump(diz, outfile)
