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
    text_input = st.text_input(label='Vamos almoçar?')
    search_button = st.form_submit_button(label='Arroz soltinho')

    print(text_input)
    
if search_button:
    st.text("Receitas relevantes:")
    doc_DIR = pesquisa.doc_DIR
    data_DIR = pesquisa.data_DIR
    idf = pesquisa.IDF(text_input)
    if (idf == 0):
        st.write("Nenhuma receita encontrada, vovó duds sente muito")
    else:
        receitas_encontradas = 0
        cont = 0
        max = 0
        cont2 = 0
        result = []
        vet_simi = []
        latest_iteration = st.empty()
        bar = st.progress(0)
        for recipes in doc_DIR:
            simil = pesquisa.similaridadeUnidade(text_input, recipes, idf)
            if simil>0:
                if simil>max:
                    max = simil
                    result.insert(0,recipes)
                    vet_simi.insert(0,simil)
                else:
                    result.append(recipes)
                    vet_simi.append(simil)
                receitas_encontradas = receitas_encontradas+1
                latest_iteration.text(f'Procurando... {cont+1}')
                bar.progress(cont+1)
                if cont != 90:
                    cont = cont+1
                if cont2 == (pesquisa.quant_docs - 2):
                    cont2 = cont2+1
                print(recipes)
    if idf != 0:
        quant_docs = pesquisa.qtdeDocsComTermo(text_input)
        st.write("Receitas encontradas: ",quant_docs)
        result2 = result
        cont = 0
        vetores = ["0","1","2","3","4"]
        for x in range(0,len(result2)):
            with st.form(key='my-form2' + vetores[x]):
                name, id, minutes, contributorid, submitted, tags, nutrition, nsteps, steps, description, ingredients = pesquisa.printDoc(result2[x])
                st.write("Similaridade: ",vet_simi[x],"\n\n Nome: " + name, "\n Id da receita: " + id, "\n Id do contribuidor: " + contributorid, "\n Data de submissão: " + submitted, 
                "\n Palavras-chave: " + tags, "\n Valor nutricional: " + nutrition, "\n Número de passos: " + nsteps, "\n Passos: " + steps, "\n Descrição: " + description)
                botao_prox = st.form_submit_button(label = "Ver no livro de receitas")
                if botao_prox: 
                    st.text("Cancelar busca, não estou mais com fome")
                if cont == 4:
                    cont = cont + 1

        print(text_input)
