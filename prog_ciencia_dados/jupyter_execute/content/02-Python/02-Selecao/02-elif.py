#!/usr/bin/env python
# coding: utf-8

# # elif
# A estrutura `elif` opera como diversas estruturas `if` encadeadas. Um `elif` será executado apenas se a condição presente no `if` ou `elif` anterior seja falsa (`False`).
# 
# A linguagem Python utiliza o `elif` em substiuição às estruturas de seleção `case` ou `switch-case` presentes em outras linguagens de programação, como Pascal, C e Java.

# **Sintaxe**  
# 
# ```python
# if <condição1 >:
#     <código if>
# elif <condição2>:
#     <código elif>
# elif <condição2>:
#     <código elif>
# elif <condição3>:
#     <código elif>
# else:
#     <código else>
# ```
# 
# O código acima seria equivalente a
# ```python
# if <condição1>:
#     <código if>
# else:
#     if <condição2>:
#         <código if>
#     else:
#         if <condição3>:
#             <código if>
#         else:
#             <código else>
# ```
# 

# **Exemplo**  
# Faça um programa em que o usuário digita um número entre 0 e 9, e o número é mostrado por extenso.
# 
# ```python
# n = int(input('Entre com um número entre 0 e 9'))
# if n == 0:
#     print('zero')
# elif n == 1:
#     print('um')
# elif n == 2:
#     print('dois')
# elif n == 3:
#     print('tres')
# elif n == 4:
#     print('quatro')
# elif n == 5:
#     print('cinco')
# elif n == 6:
#     print('seis')
# elif n == 7:
#     print('sete')
# elif n == 8:
#     print('oito')
# elif n == 9:
#     print('nove')
# ```

# **Observação**  
# Quando o código presente na estrutura `if`, `else` ou `elif` possuir uma única linha, é possível inserí-lo diretamente após o `:`. Em algumas situações esta prática melhora a legibilidade do código, mantendo a mesma funcionalidade.
# 
# **Exemplo**  
# ```python
# n = int(input('Entre com um número entre 0 e 9'))
# if   n == 0: print('zero')
# elif n == 1: print('um')
# elif n == 2: print('dois')
# elif n == 3: print('tres')
# elif n == 4: print('quatro')
# elif n == 5: print('cinco')
# elif n == 6: print('seis')
# elif n == 7: print('sete')
# elif n == 8: print('oito')
# elif n == 9: print('nove')
# ```

# In[ ]:





# In[ ]:





# In[ ]:




