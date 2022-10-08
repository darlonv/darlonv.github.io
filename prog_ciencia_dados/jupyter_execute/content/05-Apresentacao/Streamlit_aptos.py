#!/usr/bin/env python
# coding: utf-8

# # Exemplo de aplicação streamlit
# 
# Neste exemplo, desenvolveremos uma ferramenta que apresenta informações sobre apartamentos no Rio de Janeiro.
# 
# Serão realizadas diversas versões, onde cada uma aprimora a versão anterior.

# ## Apresenta base
# 
# Na primeira versão, apenas leremos a base e a apresentaremos na página.

# Importação de bibliotecas  
# 
# ```python
# #Importa bibliotecas
# import streamlit as st
# import pandas as pd
# ```

# Apresentação   
# 
# ```python
# #Título na página
# st.title('Apartamentos na cidade do Rio de Janeiro')
# ```

# Carregamento da base  
# ```python
# #Carrega a base
# rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
# base = rioAptos.copy()
# ```

# Apresentando a base  
# ```python
# #Mostra a base
# st.dataframe(base)
# ```

# **Código final**  
# ```python
# #Importa bibliotecas
# import streamlit as st
# import pandas as pd
# 
# 
# #Título na página
# st.title('Apartamentos na cidade do Rio de Janeiro')
# 
# #Carrega a base
# rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
# base = rioAptos.copy()
# 
# #Mostra a base
# st.dataframe(base)
# ```

# ## Escolhendo bairros
# 
# Nesta versão faremos com que seja possível escolher o bairro, e apresentaremos apenas os apartamentos do bairro escolhido
# 

# Escolhendo bairros  
# Incluiremos um radio button, para seleção do bairro.
# 
# Antes de mostrar a base, inclua:
# ```python
# #Escolha do bairro
# bairros = ['Botafogo','Tijuca']
# bairro = st.radio('Escolha o bairro', bairros )
# st.write('Bairro escolhido:', bairro)
# ```
# 
# Ainda precisamos informar a base que deve mostrar apenas os apartamentos no bairro escolhido. Para isso, podemos filtrar a base:
# ```python
# #Filtra de acordo com o bairro escolhido
# base = base[base['bairro']==bairro]
# ```
# 

# Da forma como está implementado até o momento, cada bairro deve ser incluído na lista de escolhas. Faremos com que todos os bairros da base estejam disponíveis para escolha.
# 
# Altere o código na escolha do bairro para:
# ```python
# #Escolha do bairro
# bairros = base['bairros'].unique() #Obtém todos os bairros presentes na base
# bairro = st.radio('Escolha o bairro', bairros )
# # st.write('Bairro escolhido:', bairro) #Esta linha não é mais necessária. A opção escolhida já é visível
# 
# #Filtra de acordo com o bairro escolhido
# base = base[base['bairro']==bairro]
# ```

# **Código final**  
# ```python
# #Importa bibliotecas
# import streamlit as st
# import pandas as pd
# 
# 
# #Título na página
# st.title('Apartamentos na cidade do Rio de Janeiro')
# 
# #Carrega a base
# rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
# base = rioAptos.copy()
# 
# #Escolha do bairro
# bairros = base['bairro'].unique()
# bairro = st.radio('Escolha o bairro', bairros )
# 
# #Filtra de acordo com o bairro escolhido
# base = base[base['bairro']==bairro]
# 
# #Mostra a base
# st.dataframe(base)
# ```

# ## Escolhendo mais de um bairro

# Outra opção além do radio button para seleção o `.selectbox()`. Ele opera da mesma maneira, porém apresenta um menu para escolha.
# 
# Substitua a linha da escolha de bairros:
# ```python
# #Escolha do bairro
# bairros = base['bairro'].unique()
# bairro = st.selectbox('Escolha o bairro', bairros )
# ```
# 
# Observe que é o mesmo comportamento.

