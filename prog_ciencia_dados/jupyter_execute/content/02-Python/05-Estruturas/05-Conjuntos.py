#!/usr/bin/env python
# coding: utf-8

# # Conjuntos
# 
# Um conjunto é uma coleção **não ordenada**, que **não permite** elementos duplicados.
# 
# Em Python, o nome da estrutura de dados que define um conjunto é chamado de `set`.
# 
# A criação de conjuntos pode ser realiza com a utilização das chaves (`{` `}`), ou com a função `set()`.

# **Exemplo**  
# ```python
# a = {'a','b','a','c','a','t','e'}
# b = set('abacaxi')
# print(type(a))
# print(type(b))
# ```

# In[ ]:





# Em seguida, observe o conteúdo dos conjuntos:  
# 
# **Exemplo** 
# 
# ```python
# print('a:', a)
# print('b:', b)
# ```

# In[ ]:





# Observe que não há elementos duplicados. Como em conjuntos não há o conceitos de ordem, obter elementos em determinada posição ou o uso de *slicing* acarretará em erros.  
# 
# **Exemplo**  
# ```python
# print(a[0]) #ERRO!
# ```

# In[ ]:





# ## Operadores
# 
# Algumas operações que podem ser aplicadas em conjuntos são:
# 
# |Operador| Operação |Exemplo|Resultado|
# |:------:|:--------:|:-----:|:-------:|
# |`-`|Diferença|`a - b`|Elementos que pertencem ao conjunto `a` e não pertencem ao conjunto `b`|
# |`\|`|União|`a \| b`|Todos os elementos dos conjuntos `a` e `b` |
# |`&`|Interseção|`a & b`|Apenas os elementos que estão simultâneamente em `a` e `b`|
# |`^`|Diferença simétrica| `a ^ b`|Elementos que estão apenas em `a` ou apenas em `b`|
# 
# - `in`
# - `not in`
# - `len()`

# **Exemplos**  
# 
# ```python
# print('Diferença:', a-b)
# print('União:', a|b)
# print('Interseção:', a&b )
# print('Diferença simétrica:',a^b)
# ```

# In[ ]:





# Para adicionar um elemento em um conjunto já existente, pode-se utilizar o método `.add()`.  
# 
# **Exemplo**  
# 
# ```python
# primos = {2}
# primos.add(3)
# primos.add(5)
# primos.add(7)
# print(primos)
# ```

# In[ ]:





# **Atividade**  
# - Considere as compras realizadas por três grupos de pessoas, A, B e C:
# ```python
# gA = {'banana','café', 'farinha', 
#         'leite', 'pão', 'presunto', 
#         'queijo', 'iogurte', 'farinha', 
#         'limão', 'chocolate' }
# gB = {'maçã', 'abacaxi', 'chocolate', 
#         'fralda', 'melancia', 'sorvete', 
#         'leite', 'café', 'pão'}
# gC = {'maçã','café', 'farinha', 
#         'maçã', 'alface', 'limão', 
#         'rúcula', 'rabanete'}
# ```
# 
# **Exercícios**  
# 1. Quais produtos que apenas o grupo A compra?
# 1. Quais produtos apenas os grupos B e C compram?
# 1. Existe algum produto que todos os grupos compram? Caso sim, quais são?
# 1. Quantos produtos diferentes existem?
# 1. Quantos produtos apenas os grupos A e B compram?

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Exercícios**
# - [Beecrowd 2783 - Figurinhas da Copa](https://www.beecrowd.com.br/judge/pt/problems/view/2783)  
# - [Beecrowd 1104 - Troca de Cartas](https://www.beecrowd.com.br/judge/pt/problems/view/1104)  
# - [Beecrowd 2174 - Colecao de Pomekon](https://www.beecrowd.com.br/judge/pt/problems/view/2174)
# 

# ## Métodos
# 
# Alguns métodos relacionados a conjuntos podem ser vistos na tabela apresentada a seguir.
# 
# |Método|Descrição|
# |------|---------|
# |`.add()`|Adiciona um elemento|
# |`.remove()`|Remove um elemento. Caso o elemento não exista, um erro ocorre|
# |`.discard()`|Remove um elemento. Caso o elemento não exista, não resulta em erro|
# |`.pop()`|Remove um elemento aleatório, retornando o elemento|
# |`.clear()`|Remove todos os elementos do conjunto|
# |`.issubset()`|Retorna se está contido em determinado conjunto|
# |`.isuperset()`|Retorna se contém determinado conjunto|
# |`.union()`|Aplica a união com outros conjuntos|
# |`.intersection()`|Aplica a interseção com outros conjuntos|
# |`.difference()`|Aplica a diferença com outros conjuntos|
# |`.symmetric_difference()`|Diferença simétrica|
# |`.copy()`|Cópia do conjunto|
# |`.update()`|Inclui um outro conjunto|
# |`.intersection_update()`|Aplica a interseção, atualizando o conjunto|
# |`.difference_update()`|Aplica a diferença, alterando o conjunto|
# |`.simmetric_difference_update()`|Aplica a diferença simétrica, alterando o conjunto|
# 
# **Exemplo**
# ```python
# vogais = set('aeiox')
# print('Conjunto:',vogais)
# print('- Adicionando u :')
# vogais.add('u')
# print('Conjunto:',vogais)
# print('- Removendo x :')
# vogais.remove('x')
# print('Conjunto:',vogais)
# print('- Descartando k :')
# vogais.discard('k') #k não existe no conjunto, mas não é gerado erro
# print('Conjunto:',vogais)
# print('- Retirando aleatoriamente', vogais.pop(),':')
# print('Conjunto:',vogais)
# print('- Removendo todos os elementos:')
# vogais.clear()
# print('Conjunto:',vogais)
# ```
# 
# 
# **Atividade**
# - Execute os exemplos e observe os resultados.

# In[ ]:





# ```python
# vogais=set('aeiou')
# alfa  = set('abcdefghijklmnopqrstuvwxyz')
# print('Conjunto novo: vogais  ',vogais)
# print('Conjunto novo: alfabeto',alfa)
# print('letras está contido em vogais?', alfa.issubset(vogais) )
# print('vogais está contido em letras?', vogais.issubset(alfa) )
# print('letras contém vogais?', alfa.issuperset(vogais) )
# print('vogais contém letras?', vogais.issuperset(alfa) )
# ```
# 
# **Atividade**
# - Execute os exemplos e observe os resultados.

# In[ ]:





# ## Referências
# 
# [Python 2.7.16 documentation - Sets](https://docs.python.org/2/tutorial/datastructures.html#sets)  
# 
# **Outros materiais**
# 
# 
# [Caelum - Apostila Python e Oientação a objetos](https://www.caelum.com.br/apostila-python-orientacao-objetos/estrutura-de-dados/#conjuntos)  
# [Cadasnos Cicomp - Conjuntos ou sets no Python 3](https://cadernoscicomp.com.br/tutorial/introducao-a-programacao-em-python-3/conjuntos-ou-sets/)  
# [Igor Sobreira - Conjuntos em Python - set e frozenset](http://igorsobreira.com/2008/01/20/conjuntos-em-python-set-e-frozenset.html)  

# In[ ]:




