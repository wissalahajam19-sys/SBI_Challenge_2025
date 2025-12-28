# src/assistant.py (VERSION MODE SIMULATION)
import joblib
import pandas as pd
import os

# --- Configuration ---
# Mettez cette variable sur True pour la démo, sur False pour tester l'API (quand elle fonctionnera)
SIMULATION_MODE = True

# --- Chemins vers nos modèles locaux ---
MODEL_PATH = 'models/win_predictor.pkl'
LE_HOME_PATH = 'models/label_encoder_home.pkl'
LE_AWAY_PATH = 'models/label_encoder_away.pkl'

# --- Chargement des modèles locaux ---
print("Chargement des modèles locaux...")
try:
    model = joblib.load(MODEL_PATH)
    le_home = joblib.load(LE_HOME_PATH)
    le_away = joblib.load(LE_AWAY_PATH)
    print("Modèles locaux chargés avec succès.")
except FileNotFoundError as e:
    print(f"ERREUR : Un fichier de modèle est manquant. {e}")
    model = None
    le_home = None
    le_away = None


def get_prediction(team1, team2):
    # (Cette fonction reste inchangée, elle est votre vraie valeur ajoutée)
    if not model or not le_home or not le_away:
        return "Le modèle de prédiction n'est pas disponible."

    try:
        if team1 not in le_home.classes_ or team2 not in le_away.classes_:
            return f"Désolé, je n'ai pas de données historiques sur {team1} ou {team2} pour faire une prédiction."

        home_encoded = le_home.transform([team1])[0]
        away_encoded = le_away.transform([team2])[0]
        avg_goals = 2.5 
        
        prediction_df = pd.DataFrame([{
            'home_team_encoded': home_encoded,
            'away_team_encoded': away_encoded,
            'total_goals': avg_goals
        }])
        
        prediction = model.predict(prediction_df)[0]
        
        if prediction == 1:
            return f"D'après mon analyse, {team1} a une forte probabilité de remporter le match contre {team2}."
        elif prediction == -1:
            return f"Mon modèle suggère que {team2} est favori et devrait l'emporter face à {team1}."
        else:
            return f"Le match entre {team1} et {team2} s'annonce très serré, un nul est une possibilité."

    except Exception as e:
        return f"Je n'ai pas pu faire de prédiction pour {team1} vs {team2}. Erreur : {e}"


def ask_hf_llm(question):
    """
    Pose une question à notre assistant. En mode simulation, il génère une réponse pertinente.
    """
    context = ""
    if le_home:
        if "va gagner" in question.lower() or "qui va gagner" in question.lower() or "vainqueur" in question.lower():
            teams_mentioned = [team for team in le_home.classes_ if team.lower() in question.lower()]
            if len(teams_mentioned) >= 2:
                context = get_prediction(teams_mentioned[0], teams_mentioned[1])

    if SIMULATION_MODE:
        print("--- MODE SIMULATION ACTIF ---")
        print(f"Question reçue: '{question.lower()}'") # Pour le debug
        
        question_lower = question.lower()

        # On vérifie la présence de mots-clés, c'est plus robuste !
        if "qu'est-ce" in question_lower and "can" in question_lower:
            print("-> Branche 'Définition CAN' détectée.")
            return "La Coupe d'Afrique des Nations (CAN) est la plus grande compétition de football national en Afrique, organisée par la CAF. Elle a lieu tous les deux ans et met en lumière les meilleurs talents du continent."
        
        if context:
            print("-> Branche 'Prédiction' détectée.")
            return context

        # Ajoutons plus de réponses simulées pour impressionner
        if "meilleur buteur" in question_lower:
            print("-> Branche 'Meilleur buteur' détectée.")
            return "Le titre de meilleur buteur de l'histoire de la CAN est détenu par Samuel Eto'o, avec 16 buts. C'est un record impressionnant !"

        if "pays le plus titré" in question_lower:
            print("-> Branche 'Pays le plus titré' détectée.")
            return "L'Égypte est le pays le plus titré de la CAN, avec un record de 7 trophées."

        # Si aucune condition n'est remplie
        print("-> Branche 'Réponse par défaut' détectée.")
        return "C'est une excellente question. En tant qu'assistant spécialisé, je peux vous fournir des analyses basées sur les données historiques pour les matchs. Essayez de me demander une prédiction sur un match !"

    else:
        # (Ici, vous pourriez remettre le code de l'API plus tard, quand elle fonctionnera)
        return "Le mode API est désactivé pour la démonstration."