import streamlit as st
from utils.func import *

#Titre
st.title("Modifier les données d'un client")

#Chargement des données
REFERENTIEL_CLIENT = SQLquery("SELECT * EXCLUDE (INDICATOR) FROM PROD_DB.TRANSVERSAL_SCH.REFERENTIEL_CLIENT ORDER BY NAME")
REFERENTIEL_MOTS_CLES = SQLquery("SELECT * FROM PROD_DB.TRANSVERSAL_SCH.REFERENTIEL_MOTS_CLES ORDER BY REF_CLIENT_ID, PRIORITY")

#Définition des session_state
if "nom_client" not in st.session_state:
    st.session_state.nom_client = ''
if "ref_client_id" not in st.session_state:
    st.session_state.ref_client_id = ''

# Page Streamlit
st.markdown(
    """
    Veuillez choisir un client pour modifier ses données.
    """)

st.session_state.nom_client = st.selectbox('Choisir un client', REFERENTIEL_CLIENT["NAME"], index=None)
st.session_state.ref_client_id = REFERENTIEL_CLIENT.loc[REFERENTIEL_CLIENT["NAME"] == st.session_state.nom_client, "REF_CLIENT_ID"].to_string(index=False)
REFERENTIEL_MOTS_CLES = REFERENTIEL_MOTS_CLES[REFERENTIEL_MOTS_CLES["REF_CLIENT_ID"] == st.session_state.ref_client_id]

if st.session_state.nom_client:

    st.markdown(""" #### Profils Client
    Données d'identification du client sur les outils métiers""")

    st.text_input('REF_CLIENT_ID',
                  value = REFERENTIEL_CLIENT.loc[REFERENTIEL_CLIENT["NAME"] == st.session_state.nom_client, "REF_CLIENT_ID"].to_string(index=False), disabled=True)
    st.text_input('GOOGLE_ANALYTICS',
                  value=REFERENTIEL_CLIENT.loc[REFERENTIEL_CLIENT["NAME"] == st.session_state.nom_client, "GOOGLE_ANALYTICS"].to_string(index=False), disabled=False)
    st.text_input('GOOGLE_SEARCH_CONSOLE',
                  value=REFERENTIEL_CLIENT.loc[REFERENTIEL_CLIENT["NAME"] == st.session_state.nom_client, "GOOGLE_SEARCH_CONSOLE"].to_string(index=False), disabled=False)
    st.text_input('GOOGLE_ADS',
                  value=REFERENTIEL_CLIENT.loc[REFERENTIEL_CLIENT["NAME"] == st.session_state.nom_client, "GOOGLE_ADS"].to_string(index=False), disabled=False)
    st.text_input('DOMAINE',
                  value=REFERENTIEL_CLIENT.loc[REFERENTIEL_CLIENT["NAME"] == st.session_state.nom_client, "DOMAINE"].to_string(index=False), disabled=False)
    st.text_input('LANGUAGE',
                  value=REFERENTIEL_CLIENT.loc[REFERENTIEL_CLIENT["NAME"] == st.session_state.nom_client, "LANGUAGE"].to_string(index=False), disabled=False)

    st.divider()

    st.markdown(""" #### Liste de mots clés
    Mots clés pour lesquels""")
    st.data_editor(REFERENTIEL_MOTS_CLES[["PRIORITY","BU","THEME","KEYWORD","SEARCH_VOLUME"]], hide_index=True)



