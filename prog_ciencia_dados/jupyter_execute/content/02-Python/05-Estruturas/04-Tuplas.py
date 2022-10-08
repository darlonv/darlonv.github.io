#!/usr/bin/env python
# coding: utf-8

# # Tuplas
# 
# Uma tupla é uma estrutura especial de lista, e uma de suas características é ser imutável. Após adicionados os elementos em uma tupla, seus elementos não podem ser removidos. Uma tupla é definida pelo uso de parênteses (`(` `)`) em seus elementos.
# 
# **Exemplo**
# 
# ```py
# t = (1,2,3)
# type(t)
# ```

# In[ ]:





# Alterar um elemento de uma tupla acarreta em um erro.  
# 
# **Exemplo**
# 
# no código
# ```python
# t[0] = 5 #ERRO!
# ```
# recebemos a mensagem de erro mostrada abaixo, informando que não é possível alterar o conteúdo de um elemento de uma tupla.
# ```
# TypeError: 'tuple' object does not support item assignment
# ```

# In[ ]:





# **Atividade**
# 
# - crie uma tupla com as vogais
# - crie uma tupla com as consoantes
# - crie uma tupla com os números primos menores que 30

# In[ ]:





# Normalmente, as tuplas são utilizadas como parâmetros ou retornos de funções. Uma das vantagens da utilização de tuplas consiste no menor tempo de criação e acesso a dados, se comparado às listas.

# É possível transformar tuplas em listas e listas em tuplas, com as funções `list()` e `tuple()`, caso a modificação seja necessária.
# 
# **Exemplo**
# 
# ```python
# tupla  = (1,2,3)      #tupla
# lista  = list(tupla)  #converte tupla em lista
# tupla2 = tuple(lista) #converte lista em tupla
# print(tupla,'tipo:',type(tupla))
# print(lista,'tipo:', type(lista))
# print(tupla2,'tipo:',type(tupla2))
# ```

# In[ ]:





# ## Referências
# 
# **Outros materiais**
# 
# 
# [Python - Built-in types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)  
# [Python - Operadores e fatiamento de sequências](http://www.devfuria.com.br/python/sequencias-fatiamento/)  
# [Apostila Python e orientação a objetos - Capítulo 4: Estrutura de dados ](https://www.caelum.com.br/apostila-python-orientacao-objetos/estrutura-de-dados/)
