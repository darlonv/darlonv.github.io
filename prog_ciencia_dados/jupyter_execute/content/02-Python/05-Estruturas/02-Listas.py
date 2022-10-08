#!/usr/bin/env python
# coding: utf-8

# # Listas
# 
# Uma lista é um conjunto de elementos, que podem ser de qualquer tipo. Uma lista é definida por elementos entre colchetes (ou parênteses angulares, rs) (`[` `]`), separados por vírgulas. Também pode-se criar uma lista utilizando a função `list()`.
# 
# **Exemplo**
# 
# Uma lista com números inteiros. Observe o tipo da variável `li`, e veja que cada elemento pode ser acessado pela sua posição.
# ```python
# li = [1,2,3,4,5]
# print(type(li)) #retorna list
# print(li[0]) #1
# print(li[1]) #2
# print(li[4]) #5
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exemplo**
# 
# Uma lista com strings. Observe que o tipo da variável `ls` não é influenciado pelo tipo de dado que a lista armazena.
# ```python
# ls = ['abc','def','ghi']
# print(type(ls)) #continua retornando list
# print(ls[0])
# print(ls[1])
# print(ls[2])
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# Uma lista pode conter elementos de diferentes tipos.  
# 
# **Exemplo**
# - Observe a lista `lvar`, e o tipo de cada elemento nela armazenado.
# ```python
# lvar=[10,'dez',2.5, True]
# print(type(lvar))
# print(type(lvar[0]))
# print(type(lvar[1]))
# print(type(lvar[2]))
# print(type(lvar[3]))
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima e observe cada tipo de dado apresentado.

# In[ ]:





# In[ ]:





# Inclusive, uma lista pode conter outras listas.  
# 
# **Exemplo**
# -  Observe a saída de cada função `print()`:
# ```python
# ll = [[1,2,3],[False, False, True]]
# print(ll[0])
# print(ll[0][1])
# print(ll[1])
# print(ll[1][2])
# type(ll[0])
# type(ll[0][1])
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exercício**
# 
# - Crie uma lista com nomes de pelo menos três pessoas
# - Crie uma lista que contenha nomes de frutas
# - Crie uma lista com os números primos de 1 a 10.

# In[ ]:





# **Exercícios**
# - [Beecrowd 3209 - Tomadas Elétricas](https://www.beecrowd.com.br/judge/pt/problems/view/3209)

# ## Funções
# 
# Algumas operações podem ser aplicadas sobre qualquer tipo de sequência, como
# - `len()`: retorna a quantidade de elementos de uma sequência;
# - `min()`: retorna o menor valor;
# - `max()`: retorna o maior valor;
# - `sorted()`: retorna uma lista, contendo a sequência ordenada;
# - `reversed()` : obtém um iterador (*iterator*), contendo os valores da sequência, em ordem inversa.
# 
# **Exemplo**
# 
# Execute os códigos abaixo, e observe seus resultados.
# ```python
# estado=['P','a','r','a','n','á']
# print(estado)
# print('len(estado)   :', len(estado))
# print('min(estado)   :', min(estado))
# print('max(estado)   :', max(estado))
# print('sorted(estado):', sorted(estado))
# for i in reversed(estado): 
#     print(i)
# ```
# **Atividade**
# 
# - Execute o exemplo acima, e observe os resultados.
#     - Explique os resultados das operações `min(estado)` e `max(estado)`.
#     - Explique o resultado da operação `sorted(estado)`.

# In[ ]:





# In[ ]:





# In[ ]:





# **Exercício**
# - [Beecrowd 1013 - O Maior](https://www.beecrowd.com.br/judge/pt/problems/view/1013)

# > **Observação**
# > 
# > Repare quendo os elementos são do tipo *string*, os caracteres são comparados de acordo com seu valor na tabela ASCII, onde letras maiúsculas, minúsculas e acentuadas possuem valores distintos. Perceba que quando a *string* 'Paraná' foi ordenada, o caractere 'P' aparece como primeira letra, e o caractere 'á' como último.
# 

# In[ ]:





# **Exemplo**
# 
# ```python
# tamanhos=['p','m','g']
# print(tamanhos)
# print('len(tamanhos)   :', len(tamanhos))
# print('min(tamanhos)   :', min(tamanhos))
# print('max(tamanhos)   :', max(tamanhos))
# print('sorted(tamanhos):',sorted(tamanhos))
# for i in reversed(tamanhos): 
#     print(i)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# In[ ]:





