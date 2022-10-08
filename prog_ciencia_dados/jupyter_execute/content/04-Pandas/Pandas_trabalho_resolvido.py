#!/usr/bin/env python
# coding: utf-8

# # T1-2

# Responda ás questões elencadas abaixo utilizando a linguagem de programação Python e as bibliotecas Pandas, Matplotlib e Seaborn.
# 
# Este trabalho consiste em realizar uma análise sobre dados de ocorrências de acidentes de trânsito, ocorridos no ano de 2018.
# 
# A fonte dos dados e especificações podem ser consultados no portal da Polícia Rodoviária Federal, disponível [aqui](https://portal.prf.gov.br/dados-abertos).

# **Dicas**
# - Assim como nos DataFrames, nas Series tamém é possível utilizar a função `.head()`.
# - A função `.value_counts()` retorna os valores ordenados por quantidade, em ordem decrescente.
# - Com a função `.value_counts()` também é possível gerar gráficos, p.ex. `.value_counts().plot()` ou `.value_counts().plot.bar()`.

# In[1]:


print('ok')


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


########################
#Leitura da base no diretório local (Jupyter)
########################
df = pd.read_csv('./bases/datatran2018.csv', sep=';', encoding='latin-1') # Carrega a base

########################
#Leitura da base no Google Drive (Colaboratory)
########################
# from google.colab import drive
# drive.mount('/drive') #monta a base no google drive
# database_path = '/drive/Shareddrives/BasesPublicas/Bases/PRF/datatran2018.csv' #caminho da base de dados
# df = pd.read_csv(database_path, sep=';', encoding='latin-1') #Carrega a base


# In[5]:


df.head() #Observa as primeiras linhas da base


# **Item 01**  
# - Qual é o estado que mais teve o manior número de acidentes?

# In[11]:


estados = df['uf'].value_counts()
estados[ estados == estados.max() ]


# **Item 02**  
# - Apresente a quantidade de acidentes por dia da semana.

# In[12]:


df['dia_semana'].value_counts()


# **Item 03**  
# - Apresente a quantidade de acidentes por estado.

# In[14]:


df['uf'].value_counts()


# **Item 04**  
# - De acordo com a quantidade de acidentes, quais são as 5 rodovias mais perigosas?

# In[18]:


df['br'].value_counts().head(5)


# **Item 05**  
# - Considerando apenas acidentes com vítimas fatais, qual rodovia é a mais perigosa?

# In[24]:


df_tmp = df[df['mortos']>0]
df_tmp['br'].value_counts().head(1)


# In[ ]:





# In[ ]:





# **Item 06**  
# - No Paraná, quais são as 10 cidades do interior que possuiram o maior número de acidentes?

# In[29]:


df_tmp = df[df['uf']=='PR']
df_tmp = df_tmp[df_tmp['municipio']!= 'CURITIBA']
df_tmp['municipio'].value_counts().head(10)


# **Item 07**  
# - Os acidentes com vítimas fatais ocorrem em sua maioria em trechos de curvas ou de reta? Apresente um gráfico indicando estes números.

# In[33]:


df_tmp = df[df['mortos']>0]
df_tmp['tracado_via'].value_counts()


# **Item 08**  
# - Quais são as 10 maiores causas de acidentes?

# In[36]:


df['causa_acidente'].value_counts().head(10)


# **Item 09**  
# - Em que estado ocorre o maior núemro de acidentes em que a causa foi animais na pista?

# In[84]:


df_tmp = df[df['causa_acidente']=='Animais na Pista']
df_tmp['uf'].value_counts()


# **Item 10**  
# - Em Cascavel, no Paraná, qual são as rodovias que existem na base de dados?

# **Item 11**  
# - Em Cascavel, no Paraná, qual é a rodovia que mais possui acidentes?

# In[38]:


df_tmp = df[df['uf'] == 'PR']
df_tmp = df_tmp[df_tmp['municipio'] == 'CASCAVEL']
df_tmp['br'].value_counts()


# In[43]:


df_tmp = df[df['uf'] == 'PR']
df_tmp = df_tmp[df_tmp['municipio'] == 'CASCAVEL']
rodo = df_tmp['br'].value_counts().head(1).index[0]
print(rodo)


# **Item 12**  
# - Em Cascavel, no Paraná, em qual kilômetro da rodovia BR 277 ocorreram o maior número de acidentes com vítimas fatais? Obs: por padrão a coluna `br` está com valores do tipo `float`. (`277.0`).

# In[45]:


df_tmp = df[df['uf'] == 'PR']
df_tmp = df_tmp[df_tmp['municipio'] == 'CASCAVEL']
df_tmp = df_tmp[df_tmp['br']==277.0]
df_tmp['km'].value_counts()


# **Item 13**  
# - Gere um gráfico apresentando os dias da semana em que ocorreram mais acidente por causa de Ingestão de Álcool.
# - Comente sobre o resultado obtido

# In[75]:


df_tmp = df[df['causa_acidente'] == 'Ingestão de Álcool']
df_tmp['dia_semana'].value_counts().plot.bar()


# **Item 14**  
# - Apresente um gráfico que mostre a quantidade de acidentes de acordo com a condição meteorológica, subdividida de acordo com a fase do dia.
# - Explique o resultado obtido.

# In[82]:


plt.figure(figsize=(10,5))
sns.countplot(x='condicao_metereologica', hue='fase_dia', data=df)
plt.show()


# **Item 15**  
# - Faça uma análise utilizando algum critério próprio e explique o resultado obtido.

# In[ ]:




