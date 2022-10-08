#!/usr/bin/env python
# coding: utf-8

# # Arquivos

# Os arquivos são uma maneira de trasferir informações para uma memória não volátil, comumente discos rígidos ou discos *flash*. As informações gravadas em arquivos podem ser recuperadas posteriormente. As operações sobre arquivos consistem basicamente em leitura e escrita.  
# 
# 

# ## Arquivos texto e binário

# Os arquivos podem ser de duas formas: **texto** ou **binário**. Um arquivo texto armazena a informação utilizando algum tipo de codificação, como a ASCII. Já os arquivos binários armazenam as informações diretamente em modo binário.

# Ambos os modos possuem vantagens e desvantagens.
# 
# - Texto
#     - Vantagens
#         - Facilidade de leitura
#         - É possível abrir o arquivo em diversas outras aplicações
#     - Desvantagens
#         - Maior necessidade de armazenamento
# - Binário
#     - Vantagens
#         - Menor armazenamento
#     - Desvantagens
#         - Dificuldade para a leitura de dados, é necessário conhecer toda a estrutura do arquivo previamente

# ### Abertura de arquivos
# 
# Para abrir arquivos em Python, utilizamos a função `open()`.
# 
# ```python
# arq = open('arquivo.txt','w')
# ```
# 
# Para salvar dados no arquivo:
# ```python
# arq.write('Hello world')
# ```
# 
# Para fechar o arquivo:
# ```python
# arq.close()
# ```
# 
# 

# **Atividade**
# - Execute os comandos apresentados no exemplo

# In[ ]:





# De forma análoga, é possível manipular arquivos dentro de um bloco `with`: 
# 
# ```python
# with open('arquivo_2.txt', 'w') as arq:
#     arq.write('Hello world')
# ```

# **Atividade**
# - Execute os comandos apresentados no exemplo

# In[ ]:





# ## Modos de abertura
# 
# Os arquivos em Python podem ser abertos com os seguintes modos:
# 
# | Operador |Tipo| Modo |
# |---|:-:|--|
# | `r` | Leitura| Abre o arquivo para leitura.  | 
# | `w` | Escrita| Abre o arquivo para escrita. Caso o arquivo já exista, é substituído.| 
# | `a`  |Escrita (*append*)| Abre o arquivo para escrita, incluindo dados ao final do arquivo.  | 
# | `w+` |Leitura e escrita| Abre o aruqivo para leitura e escrita.| 

# ## Outras funções
# 
# | Método | Descrição |
# |---|--|
# | `.tell()` | Retorna a posição do ponteiro no arquivo, em bytes.  | 
# | `.seek()` | Movimenta o ponteiro para um posição específica do arquivo.| 
# | `a`  | Abre o arquivo para escrita, incluindo dados ao final do arquivo.  | 
# | `w+` | Abre o aruqivo para leitura e escrita.| 

# In[ ]:





# ## Referências
# 
# [Stackoverflow. Quais as principais diferenças entre UTF, ASCII, ANSI?. 2016. Acesso em: 23 set 2019](https://pt.stackoverflow.com/questions/156951/quais-as-principais-diferen%C3%A7as-entre-unicode-utf-ascii-ansi)  
# [SPOLSKI, J. The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!). 2003. Acesso em: 23 set 2019.](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)  
# [MILLER, B., RANUN, D. Aprendendo com Python: Edição interativa](https://panda.ime.usp.br/pensepy/static/pensepy/index.html)  
# 
# 

# In[ ]:




