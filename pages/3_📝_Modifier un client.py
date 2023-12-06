import streamlit as st
from utils.func import *

st.title("Modifier les données d'un client")

st.markdown(
    """
    Veuillez choisir un client pour consulter ses données.
    """)

st.session_state.client_nom = st.selectbox('Choisir un client', st.session_state.referentiel_client["NAME"], index=None)

st.session_state.client_ref_id = st.session_state.referentiel_client.loc[st.session_state.referentiel_client["NAME"] == st.session_state.nom_client, "REF_CLIENT_ID"].to_string(index=False)



if st.session_state.client_nom:
    st.write("Vous pouvez modifier les données clients ci-dessous")

    st.text_input('REF_CLIENT_ID',
                  value = st.session_state.referentiel_client.loc[st.session_state.referentiel_client["NAME"] == st.session_state.client_nom, "REF_CLIENT_ID"].to_string(index=False), disabled=True)
    st.text_input('NAME',
                  value=st.session_state.referentiel_client.loc[st.session_state.referentiel_client["NAME"] == st.session_state.client_nom, "NAME"].to_string(index=False), disabled=True)
    st.text_input('GOOGLE_ANALYTICS',
                  value=st.session_state.referentiel_client.loc[st.session_state.referentiel_client["NAME"] == st.session_state.client_nom, "GOOGLE_ANALYTICS"].to_string(index=False), disabled=False)
    st.text_input('GOOGLE_SEARCH_CONSOLE',
                  value=st.session_state.referentiel_client.loc[st.session_state.referentiel_client["NAME"] == st.session_state.client_nom, "GOOGLE_SEARCH_CONSOLE"].to_string(index=False), disabled=False)
    st.text_input('GOOGLE_ADS',
                  value=st.session_state.referentiel_client.loc[st.session_state.referentiel_client["NAME"] == st.session_state.client_nom, "GOOGLE_ADS"].to_string(index=False), disabled=False)
    st.text_input('DOMAINE',
                  value=st.session_state.referentiel_client.loc[st.session_state.referentiel_client["NAME"] == st.session_state.client_nom, "DOMAINE"].to_string(index=False), disabled=False)
    st.text_input('LANGUAGE',
                  value=st.session_state.referentiel_client.loc[st.session_state.referentiel_client["NAME"] == st.session_state.client_nom, "LANGUAGE"].to_string(index=False), disabled=False)

    st.divider()

    st.markdown(""" #### Liste de mots clés
    Mots clés pour lesquels""")
    st.data_editor(st.session_state.referentiel_mots_cles[st.session_state.referentiel_mots_cles["REF_CLIENT_ID"] == st.session_state.client_ref_id], hide_index=True)
