import streamlit as st
import pandas as pd
import snowflake.connector
from utils.const import *
import boto3
from json import dumps
import time

@st.cache_data
def SQLquery(query):
    conn = snowflake.connector.connect(
        user=SF_USER,
        password=SF_PASSWORD,
        account=SF_ACCOUNT,
        warehouse=SF_WAREHOUSE,
        database=SF_DATABASE,
        schema=SF_SCHEMA,
        role=SF_ROLE
    )

    #Se connecter à snowflake
    cursor = conn.cursor()

    #Exécuter une requête SQL
    cursor.execute(query)

    #Afficher le nom des colonnes
    df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
    return(df)

    #Afficher les résultats
    #rows = cursor.fetchall()
    #for row in rows:
    #    print(row)

    #Fermer la connexion
    cursor.close()
    conn.close()

def startInstance():
    instance_id = INSTANCE_ID

    # Créez un client EC2
    ec2_client = boto3.client('ec2')

    # Obtenez des informations sur l'instance spécifique
    response = ec2_client.describe_instances(InstanceIds=[instance_id])

    # Vérifiez le statut de l'instance
    instance_status = response['Reservations'][0]['Instances'][0]['State']['Name']

    if instance_status == 'stopped':
        # Si l'instance est éteinte, démarrez-la.
        ec2_client.start_instances(InstanceIds=[instance_id])
    elif instance_status == 'stopping':
        # Si l'instance est en train de s'éteindre, attendez 30s et démarrez-la.
        time.sleep(30)
        ec2_client.start_instances(InstanceIds=[instance_id])
    elif instance_status == 'pending':
        # Si l'instance est en train de s'allumer, attendez 30s.
        time.sleep(30)

def processKeyword(keyword):
    if '&' in keyword:
        keyword = keyword.replace("&", "&amp;")
    if "'" in keyword:
        keyword = keyword.replace("'", "&apos;")

    return keyword.lower()

def HistorisationSQS(REF_CLIENT_ID, VUE_ID, START_DATE, END_DATE):
    startInstance()

    sqs = boto3.client('sqs', region_name='eu-west-1')

    # Convert date objects to their string representations (ISO 8601 format).
    start_date_str = START_DATE.strftime("%Y-%m-%d")
    end_date_str = END_DATE.strftime("%Y-%m-%d")

    payload = {
        'group': 'adcom',
        'project': 'prod',
        'version': 'prod',
        'environment': 'prod',
        'job': '600_ga3_historisation',
        'variables': {
           'v_bucket': '',
            'v_file_prefix':'',
            'v_client_id': REF_CLIENT_ID,
            'v_end_date': end_date_str,
            'v_profile_id':VUE_ID,
            'v_start_date':start_date_str
        }
    }

    response = sqs.send_message(
        QueueUrl=SQS_URL,
        MessageBody=dumps(payload)
    )

    return response

def RanksModificationSQS(REF_CLIENT_ID, DATE, KEYWORD, OLD_POSITION, NEW_POSITION):
    startInstance()

    sqs = boto3.client('sqs', region_name='eu-west-1')

    payload = {
        'group': 'adcom',
        'project': 'prod',
        'version': 'prod',
        'environment': 'prod',
        'job': '100_modifications_ranks',
        'variables': {
           'v_bucket': '',
            'v_file_prefix' : '',
            'v_client_id': REF_CLIENT_ID,
            'v_date': DATE,
            'v_keyword': processKeyword(KEYWORD),
            'v_position_new': NEW_POSITION,
            'v_position_old': OLD_POSITION
        }
    }

    response = sqs.send_message(
        QueueUrl=SQS_URL,
        MessageBody=dumps(payload)
    )

    return response

def processListeMotsClesDF(rows):
    df = pd.DataFrame(columns=['#', 'BU', 'THEME', 'KEYWORD', 'SEARCH_VOLUME'])

    # Ajouter 10 lignes avec des valeurs vides
    nouvelles_lignes = rows
    valeurs_vides = [
                        None] * nouvelles_lignes  # Vous pouvez également utiliser np.nan au lieu de None pour des valeurs NaN
    nouvelles_donnees = {colonne: valeurs_vides for colonne in df.columns}
    df_nouvelles_lignes = pd.DataFrame(nouvelles_donnees)

    # Concaténer les deux DataFrames
    st.session_state.liste_mots_cles = pd.concat([df, df_nouvelles_lignes], ignore_index=True)

def processBusinessProfileDF(rows):
    df = pd.DataFrame(columns=['Location ID Business Profile'])

    # Ajouter 10 lignes avec des valeurs vides
    nouvelles_lignes = rows
    valeurs_vides = [
                        None] * nouvelles_lignes  # Vous pouvez également utiliser np.nan au lieu de None pour des valeurs NaN
    nouvelles_donnees = {colonne: valeurs_vides for colonne in df.columns}
    df_nouvelles_lignes = pd.DataFrame(nouvelles_donnees)

    # Concaténer les deux DataFrames
    st.session_state.BUSINESS_PROFILE = pd.concat([df, df_nouvelles_lignes], ignore_index=True)

def processGAdimensionsDF(rows):
    df = pd.DataFrame(columns=['Nom de la dimension personnalisée', 'Description de la dimension personnalisée'])

    # Ajouter 10 lignes avec des valeurs vides
    nouvelles_lignes = rows
    valeurs_vides = [
                        None] * nouvelles_lignes  # Vous pouvez également utiliser np.nan au lieu de None pour des valeurs NaN
    nouvelles_donnees = {colonne: valeurs_vides for colonne in df.columns}
    df_nouvelles_lignes = pd.DataFrame(nouvelles_donnees)

    # Concaténer les deux DataFrames
    st.session_state.GA4_DIMENSIONS = pd.concat([df, df_nouvelles_lignes], ignore_index=True)

def initializeSessionStates():
    session_states = ['referentiel_client','referentiel_mots_cles','referentiel_google_analytics','referentiel_business_profile','referentiel_languages',
                      'client_nom','client_ref_id','client_suffixe','client_ga4','client_gsc','client_gads','client_domaine','client_langue',
                      'liste_mots_cles',
                      'business_profile_account_id','business_profile_locations_id',
                      'google_analytics_dimensions']

    for state in range(len(session_states)):
        if state not in st.session_state:
            st.session_state[state] = ''

    st.session_state.referentiel_client = SQLquery("SELECT * EXCLUDE (INDICATOR) FROM PROD_DB.TRANSVERSAL_SCH.REFERENTIEL_CLIENT ORDER BY NAME")
    st.session_state.referentiel_mots_cles = SQLquery("SELECT * FROM PROD_DB.TRANSVERSAL_SCH.REFERENTIEL_MOTS_CLES ORDER BY REF_CLIENT_ID, PRIORITY")
    st.session_state.referentiel_google_analytics = SQLquery("SELECT * FROM PROD_DB.TRANSVERSAL_SCH.REFERENTIEL_GOOGLE_ANALYTICS")
    st.session_state.referentiel_business_profile = SQLquery("SELECT * FROM PROD_DB.TRANSVERSAL_SCH.REFERENTIEL_BUSINESS_PROFILE")
    st.session_state.referentiel_languages = SQLquery("""SELECT "Language", Count(*) FROM BRONZE_SCH.RANKS WHERE "Date" > '2020-01-01' GROUP BY 1 ORDER BY 2 desc""")