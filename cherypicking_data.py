
import streamlit as st
import pandas as pd
import numpy as np
import models as models
from models import Genre, Sales, Game, Platform, Publisher, Base
import session as session

st.title('Mon Projet SQL Alchemy - récupération des dinnées pour les transférer dans la bse de données')

# Nettoyer et préparer les données avec Pandas
# Charger le fichier "vgsales.csv" dans un DataFrame

# Création des table dans la base de données
Base.metadata.create_all(session.engine)


vgsales = pd.read_csv("data/vgsales.csv")

st.dataframe(vgsales)

namesArray = vgsales['Name'].unique()
# names = names.sort_values(by=['Name'])
names_nparray = np.array(namesArray)

df_names = pd.DataFrame(names_nparray, columns=['Name']).sort_values(by=['Name'])
# df = namesDF
st.text('Games names')
print(df_names)

st.dataframe(df_names)

genreArray = vgsales['Genre'].unique()

genre_array = np.array(genreArray)
df_genre = pd.DataFrame(genre_array,columns=['Genre']).sort_values(by=['Genre'])

st.text('Games genres')
st.dataframe(df_genre)

print('ici')
for index, row in df_genre.iterrows():
    # print(type(item))
    print(row['Genre'])
    # print(type(row['Genre']))
    myGenre = models.Genre(name=row['Genre'])
    print('ajout')
    # session.add(myGenre)


