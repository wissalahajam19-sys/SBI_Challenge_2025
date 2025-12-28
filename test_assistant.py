# test_assistant.py
from src.assistant import ask_hf_llm

# Test 1 : Question simple
print("--- Test 1 : Question simple ---")
question1 = "Qu'est-ce que la CAN 2025 ?"
reponse1 = ask_hf_llm(question1)
print(f"Question: {question1}\nRéponse: {reponse1}\n")

# Test 2 : Question de prédiction (remplacez par des équipes de la CAN)
print("--- Test 2 : Question de prédiction ---")
# Assurez-vous que 'Maroc' et 'Sénégal' sont dans vos données d'entraînement
question2 = "Qui va gagner du Maroc contre le Sénégal ?"
reponse2 = ask_hf_llm(question2)
print(f"Question: {question2}\nRéponse: {reponse2}\n")

# Test 3 : Une autre question de prédiction
print("--- Test 3 : Autre prédiction ---")
question3 = "Quel est le vainqueur probable entre l'Égypte et le Cameroun ?"
reponse3 = ask_hf_llm(question3)
print(f"Question: {question3}\nRéponse: {reponse3}\n")

print("Tests terminés.")