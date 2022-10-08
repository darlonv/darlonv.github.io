#!/usr/bin/env python
# coding: utf-8

# # XML

# O XML (*eXtensible Markup Language*) é uma **linguagem de marcação**, amplamente utilizada para descrição de dados e estruturas. Um arquivo XML possui o conteúdo da linguagem de marcação XML. 
# 
# O XML organiza as estruturas utilizando *tags* e atributos.

# **Exemplo**
# 
# ```xml
# <planetas>
#     <Terra>
#         <Ordem>3</Ordem>
#         <Nome>Terra</Nome>
#         <Distancia>149600000</Distancia>
#         <Diametro>12742</Diametro>
#         <Rochoso>Sim</Rochoso>
#     </Terra>
# </planetas>
# ```

# %%bash
# echo '<Solar>
#     <Planeta Nome="Mercurio">
#         <Ordem>1</Ordem>
#         <Nome>Mercurio</Nome>
#         <Distancia>57910000</Distancia>
#         <Diametro>4879</Diametro>
#         <Rochoso>Sim</Rochoso>
#     </Planeta>
#     <Planeta Nome="Venus">
#         <Ordem>2</Ordem>
#         <Nome>Terra</Nome>
#         <Distancia>108200000</Distancia>
#         <Diametro>12104</Diametro>
#         <Rochoso>Sim</Rochoso>
#     </Planeta>
#     <Planeta Nome="Terra">
#         <Ordem>3</Ordem>
#         <Nome>Terra</Nome>
#         <Distancia>149600000</Distancia>
#         <Diametro>12742</Diametro>
#         <Rochoso>Sim</Rochoso>
#     </Planeta>
#     <Satelite Nome="Lua">
#         <Ordem>1</Ordem>
#         <Nome>Lua</Nome>
#         <Orbita>Terra</Orbita>
#     </Satelite>
#     <Satelite Nome="Fobos">
#         <Orbita>Marte</Orbita>
#     </Satelite>
#     <Satelite Nome="Deimos">
#         <Orbita>Marte</Orbita>
#     </Satelite>
#     
#     <Satelite Nome="Ganimedes">
#         <Orbita>Jupiter</Orbita>
#     </Satelite>
#     <Satelite Nome="Calisto">
#         <Orbita>Jupiter</Orbita>
#     </Satelite>
#     <Satelite Nome="Europa">
#         <Orbita>Jupiter</Orbita>
#     </Satelite>
#     <Satelite Nome="Io">
#         <Orbita>Jupiter</Orbita>
#     </Satelite>
#     
#      <Satelite Nome="Mimas">
#         <Orbita>Saturno</Orbita>
#     </Satelite>
#     <Satelite Nome="Encélado">
#         <Orbita>Saturno</Orbita>
#     </Satelite>
#     <Satelite Nome="Tétis">
#         <Orbita>Saturno</Orbita>
#     </Satelite>
#     <Satelite Nome="Dione">
#         <Orbita>Saturno</Orbita>
#     </Satelite>
#     <Satelite Nome="Reia">
#         <Orbita>Saturno</Orbita>
#     </Satelite>
#     <Satelite Nome="Titã">
#         <Orbita>Saturno</Orbita>
#     </Satelite>
#     <Satelite Nome="Jápeto">
#         <Orbita>Saturno</Orbita>
#     </Satelite>
#     
#     <Satelite Nome="Miranda">
#         <Orbita>Urano</Orbita>
#     </Satelite>
#     <Satelite Nome="Ariel">
#         <Orbita>Urano</Orbita>
#     </Satelite>
#     <Satelite Nome="Umbriel">
#         <Orbita>Urano</Orbita>
#     </Satelite>
#     <Satelite Nome="Titânia">
#         <Orbita>Urano</Orbita>
#     </Satelite>
#     <Satelite Nome="Oberon">
#         <Orbita>Urano</Orbita>
#     </Satelite>
#     
#     <Satelite Nome="Náiade">
#         <Orbita>Netuno</Orbita>
#     </Satelite>
#     <Satelite Nome="Talassa">
#         <Orbita>Netuno</Orbita>
#     </Satelite>
#     <Satelite Nome="Despina">
#         <Orbita>Netuno</Orbita>
#     </Satelite>
#     <Satelite Nome="Galateia">
#         <Orbita>Netuno</Orbita>
#     </Satelite>
#     <Satelite Nome="Larissa">
#         <Orbita>Netuno</Orbita>
#     </Satelite>
#     <Satelite Nome="Hipocampo">
#         <Orbita>Netuno</Orbita>
#     </Satelite>
#     <Satelite Nome="Proteu">
#         <Orbita>Netuno</Orbita>
#     </Satelite>
#     
#     <Satelite Nome="Caronte">
#         <Orbita>Plutão</Orbita>
#     </Satelite>
#     <Satelite Nome="Nix">
#         <Orbita>Plutão</Orbita>
#     </Satelite>
#     <Satelite Nome="Hidra">
#         <Orbita>Plutão</Orbita>
#     </Satelite>
#     <Satelite Nome="Cérbero">
#         <Orbita>Plutão</Orbita>
#     </Satelite>
#     <Satelite Nome="Estige">
#         <Orbita>Plutão</Orbita>
#     </Satelite>
#     
#     <Satelite Nome="Namaka">
#         <Orbita>Haumea</Orbita>
#     </Satelite>
#     <Satelite Nome="Hi\'iaka">
#         <Orbita>Haumea</Orbita>
#     </Satelite>
#     
#     <Satelite Nome="MK 2">
#         <Orbita>Makemake</Orbita>
#     </Satelite>
#     
#     <Satelite Nome="Disnomia">
#         <Orbita>Éris</Orbita>
#     </Satelite>
#     
#     <planeta>
#         <Orbita>Ceres</Orbita>
#         <tipo>Planeta anão</tipo>
#     </planeta>
#     
#     
#     
#     
#     <Satelite Nome="">
#         <Orbita></Orbita>
#     </Satelite>
#     
#     
#     
#     <Estrela Nome="Sol">
#         <Nome>Sol</Nome>
#     </Estrela>
# </Solar>' > planetas.xml

