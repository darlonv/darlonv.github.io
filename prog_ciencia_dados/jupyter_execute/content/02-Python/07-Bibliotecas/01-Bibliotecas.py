#!/usr/bin/env python
# coding: utf-8

# # Bibliotecas

# ## Importação

# Para importar uma biblioteca pode-use utilizar o comando `import`, seguido do nome da biblioteca. É necessário importar as bibliotecas uma única vez, e é comum que a importação das bibliotecas necessárias ao sistema seja realizada nas primeiras linhas de código do programa.
# 
# **Exemplo**  
# ```python
# import random
# import sys
# import os
# ```
# 
# **Exemplo**  
# - várias bibliotecas em uma única linha:
# ```python
# import random, sys, os
# ```
# 
# **Atividade**  
# - Execute um dos exemplos.

# In[ ]:





# Após importada a biblioteca, pode-se utilizar as funções que estão presentes na biblioteca. Acessar elementos da biblioteca antes da importação ocasiona um erro.
# 
# **Exemplo**  
# - Um número aleatório entre 10 e 20, com o método `.randint()`, da biblioteca `random`.
# ```python
# r = random.randint(10,20)
# print(r)
# ```
# 
# **Exemplo**
# - Parâmetros utilizados na chamada da aplicação, com o atributo `argv`, da biblioteca `sys`.
# ```python
# print(sys.argv)
# ```

# In[ ]:





# In[ ]:





# ### Alias
# 
# Outra possibilidade é renomear a biblioteca durante a execução do programa, utilizando a palavra reservada `as` durante o `import`.
# 
# **Exemplo**  
# ```python
# import random as rand
# 
# print(rand.randint(10,20))
# ```

# In[ ]:





# Em bibliotecas que possuem diversas classes dentro delas, uma possibilidade é importar apenas o necessário.
# 
# **Exemplo**  
# ```python
# from random import randint
# 
# print(randint(10,20))
# ```
# 
# Ou então, importar e renomear
# 
# ```python
# from random import randint as ri
# 
# print(ri(10,20))
# ```

# In[ ]:





# ## Bibliotecas comuns
# 
# |Biblioteca|Descrição|Documentação|
# |----------|:--------|------------|
# |`random`  |Números aleatórios|[random](https://docs.python.org/3/library/random.html)|
# |`sys`     |Informações sobre a execução da aplicação|[sys](https://docs.python.org/3/library/sys.html)|
# |`os`      |Acesso e informações relacionados ao sistema operacional|[os](https://docs.python.org/3/library/os.html)|
# |`math`    |Rotinas e constantes matemáticas | [math](https://docs.python.org/3/library/math.html) |
# |`datetime`    |Manipulação de data e hora | [datetime](https://docs.python.org/3/library/datetime.html) |

# **Exemplos**
# ```python
# import random, sys, os, math
# ```

# In[ ]:





# **`random`**  
# - Números aleatórios
#     - Define a semente (*seed*), base de geração para os números aleatórios. Definir uma mesma semente significa que os mesmos números sempre serão obtidos.
# ```python
# random.seed(10) 
# ```
#     - Inteiros
# ```python
# print(f'entre 0 e 10       : {random.randrange(10)}')
# print(f'entre 10 e 30      : {random.randint(10,30)}')
# print(f'Pares entre 10 e 30: {random.randint(10,30, 2)}')
# ```
#     - Sequências
# ```python
# lista = list(range(10))
# print(f'lista: {lista}'
# print(f'escolhe um valor da lista       : {random.choice(lista)}')
# print(f'modifica a posição dos elementos: {random.shuffle(lista)}')
# print(f'escolhe valores da listas       : {random.sample(lista,2)}')
# ```
#     - Floats 
# ```python
# print(f'valor entre 0 e 1: {random.random()}')
# print(f'valor entre 5 e 7: {random.uniform(5,7)}')
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# **`sys`**  
# - parâmetros utilizados na chamada da aplicação
# ```python
# print(f'Argumentos: {print(sys.argv)}')
# ```

# In[ ]:





# **`os`**  
# - lista com as variáveis de ambiente
# ```python
# print(os.environ)
# ```
# - diretório local
# ```python
# print(os.getcwd())
# ```

# In[ ]:





# In[ ]:





