from calendar import c
import csv
import re

from jinja2 import DictLoader
from recipe_book import book
import pandas as pd
from nltk import word_tokenize
import nltk
from recipe_book import book
import numpy as np
import math

class bow:


    def criaVetorDocumento(documento,vocab):
        vetor = []
        for palavra in vocab:
            if palavra in documento:
                vetor.append(1)
            else:
                vetor.append(0)

        return np.array(vetor)

    def tratamento(texto):
        texto_min = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ. ]', '', texto)
        return texto_min



    table = pd.read_csv('RAW_recipes.csv')
    livro = book()
    doc_DIR = livro.doc_DIR
    data_DIR = livro.data_DIR
    text = []
    arquivos = []
    lista_deNomes = []
    arquivosTotal = []

    for l in range(0,len(doc_DIR)):
        op1,op2,op3,op4,op5,op6,op7,op8,op9,op10,op11 = livro.printRecipe(livro.doc_DIR[l])
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
    

    tokens = word_tokenize(texto)

    Vocab = []
    for token in tokens:
        if token not in Vocab:
            Vocab.append(token)


#TF e IDF

    #tokeniza cada arquivo
    def tokenizeArquivosSepar(arquivos):
        arqTokenizados = []
        for i in range(0,len(arquivos)):
            arquivos[i] = " ".join(arquivos[i])
            arqTokenizados.append(arquivos[i])
            arqTokenizados[i] = arqTokenizados[i].split()
        return arqTokenizados

    #conta quantas vezes uma palavra do vocabulario aparece no doc
    def dicionario_de_contagem(vocabulario, documento):    
        dic = dict.fromkeys(vocabulario, 0)
        try:
            for palavra in documento:
                dic[palavra] += 1
            return dic
        except:
            print("\n#\n")

        return dic

    tokenArq = tokenizeArquivosSepar(arquivos)
    
    dictDeCont = []
    for i in range(0,len(tokenArq)):
        aux = dicionario_de_contagem(Vocab,tokenArq[i])
        dictDeCont.append(aux)

    print(tokenArq)


    #qtde vezes q uma palavara aparece no doc/qtde palavras no doc
    def calculaTF(dic_de_cont, doc): 
        dicDeDic = []
        
        for i in range(0,len(doc)):
            dicty = {}
            comp_doc = len(doc[i])
            for palavra, quantidade in dic_de_cont[i].items():
                dicty[palavra] = quantidade/float(comp_doc)
            dicDeDic.append(dicty)
        return dicDeDic
 
    resultadoTF = calculaTF(dictDeCont,tokenArq)
    #print(resultadoTF) 
    


    def computaIDF(lista_de_docs,vocab):
        idf_dic = {}
        N = len(lista_de_docs)

        for palavra in vocab:
            num_docs_aparece = 0
            for doc in lista_de_docs:
                if palavra in doc:
                    num_docs_aparece += 1
            if num_docs_aparece > 0:
                idf_dic[palavra] = (N/(num_docs_aparece))

        return (idf_dic)

    resultIdf = computaIDF(tokenArq,Vocab)
    #print(resultIdf)
    


    def computaTFIDF(tf_bow, idfs):
        tfidf = {}
        listfidf = []
        for doc in tf_bow:
            for word in idfs:
                if word in doc:
                    tf = doc[word]
                else:
                    tf = 0.0
                idf = idfs[word]
                tfidf[word] = tf*idf
                listfidf.append(tfidf)
        return listfidf
    
    resultTfIdf = computaTFIDF(resultadoTF,resultIdf)
    print(resultTfIdf)
    



    def similaridadeUnidade(self,busca,arquivo,idf):
        tf = self.contaOcorrencias(arquivo,busca)
        #peso do doc
        pesoDoc = self.pesoTermo(tf,idf)
        #peso de busca
        pesoBusca = (0.5+(tf/2))*idf

        sim = (pesoBusca*pesoDoc)/(math.sqrt(math.pow(pesoBusca,2)) +math.sqrt(math.pow(pesoDoc,2))) 
        return sim


    #similaridade
    #ordenar documentos a partir da similaridade