# **Exemplo**
# 
# ```python
# idades = [23,11,50,4,12,37,35]
# print(idades)
# print('len(idades):', len(idades))
# print('min(idades)', min(idades))
# print('max(idades)',max(idades))
# print('sorted(idades):',sorted(idades))
# for i in reversed(idades): print(i)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exemplo**
# 
# ```python
# indices = [88,34,12,43,20]
# print(indices)
# print('len(indices):', len(indices))
# print('min(indices)', min(indices))
# print('max(indices)',max(indices))
# print('sorted(indices):',sorted(indices))
# for i in reversed(indices): print(i)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# ## Índices
# 
# **Índices negativos**
# 
# É possível acessar um elemento de uma sequência em ordem inversa. Basta utilizar índices negativos. O índice -1 indica o último elemento, -2 o penúltimo e assim sucessivamente.  
# 
# **Exemplo**
# 
# ```python
# vogais=['a','b','c']
# print(vogais[-1])
# print(vogais[-2])
# print(vogais[-3])
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# ### Acesso a índices não existentes
# Cada elemento em uma sequência pode ser acessado utilizando seu índice, como já mostrado anteriormente. Porém, perceba que acessar um elemento em uma posição que não existe indica um erro do tipo *index out of range*, tanto para operações de leitura como escrita do dado.  
# 
# **Exemplo**  
# Acessar as posições 3, 4 e -4 da lista `valores` acarreta em erros, visto que estas posições são inexistentes na lista.
# ```python
# valores=[10,20,30]
# print(valores[3])
# valores[4]=0
# print(valores[-4])
# ```
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# ## Fatiamento
# Em sequências, é possível acessar um intervalo de elementos de uma única vez, utilizando o operador `:` no índice da sequência. Este operador pode ser utilizado da seguinte maneira:  
# 
# |Formato|Resultado|
# |--|--|
# |`[:]`|Todos os elementos da sequência|
# |`[a:b]`| Da posição `a` até `b-1`|
# |`[a:]`|Da posição `a` até a posição final|
# |`[:b]`|Da posição inicial até a posição `b-1`|
# |`[a:b:c]`| Da posição `a` até a posição `b-1`, com incremento de `c`|
# 
# **Observação**
# 
# A posição final não é incluída, sendo apenas até seu elemento anterior.
# 
# **Exemplo**
# 
# ```python
# letras=['a','b','c','d','e','f','g','h','i','j']
# print('[:]     :' , letras[:])    #Todos os elementos
# print('[:3]    :' , letras[:3])   # 'abc' (posições 0, 1 e 2)
# print('[5:]    :' , letras[5:])   # 'fghij' (posições 5, 6, 7, 8 e 9)
# print('[3:8]   :' , letras[3:8])  # 'defgh' (posições 3, 4, 5, 6 e 7)
# print('[2:9:2] :' , letras[2:9:2]) # 'cegi' (posições 2, 4, 6 e 8)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# In[ ]:





# In[ ]:





# Também é possível modificar diversos elementos, informando o que será inserido em cada posição.  
# 
# **Exemplo**
# 
# ```python
# numeros=[1,2,3,4,5]
# numeros[:3] = [10,20,30]
# print(numeros)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# ## Iteráveis
# Uma sequência pode ser utilizada como iterável (*iterable*), ou seja, podemos utilizar uma estrutura de repetição **for** para percorrer cada elemento da sequência, onde a variável de controle assume os elementos da sequência a cada iteração.  
# 
# **Exemplo**
# 
# ```python
# nomes=['Jonas', 'João', 'Márcio']
# for i in nomes:
#     print(i)
#     
# primos = [2,3,5,7,11,13,17,19]
# for p in primos :
#     print(p)
# ```
# 
# **Atividade**
# 
# - Execute os exemplos acima.

# In[ ]:





# In[ ]:





# ## Operações específicas
# Algumas sequências possuem métodos específicos. A lista completa de métodos é descrita na [API](https://docs.python.org/3/library/stdtypes.html) do Python

# **Listas**
# 
# |Método|Descrição|
# |------|---------|
# |`.append(e)`  | Adiciona o elemento `e` ao final da lista|
# |`.insert(p,e)`| Adiciona na posição `p` da lista o elemento `e`|
# |`.extend(s)`| Adiciona à lista os elementos da sequência `s`|
# |`.pop()`| Retira o último elemento da lista|
# |`.remove(e)`| Remove da lista o elemento `e`|
# |`.count(e)`| Obtém o número de de vezes em que o elemento `e` aparece na lista|
# |`.index(e)`| Obtém a primeira posição em que o elemento `e` aparece|
# |`.sort()`| Ordena a lista|
# |`.reverse()`| Inverte a ordem dos elementos na lista|
# |`.clear()`| |
# |`.copy()`| obtém uma cópia dos elementos na lista|

# **Exemplo**
# - `.append()`
# 
# ```python
# l = [1,3,5,7]
# l.append(9)
# print(l)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# In[ ]:





