#!/usr/bin/env python
# coding: utf-8

# # Equações polinomiais
# 
# A biblioteca numpy possui funções para o cálculo de polinômios, de ordem $n$.

# In[ ]:





# Utilizaremos também o módulo **pyplot** da biblioteca **matplotlib**, para plotar gráficos das funções. Para importar a biblioteca:
# ```py
# import matplotlib.pyplot as plt
# %matplotlib inline
# ```
# O comando `%matplotlib inline` indica ao Jupyter para plotar os gráficos diretamente no Jupyter.

# In[ ]:





# ## Gráficos

# Antes de iniciar com os polinômios, faremos alguns exemplos utilizando gráficos. Para plotar um gráfico, é necessário indicar quais são os pontos $x$ e $y$ que devem ser mostrados. O gráfico de *scatter* serve para essa finalidade.
# 
# ```py
# x = [1,2,3,4,5]
# y = [1,2,1,2,3]
# plt.scatter(x,y)
# ```

# In[ ]:





# **Exemplo**
# 
# Plotando os pontos da função $x^2$.
# 
# ```py
# x = np.arange(5)
# y = x**2
# plt.scatter(x,y)
# ```
# 

# In[ ]:





# Com a função `plot` do módulo `pyplot` é possível fazer o gráfico de linhas, de forma que estas interligam cada ponto.
# 
# **Exemplo**
# ```py
# x = np.arange(3)
# y = x**2
# plt.plot(x,y)
# ```

# In[ ]:





# **Atividade**
# 
# Com a função $x^2$, faça:
# - Aumente o número de pontos para 5 e plote um gráfico de linhas
# - Aumente o número de pontos para 10 e plote um gráfico de linhas
# - Aumente o número de pontos para 100 e plote um gráfico de linhas
# 

# In[ ]:





# O parâmetro `c` permite que seja escolhida a cor do gráfico.
# **Exemplo**
# 
# ```py
# x = np.arange(3)
# y = x**2
# plt.scatter(x,y, c='r')
# ```

# In[ ]:





# Outra possibilidade são várias funções no mesmo gráfico.
# **Exemplo**
# 
# ```py
# x = np.arange(-10,10)
# y0 = x**2
# y1 = x+10
# plt.plot(x,y0, c='r')
# plt.plot(x,y1, c='k')
# ```

# In[ ]:





# **Atividade**
# 
# Plote o gráfico de linhas da função $x^2$, com 1000 valores de $x$, indo de -100 a 100. Compare a diferença com o gráfico da atividade anterior.

# In[ ]:





# **Polinômios**
# 
# A representação de um polinômio com uma lista que consiste nos **coeficientes** do polinômio. A função `polyval` calcula os valores de $y$ para uma entrada $x$ utilizando os coeficientes definidos.
# 
# **Exemplo**
# 
# Na função $$y=2x^2 + 5x + 1$$ os coeficientes são 2, 5 e 1.
# ```py
# coefs=[2,5,1]
# x=np.arange(10)
# y = np.polyval(coefs,x)
# plt.plot(x,y)
# ```

# In[ ]:





# **Atividade**
# 
# Faça o gráfico de linha da equação $2x^2 + 5x + 1$, com valores para $x$ de -100 a 100.

# In[ ]:





# **Atividade**
# 
# Faça o gráfico da equação $$y=x^3-4x^2+2x+3$$ para $x$ de -100 a 100.

# In[ ]:





# **Atividade**
# 
# Plote um gráfico de linha que contenha o gráfico de duas funções, o do polinômio $x^3-4x^2+2x+3$ e uma reta interligando os pontos inicial e final do polinômio. Utilize cores diferentes, e valores de $x$ de -100 a 100.

# In[ ]:





# ## Raízes de um polinômio
# É possível obter as raízes de determinado polinômio, utilizando a função `np.roots()`.
# 
# **Exemplo**
# 
# As raízes do polinômio $$y=x^2-5$$
# ```py
# coefs=[1,0,-5]
# raizes = np.roots(coefs)
# print(raizes)
# ```

# In[ ]:





# In[ ]:





# **Atividade**
# 
# Calcule as raízes do polinômio $$y=-x^3-4x^2+2x+3$$
# Plote o gráfico do polinômio e também os pontos das raízes.

# In[ ]:





# **Atividade**
# 
# Plote o gráfico e calcule as raízes do polinômio $$y=x^2+2$$
# - Observe o gráfico e as raízes, e explique o resultado.
# - Qual é o tipo de dado utilizado nas raízes?

# In[ ]:





# In[ ]:





# ## Referências
# 
# [SCIPY. numpy.polyval](https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyval.html#numpy.polyval)  
# [SCIPY. numpy.roots](https://docs.scipy.org/doc/numpy/reference/generated/numpy.roots.html)
# 

# In[ ]:




