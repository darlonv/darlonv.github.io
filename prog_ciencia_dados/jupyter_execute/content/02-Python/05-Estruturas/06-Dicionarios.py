#!/usr/bin/env python
# coding: utf-8

# # Dicionários
# 
# Os dicionários são estruturas de dados em que os dados são agrupados sem uma ordem definida. Os elementos armazenados em dicionários têm sua posição associada a uma chave. 
# 
# Para criar um dicionário pode-se utilizar as chaves (`{` `}`) ou a função `dict()`.  
# 
# **Exemplo**  
# 
# ```py
# dpr = {'nome': 'Paraná', 'sigla':'PR', 'gentilico':'Paranaense'}
# print(type(dpr))
# ```
# 
# **Atividade**
# - Execute o exemplo.

# In[ ]:





# Para ver todos os elementos, com chaves e valores:  
# 
# **Exemplo**
# 
# ```py
# print(dpr)
# ```

# In[ ]:





# É possível acessar os elementos de um dicionário utilizando sua chave como posição.  
# 
# **Exemplo**
# 
# ```py
# print(dpr['sigla'])
# ```

# In[ ]:





# Resulta em um erro acessar os elementos pela posição numérica, como é feito como as listas.
# 
# **Exemplo**
# 
# ```py
# print(dpr[0])
# KeyError: 0
# ```
# 

# In[ ]:





# Para adicionar um novo item, basta apenas informar a nova chave.
# ```py
# dpr['regiao'] = 'sul'
# print(dpr)
# ```

# In[ ]:





# Para alterar um valor, é possível substituir um elemento na posição.  
# 
# **Exemplo**
# 
# ```py
# dpr['regiao'] = 'Sul'
# print(dpr)
# ```

# In[ ]:





# Os valores podem ser de qualquer tipo.  
# 
# **Exemplo**  
# 
# ```py
# dpr['numMunicipios'] = 399
# print(dpr)
# ```

# In[ ]:





# O método `.values()` retorna apenas os valores presentes no dicionário.  
# 
# **Exemplo**
# 
# ```py
# print(dpr.values())
# ```

# In[ ]:





# O método `.keys()` retorna todas as chaves do dicionário.  
# 
# **Exemplo**
# 
# ```py
# print(dpr.keys())
# ```

# In[ ]:





# E cada par pode ser acessado pelo método `.items()`.  
# 
# **Exemplo**
# 
# ```py
# print(dpr.items())
# ```

# In[ ]:





# O índice em um dicionário pode ser de diferentes tipos.
# ```py
# dicNum = {9:'nove', True:'verdadeiro', 5.6:'cinco ponto seis'}
# print(dicNum)
# print(dicNum[9])
# print(dicNum[True])
# print(dicNum[5.6])
# ```

# In[ ]:





# Desta forma, também pode-se utilizar o dicionário como um vetor esparso.  
# 
# **Exemplo**  
# 
# ```py
# dicVetEsparso = {0:'zero', 5: 'cinco', 34:'trinta e quatro'}
# ```
# Com isso, pode-se utilizar o dicionário do exemplo como um *array* que possui apenas as posições 0, 5 e 34.
# 
# **Atividade**
# - Execute o exemplo.

# In[ ]:





# Um dicionário é uma estrutura *iterável*, assim como as sequências. Porém ao utilizá-lo em uma estrutura **for**, cada iteração receberá a **chave** (índice) das estruturas nele armazenadas.  
# 
# **Exemplo**  
# 
# ```py
# for i in dpr:
#     print(i)
# ```

# In[ ]:





# Para que seja obtido o valor associado à chave, pode-se usar a variável iteradora como índice na estrutura.  
# 
# **Exemplo**  
# 
# ```py
# for i in dpr:
#     print(dpr[i])
# ```

# In[ ]:





# Outra forma é iterar sobre os valores, obtendo-os pelo método `.values()`.  
# 
# **Exemplo**  
# 
# ```py
# for i in dpr.values():
#     print(i)
# ```

# In[ ]:





# Ou então iterar sobre cada **item** armazenado, obtendo-os pelo método `.items()`.  
# 
# **Exemplo**
# 
# ```py
# for i in dpr.items():
#     print(i)
# ```

