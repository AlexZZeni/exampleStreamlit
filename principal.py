import streamlit as st

contador = 0

st.text('Aplicação Contador')

if st.button('Incrementar'):
    contador += 1
    st.text('Contador ' + str(contador))

if st.button('Decrementar'):
    contador -= 1
    st.text('Contador ' + str(contador))