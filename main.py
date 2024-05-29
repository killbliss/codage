import streamlit as st
# import du module "secret"
from secret import encode, decode


st.set_page_config(
    page_title="Fonction de codage/décodage", initial_sidebar_state="collapsed"
)

### Titre d'accueil

st.header('This is a test')

## Saisie du texte à coder/décoder:

sentence = st.text_input('rentre une phrase à encoder:')

if st.button('Encoder', key=1):
    resultat = encode(sentence)
    st.write(f'texte encodé : {resultat}')

elif st.button('Decoder', key=2):
        decode_sentence = decode(sentence)
        st.write(f'Texte décodé: {decode_sentence}')

else:
    st.error("On t'as dit de rentrer du text t'es bouché à l'emery ou quoi frérot ?")

### Affichage de la réponse (encodage ou décodage):
