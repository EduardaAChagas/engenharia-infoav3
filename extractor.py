import csv
import re

def tratamento(string):
  string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ. ]', '', string)
  return string_nova

with open('RAW_recipes.csv', encoding='utf-8') as arquivo_referencia:
  tabela = csv.reader(arquivo_referencia, delimiter=',')
  cont = 1
  for l in tabela:
    arquivo = open("biblioteca/"+l[0] +'.txt', 'w')
    arquivo_treino = open('./biblioteca/arquivotreino.txt', 'w+')
    col1 = l[0]
    col1 = tratamento(col1)
    nome = l[2]
    nome = tratamento(nome)
    col2 = l[1]
    col2 = tratamento(col2)
    col3 = l[2]
    col3 = tratamento(col3)
    col4 = l[3]
    col4 = tratamento(col4)
    col5 = l[4]
    col5 = tratamento(col5)
    col6 = l[5]
    col6 = tratamento(col6)
    col7 = l[6]
    col7 = tratamento(col7)
    col8 = l[7]
    col8 = tratamento(col8)
    col9 = l[8]
    col9x = l[8]
    col9x = tratamento(col9x)
    col9 = tratamento(col9)
    col10 = l[9]
    col10 = tratamento(col10)
    col11 = l[10]
    col11 = tratamento(col11)
    arquivo.write(col1+'\n')
    arquivo.write(col2+'\n')
    arquivo.write(col3+'\n')
    arquivo.write(col4+'\n')
    arquivo.write(col5+'\n')
    arquivo.write(col6+'\n')
    arquivo.write(col7+'\n')
    arquivo.write(col8+'\n')
    arquivo.write(col9+'\n')
    arquivo.write(col10+'\n')
    arquivo.write(col11+'\n')
    arquivo_treino.write(col9x.replace('\n','')+'\n')
    arquivo_treino.write(col10+'\n')
    arquivo_treino.write(col11+'\n')
    print("Contador:")
    print(cont)
    cont = cont +1
    arquivo.close()
    if (cont == 2000):
      break