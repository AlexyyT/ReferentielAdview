import streamlit as st
from utils.func import *

st.title("Ajouter un client au référentiel Adview")

clients = {
    'BABOLAT_VS' : '19509',
    'SKEMA_FR' : '19679_FR'
}

if 'REF_CLIENT_ID_SUFFIXE' not in st.session_state:
    st.session_state.REF_CLIENT_ID_SUFFIXE = ''
if 'MULTI_CLIENT' not in st.session_state:
    st.session_state.MULTI_CLIENT = ''
if 'KEYWORDS' not in st.session_state:
    st.session_state.KEYWORDS = ''
if 'BUSINESS_PROFILE' not in st.session_state:
    st.session_state.BUSINESS_PROFILE = ''
if 'GA4_DIMENSIONS' not in st.session_state:
    st.session_state.BUSINESS_PROFILE = ''


st.markdown(""" Renseigner les données nécessaires en fonction du profil client """)
c1 = st.container()
c1.markdown(""" #### Profils Client
Données d'identification du client sur les outils métiers""")

st.session_state.client_nom = c1.selectbox('Nom du client', st.session_state.referentiel_client['NAME'], disabled=False)
multi_client = c1.selectbox('Est-ce que le client profil Creatio correspond à plusieurs clients adcom ?', ['Non', 'Oui'])

if multi_client == 'Oui':
    st.session_state.client_suffixe = c1.text_input('Choisissez le suffixe à ajouter au REF_CLIENT_ID',
                                                           help="Le suffixe doit permettre de rendre le REF_CLIENT_ID unique. Il peut permettre d'identifier la langue du site (19874_FR : sotheby's FR) ou le client (334_AIXAM : Axiam / 334_MEGA : Aixam MEGA) ...")
else :
    st.session_state.client_suffixe = ''

st.session_state.client_ref_id = c1.text_input('REF_CLIENT_ID',
                                                st.session_state.referentiel_client.loc[st.session_state.referentiel_client["NAME"] == st.session_state.client_nom, "REF_CLIENT_ID"].to_string(index=False) + st.session_state.client_suffixe,
                                               disabled=True)

st.session_state.client_ga4 = c1.text_input('Google Analytics 4 - Numéro de la propriété', help="Le numéro de propriété GA4 est composé de 9 chiffres, ne pas confondre avec l'identifiant du flux de mesure commencant par G-XXXXXX")
st.session_state.client_gsc = c1.text_input('Google Search Console - Url du site', help="Pour les clients multilingues, bien inclure le répertoire de la langue si nécessaire.")
st.session_state.client_gads = c1.text_input('Google Ads - Numéro du compte client', help='Numéro de compte au format XXX-XXX-XXXX')
st.session_state.client_domaine = c1.text_input('Nom de domaine', help="Ce paramètre est utilisé afin de remonter les bonnes données ranks")
st.session_state.client_langue = c1.selectbox('Langue du client', st.session_state.referentiel_languages["Language"], help="Ce paramètre est utilisé afin de remonter les bonnes données ranks")


st.divider()

c2 = st.container()
c2.markdown(""" #### Liste de mots clés
Mots clés pour lesquels""")

nb_mots_cles = c2.number_input('Nombre de mots-clés', placeholder="Taper un nombre...", step=1)
button_mots_cles = c2.button('Initialiser la liste des mots-clés', on_click=processListeMotsClesDF(nb_mots_cles))

if button_mots_cles:
    c2.write('Veuillez renseigner la liste des mots-clés')
    st.session_state.liste_mots_cles = c2.data_editor(st.session_state.liste_mots_cles, hide_index=True)

st.divider()

c3 = st.container()

c3.markdown(""" #### Business Profile
Liste des emplacements Google Business Profile associé au client
""")

c3.text_input('ID du compte Business Profile', help="L'identifiant du compte Google Business Profile est composé de 21 chiffres.")

nb_emplacements = c3.number_input("Nombre d'emplacements Business Profile", placeholder="Taper un nombre...", step=1)
button_emplacements = c3.button('Initialiser la liste des emplacements Business Profile', on_click=processBusinessProfileDF(nb_emplacements))

if button_emplacements:
    c3.write('Veuillez renseigner les ID des emplacements Business Profile')
    st.session_state.BUSINESS_PROFILE = c3.data_editor(st.session_state.BUSINESS_PROFILE, hide_index=True)

st.divider()

c4 = st.container()

c4.markdown(""" #### Google Analytics 4 - Dimension Personnalisée
Liste des dimensions personnalisées associés à la propriété GA4.""")

nb_dimensions = c4.number_input("Nombre de dimensions personnalisées GA4", placeholder="Taper un nombre...", step=1)
button_dimensions = c4.button('Initialiser la liste des dimensions personnalisées', on_click=processGAdimensionsDF(nb_dimensions))

if button_dimensions:
    c4.write('Veuillez renseigner les ID des emplacements Business Profile')
    st.session_state.GA4_DIMENSIONS = c4.data_editor(st.session_state.GA4_DIMENSIONS, hide_index=True)

