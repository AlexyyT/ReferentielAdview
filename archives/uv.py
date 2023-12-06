import streamlit as st
import datetime

st.markdown("""
     # atmós sphaîra
     ## Planificateur de contenus Youtube
     Veuillez renseigner l'ensemble des informations ci-dessous et valider pour commencer le traitement.
     
     #### Nom de la sortie
     
    """)

release_name = st.text_input("Veuillez renseigner le nom de la sortie.")

st.markdown("""

     #### Description

    """)

description = st.text_area("Veuillez renseigner la description du contenu.")

st.markdown("""

     #### Tags

    """)

tags = st.text_area("Veuillez renseigner les tags associé à ce contenu.")

st.markdown("""

     #### Date de publication

    """)

date = st.date_input("Veuillez renseigner la date à laquelle sera publiée ce contenu")
time = st.time_input("Veuillez renseigner l'heure à laquelle sera publiée ce contenu", value=datetime.time(16,0))

st.markdown("""

     #### Cover

    """)

cover = st.file_uploader("Importer la cover de la sortie (au format .jpg, .jpeg ou .png).", type=[".jpg",".jpeg",".png"], accept_multiple_files=False)

st.markdown("""

     #### Tracks

    """)

tracks = st.file_uploader("Importer les tracks de la sortie (au format .mp3 ou .wav).", type=[".mp3",".wav"], accept_multiple_files=True)

st.markdown("""

    """)

bouton = st.button("Planifier les contenus")

if bouton :
    st.write(f"Nom : {release_name}")
    st.write(f"Description : {description}")
    st.write(f"Tags : {tags}")
    st.write(f"\n Date - heure : {date} - {time}\n")
    st.write(f"Cover : {cover}")
    st.write(f"Tracks : {tracks}")
