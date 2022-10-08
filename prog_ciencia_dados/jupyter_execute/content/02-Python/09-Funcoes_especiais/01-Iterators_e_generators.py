#!/usr/bin/env python
# coding: utf-8

# # Iterators e generators

# Os *iterators* e *generators* são objetos em Python utilizados para percorrer elementos de determinadas estruturas.

# ## Iterators

# Um *iterator* em Python é um objeto que responde à função `next()`. Um exemplo de iterável são as listas.
# 
# **Exemplo**  
# 
# ```python
# lista = [5,6,7]
# dir(lista) #Visualiza os métodos
# ```
# 
# Um *iterator* 

# In[ ]:





# Observe que o método `__iter__` está presente.  
# 
# Vamos observar o retorno desse método:  
# 
# ```python
# val = iter(lista)
# print(type(val))
# ```
# 

# In[ ]:





# Para obter o *iterator*
# ```python
# iterador = iter(lista)
# ```

# In[ ]:





# E para percorrer o iterador:
# 
# ```python
# val = next(iterador)
# print(val)
# ```
# Execute este código diversas vezes, e observe o resultado.

# In[ ]:





# Quando um *iterator* é finalizado, ele gera uma exceção. Observe o código a seguir, que gera um erro ao final da execução:
# 
# ```python
# iterador = iter(lista)
# while True:
#     print(next(iterador))
# ```

# In[ ]:





# Para obter a excessão:
# 
# ```python
# iterador = iter(lista)
# fim = False
# while not fim:
#     try:
#         print(next(iterador))
#     except:
#         fim = True
# ```

# In[ ]:





# Utilizando `for`:
# 
# ```python
# iterador = iter(lista)
# for val in iterador:
#     print(val)
# ```

# In[ ]:





# In[ ]:





# ## Generators

# Um *generator* é semelhante a um *iterator*, porém o próximo valor é calculado apenas quando o método `next()` é chamado.
# 
# **Exemplo**  
# - O que é retornado nesta função?
# ```python
# def sequencia():
#     for i in 1,2,3,4,5:
#         return i
# ```

# In[ ]:





# Chame a função diversas vezes e observe o resultado:
# ```python
# sequencia()
# ```

# In[ ]:





# Um *generator* utiliza como retorno a palavra-chave `yield`. Modificando o exemplo anterior, temos:
# 
# ```python
# def sequencia_gen():
#     for i in 1,2,3,4,5:
#         yield i
# ```

# In[ ]:





# Observando o tipo retornado pela nova função:
# ```python
# gerador = sequencia_gen()
# print(type(gerador))
# ```

# In[ ]:





# Um *generator* obtém o estado em que a função anterior foi chamada. Semelhante ao *iterator*, podemos percorrê-lo com `next()`..
# 
# ```python
# gerador = sequencia_gen()
# fim = False
# while not fim:
#     try:
#         print(next(gerador))
#     except:
#         fim = True
# ```

# In[ ]:





# 

# ... ou utilizando `for`:
# 
# ```python
# gerador = sequencia_gen()
# for val in gerador:
#     print(val)
# ```

# In[ ]:





# In[ ]:





# In[ ]:




