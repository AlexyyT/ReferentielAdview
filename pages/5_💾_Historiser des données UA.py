import streamlit as st
import datetime
from utils.func import *
import boto3

# session_states
session_states = ['ref_client_id','nom_compte_ua','id_compte_ua','nom_propriete_ua',
                'id_propriete_ua','nom_vue_ua','id_vue_ua','start_date','end_date']
for state in range(len(session_states)):
    if state not in st.session_state:
        st.session_state[state] = ''


st.markdown("""
# Historiser des données UA

Cette page vous permet de lancer l'histotisation des données UA pour un client.

🚩 Attention, veuillez bien vous assurer que la prestation commerciale a été vendue avant de lancer une historisation de données.

""")

with st.form('MyForm'):
    st.markdown("""### Renseignez les informations de la vue UA à historiser""")
    st.session_state.ref_client_id = st.text_input('REF_CLIENT_ID')
    st.session_state.nom_compte_ua = st.text_input('Nom du compte Universal Analytics')
    st.session_state.id_compte_ua = st.text_input('Numéro du compte Universal Analytics')
    st.session_state.nom_propriete_ua = st.text_input('Nom de la propriété Universal Analytics')
    st.session_state.id_propriete_ua = st.text_input('Identifiant de la propriété Universal Analytics')
    st.session_state.nom_vue_ua = st.text_input('Nom de la vue Universal Analytics')
    st.session_state.id_vue_ua = st.text_input('Numéro de la vue Universal Analytics')
    st.session_state.start_date = st.date_input('Date de début de collecte', value=datetime.date(2006,1,1))
    st.session_state.end_date = st.date_input('Date de fin de collecte',value=datetime.date(2023,7,31))

    submitted = st.form_submit_button('Valider')
    if submitted:
        if not st.session_state.ref_client_id or not st.session_state.nom_compte_ua or not st.session_state.id_compte_ua or not st.session_state.nom_propriete_ua or not st.session_state.id_propriete_ua_propriete_ua or not st.session_state.nom_vue_ua or not st.session_state.id_vue_ua or not st.session_state.start_date or not st.session_state.end_date:
            st.markdown("Veuillez renseigner tous les champs afin de lancer l'historisation des données Universal Analytics.")

        else:
            check = SQLquery(f"SELECT * FROM TRANSVERSAL_SCH.REFERENTIEL_HISTORISATION_UA WHERE REF_CLIENT_ID = '{st.session_state.ref_client_id}' AND UA_VIEW_ID = '{st.session_state.id_vue_ua}'")

            if check['REF_CLIENT_ID'].count() > 0:
                st.markdown(f"L'historisation des données du client **{st.session_state.ref_client_id}** a déjà été effectuée pour la vue **{st.session_state.id_vue_ua}**.")
                st.markdown(f"Les données ont été collectées pour la période du **{check['START_DATE'].to_string(index=False)}** au **{check['END_DATE'].to_string(index=False)}**.")
                st.write(datetime.date.today())
            else:
                SQLquery(f"INSERT INTO TRANSVERSAL_SCH.REFERENTIEL_HISTORISATION_UA VALUES ('{st.session_state.ref_client_id}', '{st.session_state.nom_compte_ua}', '{st.session_state.id_compte_ua}', '{st.session_state.nom_propriete_ua}', '{st.session_state.id_propriete_ua}', '{st.session_state.nom_vue_ua}', '{st.session_state.id_vue_ua}', '{st.session_state.start_date}', '{st.session_state.end_date}', '{datetime.date.today()}')")
                st.markdown(f"Le profil du client **{st.session_state.ref_client_id}**, pour la vue **{st.session_state.id_vue_ua}** a été ajoutée à la base de données.")
                st.markdown(f"L'historisation des données est en cours, pour la période du  **{st.session_state.start_date}** au **{st.session_state.end_date}** .")
                st.markdown(f"Cette étape peut prendre jusqu'à une heure d'exécution.")


                HistorisationSQS(st.session_state.ref_client_id,st.session_state.id_vue_ua,st.session_state.start_date,st.session_state.end_date)