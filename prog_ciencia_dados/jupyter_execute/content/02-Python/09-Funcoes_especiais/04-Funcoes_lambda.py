#!/usr/bin/env python
# coding: utf-8

# # Map e funções lambda

# ## Map

# Considere as seguintes funções, que correspondem ao quadrado e à enésima potência:
# 
# ```python
# def quad(x):
#     return x**2
# 
# def pot(x,n):
#     return x**n
# ```
# 
# 

# In[ ]:





# Para aplicar a função a todos os valores de uma lista:
# ```python
# valores = [4,5,6,7,8]
# quadrados = []
# for i in range(len(valores)):
#     quadrados.append(quad(valores[i]))
# print(quadrados)
# ```

# In[ ]:





# In[ ]:





# A função `map()` aplica uma função a todos os elementos de um iterável.
# 
# ```python
# valores = [4,5,6,7,8]
# for i in map(quad,valores):
#     print(i)
# ```

# In[ ]:





# Com a função `map()` é possível aplicar a todos os elementos de uma única vez.
# ```python
# quadrados = list(map(quad, valores))
# print(quadrados)
# ```

# In[ ]:





# De maneira similar, é possível aplicar a diversos iteráveis:
# 
# ```python
# valores   = [4,5,6,7,8,9]
# potencias = [1,2,3,2,1,0]
# resultados = list(map(pot, valores, potencias))
# print(resultados)
# ```

# In[ ]:





# Observe que os valores foram passados igualmente como parâmetro para a função `pot()`.

# ## Funções lambda
# 
# Uma função `lambda` consiste na especificação e utilização de código sem a necessidade de declará-lo explicitamente como função.
# 
# **Exemplo**
# - Considere a função que eleva valores ao quadrado:
# ```python
# valores   = [4,5,6,7,8,9]
# quadrados = list(map(quad, valores))
# print(quadrados)
# ```

# In[ ]:





# Como `quad()` é uma função curta, ela também poderia ser escrita como uma função `lambda`:
# 
# ```python
# pot_2 = lambda x: x**2
# valores   = [4,5,6,7,8,9]
# quadrados = list(map(pot_2, valores))
# print(quadrados)
# ```

# In[ ]:





# Como a função é curta, pode ser passada diretamente no parâmetro da função `map()`. Este é o uso mais comum das funções `lambda`.
# 
# ```python
# valores   = [4,5,6,7,8,9]
# quadrados = list(map(lambda x: x**2, valores))
# print(quadrados)
# ```

# In[ ]:





# Observe que todo o código da função a ser executado pelo `map` é passado diretamente via parâmetro.
# 
# **Sintaxe**  
# ```python
# lambda parâmetros : expressão
# ```

# In[ ]:





# Um outro uso comum das funções `lambda` é na ordenação de elementos.
# 
# **Exemplo**  
# - Ordene a seguinte lista de tuplas pelo segundo elemento presente em cada tupla:
# ```python
# valores = [(10,2,10), (1,5,1), (1,2,3), (3,0,50), (2,50,3), (20,20,20), (0,50,8)]
# ```

# In[ ]:





# É possível utilizar a função `sorted()` passando uma função para o parâmetro `key`:
# 
# ```python
# def pos_1(x):
#     return x[1]
# ordenados = sorted(valores, key=pos_1)
# print(ordenados)
# ```

# In[ ]:





# Utilizando `lambda`:
# ```python
# ordenados = sorted(valores, key=lambda x: x[1])
# print(ordenados)
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# ```python
# ordenados = sorted(valores, key=lambda x: x[1])
# print(ordenados)
# ```

# In[ ]:





# Colocando o primeiro elemento da tupla como segundo critério da ordenação:
# ```python
# ordenados = sorted(valores, key=lambda x: (x[1], x[0]))
# print(ordenados)
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




