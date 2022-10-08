#!/usr/bin/env python
# coding: utf-8

# # Exercícios

# **Exercício**

# Implemente as funções `maior` e `menor`, que recebem como entrada 5 números. Uma delas retorna o maior valor e outra o menor valor.
# 
# > **Exemplo**
# > ```python
# maior(1,2,5,4,3) #retorna 5
# maior(91,22,-5,14,109) #retorna 109
# menor(1,2,5,4,3) #retorna 1
# menor(91,22,-5,14,109) #retorna -5
# ```

# In[ ]:





# **Exercício**

# Implemente a função `minmax`, que retorna o maior e o menor número, considerando 5 valores de entrada.
# 
# > **Exemplo**
# > ```python
# minmax(1,2,5,4,3) #retorna 1, 5
# minmax(91,22,-5,14,109) #retorna -5, 109
# >```

# In[ ]:





# **Exercício**

# Faça uma função chamada `tabuada` que recebe um número `n`, e apresenta a tabuada desse número na tela, com seu múltiplos de 1 a 10.
# 
# > **Exemplo**
# > - Entrada, com a chamada da função:
# >```python
# tabuada(5)
# >```
# > - Saída na tela:
# >```
# 5x1 = 5
# 5x2 = 10
# 5x3 = 15
# 5x4 = 20
# 5x5 = 25
# 5x6 = 30
# 5x7 = 35
# 5x8 = 40
# 5x9 = 45
# 5x10 = 50
# >```
# 
# 
# 
# 

# **Exercício**

# Implemente a função `fatorial`, que calcula e retorna o fatorial de um número. Considere que a entrada será sempre um número inteiro não negativo. Lembre também que por definição, $0!=0$.
# 
# > **Exemplo**
# > ```python
# fatorial(5) #retorna 120
# fatorial(8) #retorna 40320
# fatorial(0) #retorna 1
# fatorial(1) #retorna 1
# > ```

# In[ ]:





# **Exercício**

# Implemente um procedimento chamado `divdiv` que recebe dois inteiros: o dividendo e o divisor. O procedimento deve mostrar na tela:
# - o resultado inteiro da divisão,
# - o resto da divisão inteira e
# - o resultado da divisão, com precisão de 3 casas decimais.  
# 
# > **Dica**
# > 
# > Utilize a função `round(val,n)`, que arredonda `val` para `n` casas decimais.
# 
# > **Exemplo**
# > - Entrada
# > ```python
# divdiv(11,3)
# > ```
# > - Saída
# > ```
# resultado inteiro: 3
# resto: 2
# resultado: 3.667
# > ```

# In[ ]:





# **Exercício**

# Implemente uma função chamada `par`, que retorna `True` caso o valor passado por parâmetro seja par, e `False` caso contrário.
# 
# > **Exemplo**
# > ```python
# > par(3) #retorna False
# > par(0) #retorna True
# > par(9) #retorna False
# > par(200) #retorna True
# > ```

# In[ ]:





# **Exercício**

# Implemente uma função chamada `impar`, que retorna `True` caso o valor passado por parâmetro seja impar, e `False` caso o valor seja par.
# 
# > **Exemplo**
# > ```python
# > impar(3) #retorna True
# > impar(0) #retorna False
# > impar(9) #retorna True
# > impar(200) #retorna False
# > ```

# In[ ]:





# **Exercício**

# Implemente uma função chamada primo, que retorna `True` caso o valor passado por parâmetro seja um númeor primo, e `False` caso contrário.
# 
# > **Exemplo**
# > ```python
# > primo(3) #retorna True
# > primo(9) #retorna False
# > primo(200) #retorna False
# > primo(15) #retorna False
# > primo(37) #retorna True
# > primo(2521) #retorna True
# > ```

# In[ ]:





# **Exercício**

# Desenvolva uma função que calcula o número de combinações $C$ de $n$ elementos tomados $p$ a $p$.
# $$C^n_p = \frac{n!}{p!(n-p)!}$$
# 
# > **Exemplo**
# > ```python
# combinacao(7,2) #retorna 21
# combinacao(4,3) #retorna 4
# > ```

