#!/usr/bin/env python
# coding: utf-8

# # A linguagem

# Python é uma linguagem de programação interpretada e orientada a objetos. Tem crescido muito nos últimos anos, visto sua portabilidade, alto nível e compatibilidade com diversos sistemas e outras linguagens.

# A linguagem possui diversas características, como
# - A identação define os blocos
# - Os tipos de variáveis são definidos pelo tipo do dado que lhe é atribuído

# As versões de Python não são retrocompatíveis. Exemplo: um código desenvolvido para Python versão 2.x não irá funcionar quando executado em versões 3.x.
# 
# Para verificar a versão atual:
# ```bash
# python --version
# ```

# ## Entrada e saída de dados
# 
# Inicialmente trataremos a entrada de dados como sendo a partir da entrada padrão e saída padrão. Comumente, a entrada padrão é o teclado e a saída padrão é a tela.
# 
# As funções nativas básicas que utilizaremos são:
# 
# - `print()`
# - `input()`
# 
# `print()`
# 
# A função `print()` mostra dados na saída padrão.
# 
# **Exemplo**  
# 
# ```python
# print('Hello world!')
# total = 10
# print('O valor total é', total)
# ```

# In[ ]:





# `input()`
# 
# A função `input()` trata de obter os dados a partir da entrada padrão.
# 
# **Exemplo**  
# 
# ```python
# valor = input('Entre com um valor: ')
# print('O valor digitado é:', valor)
# ```

# In[ ]:





# No Python 3, a saída da função `input()` é do tipo cadeia de caracteres (*string*).  
# 
# **Exemplo**  
# ```python
# nome = input('Entre com seu nome:')
# print('Olá', nome, '. Seja bem vindo ao sistema.')
# ```

# In[ ]:





# Neste caso, para que operações sejam realizadas com tipos específicos, é necessário fazer a conversão do dado para o qual se deseja trabalhar. A não conversão pode resultar em um erro.
# 
# **Exemplo**  
# ```python
# val = input('Entre com um valor:')
# quad = val * val #Aqui ocorre um erro. Val não é numérico
# print('O quadrado de',val,'é',quad)
# ```

# In[ ]:





# Nestas situações, é necessário fazer a conversão para o formato desejado.
# ```python
# val = input('Entre com um valor:')
# val = int(val) #converte a entrada para inteiro
# quad = val * val #Aqui ocorre um erro. Val não é numérico
# print('O quadrado de',val,'é',quad)
# ```

# In[ ]:




