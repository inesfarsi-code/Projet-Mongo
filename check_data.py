import pandas as pd

CSV_PATH = "data/healthcare_dataset.csv"

df = pd.read_csv(CSV_PATH)

print("Fichier chargé avec succès")
print("Nombre de lignes :", df.shape[0])
print("Nombre de colonnes :", df.shape[1])

print("\n Colonnes :")
print(df.columns.tolist())

print("\n Valeurs manquantes par colonne :")
print(df.isnull().sum())

print("\n Nombre de lignes dupliquées :", df.duplicated().sum())