# Para que possamos escolher diversos apartamentos, utilizaremos o `.multiselect()`, que retorna uma lista com as escolhas. Tendo as escolhas, é necessário filtrar a base utilizando o método `.isin()`.
# 
# ```python
# #Escolha do bairro
# bairros = base['bairro'].unique()
# bairro = st.multiselect('Escolha o bairro', bairros ) #Uso do multiselect
# 
# #Filtra de acordo com o bairro escolhido
# base = base[base['bairro'].isin(bairro)] #Filtra pelos nomes de bairro que estiverem na lista
# ```

# **Código final**  
# 
# ```python
# #Importa bibliotecas
# import streamlit as st
# import pandas as pd
# 
# 
# #Título na página
# st.title('Apartamentos na cidade do Rio de Janeiro')
# 
# #Carrega a base
# rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
# base = rioAptos.copy()
# 
# #Escolha do bairro
# bairros = base['bairro'].unique()
# bairro = st.multiselect('Escolha o bairro', bairros ) #Uso do multiselect
# 
# #Filtra de acordo com o bairro escolhido
# base = base[base['bairro'].isin(bairro)] #Filtra pelos nomes de bairro que estiverem na lista
# 
# #Mostra a base
# st.dataframe(base)
# ```

# ## Versão 04 - Filtrando valores
# 
# Agora aplicaremos um segundo filtro, em que sejam apresentados apenas apartamentos em um uma determinada faixa de valores.
# 
# Para tal, utilizaremos um slider. Após o filtro da base de acordo com a escolha do bairro, inclua:
# 
# ```python
# # Escolha dos valores
# faixa = st.slider('Faixa de valor (R$)', 100000, 200000, 150000) #Valor inicial e final
# st.write(faixa)
# ```
# 
# Modifique para haja 2 valores padrão, utilizando uma lista
# ```python
# # Escolha dos valores
# faixa = st.slider('Faixa de valor (R$)', 100000, 200000, [140000,160000]) #Valor inicial e final
# st.write(faixa)
# ```

# Agora, atualizaremos os possíveis valores a serem escolhidos de acordo os valores existentes na base.
# 
# ```python
# # Escolha dos valores
# menor = base['preco'].min() #Obtem o menor preço
# maior = base['preco'].max()#Obtem o maior preço
# faixa = st.slider('Faixa de valor (R$)', menor, maior, [menor,maior]) #Valor inicial e final
# st.write(faixa)
# ```

# Finalmente, realizaremos o filtro na base de acordo com os valores selecionados
# 
# ```python
# # Escolha dos valores
# menor = int(base['preco'].min()) #Obtem o menor preço
# maior = int(base['preco'].max()) #Obtem o maior preço
# 
# faixa = st.slider('Faixa de valor (R$)', menor, maior, [menor, maior]) #Valor inicial e final
# st.write(faixa) #Já pode ser removido
# 
# #Filtra a base pelos valores escolhidos
# base = base[base['preco']>=faixa[0]] #Apenas preços acima do menor escolhido
# base = base[base['preco']<=faixa[1]] #Apenas preços abaixo do maior escolhido
# ```

# **Código final**  
# ```python
# #Importa bibliotecas
# import streamlit as st
# import pandas as pd
# 
# 
# #Título na página
# st.title('Apartamentos na cidade do Rio de Janeiro')
# 
# #Carrega a base
# rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
# base = rioAptos.copy()
# 
# #Escolha do bairro
# bairros = base['bairro'].unique()
# bairro = st.multiselect('Escolha o bairro', bairros )
# 
# #Filtra de acordo com o bairro escolhido
# base = base[base['bairro'].isin(bairro)]
# 
# # Escolha dos valores
# menor = int(base['preco'].min()) #Obtem o menor preço
# maior = int(base['preco'].max()) #Obtem o maior preço
# 
# faixa = st.slider('Faixa de valor (R$)', menor, maior, [menor, maior]) #Valor inicial e final
# 
# #Filtra a base pelos valores escolhidos
# base = base[base['preco']>=faixa[0]] #Apenas preços acima do menor escolhido
# base = base[base['preco']<=faixa[1]] #Apenas preços abaixo do maior escolhido
# 
# #Mostra a base
# st.dataframe(base)
# ```

# ## Apresentando valores médios
# 
# Nesta versão, destacaremos os valores médios de condomínio, preço e área do apartemento.

# Ao final, utilizaremos `.metric()` para apresentar os valores médios.

# Valor médio do condomínio:
# ```python
# #Valor médio do condomínio
# cond_med = base['condominio'].mean()
# st.metric('Valor médio do condomínio (R$)', round(cond_med))
# ```

# Preço médio:
# ```python
# #Preço médio
# preco_med = base['preco'].mean()
# st.metric('Preço médio (R$)', round(preco_med))
# ```

# ```python
# #Área média
# area_med = base['area'].mean()
# st.metric('Área média (M2)', round(area_med))
# ```

# **Código final**  
# ```python
# #Importa bibliotecas
# import streamlit as st
# import pandas as pd
# 
# #Título na página
# st.title('Apartamentos na cidade do Rio de Janeiro')
# 
# #Carrega a base
# rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
# base = rioAptos.copy()
# 
# #Escolha do bairro
# bairros = base['bairro'].unique()
# bairro = st.multiselect('Escolha o bairro', bairros )
# 
# #Filtra de acordo com o bairro escolhido
# base = base[base['bairro'].isin(bairro)]
# 
# # Escolha dos valores
# menor = int(base['preco'].min()) #Obtem o menor preço
# maior = int(base['preco'].max()) #Obtem o maior preço
# 
# faixa = st.slider('Faixa de valor', menor, maior, [menor, maior]) #Valor inicial e final
# 
# #Filtra a base pelos valores escolhidos
# base = base[base['preco']>=faixa[0]] #Apenas preços acima do menor escolhido
# base = base[base['preco']<=faixa[1]] #Apenas preços abaixo do maior escolhido
# 
# #Mostra a base
# st.dataframe(base)
# 
# #Valores médios
# #Valor médio do condomínio
# cond_med = base['condominio'].mean()
# st.metric('Valor médio do condomínio (R$)', round(cond_med))
# #Preço médio
# preco_med = base['preco'].mean()
# st.metric('Preço médio (R$)', round(preco_med))
# #Área média
# area_med = base['area'].mean()
# st.metric('Área média (M2)', round(area_med))
# ```
# 

# ## Valores médios em colunas
# 
# Os valores em destaque podem ser organizados lado a lado. Para tal, utilizaremos o método `.columns()`, com 3 colunas
# 
# ```python
# #Valores médios
# cond_med = base['condominio'].mean() #Valor médio do condomínio
# preco_med = base['preco'].mean() #Preço médio
# area_med = base['area'].mean() #Área média
# 
# st.write('Valores médios')
# c1,c2, c3 = st.columns(3) # Cria as 3 colunas
# c1.metric('Condomínio (R$)', round(cond_med)) #1ra coluna: condomínio
# c2.metric('Preço (R$)', round(preco_med)) #2da coluna: preço
# c3.metric('Área(M2)', round(area_med)) #4ra coluna: área
# ```

