#!/usr/bin/env python
# coding: utf-8

# # *Strings*
# 
# O tipo `str` corresponde às *strings*. Uma *string* é uma **sequência** de caracteres, e denota-se um dado como uma *string* colocando seu conteúdo entre aspas simples (`'`) ou aspas duplas (`"`), de maneira equivalente. Cada elemento é um caractere.
# 
# **Exemplo**
# 
# A variável `s` recebe o texto `pudim`, e em seguida observa-se o tipo da variável `s`.
# ```python
# s = 'pudim'
# type(s)
# ```

# In[ ]:





# Como uma *string* é uma sequência, pode-se acessar cada elemento (caractere) pela sua posição.  
# 
# **Exemplo**
# 
# Pode-se acessar o primeiro caracter (`'p'`) acessando a posição 0, e o terceiro caracter (`'d'`) acessando a posição 2.
# ```python
# print(s[0])
# print(s[2])
# ```

# In[ ]:





# **Atividade**
# 
# - Crie uma variável *string* chamada `p`, com o conteúdo `programação`. 
# - Mostre todos os caracteres de `p` nas posições de número par.

# In[ ]:





# ## Operações sobre sequências
# 
# Algumas operações podem ser realizadas diretamente sobre sequências.
# 
# - `+`: concatena duas sequências;
# - `*`: repete uma sequência diversas vezes;
# - `in`: verifica se um item está ou não em uma sequência;
# - `not in`: verifica se um item **não está** em uma sequência.
# 
# **Exemplo**
# 
# ```python
# pares=[2,4,6,8]
# vogais=['a','e','i','o','u']
# print(pares+vogais)
# print(vogais*3)
# print(5 in pares)
# print('a' not in vogais)
# ```
# 
# 

# In[ ]:





# **Exercícios**  
# - [Beecrowd 3300 - Números Má Sorte Recarregados](https://www.beecrowd.com.br/judge/pt/problems/view/3300)
# - [Beecrowd 2242 - Huaauhahhuahau](https://www.beecrowd.com.br/judge/pt/problems/view/2242)

# ## Operações específicas

# Outros métodos sobre *strings* podem ser conferidos na tabela apresentada a seguir. Todos os métodos disponíveis podem ser consultados na API da linguagem.[PYTHON. Built-in methods: string methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
# 
# - `.capitalize()`: converte a primeira letra para maiúscula;
# - `.lower()`: converte as letras para minúsculas;
# - `.upper()`: converte as letras para maiúsculas;
# - `.islower()`: verifica se todos os caracteres são letras minúsculas;
# - `.isupper()`: verifica se todas os caracteres são letras maiúsculas;
# - `.split()`: divide em várias outras *strings*, de acordo com algum caractere de separação;
# - `.find(b)`: retorna a posição *string* `a` aparece;
# - `.replace(a, b)`: substitui na *string* as *substrings* `a` por `b`;
# - `.strip()`: remove espaços existentes no início e fim da *string*;
# - `.format()`: formata a *string*, podendo realizar substituição de variáveis.
# 
# 
# **Exemplos**
# 
# ```python
# frase='  um EXEMPLO interessante.  '
# print(frase.capitalize())
# print(frase.lower())
# print(frase.upper())
# print(frase.islower())
# print(frase.isupper())
# print(frase.split(' '))
# print(frase.find('inter'))
# print(frase.replace('inter','estr'))
# print(frase.strip())
# 
# valor1, valor2, soma = 25,5,30
# print('A soma de {} e {} é {}.'.format(valor1, valor2, soma))
# ```
# **Atividade**  
# - Execute os exemplos apresentados acima.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Formatação
# ### Substituição
# O método `.format()` merece destaque aqui. Com ele, é possível utilizar o de maneira simplificada a apresentação de informações. Neste, o local em que os dados serão incluídos é marcado com `{}`, e os valores a serem inseridos, na ordem, são passados como parâmetro ao método `.format()`.
# 
# **Exemplo**
# ```python
# v=6
# q=v**2
# c=v**3
# print(v,'ao quadrado é igual a', q, ', e', v, 'ao cubo é igual a',c,'.')
# print('{} ao quadrado é igual a {} , e {} ao cubo é igual a {}'.format(v, q, v, c))
# ```
# **Atividade**
# - Execute o exemplo.

# In[ ]:





# Outra forma de de fomatação é adicionar `f` ao início da *string*, e os valores pode ser informados diretamente no local onde deverão aparecer.
# 
# **Exemplo**  
# ```python
# print(f'{v} ao quadrado é igual a {q} , e {v} ao cubo é igual a {c}')
# ```
# **Atividade**
# - Execute o exemplo.

# In[ ]:





# In[ ]:





# Outra maneira é nomear o argumento na *string*. Com isso, a ordem dos parâmetros no momento de informar pode variar.
# 
# **Exemplo**  
# 
# - Observe que independente da ordem dos parâmetros, a saída é idêntica
# 
# ```python
# print('{dia} de {mes} de {ano}'.format(dia='4', mes='abril', ano='2005'))
# print('{dia} de {mes} de {ano}'.format(ano='2005', dia='4', mes='abril'))
# ```

# In[ ]:





# ### Espaço do valor
# Outra possibilidade é especificar qual o tamanho do espaço que o valor deve ocupar.  
# 
# **Exemplo**
# - A *string* deve ocupar o espaço de no mínimo 7 caracteres:
# 
# ```python
# print('-{:7}-'.format('abc'))
# print('-{:7}-'.format('paralelepípedo'))
# ```
# 
# **Exemplo**
# - A *string* deve ocupar o espaço de no máximo 7 caracteres, truncando os caracteres no espaço.
# 
# ```python
# print('-{:.7}-'.format('abc'))
# print('-{:.7}-'.format('paralelepípedo'))
# ```
# **Atividade**
# - Execute os exemplos e observe as diferenças.

# In[ ]:





# In[ ]:





# ### Alinhamento
# Também é possível especificar o alinhamento. À esquerda, centralizado ou à direita.  
# **Exemplo**
# ```python
# print('-{:7}-'.format('abc'))  #padrão
# print('-{:<7}-'.format('abc')) #à esquerda
# print('-{:^7}-'.format('abc')) #centralizado
# print('-{:>7}-'.format('abc')) #à direita
# ```

# In[ ]:





# Também possível truncar, definir o espaço e alinhar simultaneamente.  
# 
# **Exemplo**  
# ```python
# print('-{:>7.5}-'.format('paralelepípedo')) #espaço de 7 caracteres, truncando em 5 e alinhando à direita
# ```

# In[ ]:





# ### Tipos de dados
# Na formatação de *strings* também é possível manipular como determinados tipos de dados aparecem.
# 
# |código |significado|
# |-------|:----------|
# |`:d`   |int        |
# |`:+d`  |int com sinal  |
# |`:=+nd`|Sinal no início do espaço de tamanho `n`|
# |`:f`   |float      |
# |`:.nf` |float com precisão `n`|
# |`:+.nf`|float com sinal e precisão `n`|
# 
# 
# **Exemplo**
# - `:d`
# 
# ```python
# print('{:d}'.format(42))   #42
# print('{:d}'.format(-42))  #-42
# ```

# In[ ]:





# **Exemplo**
# 
# - `:+d`
# 
# ```python
# print('{:+d}'.format(42))   #+42
# print('{:+d}'.format(-42))  #-42
# ```

# In[ ]:





# **Exemplo**  
# 
# - `:=+nd`
# 
# ```python
# print('{:=+5d}'.format(42))       #+  42
# print('{:=+5d}'.format(-42))      #-  42
# print('{:=+5d}'.format(123456))   #+123456
# print('{:=+5d}'.format(-123456))  #-123456
# ```

# In[ ]:





# **Exemplo**  
# 
# - `:f`, `:.nf` e `:+.nf`
# 
# ```python
# print('{:f}'.format(0.45678))    #0.456780
# print('{:.2f}'.format(0.45678))  #0.46
# print('{:+.2f}'.format(0.45678)) #+0.46
# ```
#     - Observe que os valores são arredondados.

# In[ ]:





# ### Substituições aninhadas
# 
# Pode-se aplicar substituições dentro do espaço das substituições.
# 
# **Exemplo**  
# - O alinhamento e o espaço são informados por parâmetro
# 
# ```python
# print('_{:{}{}}_'.format('hello', '^', '10')) #_  hello   _
# ```

# In[ ]:





# Substituições também podem ser utilizadas múltiplas vezes.
# 
# **Exemplo**  
# 
# ```python
# print('{:.{prec}} = {:.{prec}f}'.format('Valor', 3.141592653, prec=3)) #Val = 3.142
# ```
#     - Observe que o espaço da palavra `valor` e a precisão do número estão indicados no mesmo parâmetro

