#!/usr/bin/env python
# coding: utf-8

# ## Enumerate e Zip
# 

# ## Enumerate
# 
# Considere a seguinte lista `vogais`:
# 
# ```python
# vogais = ['a','e','i','o','u']
# ```

# In[ ]:





# - Para percorrer a lista a partir de seu índice, é necessário gerar os índices e então, a partir do índice acessar a lista na referida posição.
# ```python
# for i in range(len(vogais)): #Gera a lista de índices
#     v = vogais[i]            #Acessa a lista no índice
#     print(f'vogais[{i}] = {v}')
# ```

# In[ ]:





# A função `enumerate()` retorna uma tupla contendo o índice e o valor de uma estrutura iterável.
# 
# **Exemplo**  
# ```python
# for i,v in enumerate(vogais):
#     print(f'vogais[{i}] = {v}')
# ```

# In[ ]:





# In[ ]:





# ## Zip
# 
# Considere duas listas referentes a nomes e idades, onde cada posição é referente a uma mesma pessoa.
# ```python
# nomes  = ['Celso', 'Sergio', 'João', 'Eriberto']
# idades = [30, 12, 28, 25]
# ```

# In[ ]:





# **Exemplo**  
# - Para obter os nomes e idades das pessoas:
# ```python
# for i in range(len(nomes)):
#     nome = nomes[i]
#     idade = idades[i]
#     print(f'{nome} tem {idade} anos')
# ```

# In[ ]:





# A função `zip()` possibilita que duas listas sejam percorridas simultaneamente.
# ```python
# for nome, idade in zip(nomes, idades):
#     print(f'{nome} tem {idade} anos')
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




