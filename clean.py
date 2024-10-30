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


def checkColumn(df, columnName, type):

    incorrectValues = df[~df[columnName].apply(lambda x: isinstance(x, type) or pd.isnull(x))]

    if incorrectValues.empty:
        return "Les valeurs sont du bon type"
    else:
        return "Les valeurs ne sont PAS du bon type"

print(vgsales['Year'].head().tolist())
print(checkColumn(vgsales, "Year", int))
print(vgsales["Year"].dtypes)

# Remplace les années null par des 0
vgsales['Year'].fillna(0, inplace=True)

# Transforme le type des années en int
vgsales['Year'] = vgsales['Year'].astype(int)

# Remplace les années de nombre 0 par des null
vgsales['Year'] = vgsales['Year'].replace(0, None)

print("")
print(vgsales['Year'].head().tolist())
print(checkColumn(vgsales, "Year", int))
print(vgsales["Year"].dtypes)

vgsales.to_csv('data/vgsales.csv', index=False)