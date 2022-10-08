#!/usr/bin/env python
# coding: utf-8

# # Exercícios

# >**Dica**  
# >Para obter e mostrar um número aleatório $r$ no intervalo de 5 a 10:
# >```py
# import random
# r = random.randrange(5,10+1)
# print(r)
# ```

# **Exercício 01**

# Implemente o clássico **jogo da forca**. Elabore uma base de dados de palavras, e escolha uma aleatoriamente.    
# Para jogar, peça ao usuário que digite as letras, atualizando o resultado a cada letra digitada. Deve ser mostrado as lacunas (letras ainda não preenchidas, mostradas com um `_` ) a serem preenchidas, o número de tentativas possíveis e as letras já digitadas. O usuário possui um total de $8$ tentativas.

# In[ ]:





# **Exercício 02**

# Considere uma prova que possui respostas "A", "B", "C" ou "D". Armazene uma lista, que seria correspondente ao gabarito da prova, contendo a resposta correta para cada questão.  
# Faça um programa que pergunta ao usuário suas respostas na prova, e então responde quantas respostas corretas ele teve, e sua taxa de acerto. Como gabarito, utilize a sequência "ADCAABDCCB".
# 
# **Exemplo**
# >- Entrada:
# >```
# 'ADCABBACCB'
# ```
# >- Saída:
# >```
# (8,80.0)
# ```
# 
# >- Entrada:
# >```
# 'AAAAAAAAAA'
# ```
# >- Saída:
# >```
# (3, 30.0)
# ```
# 
# >- Entrada:
# >```
# 'CBDBBCBAAA'
# ```
# >- Saída:
# >```
# (0, 0.0)
# ```

# In[ ]:





# **Exercício 03**

# Peça ao usuário que digite 10 números. Em seguida, mostre esses números de maneira ordenada, e sem repetição.

# In[ ]:





# **Exercício 04**

# Peça ao usuário que digite os valores $a$, $b$ e $c$, que correspondem à equação de segundo grau
# $$
# y = ax^2+bx+c
# $$
# Em seguida, armazene os valores de $y$ para $x$ de $0$ a $100$, considerando $x$ como números inteiros.

# In[ ]:





# **Exercício 05**

# Desenvolva um código que pergunta ao usuário $20$ valores inteiros. Em seguida, apresente:

# 1. o total de números pares;
# 2. quais são os números pares;
# 3. o total de números ímpares;
# 4. quais são os números ímpares;
# 5. o total de números primos;
# 6. quais são os números primos.

# In[ ]:





# **Exercício 06**

# Peça ao usuário que digite os valores $a$, $b$, $c$, que correspondem aos coeficientes de uma equação de segundo grau, no formato
# $$y=ax^2+bx+c$$
# 
# Em seguida, calcule e mostre todos os valores de $y$, considerando para $x$ os valores de 0 a 20.

# In[ ]:





# **Exercício 07**

# Peça ao usuário que digite os coeficientes $c$ de uma equação de grau $n$. Em seguida, calcule e mostre todos os valores de $y$, considerando para $x$ os valores de 0 a 20.
# 
# Uma equação de grau $n$ posui a seguinte estrutura:
# 
# $$
# y = c_0x^n + c_1x^{n-1} + c_2x^{n-2} + ... + c_{n-1}x^1 + c_nx^0
# $$
# 
# Considere que utilizar uma entrada vazia indica o final da entrada de coeficientes.

# In[ ]:





# **Exercício 08**

# Dada uma seqüência de $n$ números inteiros, determinar qual subconjunto dessa dessa sequência possui o maior valor de soma. Mostre o valor, a sequência e as posições na sequência de entrada.
# 
# **Exemplo**
# 
# 
# - Entrada:  
# ```
# [5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]
# ```
# - Saída:
# ```
# Soma: 33
# Posições: 4 a 8
# Valores: 3, 14, 10, -3, 9
# ```
# 

# In[ ]:





# **Exercício 09**

# Implemente uma função que retorna uma lista com $n$ posições. Utilize `float` como tipo de dado. Todos os valores devem ser inicializados com 0.

# In[ ]:





# **Exercício 10**

# Implemente uma função que retorna uma lista com $n$ posições. Todos os valores da lista devem ser inicializados com o valor $p$, passado por parâmetro.

# In[ ]:





# **Exercício 11**

# Implemente uma função que procura por um valor em uma lista, retornando a posição em que ele se encontra. Retorna `False` caso o valor não seja encontrado.

# In[ ]:





# **Exercício 12**

# Implemente uma função que calcula a média dos valores passados em uma lista.
# 
# >**Observação**  
# >A média de determinado conjunto de dados é a soma de todas os seus valores, dividida pela quantidade de valores. A letra grega $\mu$ é comumente utilizada para representar a média.
# >$$
# \mu = \frac{\sum\limits_{i=0}^{n-1}{x_i}}{n}
# $$
# >onde:
# - $\mu$: média dos valores
# - $n$: número de valores
# - $x_i$ valor na i-ésima posição
# - $\sum\limits_{i=0}^{n-1}{x_i}$: soma dos valores de $x$, onde $i$ varia de 0 a $n-1$

# In[ ]:





# **Exercício 13**

