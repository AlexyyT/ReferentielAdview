import streamlit as st
from utils.func import *

def intro():
    import streamlit as st

    st.sidebar.success("Sélectionner une page ci-dessous.")

    st.markdown(
        """
        # Plateforme de gestion des données clients.
        
        ### Référentiel Adview
        
        Via cette plateforme vous pouvez réalisez plusieurs opérations.
        
        - Consulter les données clients disponibles dans le référentiel Adview (en construction).
        - Ajouter un nouveau client au référentiel Adview (en construction).
        - Lancer la collecter des données historique UA (en construction).
        
        ### Quel est le but du référentiel Adview ?
        
        Le référentiel Adview contient tous les identifiants clients et les données nécessaire à la réalisation des flux de récupération de données.
        Par exemple :
        - Numéro client Créatio.
        - Numéro de propriété GA4.
        - Numéro de compte Google Ads.
        - Liste de mots-clés Ranks.
        - ... 

    """
    )


def CreerClient():
    import streamlit as st
    st.markdown("""
    # Ajouter un client

    Cette page vous permet d'ajouter les données d'un client dans le référentiel Adview.
    """)

def ModifierClient():
    import streamlit as st

    clients = SQLquery("SELECT * EXCLUDE (INDICATOR) FROM PROD_DB.TRANSVERSAL_SCH.REFERENTIEL_CLIENT ORDER BY REF_CLIENT_ID")

    client_name = st.sidebar.selectbox('Choisir un client', clients["NAME"], index=None)

    if client_name == None:
        st.markdown(
            """
            # Gestion des données de référentiel client dans Adview

            Veuillez choisir un client pour consulter ses données.
            """)
    else:
        st.markdown("# Gestion des données de référentiel client dans Adview")
        st.write("Données pour le client : " + client_name)

        if st.button("Modifier les données"):

            st.write("Vous pouvez modifier les données clients ci-dessous")

            st.text_input('REF_CLIENT_ID',
                          value = clients.loc[clients["NAME"] == client_name, "REF_CLIENT_ID"].to_string(index=False), disabled=True)
            st.text_input('NAME',
                          value=clients.loc[clients["NAME"] == client_name, "NAME"].to_string(index=False), disabled=True)
            st.text_input('GOOGLE_ANALYTICS',
                          value=clients.loc[clients["NAME"] == client_name, "GOOGLE_ANALYTICS"].to_string(index=False), disabled=False)
            st.text_input('GOOGLE_SEARCH_CONSOLE',
                          value=clients.loc[clients["NAME"] == client_name, "GOOGLE_SEARCH_CONSOLE"].to_string(index=False), disabled=False)
            st.text_input('GOOGLE_ADS',
                          value=clients.loc[clients["NAME"] == client_name, "GOOGLE_ADS"].to_string(index=False), disabled=False)
            st.text_input('DOMAINE',
                          value=clients.loc[clients["NAME"] == client_name, "DOMAINE"].to_string(index=False), disabled=False)

            validation_modifs_client = st.button("Cliquer ici pour valider les modifications")
        else :
            st.write("Vous pouvez modifier les données clients ci-dessous")

            st.text_input('REF_CLIENT_ID',
                          value = clients.loc[clients["NAME"] == client_name, "REF_CLIENT_ID"].to_string(index=False), disabled=True)
            st.text_input('NAME',
                          value=clients.loc[clients["NAME"] == client_name, "NAME"].to_string(index=False), disabled=True)
            st.text_input('GOOGLE_ANALYTICS',
                          value=clients.loc[clients["NAME"] == client_name, "GOOGLE_ANALYTICS"].to_string(index=False), disabled=True)
            st.text_input('GOOGLE_SEARCH_CONSOLE',
                          value=clients.loc[clients["NAME"] == client_name, "GOOGLE_SEARCH_CONSOLE"].to_string(index=False), disabled=True)
            st.text_input('GOOGLE_ADS',
                          value=clients.loc[clients["NAME"] == client_name, "GOOGLE_ADS"].to_string(index=False), disabled=True)
            st.text_input('DOMAINE',
                          value=clients.loc[clients["NAME"] == client_name, "DOMAINE"].to_string(index=False), disabled=True)

def ModifierPosition():
    import streamlit as st
    st.markdown("""
    # Modifier un positionnement
    
    Cette page vous permet de modifier une position Ranks en cas de mauvais calcul des données.""")

def HistorisationUA():
    import streamlit as st

    st.markdown("""
    # Récupérer l'historique des données UA
    
    """)

    client = st.selectbox('Choisissez une client',['1','2'])

    st.text_input('Nom', value = client,disabled=True)
    st.text_input('ID', disabled=True)
    st.text_input('ID du compte UA',  disabled=True)
    st.text_input('Nom du compte UA', disabled=True)
    st.text_input('ID de la propriété UA', disabled=True)
    st.text_input('Nom de la propriété UA', disabled=True)
    st.text_input('ID de la vue UA', disabled=True)
    st.text_input('Nom de la vue UA', disabled=True)
    st.date_input('Date de début de collecte', disabled=True)
    st.date_input('Date de fin de la collecte', value="2023/07/31", disabled=True)


page_names_to_funcs = {
    "Accueil": intro,
    "Ajouter un client": CreerClient,
    "Modifier un client": ModifierClient,
    "Modifier un positionnement": ModifierPosition,
    "Historisation UA": HistorisationUA
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()