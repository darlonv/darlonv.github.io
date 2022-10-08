#!/usr/bin/env python
# coding: utf-8

# # Exercícios

# **Exercício**
# 
# Qual é a saída do trecho de código abaixo? Tente responder antes de executar.
# 
# ```py
# for i in 1,2,3 :
#     print(1, end='')
# ```
# 
# 1. `3`
# 1. `i`
# 1. `123`
# 1. `ERRO`
# 1. `111`

# In[1]:


#111


# **Exercício**
# 
# Qual é a saída do trecho de código abaixo? Tente responder antes de executar.
# 
# ```py
# for i in 1,2,3 :
# print(i, end='')
# ```
# 
# 1. `3`
# 1. `i`
# 1. `1 2 3`
# 1. `IndentationError`
# 1. `123`

# In[2]:


#IndentationError


# **Exercício**
# 
# Peça o usuário que digite $5$ números, com valores que podem ser entre $0$ e $1000$. Mostre o maior e menor número digitados.

# In[3]:


import random

n = 5
menor = 1000
maior = 0

for i in range(n):
    val = r = random.randint(0,1000)
    if val < menor:
        menor = val
    if val > maior:
        maior = val
print('Menor: ', menor)
print('Maior: ', maior)


# **Exercício**
# 
# Mostre os números de $n$ a $1$, na ordem do maior para o menor.

# In[4]:


n = 5
for i in range(n,0, -1):
    print(i, end=' ')


# **Exercício**
# 
# Pergunte um número $k$ ao usuário, e mostre a tabuada desse número, com múltiplos de $1$ a $20$.

# In[5]:


k=10
for i in range(1,21):
    print(f'{k}x{i}={k*i}')


# **Exercício**
# 
# 
# Calcule a soma $s$ e a média $m$ dos primeiros $n$ números, começando por $1$, de forma que $n$ é digitado pelo usuário.  
# Matematicamente, isto é equivalente a:
# 
# $$s = \sum_{i=1}^ni$$
# 
# $$m = \frac{\sum_{i=1}^ni}{n} = \frac{s}{n}$$ 

# In[6]:


n = 10
S = 0
for i in range(1,n+1):
    S+=i
M = S/n

print('Soma :', S)
print('Média:', M)


# **Exercício**
# 
# Calcula a soma $s$ e a média $m$ de todos os números inteiros no intervalo $[a,b]$, de forma que $a$ e $b$ são digitados pelo usuário.  
# 
# De forma matemática:  
# 
# $$s = \sum_{i=a}^{b}i$$
# 
# $$m = \frac{\sum_{i=a}^{b}i}{b-a+1} = \frac{s}{b-a+1}$$ 

# In[7]:


ini = 4
fim = 5
n = fim - ini + 1

S = 0
for i in range(ini,fim+1):
    S+=i
M = S/n

print('Soma :', S)
print('Média:', M)


# **Exercício**
# 
# Pergunte um número $x$ ao usuário, e então mostre todos os números de $1$ a $100$ que são divisíveis por $x$.

# In[8]:


x = 15
for i in range(1,100+1):
    if i%x == 0:
        print(i)


# **Exercício**
# 
# Calcule o fatorial $f$ de um número $x$, tal que $x$ é digitado pelo usuário.  
# De forma matemática:
# 
# $$f=x!$$
# $$f= x\times(x-1)\times(x-2)\times...\times2\times1$$

# In[9]:


x = 5
F = 1
for i in range(1,x+1):
    F*=i
print(f'F({x})={F}')


# **Exercício**
# 
# Faça um programa para calcular a soma dos números pares no intervalo $[a,b]$, tal que $a$ e $b$ são digitados pelo usuário.

# In[10]:


ini = 4
fim = 8

S = 0
for i in range(ini,fim+1):
    if i%2 == 0:
        S+=i

print('Soma :', S)


# **Exercício**
# 
# Pergunte $n$ ao usuário, e informe se $n$ é ou não um número primo. Considere que o primeiro número primo é $2$.

# In[11]:


primo = True
n = 13

for i in range(2,n):
    if n%i==0:
        primo=False
        break

print(primo)


# **Exercício**
# 
# Mostre todos os números entre $500$ e $2000$ que, quando divididos por $11$, possuem resto da divisão igual a $5$.

# In[12]:


for i in range(500,2000+1):
    if i%11==0:
        print(i, end=',')


# **Exercício**
# 
# Pergunte $n$ ao usuário, e mostre a seguinte soma $s$, de forma que:
# 
# $$
# s = 1/1 + 1/2 + 1/2 + 1/n
# $$  
# 
# que, matematicamente é:
# 
# $$
# \sum_{i=1}^{n}\frac{1}{i}
# $$

# In[13]:


n=2
S=0
for i in range(1,n+1):
    S+=(1/i)
print(f'S={S}')


# **Exercício**
# 
# Desenvolva um algoritmo que mostra todos os divisores de um número que são menores que ele.
# 
# **Exemplo**
# 
# Para `n=20`:
# ```
# Divisores:
# 1
# 2
# 4
# 5
# 10
# ```
# Para `n=81`:
# ```
# Divisores:
# 1
# 3
# 9
# 27
# ```

# In[14]:


n = 81
for i in range(1,n):
    if n%i==0:
        print(i)


# **Exercício**
# 
# Dado um número $n$, inteiro e positivo, dizemos que $n$ é perfeito se $n$ for igual à soma de seus divisores positivos e diferentes de $n$. Desenvolva um algoritmo que verifica se determinado número é perfeito.  
# 
# **Exemplo**
# 
# Para `n=6`:
# ```
# True
# ```
# 
# $6$ é perfeito, pois $6=3+2+1$.
# 
# Para `n=15`:
# ```
# False
# ```
# 
# $15$ não é perfeito, pois $15\neq5+3+1$.

# In[15]:


n=6
S=0

for i in range(1,n):
    if n%i==0:
        S+=i

if S==n:
    print(True)
else:
    print(False)


# **Exercício**
# 
# Pergunte ao usuário dois números, $x$ e $y$, e mostre todos os números perfeitos no intervalo $[x,y]$.

# In[16]:


ini=4
fim=1000
for k in range(ini,fim+1):
    n=k
    S=0

    for i in range(1,n):
        if n%i==0:
            S+=i

    if S==n:
        print(k)


# **Exercício**
# 
# Calcule e mostre a sequência de Fibonacci $F$, de $1$ até $n$.  
# Considere:  
# 
# $$
# F(1)=1\\
# F(2)=1\\
# F(n) = F(n-1)+F(n-2)\\
# $$
# 
# **Exemplo**
# 
# Para `n=11`:
# ```
# 1 1 2 3 5 8 13 21 34 55 89 
# ```

# In[17]:


n=11
for i in range(1,n+1):
    if i == 1:
        F = 1
    elif i == 2:
        F2 = 1
        F = 1
    else:
        nF = F2 + F
        F2 = F
        F = nF
    
    print(F,end=' ')
print('')


# **Exercício**
# 
# Faça um programa que pergunte $n$ ao usuário, tal que $n$ corresponde ao número de linhas, que devem ser impressas de acordo com o padrão mostrado no exemplo.
# 
# **Exemplo**
# 
# Para `n=5`: 
# ```
# *
# **
# ***
# ****
# *****
# ```

# In[18]:


n=5
for k in range(n):
    for j in range(0,k+1):
        print('*', end='')
    print('')


#  