# Implemente uma função que calcula o desvio padrão dos valores passados em uma lista.
# 
# >**Observação**  
# > O desvio padrão é uma medida que informa quanto os valores de um conjunto estão próximos de sua média. Um conjunto com desvio padrão baixo indica que os valores estão mais perto da média do conjunto, enquanto que um desvio padrão alto indica que os valores estão mais afastados da média.  
# > 
# > O desvio padrão é representado pela letra grega $\sigma$ (*sigma*), e seu valor pode ser calculado pela seguinte equação: 
# $$
# \sigma = \sqrt{\frac{\sum\limits_{i=0}^{n-1}{(x_i- \mu)^2}}{n}}
# $$
# onde:
# - $\sigma^2$: variância
# - $n$: número de elementos
# - $\mu$: média dos valores
# - $x_i$: elemento na i-ésima posição
# 

# In[ ]:





# **Exercício 14**

# Implemente duas funções retornam os valores de P.A. e P.G., respectivamente. Como entrada, são passados o valor inicial, a razão e o número de elementos da progressão.

# In[ ]:





# **Exercício 15**

# Implemente uma função que retorna todos os divisores inteiros de determinado número.

# In[ ]:





# **Exercício 16**

# Implemente uma função que retorna todos os números primos em determinado intervalo.

# In[ ]:





# **Exercício 17**

# Implemente funções que realizam a adição, subtração e multiplicação de matrizes 3x3 utilizando listas. Utilize `float` como tipo de dado.

# In[ ]:





# **Exercício 18**

# Implemente uma função que retorna uma matriz quadrada, de tamanho $n\times n$, passado como parâmetro para a função. Utilize `float` como tipo de dado. Todos os valores da matriz devem ser inicializados com 0. Utilize listas como matrizes.

# In[ ]:





# **Exercício 19**

# Implemente uma função que aloca matrizes de qualquer ordem, utilizando listas. Todos os valores da matriz devem ser inicializados com um valor definido via parâmetro. Caso esse valor seja omitido, 0  deve ser utilizado.

# In[ ]:





# **Exercício 20**

# Implemente uma função que aloca e retorna uma matriz identidade de ordem $n$, utilizando listas.

# In[ ]:





# **Exercício 21**

# Implemente uma função que mostra na tela o conteúdo de uma matriz com qualquer número de linhas e colunas, com seus elementos separados por espaço.

# In[ ]:





# **Exercício 22**

# Implemente uma função que realiza a cópia de duas matrizes.

# In[ ]:





# **Exercício 23**

# Implemente uma função que aloca e retorna matrizes de qualquer ordem, preenchendo-a com um valor definido por parâmetro. A ordem da matriz também deve ser passada por parâmetro.

# In[ ]:





# **Exercício 24**

# Implemente uma função chamada `comparaListaValor` que retorna uma lista com valores booleanos, tendo como entradas uma lista $m$ e um valor $p$. A lista retornada resulta da comparação de cada valor da lista $m$ com o valor $p$, sendo que a posição na lista booleana deve ser `True` caso o valor armazenado em $m$ seja igual $p$ e `False` caso contrário.
# 
# **Exemplo**
# - Entradas:
# ```python
# m: [1,2,3,4,4,3,2,1]
# p: 2
# ```
# - Saída:
# ```python
# [False, True, False, False, False, False, True, False]
# ```

# In[ ]:





# **Exercício 25**

# Semelhante ao exercício anterior, implemente a função que retorna a lista binária para as posições de $m$ com valores menores que $p$.

# In[ ]:





# **Exercício 26**

# Semelhante ao exercício anterior, implemente a função que retorna a lista binária para as posições $m$ com valores maiores que o $p$.

# In[ ]:





# **Exercício 27**

# Implemente funções que retornam o maior e menor valor de uma lista com valores `float` ou `int`.

# In[ ]:





# **Exercício 28**

# Na matriz de $20 \times 20$ abaixo, quatro números ao longo de uma linha diagonal foram marcadas em negrito. O produto desses números é $26 \times 63 \times 78 \times 14 = 1788696.$
# 
# 
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08  
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00  
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65  
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91  
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80  
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50  
# 32 98 81 28 64 23 67 10 **26** 38 40 67 59 54 70 66 18 38 64 70  
# 67 26 20 68 02 62 12 20 95 **63** 94 39 63 08 40 91 66 49 94 21  
# 24 55 58 05 66 73 99 26 97 17 **78** 78 96 83 14 88 34 89 63 72  
# 21 36 23 09 75 00 76 44 20 45 35 **14** 00 61 33 97 34 31 33 95  
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92  
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57  
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58  
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40  
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66  
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69  
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36  
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16  
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54  
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 
# 
# 
# Qual é o maior produto de quatro números adjacentes em qualquer direção (cima, baixo, esquerda, direita, ou na diagonal) na matriz de 20x20?

# In[ ]:





# **Exercício 29**

# Desenvolva uma função chamada `somaAcumulada`, que possui como entrada uma lista com números e retorna uma lista a soma acumulada dos valores até a i-ésima posição.
# 
# **Exemplo**
# 
# - Entrada:
# ```
# [8, 2, 10, 1]
# ```
# - Saída:
# ```
# [8, 10, 20, 21]
# ```
# 

# In[ ]:





# **Exercício 30**

# Programe uma funcao chamada `isSorted` que verifica se uma lista com números está ordenada de maneira crescente, retornando `True` ou `False`.

# In[ ]:





# **Exercício 31**

# Faça uma função que mostra a maior diferença entre dois elementos consecutivos de uma lista, apresentando também quais são esses valores e suas posições.

# In[ ]:





# ## Referências
# 
# **Outros materiais**
# 