# **Exemplo**
# - `.insert()`
# 
# ```python
# l = [1,3,5,7]
# l.insert(1,9) #Insere o elemento 9 na posição 1
# print(l)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exemplo**
# - `.extend()`
# 
# Observe a diferença entre as funções `.append()` e `.extend()`:
# ```python
# l=[1,2,3]
# m=[10,11,12]
# print('l          :', l)
# print('m          :', m)
# l.append(m)
# print('l.append(m):', l)
# l=[1,2,3]
# m=[10,11,12]
# l.extend(m)
# print('l.extend(m):',l)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima
#     - qual é a diferença entre os resultados?

# In[ ]:





# **Exemplo**
# - `.pop()`
# 
# ```python
# frutas=['banana', 'melancia', 'caju']
# print(frutas)
# frutas.pop()
# print(frutas)
# frutas.pop()
# print(frutas)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exemplo**
# - `.remove()`
# 
# ```python
# frutas=['banana', 'melancia', 'caju']
# frutas.remove('melancia')
# print(frutas)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exemplo**
# - `.count()`
# 
# ```python
# valores=[1,4,3,1,1,2,4,6,3,6,8,1,5,8,7,9,7,7,5,4,2]
# print(valores.count(1)) #Número de vezes em que o elemento 1 aparece na lista
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exemplo**
# - `.index()`
# 
# ```python
# alunos=['Maria', 'João', 'José', 'Vinícius']
# print(alunos.index('José'))
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exemplo**
# - `.sort()`
# 
# ```python
# valores=[1,4,3,1,1,2,4,6,3,6,8,1,5,8,7,9,7,7,5,4,2]
# valores.sort()
# print(valores)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exemplo**
# - `.reverse()`
# 
# ```python
# seq = [1,5,2,7]
# seq.reverse()
# print(seq)
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exemplo**
# - `.clear()`
# 
# ```python
# val = [5,8,8,1]
# print('val possui ', len(val), 'elementos')
# val.clear()
# print('val possui ', len(val), 'elementos')
# ```
# 
# **Atividade**
# 
# - Execute o exemplo acima.

# In[ ]:





# **Exemplo**
# - `.copy()`
# 
# O método `.copy()` torna-se necessário para manter o conteúdo da lista original, visto que o operador de atribuição realiza apenas uma **referência** à lista original. Este assunto será discutido com mais detalhes adiante.
# ```python
# original = [1,2,3,4,5]
# ref = original #aqui ref é uma referência
# ref[0]=0
# print(original,'original') #Perceba que a lista original foi modificada
# print(ref,'ref')  #Original e referencia possuem o mesmo conteúdo. Alterar uma lista significa alterar a outra
# ```
# 
# ```python
# original = [1,2,3,4,5]
# copia = original.copy() #aqui é realizada uma cópia dos elementos
# copia[0]=0
# print(original,'original') #Perceba que a lista original não foi foi modificada
# print(copia,'cópia') #original e copia são listas distintas
# ```
# 
# **Atividade**
# 
# - Execute os exemplos acima e observe as diferenças.

# In[ ]:





# In[ ]:





# In[ ]:





# ## Operações sobre sequências
# 
# Algumas operações podem ser realizadas diretamente sobre sequências, não restrito às listas.
# 
# |Operação|Função|
# |--------|------|
# |`+`     | concatena duas sequências|
# |`*`     | repete uma sequência diversas vezes|
# |`in`    | verifica se um item está em uma sequência|
# |`not in`| verifica se um item **não está** em uma sequência|
# 
# **Exemplo**
# 
# ```python
# pares=[2,4,6,8]
# vogais=['a','e','i','o','u']
# print('pares           :', pares)
# print('vogais          :', vogais)
# print('pares + vogais  :', pares+vogais)
# print('vogais * 3      :', vogais*3)
# print('5 in pares      :', 5 in pares)
# print('a not in vogais :', 'a' not in vogais)
# ```
# **Atividade**
# - Execute os exemplos apresentados acima.
# 

# In[ ]:





# **Exercícios**
# - [Beecrowd 3147 - A Batalha do  Cinco Exércitos](https://www.beecrowd.com.br/judge/pt/problems/view/3147)  
# - [Beecrowd 1259 - Pares e Ímpares](https://www.beecrowd.com.br/judge/pt/problems/view/1259)
# - [Beecrowd 1961 - Pula Sapo](https://www.beecrowd.com.br/judge/pt/problems/view/1961)

# ## Referências
# 
# **Outros materiais**
# 
# [Python - Built-in types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)  
# [Python - Operadores e fatiamento de sequências](http://www.devfuria.com.br/python/sequencias-fatiamento/)  
# [Apostila Python e orientação a objetos - Capítulo 4: Estrutura de dados ](https://www.caelum.com.br/apostila-python-orientacao-objetos/estrutura-de-dados/)

#  