# In[ ]:





# **Exemplo**  
# ```python
# msg = 'Valor do pi'
# pi = 3.141592653
# pre = 3   #precisao do valor e 
# esp = 7   #número de caracteres
# ali = '>' #alinhamento à direita
# print('_{:{a}{e}.{p}} = {:.{p}f}_'.format(msg, pi, p=pre, a=ali, e=esp)) #Val = 3.142
# ```
#     - Repare que o alinhamento, a precisão e o espaço destinada aos caracteres são especificados anteriormente, em substituições dentro da substituição

# In[ ]:





# ### Separação
# 
# Outro método das *string* que merece destaque é o `.split()`. Com ele, é possível dividir a sentença em diversas partes. O resultado é uma lista em que cada posição da lista consta uma parte da *string*, dividida pela *string* informada via parâmetro.
# 
# **Exemplo**  
# ```python
# texto = 'Python é uma linguagem de programação. É interpretada e orientada a objetos'
# print(texto.split()) #separação padrão, utilizando espaços
# print(texto.split('.')) #separação das frases, pelo .
# ```

# In[ ]:





# Com isto, é possível obter apenas trechos ou palavras desejadas.
# 
# **Exemplo**
# ```python
# texto    = 'Python é uma linguagem de programação. É interpretada e orientada a objetos'
# palavras = texto.split() #Separa pelo espaço
# de  = 2
# ate = 4
# print('Palavra na posição',ate,'       :', palavras[ate])
# print('Palavras nas posições',de,'a',ate,':', palavras[2:ate+1])
# print('Palavras nas posições {ini} a {fim} : {}'.format(palavras[de:ate+1], ini=de,fim=ate ))
# print(f'Palavras nas posições {de} a {ate} : {palavras[de:ate+1]}')
# ```

# **Exercícios**
# - [Beecrowd 2234 - Cachorros-Quentes](https://www.beecrowd.com.br/judge/pt/problems/view/2234)  
# - [Beecrowd 2311 - Saltos Ornamentais](https://www.beecrowd.com.br/judge/pt/problems/view/2311)

# ### Fatiamento
# 
# Em *strings* é possível aplicar o fatiamento, visto que são estruturas de sequências. Para tal, basta informar o intervalo inicial e final dos caracteres que se deseja acessar.
# 
# 
# 
# **Exemplo**  
# ```python
# texto = 'Python é uma linguagem de programação. É interpretada e orientada a objetos'
# print(texto[10:20]) #Mostra do caractere na posição 10 ao da 19.
#                     #Observe que é o valor final -1
#     
# print(texto[0:5])   #Mostra os caracteres nas posições 0 a 4
# 
# print(texto[10:])   #Mostra os caracteres da posição 10 em diante. 
#                     #Observe que o valor final não é informado
#     
# print(texto[:10])   #Mostra do início até o caractere na posição 9. 
#                     #Observe que o valor inicial (0) foi omitido.
# ```

# **Exercícios**
# - [Beecrowd 1241 - Encaixa ou Não II](https://www.beecrowd.com.br/judge/pt/problems/view/2241) <- Resolver utilizando fatiamento
# - [Beecrowd 3358 - Sobrenome não é fácil](https://www.beecrowd.com.br/judge/pt/problems/view/3358)
# - [Beecrowd 2714 - Minha Senha Provisória](https://www.beecrowd.com.br/judge/pt/problems/view/2714)

# In[ ]:





# ## Referências
# 
# VELOSO, P., SANTOS, C. Estruturas de Dados. Editora Campus, 4. ed. Rio de Janeiro: 1986.
# 
# **Outros materiais**  
# 
# [PYTHON. Built-in methods: string methods.](https://docs.python.org/3/library/stdtypes.html#string-methods)  
# [PYTHON. Built-in types: sequence types.](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)  
# [PYTHON. String - common string operations: format string syntax.](https://docs.python.org/3/library/string.html#format-string-syntax)  
# 
# 
# [CAELUM. Python e orientação a objetos.](https://www.caelum.com.br/apostila-python-orientacao-objetos/estrutura-de-dados/)  
# [DEVFURIA. Python - Operadores e fatiamento de sequências.](http://www.devfuria.com.br/python/sequencias-fatiamento/)  
# [PETRI, U; GUTMANN, H. PyFormat: Using % and .format() for great good!](https://pyformat.info)  
# 

#  
