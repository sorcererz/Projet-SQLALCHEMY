
import streamlit as st
import pandas as pd
import numpy as np
import models as models
import sqlite3
from models import Genre, Sales, Game, Platform, Publisher, Base
# from sqlalchemy.orm import session
from sqlalchemy import create_engine

from sqlalchemy.orm import Session

import os

try: 
    os.remove('./data/vgsales.db')
    print('remove database')
except:
    print('no database sqlite')

engine = create_engine('sqlite:///data/vgsales.db')
session = Session(bind=engine)


st.title('Mon Projet SQL Alchemy - récupération des dinnées pour les transférer dans la bse de données')

# Nettoyer et préparer les données avec Pandas
# Charger le fichier "vgsales.csv" dans un DataFrame

# Création des table dans la base de données
Base.metadata.create_all(engine)


vgsales = pd.read_csv("data/vgsales.csv")

st.dataframe(vgsales)

############################################################## names in streamlit

namesArray = vgsales['Name'].unique()
    
names_nparray = np.array(namesArray)

df_names = pd.DataFrame(names_nparray, columns=['Name']).sort_values(by=['Name'])
st.text('Games names')

st.dataframe(df_names)

############################################################## add Genre in database
genreArray = vgsales['Genre'].unique()
for genre in genreArray:
    myGenre = models.Genre(name=genre)
    session.add(myGenre)
session.commit()

df_genre = pd.read_sql_table('genres','sqlite:///data/vgsales.db')


############################################################## add Platform in database

platformArray = vgsales['Platform'].unique()
for plateform in platformArray:
    myPlatform = models.Platform(name=plateform)
    session.add(myPlatform)

session.commit()

df_platform = pd.read_sql_table('platforms','sqlite:///data/vgsales.db')

############################################################## add Publisher in database

publisherArray = vgsales['Publisher'].unique()
for publisher in publisherArray:
    myPublisher = models.Publisher(name=publisher)
    session.add(myPublisher)

session.commit()

df_publisher = pd.read_sql_table('publishers','sqlite:///data/vgsales.db')


############################################################## add Game in database

# gameArray = vgsales['Name','Genre']
df_game = pd.DataFrame(vgsales, columns=['Name', 'Genre'])

for index_game, row_game in df_game.iterrows():
    for index_genre, row_genre in df_genre.iterrows():
        if row_game['Genre'] == row_genre['name']:
            myGame = models.Game(name=row_game['Name'], genre_id=row_genre['id'])
            session.add(myGame)
session.commit()


