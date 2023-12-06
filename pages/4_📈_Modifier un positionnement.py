import datetime

import streamlit as st
from utils.func import *

st.title("Modifier un positionnement Ranks")

st.write('Via cette page, vous pouvez modifier un positionnement Ranks qui aurait pu être mal calculé.')
st.write('Pour cela, renseignez les filtres ci-dessous.')

clients = SQLquery("SELECT * FROM GOLD_SCH.RANKS_SUIVI_POSITION ORDER BY DATE DESC, NAME, PRIORITY")

client_name = st.selectbox('Choisir un client', clients["NAME"].unique(), index=None)
month = st.selectbox('Choisir un mois', clients.loc[clients["NAME"] == client_name, "DATE"].unique(), index=None)

if client_name and month:

    st.markdown("""### Liste des positions en base de données""")
    filtered_df = clients[(clients['NAME'] == client_name) & (clients['DATE'] == month)]
    st.dataframe(filtered_df[['PRIORITY', 'BU','THEME','KEYWORD','SEARCH_VOLUME','POSITION']], hide_index = True, use_container_width=True)

    st.markdown("""### Modifier une position""")
    st.write("Sélectionner le mot-clé pour lequel vous souhaitez modifier la position.")
    keyword = st.selectbox('Choisir le mot-clé',clients.loc[clients["NAME"] == client_name, "KEYWORD"].unique(), index=None)

    if keyword:
        priority_df = clients[(clients['NAME'] == client_name) & (clients['DATE'] == month) & (clients['KEYWORD'] == keyword)]

        DATE = priority_df["DATE"].values[0]
        REF_CLIENT_ID = priority_df["REF_CLIENT_ID"].values[0]
        KEYWORD = priority_df["KEYWORD"].values[0]
        POSITION_OLD = priority_df["POSITION"].values[0]

        with st.form('ModifierPosition'):
            st.text_input('Mois', DATE, disabled=True)
            st.text_input('Mot-clé', KEYWORD, disabled=True)
            st.text_input('Anciennne Position', POSITION_OLD, disabled=True)
            POSITION_NEW = st.text_input('Nouvelle Position')

            submitted = st.form_submit_button('Valider')

        if submitted:
            if POSITION_NEW :
                # if POSITION_NEW == POSITION_OLD:
                #     st.write('Veuillez renseigner une nouvelle position différente de la position originale.')
                #
                # else:
                #     st.success('Position modifiée')
                #
                #     RanksModificationSQS(REF_CLIENT_ID, DATE, KEYWORD, POSITION_OLD, POSITION_NEW)
                #         # Monitoring
                RanksModificationSQS(REF_CLIENT_ID, DATE, KEYWORD, POSITION_OLD, POSITION_NEW)
            else:
                st.error('Veuillez renseigner la nouvelle position.')