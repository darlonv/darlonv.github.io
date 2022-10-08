#!/usr/bin/env python
# coding: utf-8

# # CSV

# Um arquivo o formato CSV (*Comma Separated Values*) consiste em organizar os dados em um formato de tabela, onde cada coluna dessa tabela está separada por vírgulas. Cada linha do arquivo corresponde a uma linha da tabela, e a primeira linha pode conter títulos para as colunas. Um arquivo CSV é um arquivo texto, o que o caracteriza é a sua maneira de organização dos dados nele contidos.
# 
# Os arquivos em formato CSV são bastante utilizados para salvar bases de dados.

# Um arquivo csv típico possui seu conteúdo organizado da seguinte maneira:
# 
# ```
# Ordem,Nome,Distancia,Diametro,Rochoso
# 1,Mercurio,57910000,4879,Sim
# 2,Venus,108200000,12104,Sim
# 3,Terra,149600000,12742,Sim
# ```
# 
# **Atividade**  
# - Execute o código a seguir para criar um arquivo de exemplo.
# 
# ```python
# file = open('planetas.csv',mode='w')
# file.writelines('Ordem,Nome,Distancia,Diametro,Rochoso\n')
# file.writelines('1,Mercurio,57910000,4879,Sim\n')
# file.writelines('2,Venus,108200000,12104,Sim\n')
# file.writelines('3,Terra,149600000,12742,Sim\n')
# file.close()
# ```

# In[ ]:





# Como um arquivo CSV é um arquivo texto, e é possível visualizar seu conteúdo acessando-o como arquivo texto.
# 
# **Exemplo**  
# - Lendo o conteúdo como arquivo texto
# ```python
# txt_file = open('planetas.csv',mode='r')
# for linha in txt_file:
#     print(linha end='')
# txt_file.close()
# ```
# 
# **Atividade**  
# - Leia o arquivo como texto, e observe o caractere que separa cada campo.

# In[ ]:





# ## Leitura
# Uma das formas de manipulação é utilizando a biblioteca `csv`. O uso das bibliotecas permite que a leitura dos arquivos seja mais fácil e organizada pelo programador.
# 
# ```python
# import csv
# ```

# In[ ]:





# A biblioteca `csv` possibilita que cada linha seja lida como um dicionário, utilizando o método `.DictReader()`. O parâmetro `delimiter` define qual é o caractere que separa os campos. Seu valor padrão é `,`, e nosso caso poderia ser omitido.
# 
# **Exemplo**  
# - Lendo o conteúdo como arquivo csv, utilizando dicionários.  
# 
# ```python
# csv_file = open('planetas.csv', mode='r')
# csv_reader = csv.DictReader(csv_file, delimiter=',')
# 
# for linha in csv_reader:
#     print(f"{linha['Nome']} {linha['Ordem']}") #Obtêm-se apenas as colunas desejadas
# csv_file.close()
# 
# ```

# In[ ]:





# 

# ## Escrita
# Com a mesma biblioteca também é possível salvar dados em arquivos CSV.
# 
# ```python
# csv_file = open('planetas.csv', mode='a') #abre com append. w para criar novo arquivo.
# csv_writer = csv.writer(csv_file, delimiter=',')
# 
# csv_writer.writerow([4,'Marte',227900000,6779,'Sim'])
# csv_writer.writerow([5,'Júpiter',778500000,139820,'Não'])
# csv_writer.writerow([6,'Saturno',1429400000,116460,'Não'])
# csv_writer.writerow([7,'Urano',2870990000,50724,'Não'])
# csv_writer.writerow([8,'Netuno',4504300000,49244,'Não'])
# csv_file.close()
# ```

# In[52]:





# **Atividade**
# - Visualize o arquivo atualizado, como texto.
# <!-- Vamos visualizar o arquivo, atualizado.
# ```python
# txt_file = open('planetas.csv', mode='r')
# for linha in txt_file:
#     print(linha, end='')
# txt_file.close()
# ``` -->

# In[ ]:





# **Exercícios**
# 
# - Mostre os planetas por ordem de tamanho
# - Calcule e apresente o tamanho de cada planeta em relação à Terra. 

# In[ ]:




