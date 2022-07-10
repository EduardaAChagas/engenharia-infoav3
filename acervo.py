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
    
    def IDF(self, pesquisa):
        quantidade = self.qtdeDocsComTermo(pesquisa)
        if (quantidade == 0):
            return 0
        idf = (self.quant_docs/quantidade)
        return idf

    #checa se há o termo pesquisado em determinado arquivo
    def ocorrNoDoc(self,arquivo,pesquisa):
        with open(arquivo) as f:
            if pesquisa in f.read():
                return True
            else:
                return False

    def printDoc(self,arquivo):
        f = open(arquivo, 'r')
        
        f.readline()
        id_receita = f.readline()
        f.readline()
        f.readline()
        data_receita = f.readline()

        return id_receita, data_receita

    def Idf(self,pesquisa):
        if(self.qtdeDocsComTermo(pesquisa) != 0):
            return (self.quant_docs/self.qtdeDocsComTermo(pesquisa))
        else:
            return 0

    def pesoTermo(self,contaOcorrencias,idf):
        return contaOcorrencias*idf

    def similaridadeUnidade(self,busca,arquivo,idf):
        tf = self.contaOcorrencias(arquivo,busca)
        #peso do doc
        pesoDoc = self.peso(tf,idf)
        #peso de busca
        pesoBusca = (0.5+(tf/2))*idf

        sim = (pesoBusca*pesoDoc)/(math.sqrt(math.pow(pesoBusca,2)) +math.sqrt(math.pow(pesoDoc,2)) ) 
        return sim
