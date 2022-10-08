#!/usr/bin/env python
# coding: utf-8

# # Exercícios `elif`
# 
# Resolva os exercícios abaixo utilizando a linguagem de programação Python e estruturas `elif`.

# Faça um programa simula uma calculadora simples, perguntando ao usuários dois valores e um operador (+, -, \*, /). O programa deve mostrar o resultado da operação utilizando os operadores e o operador.

# In[ ]:





# Faça um programa em que o usuário entra com o número do dia da semana (1=domingo, 2=segunda-feira...) e o programa apresenta o dia da semana por extenso.

# In[ ]:





# Faça um programa em que o usuário digita o número do mês (1: janeiro, 2: fevereiro...), e o programa apresenta o nome do mês por extenso.

# In[ ]:





# Faça um programa em que o usuário digita o número do mês e tem como resultado o número de dias que aquele mês possui. Desconsidere anos bissextos.

# In[ ]:





# Faça um programa que mostra a data atual por extenso, e quantos dias faltam para o próximo mês.
# 
# **Exemplo de saída**  
# 
# ```
# Hoje é terça-feira, 10 de março de 2020. Faltam 14 dias para o próximo mês.
# ```
# 
# Para obter as informações sobre a data, utilize a biblioteca `datetime`, como no exemplo apresentado abaixo.
# 
# ```python
# import datetime
# dt = datetime.datetime.today()
# 
# ano = dt.year #Ano atual
# mes = dt.month #Mês atual
# diaMes = dt.day #Dia do mês atual
# diaSeM = dt.weekday() #Dia da semana atual
# ```
# 
# 

# In[ ]:





# Faça um programa que informa quantos dias já se passaram desde o início do ano. Desconsidere anos bissextos.

# In[ ]:





# Um banco concederá um crédito especial aos seus clientes, variável de acordo com com o saldo médio no último ano. Faça um algoritmo que a partir do saldo médio de um cliente calcula o valor do crédito de acordo com a tabela apresentada abaixo. Mostre uma mensagem informando o saldo médio e o valor do crédito a ser concedido ao cliente. 
# 
# |    Saldo médio       | Crédito concedido|
# |----------------------|------------------|
# |R\$ 0,00 a 200,00     | 0%               |
# |R\$ 201,00 a 400,00   | 20%              |
# |R\$ 401,00 a 600,00   | 30%              |
# |maior de R\$ 601,00   | 40%              |
# 

# In[ ]:




