#!/usr/bin/env python
# coding: utf-8

# # While

# O `while` é uma estrutura de repetição, que consiste em repetir um bloco **enquanto** determinada condição for verdadeira.

# **Exemplo**
# 
# *Enquanto* `x < 5`, mostre `x`.
# ```python
# x=0
# while x<5:
#     print(x)
#     x = x+1
# ```
# **Atividade**
# 
# - Execute o exemplo

# In[ ]:





# **Sintaxe**
# 
# ```python
# while <condição>:
#     <código>
# ```
# onde:
# - `<condição>` corresponde ao teste que será executado **antes** de entrar em cada iteração.
# - `<código>` corresponde ao bloco de código que será executado caso a condição seja verdadeira.

# No `while` não é necessário conhecer todos os valores antes de iniciar a execução, visto que para entrar na bloco da repetição basta apenas que a condição testada tenha resultado verdadeiro.

# **Exemplo**
# 
# *Enquanto* `x < 5`, mostre `x`.
# ```python
# x=0
# while x<5:
#     print(x)
#     x = x+1
# ```
# No `while`, sempre é necessário o controle da condição. Observe:
# - Antes do `while` iniciar, o valor de `x` é definido para $0$.
# - Dentro do bloco existe uma *atualização* do valor testado na condição.

# **Exemplo**
# 
# Observe a situação em que a variável da condição não é atualizada:
# ```python
# x=0
# while x<5:
#     print(x)
# ```
# A estrutura se repetirá indefinidamente, visto o valor de `x` não é modificado e a condição sempre será verdadeira. A saída na tela será uma sequência de zeros infinita.

# **Exercícios**
# 
# 1. Peça ao usuário que digite vários números inteiros positivos, parando quando um número negativo for digitado. Ao final, mostre a soma de todos os números digitados.
# 1. Peça ao usuário que digite vários números inteiros positivos, parando quando um número negativo for digitado. Ao final, mostre a média de todos os números digitados.
# 1. Desenvolva um programa que pergunta números ao usuário, parando apenas quando a soma de todos os números digitados for maior que $50$.

# In[ ]:





# In[ ]:





# In[ ]:





# ## Break

# O `break` possibilita a saída de um `while` sem que a condição seja atendida.

# **Exemplo**
# 
# ```python
# x=0
# while x<10:
#     print(x)
#     if x==5:
#         break
#     x=x+1
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima

# In[ ]:





# **Exemplo**
# 
# - Peça ao usuário que digite números pares, e saia do programa caso ele digite um número ímpar.
# ```python
# par = True
# while par:
#     num = int(input('Digite um número par'))
#     if num%2 == 1:
#         print('Número ímpar digitado')
#         par = False
# ```  
# 
# **Atividade**
# 
# - Execute o exemplo

# In[ ]:





# **Exemplo**
# 
# - Peça ao usuário que digite números pares, e saia do programa caso ele digite um número ímpar, utilizando `break`:
# ```python
# while True:
#     num = int(input('Digite um número par'))
#     if num%2 == 1:
#         print('Número ímpar digitado')
#         break
# ```
# 
# **Atividade**
# 
# - Execute o exemplo

# In[ ]:





# **Exercício**
# - [Beecrowd 2334 - Patinhos](https://www.beecrowd.com.br/judge/pt/problems/view/2334)
# - [Beecrowd 1159 - Soma de Pares Consecutivos](https://www.beecrowd.com.br/judge/pt/problems/view/1159)
# - [Beecrowd 1101 - Sequência de Números e Soma](https://www.beecrowd.com.br/judge/pt/problems/view/1101)
# 

# ## Continue

# O `continue` possibilita que o `while` avance para a próxima iteração.

# **Exemplo**
# - Mostre a sequência de números de 1 a 50, menos aqueles que são divisíveis por 2, 3, 5, 7, 11 ou 12.
# - Testando todas as condições utilizando `if`s aninhados:
# ```python
# x=1
# while x<=50:
#     if x%2 !=0:
#         if x%3 != 0:
#             if x%5 != 0:
#                 if x%7 != 0:
#                     if x%11 != 0:
#                         if x%12 != 0:
#                             print(x) #Só executa se todas as condições forem verdadeiras
#     x=x+1
# ```

# In[ ]:





# - Testando todas as condições em um único `if`:
# ```python
# x=0
# while x<50:
#     x=x+1
#     if x%2 !=0 and x%3 != 0 and x!=5 != 0 and x%7 != 0 and x%11 != 0 and x%12 != 0 :
#         print(x) 
# ```

# In[ ]:





# - Utilizando `continue`:
# ```python
# x=0
# while x<50:
#     x=x+1
#     if x%2 ==0: 
#         continue
#     if x%3 == 0: 
#         continue
#     if x%5 == 0: 
#         continue
#     if x%7 == 0: 
#         continue
#     if x%11 == 0: 
#         continue
#     if x%12 == 0: 
#         continue
#     print(x) #Só executará se todas as condições anteriores não forem atendidas
# ```
# Observe que se uma das condições forem verdadeiras, as próximas não serão testadas.

# In[ ]:





# ## Erros comuns

# ### *loop* infinito
# A condição de parada nunca é atendida.
# 
# **Exemplo**
# 
# ```python
# x=0
# while x<10:
#     print(x)
# ```
# 
# **Exemplo**
# 
# ```python
# x=0
# while x<10:
#     print(x)
# x=x+1
# ```

# ### Sintaxe incorreta
# Erros na codificação.
# 
# **Exemplo**
# 
# ```python
# x=0
# while x<10
#     print(x)
#     x=x+1
# ```
# 
# **Exemplo**
# 
# ```python
# x=0
# while x<10:
# print(x)
# x=x+1
# ```

# **Exercícios**
# 
# 1. Calcule o valor do fatorial de determinado número.
# 1. Calcule se um número é primo
# 1. Desenvolva um menu fictício, com pelo menos 3 opções de funcionalidades que o usuário pode escolher utilizando valores. Além destas, uma das opções é o valor $0$ para sair do menu.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Referências
# 
# [FORBELLONE, A. L. V.; EBERSPÄCHER, H. F. Lógica de programação a construção de algoritmos e estruturas de dados. 3. ed. -. São Paulo: Prentice Hall, 2005. ISBN 9788576050247.](https://plataforma.bvirtual.com.br/Leitor/Publicacao/323/pdf/11?code=DUT9ceW6cevP76Zo+EZuhLshlFiipf6bm1qH+Er9IE2FR2aabpwRBUFHWBQY+ppEDI1u1phvX3Bo9xII7UTG/g==)  
# 
# [ASCENCIO, A. F. G.; CAMPOS, E. A. V. Fundamentos da programação de computadores algoritmos, Pascal e C/C++. São Paulo: Prentice Hall, 2002. ISBN 9788587918369.](https://plataforma.bvirtual.com.br/Leitor/Publicacao/474/pdf/17?code=5aKNgQDVA1oGkIID/Mxq/5biXE3mV+4408hOmSg69vmeXo0W9VHrtyzrwyezUND1EQo7jhOxxg2X7UCNFBYZHg==)  
# 
# MATTHES, E. Curso intensivo de Python: uma introdução à prática e baseada em projetos à programação. São Paulo: Novatec, 2015.  
# 
# MENEZES, N. N. C. Introdução à programação com Python: algoritmos e lógica de programação para iniciantes. 3.ed. São Paulo: Novatec, 2019.  
# 
# 
# 
# ### Outros materiais
# 
# [Python. WhileLoop - Python Wiki.](https://wiki.python.org/moin/WhileLoop)  
# 

#  
