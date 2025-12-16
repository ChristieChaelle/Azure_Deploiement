# Import nécessaire
import streamlit as st
import requests
from streamlit.components.v1 import html
import pandas as pd
import json
import os
import pymongo
from dotenv import load_dotenv
import time
from datetime import datetime

# Charger les variables d'environnement
load_dotenv()

# Configuration de la page
st.set_page_config(
    page_title="Prédiction de défaut client | Risk Banking",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Insertion du CSS
st.markdown("""
<style>
/* =========================
   VARIABLES CSS (THÈME)
   ========================= */
:root {
    --primary-blue: #1f4fd8;
    --secondary-green: #2ecc71;
    --background-light: #f5f7fb;
    --card-bg: #ffffff;
    --text-dark: #1f2937;
    --text-muted: #6b7280;
    --border-radius: 12px;
}

/* =========================
   BASE
   ========================= */
html, body, [class*="css"] {
    font-family: "Inter", sans-serif;
    background-color: var(--background-light);
    color: var(--text-dark);
}

/* =========================
   CARTES (KPIs / BLOCS)
   ========================= */
.card {
    background: var(--card-bg);
    border-radius: var(--border-radius);
    padding: 20px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.06);
    transition: transform 0.2s ease;
}

.card:hover {
    transform: translateY(-4px);
}

/* =========================
   INDICATEURS
   ========================= */
.metric-value {
    font-size: 32px;
    font-weight: 700;
    color: var(--primary-blue);
}

.metric-label {
    font-size: 14px;
    color: var(--text-muted);
}

/* =========================
   BOUTONS
   ========================= */
.stButton > button {
    background-color: var(--primary-blue);
    color: white;
    border-radius: 8px;
    padding: 10px 18px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #183bb5;
}

/* =========================
   AVATAR CLIENT
   ========================= */
.avatar {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background-color: var(--secondary-green);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 700;
    font-size: 24px;
}

/* =========================
   RESPONSIVE
   ========================= */
@media (max-width: 768px) {
    .card {
        padding: 15px;
    }

    .metric-value {
        font-size: 26px;
    }
}
</style>
""", unsafe_allow_html=True)

# Création de la barre latérale
with st.sidebar:
    # LOGO
    st.markdown("""
        <div style="
            font-size: 32px;
            font-weight: 800;
            text-align: center;
            color: #1f4fd8;
            margin-bottom: 30px;
        ">
            RB
            <div style="font-size: 14px; color: #6b7280;">Risk Banking</div>
        </div>
    """, unsafe_allow_html=True)

    # Saisie ID client
    client_id = st.text_input(
        "ID Client",
        placeholder="Ex : 100123"
    )

    # Bouton analyse
    analyze_clicked = st.button("🔍 Analyser le risque", use_container_width=True)

    st.markdown("---")

    # ❓ PANNEAU D'AIDE RÉTRACTABLE
    with st.expander("❓Aide & instructions"):
        st.markdown("""
        **Comment utiliser l'application :**
        - Entrez l’**ID client** dans le champ prévu
        - Cliquez sur **Analyser le risque**
        - Consultez les indicateurs et graphiques générés
        - Utilisez les filtres pour affiner l’analyse
        """)

# Exemple de logique associée
if analyze_clicked and client_id:
    st.success(f"Analyse du risque en cours pour le client {client_id}")
elif analyze_clicked and not client_id:
    st.warning("Veuillez saisir un ID client avant de lancer l’analyse.")
