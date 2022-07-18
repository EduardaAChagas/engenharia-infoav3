from logging import error
import streamlit as st
import numpy as np
import pandas as pd
import time
from nltk import word_tokenize

from streamlit.type_util import data_frame_to_bytes
from recipe_book import book
from bag_of_words import bow


st.title('Busca em Receitas da Vovó Duds')
 
bgow = bow()
pesquisa = book()
total = st.write('Livro da vovó Duds contém', pesquisa.quant_docs, 'receitas.')
with st.form(key='my_form'):
    text_input = st.text_input(label='Vamos almoçar?')
    search_button = st.form_submit_button(label='Arroz soltinho')

doc_DIR = pesquisa.doc_DIR
data_DIR = pesquisa.data_DIR
text = []
arquivos = []
lista_deNomes = []
arquivosTotal = []

for l in range(0,len(doc_DIR)):
    op1,op2,op3,op4,op5,op6,op7,op8,op9,op10,op11 = pesquisa.printRecipe(pesquisa.doc_DIR[l])
    text.append(op1)
    text.append(op2)
    text.append(op3)
    text.append(op4)
    text.append(op5)
    text.append(op6)
    text.append(op7)
    text.append(op8)
    text.append(op9)
    text.append(op10)
    text.append(op11)
    texto = " ".join(text)
    lista_deNomes.append(op1)
    arquivos.append([op1,op2,op3,op4,op5,op6,op7,op8,op9,op10,op11])

#vocabulario
tokens = word_tokenize(texto)
vocab = []
for token in tokens:
    if token not in vocab:
        vocab.append(token)


    
if search_button:

    valueBase = 0.0
    idf = bgow.IDF(text_input,vocab)
    for nome,value in idf.items():
        if value > valueBase:
            valueBase = value
        indice = valueBase
    idfe = indice
    if (idfe == 0 or idf == None):
        st.write("Nenhuma receita encontrada, vovó duds sente muito")
    else:
        receitas_encontradas = 0
        cont = 0
        max = 0
        cont2 = 0
        result = []
        vet_simi = []
        latest_iteration = st.empty()
        colecaoRef = pesquisa.createCollection(text_input)
        for recipes in doc_DIR:
            name, id, minutes, contributorid, submitted, tags, nutrition, nsteps, steps, description, ingredients = pesquisa.printRecipe(recipes)
            if pesquisa.isTermInThisDoc(recipes, text_input) == True:
                pesquisa.updateCollection(colecaoRef, idfe)
            simil = pesquisa.similaridadeUnidade(text_input, recipes,idfe)
            if simil>0:
                if simil>max:
                    max = simil
                    result.insert(0,recipes)
                    vet_simi.insert(0,simil)
                else:
                    result.append(recipes)
                    vet_simi.append(simil)
                receitas_encontradas = receitas_encontradas+1
            if cont != 90:
                cont = cont+1
            if cont2 == (pesquisa.quant_docs - 2):
                cont2 = cont2+1
    if idf != 0:
        quant_docs = pesquisa.qtdeDocsComTermo(text_input)
        st.write("Receitas encontradas: ",quant_docs)
        result2 = result
        cont = 0
        vetores = ["0","1","2","3","4","6","7","8","9","10"]
        idResults = []
        for x in range(0,len(result2)): 
            with st.form(key='my-form2' + vetores[x]):
                name, id, minutes, contributorid, submitted, tags, nutrition, nsteps, steps, description, ingredients = pesquisa.printRecipe(result2[x])
                idResults.append(id)
                st.write("Similaridade: ",vet_simi[x],"\n\n Nome: " + name, "\n Id da receita: " + id, "\n Id do contribuidor: " + contributorid, "\n Data de submissão: " + submitted, 
                "\n Palavras-chave: " + tags, "\n Valor nutricional: " + nutrition, "\n Número de passos: " + nsteps, "\n Passos: " + steps, "\n Descrição: " + description)
                
                botao_prox = st.form_submit_button(label = "Ver no livro de receitas")
                if botao_prox: 
                    st.text("Cancelar busca, não estou mais com fome")
                if cont == 4:
                    cont = cont + 1
        try:
            vp, fn, fp = pesquisa.indicesEffect(colecaoRef, idResults)
            recall = pesquisa.recall(vp,fn)
            precision = pesquisa.precision(vp,fp)
            st.write("Recall: ",recall,"\n Precision: ", precision)
        except:
            st.write("Nenhuma receita encontrada, vovó duds sente muito")