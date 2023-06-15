import streamlit as st
import os
from datetime import datetime

listaArquivos = os.listdir("./")

st.text(listaArquivos)


now = datetime.now()

if st.button("Escreve"):
    file = open("./texto.txt", "a+")
    texto = now.strftime("%H:%M:%S %d/%m/%Y\n")
    file.write(texto)
    file.close()
    st.experimental_rerun()



file = open("./texto.txt", "r")
st.code(file.read())
file.close()

#if(button)