# In[ ]:





# In[ ]:





# Observe que o tipo de cada item é uma tupla.  
# 
# **Exemplo**
# 
# ```py
# for i in dpr.items():
#     print(type(i))
# ```
# 

# In[ ]:





# Desta forma, podemos acessar cada item também da seguinte maneira  
# 
# **Exemplo**
# 
# ```py
# for i in dpr.items():
#     print('chave:',i[0],'valor:',i[1])
# ```

# In[ ]:





# In[ ]:





# **Operações**
# 
# - `in`: verifica se a chave existe no dicionário;  
# - `not in`: verifica se a chave não existe no dicionário;  
# 
# **Funções**
# - `len()` obtém a quantidade de elementos;  
# - `del()` remove um dicionário, ou apenas o elemento na chave especificada por parâmetro.

# In[ ]:





# ## Métodos
# 
# Alguns métodos das estruturas de dicionário são apresentados na tabela a seguir.
# 
# |método         |descrição|
# |---------------|:--------|
# |`.get()`       |retorna o valor na chave especificada|
# |`.pop()`       |remove o elemento na chave especificada|
# |`.fromkeys()`  |retorna um dicionário, com as chaves e valores especificados|
# |`.items()`     |retorna uma lista contendo tuplas para cada par (chave,valor)|
# |`.keys()`      |retorna uma lista com as chaves da estrutura|
# |`.popitem()`   |remove o último par (chave,valor) inserido|
# |`.values()`    |retorna uma lista com os valores armazenados|
# |`.copy()`      |retorna uma cópia da estrutura|
# |`.clear()`     |remove todos os elementos|
# 
# **Exemplo**
# 
# ```python
# dados = {'Peso': 75.2, 'Altura':1.68, 'Idade': 26, 'Sexo': 'M'}
# print(f"dados            : {dados}")
# print(f"dados.get('Peso'): {dados.get('Peso')}")
# print(f"dados            : {dados}")
# print(f"dados.pop('Sexo'): {dados.pop('Sexo')}")
# print(f"dados            : {dados}")
# print(f"dados.items()    : {dados.items()}")
# print(f"dados.keys()     : {dados.keys()}")
# print(f"dados.values()   : {dados.values()}")
# dados['Sexo']='F'
# print("dados['Sexo']='F'")
# print(f"dados            : {dados}")
# print(f"dados.popitem()  : {dados.popitem()}")
# print(f"'Idade' in dados : {'Idade' in dados}")
# print(f"'Nasc' in dados  : {'Nasc' in dados}")
# ```
# 
# **Atividade**
# - Execute o exemplo, e observe o que ocorre em cada linha.

# In[ ]:





# **Exemplo**
# ```python
# print('== Com referência ==')
# dados = {'Peso': 75.2, 'Altura':1.68, 'Idade': 26, 'Sexo': 'M'}
# dados2 = dados #é uma referência, e não uma cópia
# dados2['Altura'] = 1.81 #a estrutura original também é alterada
# print('original :', dados ['Altura']) #O mesmo valor em ambas é retornado
# print('nova     :',dados2['Altura'])
# 
# print('== Com cópia ==')
# dados = {'Peso': 75.2, 'Altura':1.68, 'Idade': 26, 'Sexo': 'M'}
# dados2 = dados.copy() #é uma cópia
# dados2['Altura'] = 1.81 #a estrutura original não é alterada
# print('original :', dados ['Altura']) #valor original é mantido
# print('nova     :',dados2['Altura'])  #valores diferentes são retornados
# ``` 
# 
# **Atividade**
# - Execute o exemplo, e observe os códigos em cada linhas e as saídas.

# In[ ]:





# In[ ]:





# **Exercícios**  
# Resolva os exercícios a seguir utilizando **Dicionários**:
# - [Beecrowd 2482 - Etiquetas de Noel](https://www.beecrowd.com.br/judge/pt/problems/view/2482) 
# - [Beecrowd 1049 - Animais](https://www.beecrowd.com.br/judge/pt/problems/view/1049)
# - [Beecrowd 1050 - DDD](https://www.beecrowd.com.br/judge/pt/problems/view/1050)

# In[ ]:




