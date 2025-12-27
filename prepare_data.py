# prepare_data.py
import pandas as pd

# Charger les données brutes
try:
    df = pd.read_csv('data/raw_data.csv')
    print("Fichier brut chargé avec succès.")
    print("Nombre de lignes avant nettoyage :", len(df))
except FileNotFoundError:
    print("ERREUR : Assurez-vous que le fichier 'data/raw_data.csv' existe.")
    exit()

# --- Nettoyage et Préparation ---

# 1. Garder seulement les matchs de la CAN
# La colonne 'tournament' contient le nom de la compétition
can_df = df[df['tournament'].str.contains("African Cup of Nations", na=False)].copy()

# 2. Convertir la colonne 'date' en format datetime
can_df['date'] = pd.to_datetime(can_df['date'])

# 3. Créer des features (colonnes) utiles pour notre modèle
can_df['total_goals'] = can_df['home_score'] + can_df['away_score']
can_df['goal_difference'] = can_df['home_score'] - can_df['away_score']

# 4. Créer la colonne 'result' (notre cible pour la prédiction)
# 1 = Victoire à domicile, 0 = Nul, -1 = Défaite à domicile
def get_result(row):
    if row['home_score'] > row['away_score']:
        return 1
    elif row['home_score'] < row['away_score']:
        return -1 # -1 est plus facile à gérer que 2 pour certains modèles
    else:
        return 0

can_df['result'] = can_df.apply(get_result, axis=1)

# 5. Supprimer les colonnes dont on n'a pas besoin
columns_to_drop = ['city', 'country', 'neutral']
can_df = can_df.drop(columns=columns_to_drop)

# Sauvegarder le fichier nettoyé
can_df.to_csv('data/cleaned_data.csv', index=False)

print("\nNettoyage terminé.")
print("Nombre de lignes après nettoyage (uniquement les matchs de la CAN) :", len(can_df))
print("\nAperçu des données nettoyées :")
print(can_df.head())
print("\nLe fichier 'data/cleaned_data.csv' a été créé avec succès.")