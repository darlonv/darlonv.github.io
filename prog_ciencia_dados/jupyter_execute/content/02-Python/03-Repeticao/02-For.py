#!/usr/bin/env python
# coding: utf-8

# # For

# Outra maneira de apresentar este resultado é utilizando uma *estrutura de repetição*, como o `for`. Neste caso, basta informarmos a variável que queremos utilizar e os valores que queremos.
# 
# **Exemplo**
# 
# ```python
# for var in 0,1,2,3,4,5:
#     print(var)
# ```
# No exemplo, utilizamos a variável `var`, e em seguida informamos quais valores serão armazenados na variável ($0$,$1$,$2$,$3$,$4$ e $5$).
# 
# **Atividade**
# 
# - Execute o exemplo utilizando a estrutura de repetição `for`

# In[ ]:





# **Sintaxe**
# 
# ```python
# for <variável> in <valores>:
#     <código>
# ```
# onde: 
# - <variável> corresponde a uma variável que terá seu valor alterado a cada execução, a **variável de controle**
# - <valores> são os valores que serão utilizados, e armazenados na variável de controle
# - <código> corresponde ao código que será executado para cada valor passado.
#     - Chamamos de **iteração** a cada vez que o código foi executado.
#     
#     
# **Observação**
#     
# - A indentação define qual será o bloco abrangido pelo `for`
# - ao final da primeira linha do `for` há dois pontos (`:`)

# **Exercício**
# 
# - Faça uma aplicação que apresente uma sequência de números de 5 a 9 utilizando `for`.

# In[ ]:





# **Exercício**
# 
# - Utilizando `for`, faça uma aplicação que apresente uma sequência de números em ordem decrescente, de 7 a 3.
# - Faça uma aplicação utilizando `for` que apresente uma sequência com as palavras 'batata', 'abacaxi', 'pessego' e 'beterraba'.

# In[ ]:





# In[ ]:





# ## A função `range()`
# Até aqui todos os valores a serem utilizados nas iterações foram apresentados explicitamente, visto que sempre colocamos diretamente no código cada valor a ser assumido pela variável. 
# 
# Porém, podemos utilizar algumas funções do Python para gerar esses valores. Para gerar sequências de números, pode-se utilizar a função `range()`.
# 
# **Exemplo**
# 
# Para mostrar os números de 0 a 5:
# ```python
# for i in range(6):
#     print(i)
# ```
# 
# Observe que o último valor gerado pelo `range()` é um número menor que a entrada dada à função. Ao omitirmos o valor inicial, $0$ é assumido.
# 
# **Atividade**
# 
# - Execute o exemplo acima

# In[ ]:





# **Exercício**
# 
# - Peça ao usuário que digite um número, e mostre a sequência de valores de 0 até o número imediatamente inferior ao número que ele digitou
# - Peça ao usuário que digite um número, e mostre a sequência de valores de 0 até o número que ele digitou

# In[ ]:





# In[ ]:





# **Exercícios**
# - [Beecrowd 1060 - Números Positivos ](https://www.beecrowd.com.br/judge/pt/problems/view/1060)  
# - [Beecrowd 1066 - Ímpares, Positivos e Negativos](https://www.beecrowd.com.br/judge/pt/problems/view/1066)  
# - [Beecrowd 2862 - Inseto!](https://www.beecrowd.com.br/judge/pt/problems/view/2862)
# - [Beecrowd 1133 - Resto da Divisão](https://www.beecrowd.com.br/judge/pt/problems/view/1133)

# In[ ]:





# A função `range()` também pode ser utilizada de outras maneiras, passando diferentes valores como entrada para a função.  
# 
# **Exemplo**
# 
# Especificando os valores inicial e final da sequência, como números de 5 a 8.
# ```python
# for i in range(5,9):
#     print(i)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima

# In[ ]:





# **Exemplo**
# 
# Especificando o incremento, como números de 5 a 29, incrementando de 3 em 3.
# ```python
# for i in range(5,30,3):
#     print(i)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima

# In[ ]:





# **Exemplo**
# 
# Sequência com incremento negativo (decremento), como números de 15 a 9.
# ```python
# for i in range(15,8,-1):
#     print(i)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima

