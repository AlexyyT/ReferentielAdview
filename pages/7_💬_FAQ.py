import streamlit as st

st.title("Mieux comprendre le Référentiel Adview")

st.markdown(
    """
    ### Qu'est-ce que le référentiel Adview ?

    Le référentiel Adview prend la forme d'une base de données. Il contient l'ensemble des informations nécessaires à la collecte et au traitement de données.
    Il contient des données telle qu'un numéro de compte google analytics, ou encore une liste de mots-clés ranks.

    ### Quel est le rôle de cette plateforme ?

    Elle permet à tous les intervenants internes de suivre le Référentiel Adview et de le mettre à jour en fonction des besoins.

    Ainsi la collecte des données se fait de façon automatisée et est déclenchée uniquement à partir du moment où les données sont ajoutées au référentiel via cette plateforme.

    À chaque fois qu’un nouveau client est ajouté au référentiel, un rattrapage est automatiquement effectué sur les sources Google (Ads, Analytics 4, et Search Console). Ce rattrapage récupère les quatorze derniers mois. 

    ### Pourquoi dois-t-on renseigner ces données dans le référentiel ?

    Certaines données doivent être renseignées dans le Référentiel Adview car elles permettent d’automatiser la collecte à partir de différentes sources. Si elles ne sont pas inscrites dans le référentiel pour le client, alors la collecte ne se fera pas.

    Certaines données doivent être renseignées dans le Référentiel Adview car elles sont utilisées dans le cadre des rapports livrés au client ou de rapports de pilotage interne.

    ### Quelles sont les données présentent dans le Référentiel Adview ?

    Le référentiel peut être amené à évoluer au fil du temps en fonction des changements ou des ajouts de nouvelles sources de données. Aujourd'hui les données présentes dans le référentiel sont :
    - Création : ID Client, Nom du client
    - Google Analytics 4 : ID de la propriété
    - Google Ads : Numéro du compte client
    - Google Search Console : URL du profil à requêter.
    - Ranks : Nom de domaine du site client, liste de mots-clés.
    - Universal Analytics : Nom et ID du compte client, Nom et ID de la propriété, Nom et ID de la vue et date de collecte.
    
    ### Qu'est-ce que le REF_CLIENT_ID ?
    
    Le REF_CLIENT_ID est la pierre angulaire du Référentiel Adview.
    Il s'agit de l'identifiant client qui est présent dans toutes les tables de la base de données.
    Ce champ nous permet d'identifier pour chacune des données à quel client elles font référence.
    
    ### Comment est construit le REF_CLIENT_ID ?
    Le REF_CLIENT_ID se base sur l'identifiant OpenErpID que l'on peut retrouver dans Creatio.
    Pour une partie des clients le REF_CLIENT_ID et le OpenErpID sont identiques.
    Pour d'autres clients, il est nécessaire d'ajouter un suffixe au REF_CLIENT_ID. 
    
    Un même client Creatio peut se traduire par plusieurs clients Adcom. 
    Dans ce cas-là, on est contraint d'ajouter un suffixe au REF_CLIENT_ID en référence aux différents clients adcom afin de pouvoir dissocier leurs données.
    Par exemple, le compte Aixam Creatio regroupe les comptes Aixam, Aixam Mega, Aixam Pro et My Aixam pour Adcom.
    Dans ce cas la, les REF_CLIENT_ID seront les suivants :
    - OpenErpID dans Creatio : 334
    - REF_CLIENT_ID - Aixam : 334_AIXAM
    - REF_CLIENT_ID - Aixam Mega : 334_AIXAM_MEGA
    - REF_CLIENT_ID - Aixam Pro : 334_AIXAM_PRO
    - REF_CLIENT_ID - MyAixam : 334_MY_AIXAM 
    
    Autre possibilité, pour un même client Creatio, on doit réaliser différents livrables.
    Cela implique de mettre en place des sources de données différentes. 
    Donc on est contraint, la encore, de différencier les REF_CLIENT_ID en ajoutant un suffixe.
    C'est notamment le cas pour les comptes Sotheby's pour lesquels on livre des rapports pour le site FR et EN.
    Par exemple, pour Sotheby's France, les REF_CLIENT_ID seront les suivants :
    - OpenErpID dans Creatio : 19693
    - REF_CLIENT_ID - Sotheby's France : 19693
    - REF_CLIENT_ID - Sotheby's France EN : 19693_EN
    - REF_CLIENT_ID - Sotheby's France FR : 19693_FR
    
    Vous l'aurez compris, il est important de veiller à bien définir le REF_CLIENT_ID au moment de l'ajout d'un client au Référentiel Adview.
    Un mauvais REF_CLIENT_ID, impliquera indéniablement des données erronées dans les rapports Looker Studio. 
    """
)