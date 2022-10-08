#!/usr/bin/env python
# coding: utf-8

# # Operações sobre *arrays*

# In[ ]:





# *Array* exemplo
# ```py
# x = np.array([ [1, 2],[3, 4] ])  
# y = np.array([ [5, 6],[7, 8] ])  
# print('x:',x)
# print('y:',y)
# ```

# In[ ]:





# Operações básicas podem ser realizadas sobre o array  
# 
# - adição (+)
# - subtração (-)
# - multiplicação (\*)
# - divisão (/)
# 
# **Exemplo**
# 
# ```py
# x+y
# x-y
# x*y
# x/y
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# A biblioteca numpy também possui outras operações  
# 
# ```py
# np.add  
# np.subtract  
# np.multiply  
# np.divide  
# np.sqrt  
# ```
# 
# **Exemplo**
# 
# ```py
# np.add(x,4)
# np.subtract(x,2)
# np.multiply(x,5)
# np.divide(x,2)
# np.sqrt(x)
# 
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Possui também operações sobre os valores em arrays  
# ```py
# np.sum  
# np.mean  
# np.min  
# np.max  
# ...
# ```
# **Exemplo**
# 
# ```py
# x.sum()
# x.mean()
# x.min()
# x.max()
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Atividade**
# 
# Realize as seguinte operações:
# ```py
# a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])  
# b = np.array([0, 2, 0, 1])  
# a[np.arange(4), b] += 10
# ```
# 
# Observe:
# - Quais são os conteúdos dos *arrays* `a` e `b` após a criação deles?
# - Qual é o resultado da expressão `np.arange(4)`?
# - Ao final, qual é o conteúdo do *array* `a`?
# - Quais posições de `a` foram alteradas?
#     - Por que apenas essas posições foram alteradas?
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Índices booleanos
# 
# Numpy possibilita que sejam aplicadas operações a todos os elementos. Para operadores relacionais, é retornado um array booleano.

# **Atividade**
# 
# Execute:  
# ```py
# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])  
# idx = a > 6
# ```
# 
# Observe o conteúdo:  
# - do array `a`
# - do array `idx`

# In[ ]:





# In[ ]:





# In[ ]:





# Execute:
# ```py
# a[idx]
# ```
# 
# Observe o resultado.

# In[ ]:





# Execute:  
# ```py
# a[idx] += 100
# ```
# 
# Observe o resultado. O que aconteceu?

# In[ ]:





# **Atividade**
# 
# - Qual é a soma dos números com valor maior que $8$ no array `a`?

# In[ ]:





# Qual é a soma dos valores menores que $10$ no array `a`?

# In[ ]:





# ## Where
# 
# Utilizando a função `where()`, é possível descobrir quais posições do *array* correspondem a determinada condição.
# 
# **Exemplo**
# 
# Extrair valores maiores que 15:
# ```py
# arr = np.arange(10,20)
# np.where(arr > 15)
# ```
# 
# Extrair valores pares:
# 
# ```py
# arr = np.arange(10,20)
# np.where(arr % 2 == 0)
# ```

# In[ ]:





# In[ ]:





# **Atividade**
# 
# Obtenha a posição do vetor que possui o maior valor.
# 
# 

# In[ ]:




