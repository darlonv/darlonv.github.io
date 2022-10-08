#!/usr/bin/env python
# coding: utf-8

# # Exercícios

# **Exercício**

# Pergunte o nome do usuário, e mostre o nome na vertical.
# 
# **Exemplo**:
# - Entrada:
# ```
# Celso
# ```
# - Saída:
# ```
# C
# e
# l
# s
# o
# ```

# In[ ]:





# **Exercício**

# Pergunte ao usuário uma frase, e mostre todas as vogais presentes na frase.
# 
# **Exemplo**
# - Entrada:
# ```
# batata e cebola
# ```
# - Saída:
# ```
# aeo
# ```

# In[ ]:





# **Exercício**

# Digite um nome, e informe quantas letras possuem nesse nome.
# 
# **Exemplo**
# - Entrada:
# ```
# Alessandra
# ```
# - Saída:
# ```
# O nome Alessandra possui 10 letras.
# ```

# In[ ]:





# **Exercício**

# Digite uma frase, e mostre essa frase na ordem inversa (de trás para frente).
# 
# **Exemplo**
# - Entrada:
# ```
# batata e cebola
# ```
# - Saída:
# ```
# alobec e atatab
# ```

# In[ ]:





# **Exercício**

# Utilize o texto abaixo para responder aos questionamentos seguintes.
# > '*Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. Atualmente possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem como um todo não é formalmente especificada. O padrão de facto é a implementação CPython. O nome Python teve a sua origem no grupo humorístico britânico Monty Python, criador do programa Monty Python's Flying Circus, embora muitas pessoas façam associação com o réptil do mesmo nome.*'  
# > (Adaptado de [Wikipedia - Python](https://pt.wikipedia.org/wiki/Python))
# 

# Mostre:
# 1. o número total de caracteres.
# 1. quantas vezes cada vogal aparece, desconsiderando letras acentuadas.
# 1. quantas frases existem no texto.
# 1. quantos caracteres possui a maior palavra presente no texto.
# 1. qual é a maior palavra presente no texto
# 1. as palavras que possuem duas letras iguais seguidas
# 1. todas as palavras que iniciam com letras maiúsculas
# 1. todas as palavras que possuem a letra "p" (minúscula).

# Código para entrada, atribuindo texto diretamenta à variável:
# 
# ```python
# texto = 'Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. Atualmente possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem como um todo não é formalmente especificada. O padrão de facto é a implementação CPython. O nome Python teve a sua origem no grupo humorístico britânico Monty Python, criador do programa Monty Pythons Flying Circus, embora muitas pessoas façam associação com o réptil do mesmo nome.'
# ```

# In[ ]:





# **Exercício**

# Peça ao usuário que digite uma entrada, e verifique se essa entrada forma um palíndromo, ou seja, se os caracteres da entrada forem invertidos, a entrada permanece idêntica. 
# 
# **Exemplos** 
# 
# - "A mala nada na lama"
# - "o breve verbo" e 
# - "anotaram a data da maratona".

# In[ ]:





# **Exercício**

# A Cifra de César é uma das mais antigas e conhecidas técnicas de criptografia. Sua técnica consiste na substituição de cada letra do texto por outra, em que a letra é trocada pela letra seguinte no alfabeto com um número fixo. 
# Por exemplo, para a frase **python**, e deslocamento utilizando $3$ letras no alfabeto, o texto cifrado seria **sbwkrq**. Repare que: p->s,y->b,t->w,h->k,o->r e n->q.

# In[ ]:





# **Exercício**

# Implemente um algoritmo de criptografia que utiliza a Cifra de César, utilizando um deslocamento de $3$ letras. Pergunte ao usuário qual frase deseja criptografar. Trabalhe apenas com letras minúsculas, mesmo que o usuário digite letras maiúsculas.  Utilize a função `ord()` para obter valor ASCII de um determinado caractere, e a função `chr()` para obter o caractere a partir do seu valor ASCII.

# In[ ]:





# **Exercício**

# Implemente um algoritmo que descriptografa um texto criptografado com a Cifra de César, cifrado utilizando deslocamento de $3$ letras.

