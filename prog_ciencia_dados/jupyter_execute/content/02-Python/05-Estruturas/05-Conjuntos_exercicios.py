#!/usr/bin/env python
# coding: utf-8

# # Exercícios
# Resolva os exercícios abaixo utilizando a linguagem de programação Python, conjuntamente com a estrutura de dados de conjuntos (`set`).

# **Exercício**

# Considerando os conjuntos $A$, $B$, $C$ e $D$ definidos abaixo, mostre quais destes conjuntos são iguais.
# 
# $$
# A = \{a, b, −1\} \\
# B = \{b, a, −1\} \\
# C = \{b, a, b, −1\} \\
# D = \{a, −1\}
# $$
# 
# Fonte: Exercício adaptado de [BRAVO, R.](http://www.ic.uff.br/~ueverton/files/aulasFMC/Gabarito%20-%20CONJUNTOS.pdf).

# **Exercício**

# Dados os conjuntos  
# 
# $$
# A=\{0,1\} \\
# B=\{0,1,2\} \\
# C=\{2,3\} \\
# $$
# 
# Obtenha o seguinte conjunto $R$:  
# 
# $$
# R = (A\cup B) \cap (B \cup C)
# $$

# In[ ]:





# Sejam  
# 
# $$
# U = \{0, 1, 2, 3, 4\} \\
# A = \{0, 4\} \\
# B = \{0, 1, 2, 3\} \\
# C = \{1, 4\} \\
# D = \{0, 1\} \\
# $$
# 
# Determine os seguintes conjuntos:  
# 
# $$
# F= A \cup B \\
# G= B \cap C \\
# H= A \cap B \\
# I= A \cup (B \cap C) \\
# J= (A \cup B) \cap (A \cup C) \\
# K= A \cup (B \cap C \cap D)
# $$
# 
# 
# Fonte: Exercício adaptado de [BRAVO, R.](http://www.ic.uff.br/~ueverton/files/aulasFMC/Gabarito%20-%20CONJUNTOS.pdf).

# In[ ]:





# **Exercício**

# Dados os conjuntos  
# 
# $$
# A=\{ 0, 1, 2, 3, 4, 5 \}\\
# B=\{ 4, 5, 6, 7 \}\\
# C=\{ 4, 5, 6, 8 \}
# $$
# 
# Obtenha $R$, tal que:  
# 
# $$
# R = (A -C) \cap ( B - C )
# $$
# 

# In[ ]:





# **Exercício**

# Dados os conjuntos  
# 
# $$
# C = \{15,25,30,35\}\\
# D = \{15, 25,40,50\}
# $$
# 
# obtenha $F$, tal que:  
# 
# $$
# F = C \cup D
# $$

# In[ ]:





# **Exercício**

# Considerando os conjuntos abaixos, definidos sobre os intervalos nos números inteiros:
# 
# $$
# A = ]-2,3]\\
# B = [0,6]
# $$
# 
# quais são os elementos de $B-A$?

# In[ ]:





# **Exercício**

# Faça uma função chamada `countar_unicos`, que possui como entrada uma lista de qualquer tipo de elemento básico (`float`, `int`, ou `bool`). A função deve retornar duas listas, uma contendo os elementos da entrada sem repetir elementos, e outra lista contendo a quantidade de vezes que cada elemento aparece na lista de entrada. Não é necessário que a lista de elementos na saída esteja ordenada.
# 
# **Exemplo**
# 
# - Entrada
# ```
# [4, 5, 2, 5, 1, 2, 9, 9, 1, 2, 4, 4, 4, 0, 1]
# ```
# - Saída
# ```
# [0, 1, 2, 4, 5, 9]  
# [1, 3, 3, 4, 2, 2]
# ```

# In[ ]:





# **Exercício**

# Responda às seguintes perguntas:
# - Se em uma sala há 23 pessoas, qual é a probabilidade de duas pessoas fazerem aniversário no mesmo dia?
# - Aproximadamente, qual a quantidade mínima de elementos que deve possuir um conjunto de pessoas para que a probabilidade de existir pelo menos duas que façam aniversário no mesmo dia seja de 70%?
#     
# Gere um conjunto de datas de nascimento aleatoriamente, e faça a verificação. Utilize a função `contar_unicos` desenvolvida em exercício anterior. Calcule as probabilidades utilizando pelo menos 10000 testes.
# 
# >**Informações**
# >
# > Este exercício é baseado no [paradoxo do aniversário](https://en.wikipedia.org/wiki/Birthday_problem).

# In[ ]:





# ## Referências
# 
# [Birthday problem. Wikipedia](https://en.wikipedia.org/wiki/Birthday_problem)  
# [BRAVO, R. Notas de aula da disciplina Fundamentos Matemáticos para Computação, do curso de Sistemas de Informação. Universidade Federal Fluminense](http://www.ic.uff.br/~ueverton/files/aulasFMC/Gabarito%20-%20CONJUNTOS.pdf).
# 
# **Outros materiais**
# 

#  
