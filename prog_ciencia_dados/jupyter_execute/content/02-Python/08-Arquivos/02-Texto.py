#!/usr/bin/env python
# coding: utf-8

# # Arquivos texto
# <!--
# TODO: 
# - Melhorar as referências
# --->

# Um arquivo de texto grava os dados utilizando uma codificação específica, como a ASCII, p. ex.

# Um arquivo texto contém, basicamente, *strings* armazenadas. Para abrir um arquivo texto em Python utilizamos a função `open()`.  

# **Exemplo**  
# Escrita:
# ```py
# arq = open('arquivo.txt','w')
# ```
# Leitura:
# ```py
# arq = open('arquivo.txt','r')
# ```
# 
# Os parâmetros `w` e `r` correspondem a *write* e *read*, respectivamente.

# Para fechar um arquivo, utiliza-se o método `.close()`.  
# 
# **Exemplo**  
# ```py
# arq.close()
# 
# ```

# ## Escrita
# 
# Para escrever informações em um arquivo, utiliza-se o método `.write()`.  
# 
# 

# **Exemplo**  
# ```py
# arq = open('arquivo.txt','w') #criando arquivo.txt
# #escrevendo dados no arquivo
# arq.write('Python') 
# arq.write('Manipulacao de arquivos') 
# arq.close() #fechando arquivo
# ```
# Observe o conteúdo do arquivo `arquivo.txt`.

# In[ ]:





# **Exemplo**  
# Para salvar números de 0 a 9 em um arquivo:  
# ```py
# arq = open('numeros.txt','w')
# for i in range(10):
#     arq.write('{}\n'.format(i))
# arq.close()
# ```

# In[ ]:





# **Atividade**  
# - crie um arquivo `nome.txt`, contendo seu nome
# - crie um arquivo `pares.txt`, contendo os números pares dentro de um intervalo definido pelo usuário. Os números deve estar separados por espaços

# In[ ]:





# In[ ]:





# ## Leitura
# A leitura de dados de um arquivo pode ser realizada de diversas maneiras.  
# **Exemplo**  
# Iterando entre cada linha:
# ```py
# arq = open('numeros.txt','r')
# for linha in arq: #Lê cada linha do arquivo
#     print(linha)
# arq.close()
# ```

# In[ ]:





# **Atividade**  
# - Por que entre cada linha possui uma linha sem nenhum caractere?
# - Adicione o parâmetro `end=''` na função `print()`. Observe e explique o resultado.

# Lendo todo o arquivo de uma única vez, com o método `.read()`:  
# **Exemplo**  
# ```py
# arq = open('numeros.txt','r')
# todosOsDados = arq.read()
# print(todosOsDados)
# arq.close()
# ```

# In[ ]:





# Lendo uma única linha, com o método `.readline()`:  
# 
# **Exemplo**  
# ```py
# arq = open('numeros.txt','r')
# linha = arq.readline()
# print(linha)
# arq.close()
# ```

# In[ ]:





# **Atividade**  
# - Abra o arquivo `numeros.txt`, e mostre apenas os números divisíveis por 6.

# In[ ]:





# ## Referências
# 
# [Stackoverflow. Quais as principais diferenças entre UTF, ASCII, ANSI?. 2016. Acesso em: 23 set 2019](https://pt.stackoverflow.com/questions/156951/quais-as-principais-diferen%C3%A7as-entre-unicode-utf-ascii-ansi)  
# [SPOLSKI, J. The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!). 2003. Acesso em: 23 set 2019.](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)  
# 