# In[ ]:





# **Exercício**

# Na frase "**o sapo nao lava o pe. nao lava porque nao quer**", faça:
# - Troque todas as vogais pela letra 'a';
# - Troque todas as vogais pela letra 'e';
# - Troque todas as logais pela letra 'i';
# - Troque todas as logais pela letra 'o';
# - Troque todas as logais pela letra 'u';
# 
# Em sua lógica, utilize as funções de manipulação de caracteres presentes na linguagem.

# In[ ]:





# **Exercício**

# Desenvolva um programa que verifica se um CPF está no formato válido (11 dígitos, seguindo o formato **xxx.xxx.xxx-xx**). O programa deve observar se apenas números, pontos e hífen foram digitados, observando nos locais corretos. Ao final deve informar "CPF Válido" ou "CPF Inválido".
# 
# **Exemplos**
# 
# 
# |Entrada   |Saída           |
# |----------|----------------|
# |123.456.789-01|CPF Válido  |
# |12.3456.789-01|CPF Inválido|
# |12X.456.789-01|CPF Inválido|
# |12345678901   |CPF Inválido|
# |12.3456.789-01|CPF Inválido|
# |123-456.789-01|CPF Inválido|
# 
# 
# 

# In[ ]:





# **Exercício**

# Importe a biblioteca
# ```py
# from random import shuffle
# ```
# e utilize a função 
# ```py
# shuffle(palavra)
# ```
# para embaralhar uma palavra. Com isto, implemente um jogo que mostra uma palavra embaralhada ao usuário, que deve adivinhar qual é a palavra original. Cadastre algumas palavras no código, e faça com que o sistema escolha uma delas aleatoriamente. O usuário ganha ou perde conforme adivinha corretamente ou incorretamente a palavra original.

# In[ ]:





# **Exercício**

# Peça ao usuário que digite um nome, e então converta as letras para números utilizando a tabela abaixo, e então mostre o resultado. Converta todas as letras da entrada para maiúsculas.
# 
# |letra|número|
# |----|----|
# |O|0|
# |I|1|
# |Z|2|
# |E|3|
# |H|4|
# |S|5|
# |B|6|
# |T|7|
# |X|8|
# |G|9|

# In[ ]:





# **Exercício**

# O número 153 é igual à soma dos cubos dos algarismos que o compõe.  
# **Observe:**  
# $$
# 1^3+5^3+3^3 = 1 + 125 + 27 = 153
# $$
# 
# Entre 100 e 999 também existem outros números que seguem esta propriedade. Quais são?

# In[ ]:





# In[ ]:





# **Exercício**

#  Implemente uma função que pergunte um valor x e uma frase ao usuário. Deve ser mostrado na tela a frase por colunas, como apresentado no exemplo abaixo, para `x=3` e frase ABACATES.
# 
# **Exemplo**
# 
# Observe que:
# ```
# A B A
# C A T
# E S
# ```  
# O resultado deve ser o formato acima lido de cima para baixo, esquerda par a direita.
# 
# - Entrada:
# ```
# 3
# ABACATES
# ```
# - Saída: 
# ```
# ACEBASAT
# ```
# 
# 
# **Exemplo**
# 
# - Entrada
# ```
# 2
# PARALELO
# ```
# 
# - Saída
# ```
# PRLLAAEO
# ```

# In[ ]:





# Desenvolva uma função que verifica se uma palavra pode ser anagrama da outra, ou seja, se a segunda palavra pode ser formada apenas com a transposição das letras da primeira. Chame sua função de `isAnagram`.
# 
# **Exemplo**
# 
# |Entrada|Entrada|Saida|
# |-|-|-|
# |`ABACATES`| `ACEBASAT` |`True`|
# |`primeira`|`marifrei`|`False`|
# |`frase`| `resaf`|`True`|
# |`pudim`|`batata`|`False`|
# |`abcdef`|`cbafed`|`True`|
# |`sera`|`ser`|`False`|
# |`ba`|`aba`|`False`|
# |`Roma`|`Amor`|`True`|
# |`ovni`|`ovo`|`False`|
# 

# In[ ]:





#  
