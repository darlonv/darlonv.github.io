#!/usr/bin/env python
# coding: utf-8

# # Serialização e arquivos binários

# ## Serialização

# Objetos em Python podem ser serializado utilizando a biblioteca `pickle`, e salvos como arquivo binário.

# Para utilização do `pickle`, é necessário importar a biblioteca.
# ```python
# import pickle
# ```

# In[ ]:





# Os principais métodos da biblioteca são:
# 
# |Método| Descrição|
# |------|----------|
# |`.dumps()`|Retorna a serialização do objeto|
# |`.loads()`|Retorna o objeto construído a partir de sua serialização|
# |`.dump()` |Serializa e salva em arquivo|
# |`.load()` |Carrega a partir de arquivo|

# **Exemplo**  
# - Estrutura com dados de exemplo:
# 
# ```python
# data = [{
#     'Title': 'Sandman',
#     'Author': 'Nail Gaiman'
#     },
#     {'Title': 'Watchmen',
#     'Author': 'Alan Moore'}
#     ]
# print(data)
# ```

# In[ ]:





# É possível observar os dados serializados. O `b` no início indica que os dados estão em formato binário.
# ```python
# print(pickle.dumps(data))
# ```

# In[ ]:





# ```python
# with open('dados.bin', 'wb') as arq:
#     pickle.dump(data, arq)
# ```

# In[ ]:





# ```python
# with open('dados.bin','rb') as arq:
#     livros = pickle.load(arq)
# 
# print(livros)
# ```

# In[ ]:





# ## Referências
# 
# **Outros materiais**  
# [PYTHON. Pickle - Serialização de objetos Python](https://docs.python.org/pt-br/3.7/library/pickle.html#module-pickle)  
# 

#  
