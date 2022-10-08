#!/usr/bin/env python
# coding: utf-8

# # Expressões
# Uma expressão é uma combinação de elementos, que podem ser valores, variáveis, operadores e chamadas a funções. Com o uso das expressões é possível realizar cálculos que produzem novos valores, ou seja, fazem a transformação das informações.

# ## Variáveis
# Como visto anteriormente, variáveis são localizações na memória que armazenam dados.

# **Exemplo**
# 
# Um exemplo de expressão é `S = 5 + 4`, onde:
# - `5` e `4` são valores, 
# - `+` é um operador aritmético, 
# - `=` é o operador de atribuição, e
# - `S` é uma variável.
# 
# A execução desta expressão resulta em um novo valor, que será armazenado na variável `S`.

# ## Operadores

# Os operadores são utilizados para construir **expressões**, que podem conter diferentes quantidades de operandos.

# ### Tipos de operadores

# #### Atribuição
# A atribuição é o operador que que determina a passagem de valor para uma variável. Por definição toda variável pode ser seu valor alterado, e a modificação deste valor é realizada com o operador de atribuição.

# |Operador|Função|
# |--------|------|
# |`=`|atribuição|

# É possível realizar a atribuição de mais de uma variável em uma mesma expressão.

# **Exemplo**
# 
# ```py
# A = B = C = 5
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Python também suporta atribuição múltipla, com variáveis e valores separados por `,`

# **Exemplo**
# 
# ```py
# A, B = 10, 20
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# Com isso, pode-se alternar os valores entre variáveis.
# ```py
# A, B = B, A
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# #### Aritméticos
# São aqueles utilizados para a execução de operações matemáticas, adição, multiplicação, etc. São eles:

# |Operador|Função|
# |----|----------| 
# |`+` | adição | 
# |`-` | subtração | 
# |`*` | multiplicação | 
# |`/` | divisão | 
# |`%` | resto da divisão | 
# |`//`| parte inteira da divisão | 
# |`**`| exponenciação | 

# **Exemplos**
# 
# ```py
# 5+10  
# 8-4  
# 6*4  
# 10/5  
# 20%11
# 2**5
# 11//3
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# **Exercícios**
# - [Beecrowd 1003 - Soma Simples](https://www.beecrowd.com.br/judge/pt/problems/view/1003)
# - [Beecrowd 1004 - Produto Simples](https://www.beecrowd.com.br/judge/pt/problems/view/1004)
# - [Beecrowd 1007 - Diferença](https://www.beecrowd.com.br/judge/pt/problems/view/1007)

# #### Relacionais
# São operadores de comparação entre valores. As expressões realizadas com estes operadores retornam um resultado lógico, `True` ou `False`.
# 
# |Operador|Função|
# |---|---| 
# |`>`  |maior que|
# |`<`  |menor que| 
# |`==` |igual| 
# |`!=` |diferente|
# |`>=` |maior ou igual| 
# |`<=` |menor ou igual| 

# #### Lógicos
# 
# |Operador|Função|
# |--------|------|
# |`and`|**e** lógico|
# |`or` |**ou** lógico|
# |`not`|**não** lógico (negação)|

# #### Associação
# (*membership*, livre trad.)  
# Observa se um valor é membro de uma sequência ou conjunto.

# |Operador|Função| 
# |---|---|
# |`in`    | está contido| 
# |`not in`| não está contido| 

# **Exemplo**
# 
# ```py
# 'a' in 'batata'
# 'a' in 'pudim'
# 'a' not in 'pudim'
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# #### Identidade
# Os operadores de identidade servem para identificar se os parâmetros passados correspondem ao mesmo, e não apenas os mesmos valores.

# |Operador|Função| 
# |---|---|
# |`is`|verificação de identidade| 

# **Exemplo**
# 
# ```py
# x = 5.0
# y = 5.0
# z = x
# 
# x == y
# x is y
# x == z
# x is z
# 
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### Bit a bit
# Os opereradores binários são aqueles que operam sobre os valores em nível de bit

