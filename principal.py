import streamlit as st

contador = 0

st.text('Aplicação Contador')
st.text_input('Insira seu Nome: ')

if st.button('Incrementar'):
    contador += 1
    st.text('Contador ' + str(contador))

if st.button('Decrementar'):
    contador -= 1
    st.text('Contador ' + str(contador))