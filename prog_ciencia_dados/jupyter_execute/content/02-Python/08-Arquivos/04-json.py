#!/usr/bin/env python
# coding: utf-8

# # JSON

# Os arquivos no formato JSON (*JavaScript Object Notation*) são arquivos texto com uma organização específica, bastante semelhante a listas e dicionários Python.
# 
# Sua facilidade consiste em salvar informações referentes a estruturas completas em arquivo, permitindo que conteúdos possam ser carregados posteriormente de maneira simplificada.

# Como exemplo, criaremos a seguinte estrutura, composta por uma lista de dicionários.
# 
# ```python
# planetas = [
#     {
#         'Ordem': 1,    
#         'Nome': "Mercurio",    
#         'Distancia': 57910000,    
#         'Diametro': 4879,    
#         'Rochoso': "Sim"
#     }
#     ,
#     {
#         'Ordem': 2,    
#         'Nome': "Venus",    
#         'Distancia': 108200000,    
#         'Diametro': 12104,    
#         'Rochoso': "Sim"
#     }
#     ,
#     {
#         'Ordem': 3,    
#         'Nome': "Terra",    
#         'Distancia': 149600000,    
#         'Diametro': 12742,    
#         'Rochoso': "Sim"
#     }
# ]
# ```
# 
# **Atividade**  
# - Crie a estrutura `planetas`, como indicado no exemplo.
# - Visualize a estrutura.

# In[ ]:





# Para manipular informações JSON, precisamos importar a biblioteca `json`.
# 
# ```python
# import json
# ```

# In[ ]:





# O método `.dumps()` permite que o conteúdo de uma estrutura seja convertido para *string*.
# 
# **Exemplo**
# ```python
# print(json.dumps(planetas))
# ```

# In[ ]:





# Também é possível apresentar a saída de maneira organizada, utilizando o parâmetro `indent`.
# 
# **Exemplo**  
# 
# ```python
# print(json.dumps(planetas, indent=4))
# ```

# In[ ]:





# ## Escrita

# Para salvar, basta escrever o conteúdo JSON em arquivo texto. O método `.dump()` simplifica esse processo. Neste caso, é necessário passar o descritor do arquivo.
# 
# ```python
# json_file = open('planetas.json', mode='w')
# json.dump(planetas, json_file)
# json_file.close()
# ```
# 
# **Atividade**  
# - Salve o conteúdo da estrutura `planetas` em arquivo do tipo JSON.

# In[ ]:





# Como um arquivo CSV é um arquivo texto, podemos visualizar o conteúdo como arquivo texto.
# 
# ```python
# txt_file = open('planetas.json',mode='r')
# for linha in txt_file:
#   print(linha, end='')
# txt_file.close()
# ```

# In[ ]:





# O parâmetro `indent` também pode ser utilizado para salvar o arquivo organizado, para melhor visualização.
# 
# **Exemplo**
# 
# ```python
# json_file = open('planetas.json', mode='w')
# json.dump(planetas, json_file, indent=4)
# json_file.close()
# ```

# In[ ]:





# **Atividade**  
# - Salve o conteúdo da estrutura `planetas` em arquivo JSON de maneira organizada.
# - Visualize o conteúdo do arquivo, lendo-o como arquivo texto.

# ## Leitura

# Para ler o conteúdo de um arquivo JSON, pode-se utilizar o método `.load()`, passando como parâmetro o descritor do arquivo.
# 
# **Exemplo**  
# 
# ```python
# json_file = open('planetas.json', mode='r')
# data = json.load(json_file)
# print(data)
# ```

# Observe que tanto na leitura quanto na escrita de arquivos JSON, a manipulação do arquivo ocorre de uma única vez.

# 

# ## Referências
# 
# [Introducing JSON](https://www.json.org/json-en.html)  
# 

#  