# |Operador|Função| 
# |---|---|
# |`&`|**e** lógico|
# |`\|`|**ou** lógico|
# |`~`|**não** lógico|
# |`^`|**xor** lógico (**ou exclusivo**)|
# |`>>`|deslocamento à direita|
# |`<<`|deslocamento à esquerda|
# 

# **Exemplo**
# 
# ```py
# A = 10 #(1010 em binário)
# B = 4  #(0100 em binário)
# C = 5  #(0101 em binário)
# A & B
# A | B
# ~A
# A ^ B
# B ^ C
# C << 1
# C >> 1
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### Agrupamento
# Os operadores de agrupamento servem para identificar expressões ou valores que devem ser reconhecidos como sendo um grupo.

# |Operadores|Função| 
# |---|---|
# |`(`, `)`|agrupamento de expressões| 
# |`[`, `]`|listas| 
# |`{`, `}`|conjuntos| 
# |`{`, `}`|dicionários| 
# |`(`, `)`|tuplas| 

# **Exemplo**
# 
# ```py
# 2+3*4
# (2+3)*4
# ```

# In[ ]:





# In[ ]:





# ## Operadores compostos
# É possível combinar alguns operadores, que realizam a operação utilizando os parâmetros passados ao operador, e em seguida realiza uma atribuição utilizando a variável à esquerda dos operadores.

# |Operador|Função| 
# |---|---|
# |`+=`| adição e atribuição| 
# |`-=`| subtração e atribuição| 
# |`*=`| multiplicação e atribuição| 
# |`/=`| divisão e atribuição| 
# |`//=`| divisão inteira e atribuição| 
# |`%=`| módulo e atribuição| 
# |`**=`| potência e atribuição| 
# |`&=`|**e** lógico e atribuição|
# |`\|=`|**ou** lógico e atribuição|
# |`^=`|**xor** lógico (**ou exclusivo**) e atribuição|
# |`>>=`|deslocamento à direita e atribuição|
# |`<<=`|deslocamento à esquerda e atribuição|
# 

# **Exemplo**
# 
# ```py
# X = 5
# X **=2
# print(X)
# ```

# In[ ]:





# ```py
# X = 4
# X <<= 2
# print(X)
# ```

# In[ ]:





# ## Prioridade entre operadores
# As prioridades definem quais operadores serão executados primeiro. Caso possuam a mesma prioridade, a expressão será executada da esquerda para a direita.

# Organizados da maior para menor prioridade:  
# 
# |Operadores|
# |---|
# |`()`,`[]`,`{}`|
# |`x[index]`,`x[index:index]`,`x(params)`,`x.attrib`|
# |`**`|
# |`+x`,`-x`, `~x`|
# |`*`,`@`,`/`,`//`,`%`|
# |`+`,`-`|
# |`<<`,`>>`|
# |`&`|
# |`^`|
# |`\|`|
# |`in`,`not in`,`is`,`is not`,`<`,`<=`,`>=`,`!=`,`==`|
# |`not x`|
# |`and`|
# |`or`| 
# |`if - else`|
# |`lambda`|
# |`=`|
# 
# Fonte: [PYTHON SOFTWARE FOUNDATION. Expressions - Python 3 documentation.](https://docs.python.org/3/reference/expressions.html#operator-precedence)

# **Exercícios**
#   
# - [Beecrowd 3055 - Nota Esquecida ](https://www.beecrowd.com.br/judge/pt/problems/view/3055)
# - [Beecrowd 2786 - Piso da Escola ](https://www.beecrowd.com.br/judge/pt/problems/view/2786)
# - [Beecrowd 1021 - Notas e Moedas ](https://www.beecrowd.com.br/judge/pt/problems/view/1021)

# In[ ]:





# ## Referências
# 
# [PYTHON SOFTWARE FOUNDATION. Expressions - Python 3 documentation.](https://docs.python.org/3/reference/expressions.html)  
# 

#   
