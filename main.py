import streamlit as st
import pandas as pd

# Titre de l'application
st.title('Mon Projet SQL Alchemy')

# Nettoyer et préparer les données avec Pandas
# Charger le fichier "vgsales.csv" dans un DataFrame

vgsales = pd.read_csv("data/vgsales.csv")

st.dataframe(vgsales)



