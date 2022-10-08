#!/usr/bin/env python
# coding: utf-8

# # Estruturas probabilísticas

# **Bibliotecas**  
# 
# ```bash
# #Pacotes necessários
# ##Pybloom: Bloom filters
# #!pip3 install pybloom
# !pip3 install -e git+https://github.com/jaybaird/python-bloomfilter.git#egg=pybloom
# ##Bounter: Count-min sketch
# !pip3 install bounter    
# ##Hypterloglog: Hyperloglog
# !pip3 install hyperloglog
# ```

# In[ ]:





# ## *Bloom filters*

# Responde se determinado valor está contido ou não em um conjunto de dados.  
# Mapeia para um array de bits utilizando mais de uma função de hash. 

# In[ ]:





# ```python
# import sys
# ```

# In[ ]:





# ```python
# from pybloom import BloomFilter #Caso não funcione, reiniciar o kernel
# ```

# In[ ]:





# ```python
# f = BloomFilter(capacity=1000)
# f.add('192.168.1.1')
# f.add('192.168.1.1')
# f.add('10.1.1.5')
# ```

# In[ ]:





# ```python
# '10.1.1.5' in f
# ```

# In[ ]:





# ```python
# '192.168.1.100' in f
# ```

# In[ ]:





# ```python
# sys.getsizeof(f)
# ```

# In[ ]:





# In[ ]:





# Para pensar:
# - Uma estrutura de bloom filter pode ser calculada de maneira distribuida?  
# - um **ou** lógico poderia ser utilizado em cada resposta?

# In[ ]:





# ## Count-min sketch

# ```python
# from bounter import bounter, CountMinSketch
# ```

# In[ ]:





# ```python
# counts = CountMinSketch(width=2**23, depth=8)
# ```

# In[ ]:





# ```python
# counts.update(['192.168.1.1', '192.168.1.5','192.168.1.1'])
# ```

# In[ ]:





# ```python
# counts['192.168.1.1']
# ```

# In[ ]:





# ```python
# counts['192.168.1.5']
# ```

# In[ ]:





# ```python
# counts['192.168.1.100']
# ```

# In[ ]:





# ## Hyper loglog

# ```python
# import hyperloglog
# ```

# In[ ]:





# ```python
# #Bucket com 4096 posições ou 20k elementos distintos
# hll = hyperloglog.HyperLogLog(0.03) 
# ```

# In[ ]:





# ```python
# hll.add('192.168.10.1')
# hll.add('192.168.5.1')
# hll.add('192.168.5.1')
# hll.add('10.1.1.5')
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# ```python
# len(hll)
# ```

# In[ ]:





# # Referências
# 
# [CORMODE, G.; MUTHUKRISHNAN, S. Approximating Data with the Count-Min Sketch. 2011.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.228.9927&rep=rep1&type=pdf)  
# 
# [FLAJOLET, Philippe; FUSY, Eric; GANDOUET, Olivier; MEUNIER, Frédéric. HyperLogLog: the analysis of a near-optimal cardinality estimation algorithm. Analysis of Algorithms 2007 (AofA07), Jun 2007, Juan les pins, France. pp.127–146. hal-00406166v1](https://hal.archives-ouvertes.fr/file/index/docid/406166/filename/FlFuGaMe07.pdf)  
# 
# 
# 
# 
# **Outros materiais**  
# [BARUCHI, A. Estruturas de dados probabilísticas. Python Brasil, 2020](https://youtu.be/bY_uJCIbDaM?t=3489). 
# 

# In[ ]:




