#!/usr/bin/env python
# coding: utf-8

# # Comprehensions

# As *comprehensions* em Python consistem em uma forma simplificada de construir novas estruturas, sejam elas listas, dicionários ou conjuntos.

# ## List comprehension
# Considere a criação da seguinte lista:
# 
# ```python
# lista = []
# for i in range(20):
#     lista.append(i)
# ```

# In[ ]:





# Utilizando *list comprehensions*, este mesmo código poderia ser escrito da seguinte forma:
# 
# ```python
# lista = [i for i in range(20)]
# ```

# In[16]:





# **Sintaxe**  
# 
# ```python
# lista = [ expressão for item in iterable ]
# ```
# 
# ou 
# 
# ```python
# lista = [ expressão for item in iterable if condição ]
# ```

# **Exemplo**  
# - Gerar valores ao quadrado
# 
# ```python
# quadrado = [ x**2 for x in range(20)]
# ```

# In[18]:





# **Exemplo**  
# - Gerar valores ao quadrado apenas de números pares
# ```python
# quadrado_pares = [ x**2 for x in range(20) if x%2 == 0]
# ```

# In[ ]:





# ## Dictionary comprehension
# 
# De maneira semelhantes às *lists comprehensions*, pode-se também criar dicionários utilizando *dictionary comprehensions*.  
# 
# **Sintaxe**  
# 
# ```python
# dicionario = { key:value for (key, value) in iterable }
# ```
# 
# ou  
# 
# ```python
# dicionario = { key:value for (key, value) in iterable if condicao }
# ```
# 
# **Exemplo**  
# - Valores ao quadrado
# ```python
# dict_quadrado = {val:val**2 for val in range(10)}
# ```

# In[ ]:





# In[ ]:





# ## Generator comprehension
# 
# Um *Generator comprehension* é semelhante à uma *list compreension*. Sua diferença consistem em que os dados não são gerados previamente, e sim *on the fly*.
# 
# **Sintaxe**  
# 
# ```python
# gerador = (i for i in range(20))
# ```
# 
# Observe:  
# ```python
# print(gerador)
# print(type(gerador))
# ```

# In[ ]:





# Para percorrê-lo:
# 
# ```python
# for val in gerador:
#     print(val)
# ```

# In[ ]:





# Ou então:
# (Para executar este exemplo, um novo *generator* deve ser criado).
# ```python
# try:
#     print(next(gerador))
# except:
#     print('Gerador finalizado')
# ```

# In[ ]:




