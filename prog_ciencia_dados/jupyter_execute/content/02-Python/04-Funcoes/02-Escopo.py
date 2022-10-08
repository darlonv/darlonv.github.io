#!/usr/bin/env python
# coding: utf-8

# # Escopo de variáveis

# É chamado de **escopo** ao espaço onde onde uma variável pode ser utilizada. Comumente, o escopo pode ser **local** ou **global**.
# 
# **Exemplo**  
# - Variável local, só existe dentro da função.
# 
# ```python
# def mostra_local(v): #variável v dentro da função
#     print('valor: ', v) #variável v existe dentro da função
# ```
# ```python
# mostra_local(5) #Valor será passado à variável v
# print(v)  #ERRO. A variável v não existe fora da função
# ```

# In[ ]:





# **Exemplo** 
# - Variável global, existe fora da função e função a acessa.
#  
#  ```python
# def mostra_valor_global():
#    #variável g existe fora da função
#     print('valor: ', g) 
# ```
# ```python
# g = 10
# mostra_valor_global()
# print(g) #OK. Variável g existe fora da função
# ```
# 

# In[ ]:





# In[ ]:





# **Exemplo**
# 
# - Variável global existe, e função modifica o valor dela.
# 
# ```python
# def tenta_alterar_global():
#     h=5
#     #variável h existe fora e dentro da função
#     print('valor: ', h) 
# ```
# ```python
# h = 20
# tenta_alterar_global()
# print(h) #OK. Variável g existe fora da função
# ```
# >**Observação**  
# >
# >O valor original da variável global não foi alterado. Neste caso, uma variável local foi criada dentro da função, e a variável global foi mantida.

# In[ ]:





# **Exemplo**
# 
# - Variável global existe, e função modifica o valor dela.
# 
# ```python
# def altera_global():
#     global i #identifica que a variável é global
#     i=5 #altera o valor da variável global
#     print('valor: ', i) 
# ```
# ```python
# i = 20
# print('Antes da função:',i) #OK. Variável i com valor original
# altera_global() #chamada da função
# print('Após função:',i) #OK. Variável i foi alterada dentro da função
# ```

# In[ ]:





#  **Exemplo**
# 
# - Variável global não existe e função tenta utilizar o valor dela, resultando em erro.
# :
# ```python
# def mostra_global_ne():
#     global j
#     print('valor: ', j) #ERRO. Variável global não existe
# ```
# ```python
# mostra_global_ne() #chamada da função
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
