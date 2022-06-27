from logging import error
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time

from streamlit.type_util import data_frame_to_bytes
from acervo import acervo



def form(cont,acervo,result):
    with st.form(key="formis"):
        codigo, tipo, nome, autor = acervo.printDoc(result[cont])
        st.write("Codigo: " + codigo,"\n tipo: " + tipo, "\n nome: " + nome,"\n autor: " +autor)    
        botao_prox = st.form_submit_button(label='Proximo')
        if botao_prox:
            cont = cont + 1
            form(cont,acervo,result)

st.title('Busca em Receitas da Vovó Duds')
DATE_COLUMN = 'date/time'

pesquisa = acervo()
total = st.write('Acervo = ', pesquisa.quant_docs)
with st.form(key='my_form'):
    text_input = st.text_input(label='O que deseja assistir')
    submit_button = st.form_submit_button(label='Pesquisar')

    print(text_input)
    