# In[ ]:





# **Exercício**

# Implemente uma função chamada perfeito, que retorna `True` caso o valor passado por
# parâmetro seja um número perfeito, e `False` caso contrário. Um número perfeito é aquele que é igual à soma de todos os seus divisores, exceto ele próprio.  
# 
# > **Exemplo**
# >
# > $6$ é um número perfeito, pois $6=1+2+3$.
# > ```python
# perfeito(6) #retorna True
# > ```

# In[ ]:





# **Exercício**

# Implemente uma função chamada `perfeitos` que recebe dois números inteiros `ini` e `fim` como parâmetro, e exibe na tela todos os números perfeitos que estão no intervalo entre `ini` e `fim`.
# 
# > **Exemplo**
# > ```
# perfeitos(2,10) #Mostra 6 na tela
# > ```

# In[ ]:





# **Exercício**

# Implemente uma função chamada `circuloArea`, que recebe como entrada o raio de um círculo, e retorna a área desse círculo.

# In[ ]:





# **Exercício**

# Implemente uma função chamada `primos`, que retorna todos os números primos em um intervalo especificado.

# In[ ]:





# **Exercício**

# Implemente uma função chamada `conversor_temperatura`, que recebe três parâmetros como entrada: 
# - um valor de temperatura (float), 
# - a escala da temperatura de entrada (char) e 
# - a escala da temperatura de saída (char).  
# Os possíveis valores para escala são C, F, K, R (maiúsculas ou minúsculas) que correspondem às escalas Celsius, Fahrenheit, Kelvin e Réaumur. A função deve retornar a temperatura informada na entrada para a temperatura na escala definida para saída.
# 
# > **Exemplo**
# > ```python
# conversor_temperatura(100.0, 'C', 'K') #retorna 373.15, pois 100º Celsius equivale a 273.15 Kelvin.
# conversor_temperatura(22.0, 'R', 'c') #retorna 27.5, pois 22º Réaumur equivale a 27.5º Celsius.
# > ```

# In[ ]:





# **Exercício**

# Faça uma função chamada `pot_2` que retorna `True` caso o parâmetro seja uma potência de 2.
# 
# > **Exemplo**
# > ```python
# pot_2(10) #retorna False
# pot_2(64) #retorna True
# > ```

# In[ ]:





# **Exercício**

# Desenvolva uma função chamada `pot_n`, que possui dois parâmetros $x$ e $n$. A função deve retornar `True` caso $x$ seja uma potência de $n$. Caso $n$ seja omitido, deve ser verificado se $x$ é uma potência de 2.
# 
# > **Exemplo**
# > ```python
# pot_n(25,5) #Retorna True pois 25 é potência de 5. 5^2 = 25.
# pot_n(25,2) #Retorna False pois 25 não é potência de 2.
# pot_n(1000) #Retorna False pois 1000 não é potência de 2.
# pot_n(1024) #Retorna True pois 1024 é potência de 2. 2^10=1024.
# pot_n(81,3) #Retorna True pois 27 é potência de 3. 3^4=27.
# > ```

# In[ ]:





# **Exercício**

# Implemente uma função chamada `distancia_pontos` que recebe dois pares de números, que correspondem a pontos em um plano cartesiano com coordenadas $x,y$. A função deve retornar a distância entre esses dois pontos. Não é necessário arredondar valores.
# 
# > **Exemplo**
# > ```python
# distancia_pontos(0,0,0,1) # retorna 1.0, pois a distância do ponto (0,0) a (0,1) é 1.
# distancia_pontos(5,3,7,0) # retorna 3.605551275463989, pois esta é a distância do ponto (5,3) ao ponto (7,0).
# distancia_pontos(3,0,6,4) # retorna 5.0, pois a distância do ponto (3,0) a (6,4) é 5.
# > ```

# In[ ]:





# **Exercício**

