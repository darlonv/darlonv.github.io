#!/usr/bin/env python
# coding: utf-8

# # Tipos de variáveis
# 
# Em Python, o tipo de uma variável é definido no momento de sua atribuição. Para observarmos o tipo de uma variável, utilizamos a função `type()`
# 
# **Exemplo**  
# ```python
# a = 10
# type(a)
# ```

# In[ ]:





# Existem diversos tipos de dados presentes nativamente em Python.
# 
# ## `int` e `float`
# 
# 
# ### Exercício
# Observe o tipo das seguintes variáveis
# ```python
# inteiro=10
# type(inteiro)
# 
# real=3.5
# type(real)
# ```

# In[ ]:





# Os tipos de dados `int` e `float` permitem que sejam realizados operações matemáticas sobre eles, como adição, subtração e divisão. Ambos os tipos permitem o armazenamento de números positivos e negativos, porém o tipo `float` opera utilizando *ponto flutuante*, ou seja, permite que números reais sejam armazenados.
# 
# A diferença na definição da variável se ela será um `int` ou `float`, é dado pelo uso do `.`, que separa as casas decimais.

# In[ ]:





# ### Arredondamento
# 
# Para arredondar valores `float`, pode-se utilizar a função `round()`.  
# 
# **Sintaxe**  
# ```python
# round(valor, num_casas)
# ```
# onde:
# - `valor`: valor a ser arredondado
# - `num_casas`: número de casas decimais a ser utilizado (parâmetro opcional)
# 
# **Exemplo**  
# ```python
# round(2.5) #2 (int)
# round(2.5, 2) #2.5 (float)
# round(2.5, 0) #2.0 (float)
# round(5.00002, 3) #5.0 (float)
# ```
# 
# ### Apresentando um número fixo de casas decimais
# Para que seja possível apresentar um número definido de casas decimais independente do arredondamente, pode-se utilizar a saída formatada de uma *string*.
# 
# **Exemplo**  
# Para apresentar o valor 5.0, com duas casas decimais:
# 
# ```python
# val = 5.0
# print(f'{val:.2f}') #Saída: 5.00
# ```
# 
# Observe que:
# - o `f` antes das aspas indica que a *string* será formatada.
# - as `{}` indicam que aquele conteúdo será substituído por um valor.
# - `:`: separador entre a variável e as informações de formatação.
# - `.2`: número de casas decimais. Neste caso, duas.
# - `f` : indica que é um float.

# In[ ]:





# **Atividade**
# - Qual é a diferença entre a função `round()` e a saída utilizando *string* formatada?

# In[ ]:





# **Exercício**
# - [Beecrowd 1005 - Média 1](https://www.beecrowd.com.br/judge/pt/problems/view/1005)  
# - [Beecrowd 1006 - Média 2](https://www.beecrowd.com.br/judge/pt/problems/view/1006)  
# 

# ## `bool`
# 
# O tipo de dado `bool` permite armazenar um valor *booleano*, ou seja, verdadeiro (*True*) ou falso (*False*). Este tipo de variável permite apenas estes dois valores.
# 
# **Atenção**  
# >Os valores **True** e **False** possuem letra inicial maiúscula.
# 
# **Exemplo**  
# Considere que existe uma variável que registra se uma porta e uma janela estão abertas ou fechadas. Em seguida, observe o tipo de dado dessas variáveis.
# ```python
# portaAberta = True
# type(portaAberta)
# 
# janelaAberta = False
# type(janelaAberta)
# ```
# 

# In[ ]:





# ## `str`
# 
# O tipol de dado `str` é utilizado para representar uma sequência de caracteres, ou *string*.
# 
# Para que o interpretador Python reconheça que o dado é uma *string*, deve-se colocar a sequência de caracteres entre aspas (`'`) .
# 
# **Exemplo**  
# Considere variáveis que armazenam o país e o estado. Em seguida, observe o tipo da variável.
# ```python
# pais='Brasil'
# type(pais)
# 
# estado='Santa Catarina'
# type(estado)
# ```
# 
# **Anotação**
# >Em python, uma *string* também pode ser delimitada utilizando aspas duplas (`"`), e seu funcionamento ocorrerá da mesma forma. Porém, é uma convenção entre desenvolvedores a utilização das aspas simples, como utilizado no exemplo.

# In[ ]:





# ## Conversões de tipos de dados
# Para converter um tipo de dado a outro pode-se utilizar funções que possuem o mesmo nome do tipo de dado.
# ```python
# int()
# float()
# str()
# bool()
# ```

# **Atividade**  
# 
# Observe o conteúdo e tipo de dado de cada uma das variáveis utilizadas abaixo.
# ```python
# ni = 4
# nf = float(ni)
# ns = str(ni)
# ```
# O quê ocorreu com os tipos de dados?

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Atividade**  
# 
# Observe o conteúdo e tipo de dado de cada uma das variáveis utilizadas abaixo.
# ```python
# nf = 4.7
# ni = int(nf)
# ns = str(nf)
# ```
# O quê ocorreu com os tipos de dados?

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Atividade**  
# 
# Observe o conteúdo e tipo de dado de cada uma das variáveis utilizadas abaixo.
# ```python
# ns = '4.7'
# ni = float(ns)
# ni = int(ns)
# ```
# O quê ocorreu com os tipos de dados?

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Atividade**  
# 
# Observe o conteúdo e tipo de dado de cada uma das variáveis utilizadas abaixo.
# ```py
# nb = True
# ns = str(nb)
# nf = float(nb)
# ni = int(nb)
# ```
# O quê ocorreu com os tipos de dados?

# In[ ]:





# In[ ]:





# **Exercícios**
# - [Beecrowd 1008 - Salário](https://www.beecrowd.com.br/judge/pt/problems/view/1008) 

# In[ ]:





# **Atividade**  
# - Realize um programa que calcula a soma de três valores digitados pelo usuário em uma mesma linha, com os valores separados por espaços.  
#     - **Entrada**
#         - 2 3 5
#     - **Saída**
#         - 10
#         
#     - Dica: Utilize o método `.split()` do tipo de dado `string`.

# In[ ]:





# **Exercício**
# - [Beecrowd 1963 - O Filme](https://www.beecrowd.com.br/judge/pt/problems/view/1963)

# In[ ]:




