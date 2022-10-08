#!/usr/bin/env python
# coding: utf-8

# # Exercícios

# In[1]:


#Importação da biblioteca Pandas
import pandas as pd


# ## Base dados
# 
# **Fonte da base de dados**
# 
# Enem 1998  
# [Microdados do Exame Nacional do Ensino Médio - Enem](http://www.dados.gov.br/dataset/microdados-do-exame-nacional-do-ensino-medio-enem)  
# 
# **Documentação da base de dados**  
# 
# Para entender a base, acesse a descrição dos campos, disponível neste [link](https://docs.google.com/spreadsheets/d/1tKI5o9wBzBh_SaRccHJKwEzqIekqhyze/edit#gid=1105751035).
# 
# **Carregamento da base**  
# 
# Para carregar a base em um DataFrame Pandas, execute:
# Para acessar o arquivo com a base é necessário solicitar acesso ao Google Drive. No caso desta aula, a base de dados está compartilhada entre todos os alunos incluídos na turma do Google Classroom.
# 
# **Google Colaboratory**  
# 
# Para execuções utilizando o ambiente do Google Colab, execute o código abaixo. A primeira vez que for executado, será solicitado um código de acesso. Para obter esse código, basta clicar no link gerado e seguir as instruções.
# ```python
# #Solicita acesso ao Google Drive
# from google.colab import drive
# drive.mount('/drive')
# 
# #Carrega a base de dados direto do Google Drive (Executando no Google Colab)
# enem98 = pd.read_csv('/drive/Shared drives/BasesPublicas/Bases/ENEM/1998/MICRODADOS_ENEM_1998.csv', sep=';', encoding='latin1' )
# ```
# **Jupyter**  
# 
# Para execuções no Jupyter:
# ```python
# #Colocar a base no mesmo diretório em que está executando o arquivo jupyter
# #enem98 = pd.read_csv('./MICRODADOS_ENEM_1998.csv', sep=';', encoding='latin1' )
# 
# ``` 
# 

# In[ ]:





# In[ ]:





# **Exercícios**
# 
# Sobre a base de dados referente ao ENEM do ano de 1998, responda as questões abaixo utilizando a biblioteca Pandas.

# Sobre a base:
# 1. Quantas linhas existem na base?
# 1. Quantas colunas existem?

# In[ ]:





# Obtenha cada informação solicitada a seguir:
# - Quantos alunos foram matriculados?

# In[ ]:





# - Quantos alunos matricularam-se no ENEM por estado?

# In[ ]:





# - Quantos estudantes matriculados não realizaram a prova?

# In[ ]:





# - Dos estudantes matriculados, quantos não realizaram a prova, por estado?

# In[ ]:





# - Qual é idade do(a) estudante mais velho(a)?

# In[ ]:





# - Quantos estudantes empatam com a idade mais velha?

# In[ ]:





# - Os estudantes com a idade mais mais velha são de quais estados?

# In[ ]:





# - Qual é a idade do(a) estudante mais novo(a) do Paraná?

# In[ ]:





# - Quantos estudantes possuem a mesma idade do estudante mais novo no Paraná?

# In[ ]:





# - De quais cidades são os estudantes com a menor idade?

# In[ ]:





# - No Paraná, qual a porcentagem de estudantes por sexo?

# In[ ]:




