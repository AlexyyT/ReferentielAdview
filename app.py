import streamlit as st
from st_pages import Page, show_pages, add_page_title
from utils.func import initializeSessionStates

initializeSessionStates()

add_page_title()

show_pages(
    [
        Page("app.py", "Accueil", "🏠"),
        Page("pages/2_📑_Ajouter un client.py", "Ajouter un client", "📑"),
        Page("pages/3_📝_Modifier un client.py", "Modifier un client", "📝"),
        Page("pages/4_📈_Modifier un positionnement.py", "Modifier un positionnement", "📈"),
        Page("pages/5_💾_Historiser des données UA.py", "Historiser des données UA", "💾"),
        Page("pages/6_🔗_Suivi netliking.py", "Suivi netliking", "🔗"),
        Page("pages/7_💬_FAQ.py", "FAQ", "💬"),
        Page("pages/8_♦_Test.py", "Test", "♦"),
    ])


st.markdown(
    """
    # Gestion du Référentiel Adview
    
    ### Bienvenue sur la plateforme de gestion du Référentiel Adview.
    
    Ici, vous pouvez manipuler le référentiel sans avoir à passer par des requêtes SQL.
    
    Vous retrouverez plusieurs pages vous permettant d'effectuer différentes opérations.
    - Ajouter un client : Vous permettra d'ajouter un nouveau client et de lancer la collecte de données.
    - Modifier un client : Vous permettra de modifier le profil d'un client.
    - Modifier un positionnement : Vous permettra de modifier une position Ranks factice.
    - Suivi Netlinking : Vous permettra d'ajouter ou de modifier les urls suivies.
    - Historiser des données UA : Vous permettra de déclancher un flux d'historisation pour une vue GA3.
    - FAQ : Vous permettra de mieux comprendre les enjeux autour du Référentiel Adview.
    
    📌 Veillez à bien vérifier l'exactitude des données renseignées ici.
    Des données erronées peuvent entraîner une mauvaise collecte et ête la cause de problème dans les rapports Looker Studio.
    """
)