# **Código final**
# 
# ```python
# #Importa bibliotecas
# import streamlit as st
# import pandas as pd
# 
# #Título na página
# st.title('Apartamentos na cidade do Rio de Janeiro')
# 
# #Carrega a base
# rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
# base = rioAptos.copy()
# 
# #Escolha do bairro
# bairros = base['bairro'].unique()
# bairro = st.multiselect('Escolha o bairro', bairros )
# 
# #Filtra de acordo com o bairro escolhido
# base = base[base['bairro'].isin(bairro)]
# 
# # Escolha dos valores
# menor = int(base['preco'].min()) #Obtem o menor preço
# maior = int(base['preco'].max()) #Obtem o maior preço
# 
# faixa = st.slider('Faixa de valor', menor, maior, [menor, maior]) #Valor inicial e final
# 
# #Filtra a base pelos valores escolhidos
# base = base[base['preco']>=faixa[0]] #Apenas preços acima do menor escolhido
# base = base[base['preco']<=faixa[1]] #Apenas preços abaixo do maior escolhido
# 
# #Mostra a base
# st.dataframe(base)
# 
# #Valores médios
# cond_med = base['condominio'].mean() #Valor médio do condomínio
# preco_med = base['preco'].mean() #Preço médio
# area_med = base['area'].mean() #Área média
# 
# st.write('Valores médios')
# c1,c2, c3 = st.columns(3) # Cria as 3 colunas
# c1.metric('Condomínio (R$)', round(cond_med)) #1ra coluna: condomínio
# c2.metric('Preço (R$)', round(preco_med)) #2da coluna: preço
# c3.metric('Área(M2)', round(area_med)) #4ra coluna: área
# 
# ```

# ## Barra lateral
# 
# De maneira a apresentar os dados melhor visualmente, colocaremos os elementos interativos em uma barra lateral. Para isso precisaremos modificar as linhas de código onde onde há a entrada de dados pelo usuário, incluindo `.sidebar` nos métodos `.multiselect()` e `.slider()`.
# 
# Na escolha do bairro:
# ```python
# bairro = st.sidebar.multiselect('Escolha o bairro', bairros )
# ```
# 
# Na escolha dos valores:
# ```python
# faixa = st.sidebar.slider('Faixa de valor', menor, maior, [menor, maior]) #Valor inicial e final
# ```

# **Código final**
# 
# ```python
# #Importa bibliotecas
# import streamlit as st
# import pandas as pd
# 
# #Título na página
# st.title('Apartamentos na cidade do Rio de Janeiro')
# 
# #Carrega a base
# rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')
# base = rioAptos.copy()
# 
# #Escolha do bairro
# bairros = base['bairro'].unique()
# bairro = st.sidebar.multiselect('Escolha o bairro', bairros )
# 
# #Filtra de acordo com o bairro escolhido
# base = base[base['bairro'].isin(bairro)]
# 
# # Escolha dos valores
# menor = int(base['preco'].min()) #Obtem o menor preço
# maior = int(base['preco'].max()) #Obtem o maior preço
# 
# faixa = st.sidebar.slider('Faixa de valor', menor, maior, [menor, maior]) #Valor inicial e final
# 
# #Filtra a base pelos valores escolhidos
# base = base[base['preco']>=faixa[0]] #Apenas preços acima do menor escolhido
# base = base[base['preco']<=faixa[1]] #Apenas preços abaixo do maior escolhido
# 
# #Mostra a base
# st.dataframe(base)
# 
# #Valores médios
# cond_med = base['condominio'].mean() #Valor médio do condomínio
# preco_med = base['preco'].mean() #Preço médio
# area_med = base['area'].mean() #Área média
# 
# st.write('Valores médios')
# c1,c2, c3 = st.columns(3) # Cria as 3 colunas
# c1.metric('Condomínio (R$)', round(cond_med)) #1ra coluna: condomínio
# c2.metric('Preço (R$)', round(preco_med)) #2da coluna: preço
# c3.metric('Área(M2)', round(area_med)) #4ra coluna: área
# 
# ```

# ## Referências
# 
# FIGUEIREDO, V. Base de dados com apartamentos do Rio de Janeiro. Disponível em: <https://github.com/mvinoba/notebooks-for-binder>. Acesso em 27 ago 2021.  
# 
# [STREAMLIT. Streamlit API Reference.](http://docs.streamlit.io/en/stable/api.html). Acesso em 27 ago 2021.
# 
# ### Outros materiais
# FIGUEIREDO, V. Seus primeiros passos como Data Scientist: Introdução ao Pandas!. Blog Data Hackers, via Medium.com. Disponível em <https://medium.com/data-hackers/uma-introdução-simples-ao-pandas-1e15eea37fa1>. Acesso em 27 ago 2021.