# [Fonte](https://pt.wikipedia.org/wiki/Lista_de_satélites_naturais_do_Sistema_Solar)

# import xml.etree.ElementTree as ET

# tree = ET.parse('planetas.xml')
# root = tree.getroot()

# print(root.attrib)

# k.tag

# <data>
#     <items>
#         <item name="item1">item1abc</item>
#         <item name="item2">item2abc</item>
#     </items>
# </data>

# ## Leitura

# ```python
# tree = ET.parse('planetas.xml')
# root = tree.getroot()
# ```

# #Mostra os valores na raíz
# print('Raiz:')
# print(f'tag: {root.tag} - attrib:{root.attrib} - text: {root.text}')

# #Mostra os valores nos filhos
# print('Filhos:')
# #Percorre cada nó filho do root
# for i in root.getchildren():
#     print(f'tag: {i.tag} - attrib: {i.attrib} - text: {i.text}')
#     
#     #percorre os nós filhos de cada nó filho do root
#     for j in i.getchildren():
#         print(f'\ttag: {j.tag} - attrib: {j.attrib} - {j.text}')
#         
#     print('')

# ## Busca

# 

# tree = ET.parse('planetas.xml')
# root = tree.getroot()

# x = root.findall('Planeta')
# for i in x:
#     print(f'tag: {i.tag} - attrib: {i.attrib} - text: {i.text}')

# In[95]:


#Mostrando os planetas que possuem satelites
x = root.findall('Satelite')
for i in x:
    for j in i.findall('Orbita'):
        print(f'{j.text}')


# ## Alteração

# ## Escrita

# **Exercícios**  
# 
# Sobre o conteúdo do arquivo xml, responda:
# 
# 1. Quantos planetas há no sistema solar?
# 1. Qual é o menor planeta do sistema solar?
# 1. Quantos satélites possui cada planeta?
# 1. Qual é o nome do satélite que está mais distante do planeta que orbita?
# 1. Qual é o planeta que possui mais satélites?
# 1. Existem satélites maiores que planetas? Caso sim, apresente o nome do satélite, qual planeta ele orbita e comparado a qual planeta ele é maior.
# 1. Qual é o maior satélite do sistema solar?
# 1. Qual é o planeta anão mais próximo do sol?
# 
# Responda apenas considerando as informações contidas no exemplo.

# ## Referências
# 
# **Outros materiais**  
# [Reading and Writing XML Files in Python](https://stackabuse.com/reading-and-writing-xml-files-in-python/)  
# 

#  
