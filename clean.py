import pandas as pd

# Nettoyer et préparer les données avec Pandas
# Charger le fichier "vgsales.csv" dans un DataFrame

vgsales = pd.read_csv("data/vgsales.csv")

# # Charger le fichier "GlobalLandTemperaturesByMajorCity.csv" dans un DataFrame
# print( " size before ", len(vgsales))
# # Supprimer les lignes en double du DataFrame
# vgsales.drop_duplicates(inplace=True)
# print( "size after ", len(vgsales))

vgsales['Publisher'].fillna('Unknown', inplace=True)

missing_values = vgsales.isnull().sum()

print(missing_values)

vgsales.to_csv('data/vgsales.csv', index=False)

