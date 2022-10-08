#!/usr/bin/env python
# coding: utf-8

# # Funções

# **Funções** são trechos de código definidos em um região específica, e podem ser **chamados** de acordo com a necessidade. Dentre as principais vantagens, aqui destacamos:
# - Possibilidade de codificação uma única vez para trechos que se repetem. Isto também possibilita o **reaproveitamento de código**.
# - Organização do código, com seções especializadas em determinadas funcionalidades.

# **Exemplo**
# - Desenvolva uma aplicação que mostra uma mensagem de bom dia.
#     - Sem o uso de função:
#     ```python
#     print('Bom dia')
#     ```
#     - Com o uso de função:
#     ```python
#     def bomdia():
#         print('Bom dia')
#     ```
#     ```python
#     bomdia()
#     ```
#     
# Observe que foi definido um trecho de código com o procedimento, que inicia com a palavra reservada `def`. Os procedimentos são identificados por um **nome**, neste caso `bomdia`. Com isto, sempre que nome do procedimento for invocado, o trecho de código definido será executado.
# 
# **Atividade**
# - Execute o exemplo, com e sem o uso de procedimentos.

# In[ ]:





# Com isto, trechos de código podem ser reaproveitados. A rotina é programada uma única vez, e pode ser chamada diversas vezes.
# 
# **Exemplo**
# 
# ```python
# def bomdia():
#     print('Bom dia')
# ```
# ```python
# bomdia()
# bomdia()
# bomdia()
# ```
# 
# **Atividade**  
# 
# - Execute o exemplo.

# In[ ]:





# Agora, adicionaremos uma entrada à nossa função. A entrada de uma função é dita ser um **parâmetro**, contendo uma variável que terá seu valor alterado durante a execução da função.
# 
# **Exemplo**  
# - Desenvolva uma função que mostra bom dia, junto com o nome de usuário na tela.
# 
# ```python
# def hello_user(user):
#     print('Bom dia,', user)
# ```
# ```python
# hello_user('Celso')
# hello_user('Cesar')
# hello_user('Jonas')
# ```
# 
# Ou seja, o código da função é repetido, e o valor passado para a variável `user` no momento da chamada da função é utilizado durante a execução. A função `print()` é chamada apenas dentro da função `hello_user`.
# 
# **Atividade**
# 
# - Execute o exemplo

# In[ ]:





# ## Retorno

# Ao invés de apenas mostrar o resultado na tela, uma função também pode retornar um valor para onde foi chamada.
# 
# **Exemplo**
# 
# - Considere a função que calcula o quadrado de um número:
#     - Sem retorno de valor:
#     ```python
#     def quadrado(valor):
#         quad = valor*valor
#         print(quad)
#     ```
#     ```python
#     quadrado(5)
#     quadrado(15)
#     quadrado(7)
#     ```
#     - Com retorno de valor:
#     ```python
#     def quadrado_retorno(valor):
#         quad = valor*valor
#         return quad
#     ```
#     ```python
#     q = quadrado_retorno(5)
#     print(q)
#     q = quadrado_retorno(15)
#     print(q)
#     q = quadrado_retorno(7)
#     print(q)
#     ```
#     
# No primeiro caso, a função sem retorno apresenta o resultado diretamente. Na função com retorno, um valor é retornado e armazenado em uma variável.
# 
# **Atividade**
# - Execute os exemplos, com e sem retorno de valores

# In[ ]:





# Em Python, para definir procedimentos e funções utilizamos a palavra reservada `def`. Ao trecho em que codificamos a função chamamos de **declaração da função**, composto por **cabeçalho** e **código** da função. O cabeçalho possui as especificações de como a função deve ser chamada, e o código corresponde a o que será executado quando a função for chamada.
# 
# **Sintaxe**
# 
# ``` py
# def <nome da função>(parâmetros):
#     código
#     return <valor>
# ```
# Observe:
# - Cabeçalho da função:
#     - Inicia com `def`
#     - `<nome>` corresponde a uma palavra que será utilizada para chamar a função
#     - `(parâmetros)` após o nome
#         - O uso de parâmetros é opcional. Caso não haja parâmetros, basta deixar vazio `()`
#     - `:` 
# - Código da função:
#     - Código que será executado quando a função for chamada.
#     - `<tab>` para definição do escopo da função.
#     - `return` seguido é o valor que será retornado à variável
#         - O retorno não é obrigatório.

