import streamlit as st
import pandas as pd

valor = pd.read_csv('data.csv', sep = ';')

st.text('Aplicação Contador')
st.text_input('Insira seu Nome: ', key = 'nome')
nome = st.session_state.nome
if st.button('Incrementar'):
    contador += 1
    st.text(nome + ' Contador ' + str(contador))

if st.button('Decrementar'):
    contador -= 1
    st.text(nome + ' Contador ' + str(contador))