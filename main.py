import streamlit as st
import pandas as pd
import numpy as np

# Titre de l'application
st.title('Mon Projet SQL Alchemy')

# Nettoyer et préparer les données avec Pandas
# Charger le fichier "vgsales.csv" dans un DataFrame

vgsales = pd.read_csv("data/vgsales.csv")

st.dataframe(vgsales)

namesArray = vgsales['Name'].unique()
# names = names.sort_values(by=['Name'])
names_nparray = np.array(namesArray)

df_names = pd.DataFrame(names_nparray, columns=['Name']).sort_values(by=['Name'])
# df = namesDF
print(df_names)

st.dataframe(df_names)