# In[ ]:





# Como Python permite atribuição múltipla, isso também pode ser aplicado ao retorno de funções.
# 
# **Exemplo**  
# 
# ```python
# def dois_e_Dez():
#     x=2
#     y=10
#     return x,y
# 
# a,b = dois_e_Dez()
# print('a:', a)
# print('b:', b)
# ```

# In[ ]:





# ## Parâmetros

# ### Parâmetros por posição
# 
# Os **parâmetros** de uma função são os dados de entrada para a função. Cada parâmetro corresponde a uma declaração de variável que será utilizada dentro do código da função.
# 
#  **Exemplo**
#  
# ```python
# def soma(a, b):
#     c = a+b
#     return c
# ```
# ```python
# x=soma(5,7)
# print(x)
# ```
# ```python
# y=soma(2,3)
# print(y)
# ```
# ```python
# z=soma(0,0)
# print(z)
# ```  
# >**Observação**  
# >
# >A **ordem** em que os parâmetros são declarados é a mesma ordem em que eles são chamados. `a` corresponde à primeira variável e `b` à segunda. Ao chamar `soma(5,7)`, `a=5` e `b=7`. Observe que o resultado da função (`return`) é o que será armazenado na variável `x`, dado que `x=soma(5,7)`.
# 

# In[ ]:





# **Atividades**
# 
# 1. Implememente a função `addMul`, que retorna o valor da operação $$a+b+c+a*b*c$$
# 
# 1. Implemente a função `par`, que retorna `True` caso o valor da entrada seja par, e `False` caso seja ímpar.
# 
# 1. Implemente uma função chamada `segToMin` que recebe um valor que coresponde a uma quantidade de segundos, e mostre na tela a quantidade de minutos e segundos correspondente à entrada.
# 
# **Exemplo**  
#  
# - Entrada:
# ```
# 132
# ```  
# - Saída:  
# ```
# 2 minutos e 12 segundos.  
# ```
# 

# In[ ]:





# ### Parâmetros por nome
# 
# Em Python, podemos identificar os parâmetros por nome, de maneira que a ordem que serão chamados não influencia o cálculo.
# 
# **Exemplo**
#  
# ```py
# def imc(peso, altura):
#     return peso/altura**2
# p, a = 90, 1.85
# print(imc(p,a)) #ordem correta
# print(imc(a,p)) #ordem errada
# ```
# 
# Para tal, pode-se informar de maneira explícita quais serão os valores de cada parâmetro no momento da chamada da função.
# ```py
# print(imc(peso=p, altura=a)) #ordem não importa
# print(imc(altura=a, peso=p)) #ordem não importa
# ```
# 
# Desta forma, identificando os parâmetros, a ordem em que eles são passados não interfere no cálculo da função.

# In[ ]:





# ### Valores padrão para argumentos
# 
# Omitir um argumento na chamada de uma função ocasiona em um erro:
# 
# **Exemplo**
# 
# ```py
# def contar(val):
#     for i in range(1,val+1):
#         print(i)
# contar(5) #OK
# contar()  #ERRO. A função precisa de um valor de entrada
# ```
# 
# Para isso, pode-se definir um valor padrão, informando à função qual valor utilizar quando aquele valor não for informado.
# ```py
# def contar(val=10):
#     for i in range(1,val+1):
#         print(i)
# contar(5) #ok
# contar()  #ok, utilizará o valor padrão
# ```

# In[ ]:





# ## Referências
# 
# [The Python software foundation. Compound statments: function definition. Python 3.8.5 documentation](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)  
# 
# 
# **Outros materiais**
# 
# [REIS, G. Funções em Python: entendendo parâmetros, argumentos, args e kwargs. Medium, 2019](https://medium.com/luizalabs/fun%C3%A7%C3%B5es-em-python-entendendo-par%C3%A2metros-argumentos-args-e-kwargs-4291b1f817f6)  
# 
# 

#  