# Implemente uma função chamada `triangulo_perimetro`, que recebe três pares de números, que correspondem a coordenadas em um plano cartesiano. Tais coordenadas correspondem aos vértices de um triângulo. Calcule e retorno o perímetro do triângulo formado pelos pontos. Os parâmetros devem ser identificados como `x0`, `y0`, `x1`, `y1`, `x2` e `y2`.
# 
# > **Exemplo**
# > ```python
# triangulo_perimetro(0,0,1,1,1,0) # retorna 3.414213562373095, pois é o perímetro do triângulo formado pelos pontos (0,0), (1,1) e (1,0)
# triangulo_perimetro(0,0,3,4,3,0) # retorna 12.0, pois é o perímetro do triângulo formado pelos pontos (0,0), (3,4) e (3,0)
# > ```

# In[ ]:





# **Exercício**

# Faça um procedimento que recebe a idade de um nadador. Deve ser mostrado na tela a categoria em que o nadador deve competir, de acordo com a tabela apresentada.
# 
# |Idade (anos)|Categoria|
# |------------|---------|
# |5 a 7| Infantil A|
# |8 a 10|Infantil B|
# |11 a 13| Juvenil A|
# |14 a 17| Juvenil B|
# |18 e acima de 18| Adulto|
# 
# Fonte: Adaptado de [PINHO](https://www.inf.pucrs.br/~pinho/LaproI/Exercicios/Funcoes/lista.htm).  

# In[ ]:





# **Exercício**

# Escreva uma função chamada `soma_s` que tem como entrada um valor $n$, tal que $n$ pertence aos inteiros positivos. A função deve retornar o valor da soma S, onde:
# $$S = \frac{1}{1}+\frac{1}{2}+\frac{1}{3}+...+\frac{1}{n-1}+\frac{1}{n}$$
# 
# 

# In[ ]:





# **Exercício**

# Desenvolva um procedimento que "desenha" na tela um retângulo, com valores especificados pelo usuário. Devem ser passados os valores das dimensões (largura e altura), e os caracteres que compõem a borda e o preenchimento. Largura e altura devem ser sempre maiores que 2.
# 
# >**Exemplo**
# >
# >- Entrada:
#     - Largura=20
#     - Altura=5
#     - Borda=`X`
#     - Preenchimento=`_`
# >- Saída:
# > ```python
# XXXXXXXXXXXXXXXXXXXX
# X__________________X
# X__________________X
# X__________________X
# XXXXXXXXXXXXXXXXXXXX
# > ```
# 
# 
# Fonte: Adaptado de [OLIVEIRA](http://professor.pucgoias.edu.br/SiteDocente/admin/arquivosUpload/17504/material/cmp1048-lista_exercicios-01.pdf).  

# In[ ]:





# **Exercício**

# Implemente uma função para verificar se determinado valor é ou não regular. Um número é dito regular se sua decomposição em fatores primos apresenta apenas potências de 2, 3 e 5.
# 
# Fonte: Adaptado de [OLIVEIRA](http://professor.pucgoias.edu.br/SiteDocente/admin/arquivosUpload/17504/material/cmp1048-lista_exercicios-01.pdf).  

# In[ ]:





# **Exercício**

# Implemente uma função chamada `raiz_n`, que retorna a enésima raiz $r$ de um número, tendo como parâmetros o número $n$ e a raiz $x$. Caso o valor de $x$ não seja informado, a função deve retornar a raíz quadrada do número.   
# 
# $$r = \sqrt[n]{x}$$
# 
# >**Dica**
# >
# >$$\sqrt[n]{x} = x^\frac{1}{n}$$
# 
# > **Exemplo**
# > ```python
# raiz_n(27,3) #retorna 3.0
# raiz_n(15,4) #retorna 1.9679896712654303
# raiz_n(16,4) #retorna 2.0
# raiz_n(16) #retorna 4.0
# > ```

# ## Referências
# 
# [MORAES, S., PINHO, M.S., TERRA, E. Exercícios sobre Funções e Procedimentos. Escola Politécnica da PUCRS.](https://www.inf.pucrs.br/~pinho/LaproI/Exercicios/Funcoes/lista.htm)  
# [OLIVEIRA, M.G. Lista de exercícios: Funções.](http://professor.pucgoias.edu.br/SiteDocente/admin/arquivosUpload/17504/material/cmp1048-lista_exercicios-01.pdf)  
# 
# 
