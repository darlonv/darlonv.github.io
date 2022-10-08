#!/usr/bin/env python
# coding: utf-8

# # T1-2

# Responda às questões abaixo, utilizando a linguagem de programação Python. Utilize apenas estruturas e operações trabalhadas nas atividades de aula.
# 
# Entre as atividades código executado, de maneira que seja possível visualizar as entradas utilizadas e as saídas geradas pelo seu código.

# ## Item 1
# 
# Desenvolva uma aplicação que pergunta `n` valores inteiros ao usuário. Após a entrada dos dados, a aplicação deve informar se os dados estão ordenados de maneira crescente, ordenados de maneira decrescente ou desordenados. Caso haja dois valores iguais em sequência, os valores são considerados como ordenados.

# Nos exemplos apresentados abaixo, o primeiro valor corresponde ao número `n`, que indica a quantidade de valores que serão digitados.  
# 
# **Exemplo**  
# - Entrada:
# ```
# 10
# 1
# 3
# 5
# 7
# 9
# 10
# 13
# 15
# 17
# 19
# ```
# - Saída:
# ```
# Os valores estão ordenados numericamente de maneira crescente.
# ```
# 
# **Exemplo**  
# - Entrada:
# ```
# 5
# 9
# 8
# 7
# 3
# 2
# ```
# - Saída:
# ```
# Os valores estão ordenados numericamente de maneira decrescente.
# ```
# 
# **Exemplo**  
# - Entrada:
# ```
# 7
# 1
# 2
# 3
# 4
# 2
# 6
# 7
# ```
# - Saída:
# ```
# Os valores estão desordenados numericamente.
# ```
# 
# **Exemplo**  
# - Entrada:
# ```
# 4
# 1
# 3
# 3
# 5
# ```
# - Saída:
# ```
# Os valores estão ordenados numericamente de maneira crescente.
# ```

# In[ ]:





# ## Item 2
# Pergunte ao usuário dois números inteiros, $x$ e $y$, e mostre todos os números perfeitos no intervalo $[x,y]$.  
# Um número `n` é dito perfeito, se `n` for inteiro, positivo, e se $n$ for igual à soma de seus divisores positivos e diferentes de $n$. Exemplo: O número $6$ é perfeito, pois $6=3+2+1$.
# 
# **Exemplo**
# - Entrada:
# ```
# 2
# 10
# ```
# - Saída:
# ```
# Os números perfeitos no intervalo [ 2 , 10 ] são:
# 6
# ```
# 
# **Exemplo**
# - Entrada:
# ```
# 8
# 20
# ```
# - Saída:
# ```
# Os números perfeitos no intervalo [ 8 , 20 ] são:
# não há números perfeitos no intervalo.
# ```

# In[ ]:





# ## Item 3
# 
# Faça um programa que pergunte $n$ ao usuário, tal que $n$ corresponde ao número de linhas, que devem ser impressas de acordo com o padrão mostrado no exemplo.
# 
# **Dica**:
# Pode ser utilizado parâmetro `end=''` na função `print` para que não seja feita a quebra da linha na saída do `print`. 
# ```
# print(1)
# print(2)
# saída:
# 1
# 2
# print(1,end='')
# print(2)
# saída:
# 12
# ```
# 
# **Exemplo**
# - Entrada:
# ```
# 10
# ```
# - Saída:
# 
# ```
# *
# *-
# *-*
# *-*-
# *-*-*
# *-*-*-
# *-*-*-*
# *-*-*-*-
# *-*-*-*-*
# *-*-*-*-*-
# ```

# In[ ]:




