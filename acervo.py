import os
import math

class acervo:


    def __init__(self):
        self.data_DIR = "./biblioteca/"
        self.quant_docs = len([name for name in os.listdir(self.data_DIR) if os.path.isfile(os.path.join(self.data_DIR, name))])
        self.doc_DIR = [self.data_DIR+name for name in os.listdir(self.data_DIR) if not name[0] == '.']


    def contaOcorrencias(self,arquivo,pesquisa):
        with open(arquivo) as f:
            ocorrencia = f.read().count(pesquisa)
        return ocorrencia

    def qtdeDocsComTermo(self,pesquisa):
        cont = 0
        for arq in self.doc_DIR:
            if self.check(arq,pesquisa)==True:
                cont=cont+1
        return cont

    #checa se há o termo pesquisado em determinado arquivo
    def ocorrNoDoc(self,arquivo,pesquisa):
        with open(arquivo) as f:
            if pesquisa in f.read():
                return True
            else:
                return False

    def printDoc(self,arquivo):
        f = open(arquivo, 'r')
        
        codigo = f.readline()
        tipo = f.readline()
        nome = f.readline()
        autor = f.readline()
        elenco = f.readline()
        pais = f.readline()
        data_add = f.readline()
        data_lanc =  f.readline()
        nota = f.readline()
        duracao = f.readline()
        return codigo, tipo, nome, autor, elenco, pais,data_add,data_lanc,nota,duracao