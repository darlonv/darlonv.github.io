#!/usr/bin/env python
# coding: utf-8

# # Recursividade

# Diz-se que uma função que aplica a recursividade é uma **função recursiva**. A principal característica de uma função recursiva é que ela chama a si própria durante sua execução.

# **Exemplo**
# 
# Considere a função abaixo, que apresenta números em ordem crescente:
# 
# ```python
# def contar(n):
#     for i in range(n):
#         print(i)
# contar(5)
# ```
# 
# 

# In[ ]:





# É possível implementar essa mesma função de maneira recursiva:
# 
# **Exemplo**
# 
# ```python
# def contarRec(n, i=0):
#     if i<n:
#         print(i)
#         contarRec(n,i+1)
# contarRec(5)
# ```

# In[ ]:





# Observe na função recursiva que *não existe* propriamente uma estrutura de repetição, como na função apresentada anteriormente.

# ## Critério de parada
# Uma das características da recursividade é a presença de um **critério de parada**, que controla quando a função deve parar. Sem esse recurso, a função continua sua execução indefinidamente. No exemplo do contador, a estrutura `if` define que a recursividade deve ocorrer apenas enquanto `i<n`.

# ### Iterações
# Normalmente, uma função recursiva equivale a uma estrutura de repetição, onde as cada chamada à função corresponde a uma iteração da estrutura de repetição.  
# 
# O uso de estruturas de recursão é limitado devido à pilha de chamadas de função. A pilha de chamadas é uma estrutura do sistema operacional que controla as chamadas às funções, e a cada chamada de função um elemento da pilha é adicionado.
# 
# A região de memória em que se encontra a pilha é limitada, e ao requisitar mais memória que o possível, a estrutura entra em um estado de erro. A este tipo de erro dá-se o nome de **estouro de pilha**.
# 

# **Exemplo**
# 
# Considere as duas funções abaixo, sem e com recursividade. Ambas realizam a soma da sequência de valores de 1 a $n$.
# 
# ```python
# #Função sem uso de recursão
# def soma(n):
#     s=0
#     for i in range(n+1):
#         s+=i
#     print('Soma:', s)
# ```
# 
# ```python
# #Função com uso de recursão
# def somaRec(n,i=0,s=0):
#     if i<=n:
#         somaRec(n,i+1,s+i)
#     else:
#         print('SomaRec:',s)
# ```
# 
# Execute as funções, passando para $n$ os valores abaixo, observando os valores máximos que cada função suporta.
# - 5
# - $10^2$(cem)
# - $10^3$ (mil)
# - $10^5$ (dez mil)
# - $10^6$ (1 milhão)
# - $10^9$ (1 bilhão)
# 
# 
# ```python
# x = 5
# print('x:', x)
# soma(x)
# somaRec(x)
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Atividades**
# 
# - Implemente uma função que calcula a potência de um número. $y = b^e$, onde $b$ e $e$ correspondem à base e ao expoente, respectivamente. Utilize recursividade.
# - Implemente a soma dos valores da sequência de 1 a $n$, utilizando apenas duas variáveis como parâmetro. Implemente utilizando recursividade.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




