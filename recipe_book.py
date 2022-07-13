import os
import math

class book:


    def __init__(self):
        self.data_DIR = "./biblioteca/"
        self.quant_docs = len([name for name in os.listdir(self.data_DIR) if os.path.isfile(os.path.join(self.data_DIR, name))])
        self.doc_DIR = [self.data_DIR+name for name in os.listdir(self.data_DIR) if not name[0] == '.']


    #TF
    def contaOcorrencias(self,arquivo,pesquisa):
        with open(arquivo) as f:
            ocorrencia = f.read().count(pesquisa)
        return ocorrencia

    #qtde docs com o termo pesquisado
    def qtdeDocsComTermo(self,pesquisa):
        cont = 0
        for arq in self.doc_DIR:
            if self.isTermInThisDoc(arq,pesquisa)==True:
                cont=cont+1
        return cont

    def printRecipe(self,arquivo):
        f = open(arquivo, 'r')
        name = f.readline()
        id_receita = f.readline()
        minutes = f.readline()
        contributorid = f.readline()
        submitted = f.readline()
        tags = f.readline()
        nutrition = f.readline()
        nsteps = f.readline()
        steps = f.readline()
        description = f.readline()
        ingredients = f.readline()

        return name, id_receita, minutes, contributorid, submitted, tags, nutrition, nsteps, steps, description, ingredients

    def IDF(self, pesquisa):
        quantidade = self.qtdeDocsComTermo(pesquisa)
        if quantidade == 0 or pesquisa == None or pesquisa == "":
            return 0
        idf = (self.quant_docs/quantidade)
        return idf

    def pesoTermo(self,contaOcorrencias,idf):
        return contaOcorrencias*idf

    #checa se há o termo pesquisado em determinado arquivo
    def isTermInThisDoc(self, arquivo, pesquisa):
        with open(arquivo) as f:
            if pesquisa in f.read():
                return True
            else:
                return False

    def similaridadeUnidade(self,busca,arquivo,idf):
        tf = self.contaOcorrencias(arquivo,busca)
        #peso do doc
        pesoDoc = self.pesoTermo(tf,idf)
        #peso de busca
        pesoBusca = (0.5+(tf/2))*idf

        sim = (pesoBusca*pesoDoc)/(math.sqrt(math.pow(pesoBusca,2)) +math.sqrt(math.pow(pesoDoc,2)) ) 
        return sim

    def createCollection(self, pesquisa):
        keys = pesquisa.split()
        refCollection = { }

        for x in keys:
            refCollection[x] = []
        
        return refCollection
        
    def updateCollection(self, collection, id_doc):
        for x in collection:
            collection[x].append(id_doc)

    def recall(self, vp,fn):
        """
        VP -> qtd  documentos distintos 
        presentes na coleção de referência;
         
        FN -> documentos que ESTÃO coleção 
        de referencia mas NÃO ESTÃO no vetor de resultados da busca.
        
        """
        return vp/(vp + fn)

    def precision(self, vp,fp):
        """
        VP -> qtd  documentos distintos 
        presentes na coleção de referência;
         
        FP -> documentos que não estão coleção 
        de referencia mas estão no vetor de resultados da busca.
        
        """
        return vp/(vp + fp)