# **`math`**  
# - valores de $\pi$ e $e$
# ```python
# print(f'pi: {math.pi}')
# print(f'e : {math.e}')
# ```
# - raíz quadrada e potência enésima
# ```python
# print(math.sqrt(81))
# print(math.pow(5,5))
# ```
# - seno, cosseno e tangente
# ```python
# print(f'sin(45): {math.sin(45)}')
# print(f'cos(45): {math.cos(45)}')
# print(f'tan(45): {math.tan(45)}')
# ```
# - logaritmos base $e$, e base 10
# ```python
# print(f'log 20 base e  :{math.log(20)}')
# print(f'log 20 base 10 :{math.log10(20)}')
# ```
# - logaritmos base $n$
# ```python
# print(f'log 20 base e  :{math.log(20,math.e)}')
# print(f'log 20 base 10 :{math.log(20,10)}')
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **`datetime`**  
# Esta biblioteca possui diversas classes , específicas para cada necessidade. São elas:
# 
# |tipo|função|
# |----|------|
# |`date`|data|
# |`time`|tempo|
# |`datetime`|data e tempo|
# |`timedelta`|variação de tempo|
# 
# **Exemplo**  
# 
# ```python
# from datetime import date
# ```
# 
# ```python
# today = date.today()
# print( 'hoje é :')
# print(f'dia    : {today.day}')
# print(f'mes    : {today.month}')
# print(f'ano    : {today.year}')
# 
# print('Dias da semana: (0: segunda-feira)')
# print(f'Que dia da semana é hoje? {today.weekday()}')
# print(f'Que dia da semana foi/será meu aniversário em {today.year}? {date(today.year, 9, 4).weekday()}')
# 
# print('Formatação de datas:')
# print(f'hoje é : {today}')
# print(f'hoje é : {today.strftime("%A, %d/%m de %Y")}')
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# Comparando datas, temos um dado do tipo `timedelta`.
# 
# **Exemplo**
# ```python
# natal = date(today.year, 12, 25)
# faltam = natal - today
# print(f'O natal já passou         ? {faltam.days < 0}')
# print(f'Quantos dias faltam       ? {faltam.days}')
# 
# niver = date(today.year, 9, 4)
# faltam = niver - today
# print(f'Meu aniversário já passou ? {faltam.days <= 0}')
# print(f'Meu aniversário é hoje    ? {niver == today}')
# print(f'Meu aniversário é hoje    ? {faltam == 0}')
# 
# print(f'Tipo do dado: {print(type(faltam))}')
# ```
# 

# In[ ]:





# **`time`**  
# 
# A biblioteca `time` permite fazer manipulações que envolvam tempo.  
# 
# **Exemplo**  
# ```python
# import time
# 
# for i in range(10):
#     print(i)
#     time.sleep(1) #Aguarda 1 segundo
# ```

# In[6]:





# **`tqdm`**
# 
# A biblioteca `tqdm` permite utilizar barras de progresso de maneira simplificada.
# 
# **Exemplo**  
# ```python
# from tqdm import tqdm
# 
# for i in tqdm(range(10)):
#     time.sleep(1) #Aguarda 1 segundo
# ```
# 
# **Atividade**  
# - Execute o exemplo.
# - Printe a variável `i` dentro do escopo do `for` e observe o resultado.

# In[2]:





# A biblioteca possui métodos que podem ser aplicados a ambientes de desenvolvimento como Jupyter e Google Colaboratory.
# 
# **Exemplo**  
# ```python
# from tqdm.notebook import tqdm
# 
# for i in tqdm(range(10)):
#     time.sleep(1) #Aguarda 1 segundo
# ```
# 
# **Atividade**  
# - Execute o exemplo.
# - Printe a variável `i` dentro do escopo do `for` e observe o resultado.

# In[ ]:





# In[ ]:





# ### Instalação
# 
# Python possui uma grande quantidade de bibliotecas que podem ser obtidas. Uma das formas de instalação é utilizando gerenciadores de pacotes, como o [pip](https://pypi.org/project/pip/).
# 
# **Observação**
# - A versão do Python instalada e do pip deve ser confirmada. Comumente, o pip para a versão 3.x do Python é chamada de **pip3**.
# - O pip é um *software* separado, e o comando deve ser executado em terminal.
# 
# **Exemplo**
# - procura pela biblioteca numpy
# ```bash
# pip search numpy #busca
# pip install numpy #instalação
# ```

# #### Versões e dependências
# Muitas bibliotecas dependem de outras bibliotecas. Gerenciadores de pacotes normalmente instalam todas as dependências, ou sejam todos os pacotes que as bibliotecas requerem para funcionar.
# 
# Porém, não é incomum encontrar incompatibilidade entre pacotes. Bibliotecas podem funcionar apenas em uma versão específica de alguma dependência, e caso a dependência seja atualizada, a biblioteca pode não funcionar. 
# 
# Uma boa prática é **salvar** os nomes e versões das bibliotecas instaladas no ambiente e quando um novo ambiente for executado, instalá-las nas mesmas versões.
# 
# **Exemplo**
# ```bash
# pip freeze > requirements.txt #Salva no arquivo o nome de todas as bibliotecas e versões
# pip install -r requirements.txt #Instala as bibliotecas com as versões especificadas
# ```

# In[ ]:





# In[ ]:





# ## Ambientes virtuais

# Uma maneira de manter ambientes de desenvolvimento isolados, é manter todas as bibliotecas em um mesmo local e "ativar" esse ambiente quando necessário.
# 
# **Exemplo**  
# 
# - Para criar um ambiente virtual chamado `projeto`, e ativar o ambiente virtual.
# ```bash
# virtualenv projeto #cria o ambiente
# source projeto/bin/activate #ativa o ambiente
# ```
# 
# Uma vez ativado, execuções com o `pip` e o interpretador Python utilizarão o ambiente virtual.

# In[ ]:





# ## Referências
# 
# **Outros materiais**  
# 
# 

#  
