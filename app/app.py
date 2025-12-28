# app/app.py
import streamlit as st
import sys
import os

# --- Configuration de l'App ---
st.set_page_config(
    page_title="AFRICAN-IA",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Importer la logique de l'assistant ---
# On ajoute le dossier 'src' au chemin pour que Python puisse trouver notre module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.assistant import ask_hf_llm

# --- Titre et Description ---
st.title("🏆 AFRICAN-IA")
st.markdown("*Votre assistant prédictif intelligent pour la CAN 2025*")
st.markdown("---")

st.sidebar.info("💡 **Comment ça marche ?**")
st.sidebar.markdown("""
Cette application est propulsée par :
- Un **modèle de prédiction** entraîné sur les données historiques de la CAN.
- Un **Grand Modèle de Langage (LLM)** open-source de Hugging Face pour générer des réponses naturelles.
""")

# --- Zone d'Interaction Principale ---
st.header("Posez votre question à l'assistant")

user_input = st.text_input(
    "Exemple : Qui va gagner du Maroc contre le Sénégal ?",
    placeholder="Tapez votre question ici..."
)

if st.button("🚀 Demander à AFRICAN-IA", type="primary"):
    if user_input:
        with st.spinner("L'assistant réfléchit... (cela peut prendre 15-20 secondes)"):
            response = ask_hf_llm(user_input)
        
        st.success("Réponse de l'assistant :")
        st.write(response)

    else:
        st.warning("Veuillez entrer une question avant de cliquer sur le bouton.")

# --- Pied de page ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey;'>"
    "Projet réalisé pour le SBI Student Challenge 2025 | "
    "<a href='https://github.com/wissalahajam19-sys/SBI_Challenge_2025' target='_blank'>Voir le code source</a>"
    "</div>",
    unsafe_allow_html=True
)