# In[ ]:





# **Exercícios**    
# - [Beecrowd 1067 - Números Ímpares ](https://www.beecrowd.com.br/judge/pt/problems/view/1067)
# - [Beecrowd 1073 - Quadrado de Pares](https://www.beecrowd.com.br/judge/pt/problems/view/1073)

# In[ ]:





# ## Estratégias

# ### Acumuladores
# Um **acumulador** é uma variável que *acumula* um valor, sendo utilizada em várias iterações.
# 
# **Exemplo**
# 
# Soma de uma sequência de números:
# ```python
# S=0
# for i in range(5,10+1):
#     S=S+i
# print('Soma:', S)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima

# In[ ]:





# ### Estruturas aninhadas
# É possível utilizar `for` ou `if` dentro de um `for` (e vice-versa).
# 
# **Exemplo**
# 
# - Faça um programa que gere a seguinte saída na tela:
# ```python
# 1
# 12
# 123
# 1234
# 12345
# ```
# ```python
# nlinhas=5
# for linha in range(1,nlinhas+1):
#     for col in range(1,linha+1):
#         print(col,end='')
#     print('')
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima, e explique o ocorrido

# In[ ]:





# **Exemplo**
# 
# Procure dois valores que quando multiplicados resultam em um valor especificado.
# ```python
# val = 56
# for i in range(11):
#     for j in range(11):
#         mult = i*j
#         if mult == val:
#             print(i,'*',j,'=',mult)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo.

# In[ ]:





# Neste caso, é necessário atenção ao nível em que cada estrutura está. Observe as diferenças:
# ```python
# val = 56
# for i in range(11):
#     for j in range(11):
#         mult = i*j
#     if mult == val:
#         print(i,'*',j,'=',mult)
# ```
# ```python
# val = 56
# for i in range(11):
#     for j in range(11):
#         mult = i*j
# if mult == val:
#     print(i,'*',j,'=',mult)
# ```
# 
# **Atividade**
# 
# - Execute os exemplos, e mostre a diferença destes com o exemplo anterior
# - Qual dos códigos apresenta o resultado correto?
# - O que há de errado?

# In[ ]:





# In[ ]:





# ## Erros comuns

# Alguns erros comuns ao utilizar a estrutura de repetição `for` estão descritos a seguir.
# ### Indentação incorreta
# ```python
# for j in range(0,10):
# print(j)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo e observe a saída

# In[ ]:





# ### Sintaxe incorreta
# ```python
# for k in range(5,10,2)
#     print(k)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo e observe a saída

# In[ ]:





# ### Valores incorretos
# ```python
# for k in range(10,5,2)
#     print(k)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo e observe a saída

# In[ ]:





# ### Uso incorreto da variável de controle
# ```python
# for j in range(0,10):
#     print(k)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo e observe a saída

# In[ ]:





# **Exercícios**

# Resolva os exercícios a seguir, utilizando `for`.
# 1. Peça ao usuário que digite dois números A e B, de forma que A < B. Mostre a sequência de valores de A até B.
# 1. Peça ao usuário que digite dois números: A e B. Mostre a sequência de valores, do menor número até o maior.
# 1. Peça ao usuário que digite dois números: A e B. Mostre a sequência inversa de valores, do maior até o menor número.
# 1. Peça ao usuário que digite um número par. Mostre na tela os 10 números pares seguintes.
# 1. Peça ao usuário que digite um número. Mostre na tela os 10 números pares seguintes.
# 1. Calcule e mostre na tela a soma dos números de 1 a 10.
# 1. Calcule e mostre na tela a soma dos números de 1 a 100.
# 1. Solicite ao usuário que digite dois números A e B. Calcule e mostre a soma de todos os números no intervalo de A a B.
# 1. Não execute o código abaixo. Apenas observe-o e informe qual será a saída dele.
# ```python
# for j in range(8):
# print(j)
# ```
# 1. Não execute o código abaixo. Apenas observe-o e informe qual será a saída dele.
# ```python
# for j in range(5,10,-1):
#         print(j)
# ```

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
# [Python. ForLoop - Python Wiki.](https://wiki.python.org/moin/ForLoop)  
# 

# In[ ]:





#  
