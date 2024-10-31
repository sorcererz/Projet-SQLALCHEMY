
import streamlit as st
import pandas as pd
import numpy as np
import models as models
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

############################################################## add Platform in database

platformArray = vgsales['Platform'].unique()
for plateform in platformArray:
    myPlatform = models.Platform(name=plateform)
    session.add(myPlatform)

session.commit()

############################################################## add Publisher in database

publisherArray = vgsales['Publisher'].unique()
for publisher in publisherArray:
    myPublisher = models.Publisher(name=publisher)
    session.add(myPublisher)

session.commit()
