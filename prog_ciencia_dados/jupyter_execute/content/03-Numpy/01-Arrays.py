#!/usr/bin/env python
# coding: utf-8

# # Numpy
# 
# Numpy é uma biblioteca Python voltada principalmente para cálculos utilizando *arrays* multidimensionais. São fornecidas diversas funções e operações que permitem a realização simplificada de cálculos envolvendo essas estruturas.
# 
# Comumente, a biblioteca não é instalada por padrão. Pode-se realizar a instalação utilizando gerenciadores de pacotes, como o pip, utilizando `pip install numpy`.

# ## Importação
# 
# Para importar a biblioteca, utilize
# ```python
# import numpy as np
# ```
# `np` é o nome dado que utilizaremos para acessar a biblioteca.

# In[ ]:





# ## *Arrays*
# O *array* numpy é uma lista de valores, indexada por uma tupla de inteiros não negativos. O número de dimensões do array é o *rank* do array. O *shape* de um *array* é uma tupla de inteiros, dado o tamanho do *array* em cada dimensão definida.
# 
# **Exemplo**
# 
# Crie um vetor de uma dimensão
# ```python
# a = np.array([1, 2, 3])
# ```

# In[ ]:





# Observe o tipo do dado armazenado em cada posição
# ```python
# print(type(a))
# ```

# In[ ]:





# Observe o formato do vetor
# ```python
# print (a.shape)
# ```

# In[ ]:





# Mostra os elementos em cada posição
# ```python
# print(a[0], a[1], a[2])
# ```

# In[ ]:





# Mostra todo o vetor
# ```python
# print(a)
# ```

# In[ ]:





# Altera valor em uma posição
# ```python
# a[0]=100
# ```

# In[ ]:





# Mostra todo o vetor
# ```python
# print(a)
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Atividade**
# 
# Crie um outro vetor, com o seguinte formato  
# ```python
# b = np.array([[1,2,3], [4,5,6]])
# ```

# In[ ]:





# Compare os formatos vetores `a` e `b`. Qual é a diferença?

# In[ ]:





# In[ ]:





# **Atividade**
# 
# Faça:  
# ```python
# print(b[1])
# print(b[1][1])
# ```
# 
# Explique o quê é mostrado

# In[ ]:





# ## *Reshape*
# É possível alterar o formato do *array*. Execute os código abaixo passo a passo, observando o resultado:
# ```python
# arr = np.arange(10)
# print(arr)
# print(arr.shape)
# arr.reshape(5,2)
# arr.reshape(2,5)
# ```
# **Sintaxe**
# 
# `.reshape(l,c)`  
# onde:
# - `l`: número de linhas
# - `c`: número de colunas
# 
# O valor `l*c` deve corresponder à quantidade total de elementos no *array*.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# É possível definir a ordem do *array* sem conhecer uma de suas dimensões. Para isto, para substituir o número de linhas ou colunas por `-1`.  
# 
# **Exemplo**
# 
# ```python
# arr = np.arange(10)
# ```

# In[ ]:





# ```python
# arr.reshape(5,-1)
# ```

# In[ ]:





# ```python
# arr.reshape(-1,5)
# ```

# In[ ]:





# ```python
# arr.reshape(2,-1)
# ```

# In[ ]:





# ```python
# arr.reshape(-1,2)
# ```

# In[ ]:





# **Atividade**
# 
# Crie um *array* com 100 elementos contendo inteiros em sequência. Em seguida, organize esses valores em 10 colunas.

# In[ ]:





# In[ ]:





# In[ ]:





# ## Tipos de dados
# 
# Observe os tipos de dados armazenados  
# ```python
# print(a.dtype)
# ```

# In[ ]:





# Compare com os tipos de dados destes outros vetores, e observe o que ocorre
# ```python
# x=np.array([1, 2])
# y=np.array([1.0, 2.0])
# z=np.array([1, 2], dtype=np.int64)
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Funções para criação de arrays
# 
# Teste as funções abaixo, e observe o vetor retornado por cada função.
# ```python
# np.zeros((2,2))
# ```

# In[ ]:





# ```python
# np.ones((3,3))
# ```

# In[ ]:





# ```python
# np.full((4,4),9)
# ```

# In[ ]:





# ```python
# np.eye(5)
# ```

# In[ ]:





# ```python
# np.random.random((6,6))
# ```

# In[ ]:





# Outras funções podem ser utilizadas para obter valores igualmente espaçados entre si.
# ```python
# np.linspace(0,10,5)
# np.linspace(0,10,3)
# np.linspace(0,10,11)
# ```
# **Sintaxe**
# 
# ```python
# .linspace(i,f,n)
# ```
# Onde:
# - `i`: valor inicial
# - `f`: valor final
# - `n`: quantidade de valores
# No método `linspace`, os valores de saída são do tipo `float` (`numpy.float64`).
# 
# **Atividade**  
# - Execute os exemplos acima e observe os resultados.

# In[ ]:





# In[ ]:





# In[ ]:





# ## *Slicing*
# 
# Semelhantes às listas em Python, os arrays numpy possibilitam o *slicing*. Como os arrays podem possuir diversas dimensões, é necessário identificar o *slice* para cada dimensão.  
# ```python
# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# b = a[:2, 1:3]
# ```
# 
# Significado:
# ```python
# :2: linhas 0 a 1  
# 1:3: colunas 1 a 2
# ```
# 
# Observe o conteúdo dos vetores `a` e `b`.
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Como seria para mostrar apenas determinadas colunas utilizando *slices*?

# In[ ]:





# Execute os comandos abaixo, e discorra sobre os resultados
# ```python
# b = a[[0,2], 2]  
# c = a[[0,2,2], [0,2,3]]
# ```
# 
# O que ocorreu em `b` e `c`?

# In[ ]:





# ## Alterações em *slices*
# 
# **Atividade**
# 
# - Observe o array `a`
# - Execute:
# ```python
# c = a[:2, 1:3]
# ```
# - Observe o array `c`
# - Execute:
# ```python
# c[0][0]=20
# ```
# - Observe o array a
# 
# O que ocorreu?  

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Atividade**
# 
# O que ocorre com as operações abaixo?
# ```python
# a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# b = np.array(a[0:2, 0:1])
# ```
# 
# Explique o resultado ocorrido.
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




