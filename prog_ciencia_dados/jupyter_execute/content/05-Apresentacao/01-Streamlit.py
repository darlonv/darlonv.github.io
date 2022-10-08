#!/usr/bin/env python
# coding: utf-8

# # Streamlit

# Uma das maneiras de apresentação de dados utilizando Python, principalmente para resultados intermediários, é utilizando a biblioteca Streamlit. Seu uso permite a tornar a aplicação disponível como uma aplicação web interativa, com pequenas alterações de código.
# 
# Site oficial do Streamlit: https://streamlit.io.

# ## Funcionamento da aplicação
# 
# A aplicação é realizada utilizando três elementos:
# - O código desenvolvido
# - O servidor streamlit
# - O navegador web
# 
# O servidor streamlit carrega o código desenvolvido, e abre uma porta local para ser acessada via navegador web.
# 
# O streamlit possibilita que o servidor seja recarregado sempre que houverem alterações. Desta forma, é possível editar o código e já observar o resultado.
# 
# ## Passos iniciais
# 
# **Exemplo**  
# - Crie um arquivo com o nome de aula_01.py
# - Inclua no arquivo:
# ```python
# import streamlit as st
# ```
# 
# - Execute o servidor streamlit, informando o arquivo com o código:
# 
# ```bash
# streamlit run aula_01.py
# ```
# 
# - Com isto, o Streamlit executará um serviço web na porta padrão `8501`, tendo como origem o código `aula_01.py`. A porta a ser utilizada é informada na execução do servidor.  
# - Enquanto o servidor estiver executando, acesse o seguinte endereço utilizando um navegador web: [http://localhost:8501](http://localhost:8501)
# 
# 

# # API
# 
# 
# 

# O acesso à API é realizado utilizando a biblioteca `streamlit`. Após importada a biblioteca, é possível acessar seus métodos.
# 
# ```python
# st.title('Apresentação de dados') #Título para a página
# ```  

# ## Apresentação de textos
# A apresentação de textos e todos os métodos disponível podem ser conferidas na documentação do [Streamlit](https://docs.streamlit.io/en/stable/api.html#display-text).
# 
# - `.title()`
#     - Exemplo:
# ```python
# st.title('Apresentação de dados')
# ```
# 
# - `.caption()`
#     - Exemplo:
# ```python
# st.title('Análise realizada')
# ```
# 
# - `.write()` 
#     - Apresenta uma mensagem. Todo o texto será apresentado.
#     - Exemplo:
# ```python
# st.write('Utilizando este sistema, é possível visualizar os resultados da análise realizada, de maneira interativa')
# ```
# 
# - `.text()` 
#     - Possibilita a apresentação de texto, porém utilizando um espaço fixo. Caso o texto seja grande, será utilizada barra de rolagem.
#     - Exemplo:
# ```python
# st.write('Utilizando este sistema, é possível visualizar os resultados da análise realizada, de maneira interativa')
# ```
# 
# - `.latex()`
#     - Permite apresentar fórmulas matemáticas, utilizando notação [LaTeX](https://www.latex-project.org). Um apoio das funções utilizadas pode ser encontrado aqui: [LaTeX Equations for Undergrads.](http://tug.ctan.org/info/undergradmath/undergradmath.pdf)
#     - Exemplo:
#     
# ```python
# st.write('Uma linda equação')
# st.latex('2^5=/frac{2^6}{2}')
# ```
# 
#  

# ## Entrada de Dados
# ### texto
# - `.text_input()`
#     - Obtém um texto de entrada do usuário
#     - Exemplo
# ```python
# filme = st.text_input('Digite o nome de um filme')
# st.write('Filme:', filme)
# ```
# 
# - `.number_input()`
#     - Semelhante ao `.text_input()`, porém, exige que a entrada seja numérica.
#     - Parâmetros:
#         - `label`:
#             - Apresenta uma 
#         - `step`:
#             - Define de quanto será o incremento.
#             
#     - Exemplo
# ```python
# valor = st.text_input('Digite um valor', step=1)
# st.write(f'Valor ao quadrado: {int(valor)**2}')
# ```  
# - `.date_input()`
#     - Seletor de datas. Retorna a data escolhida.
#     - Exemplo
# ```python
# data = st.date_input('Escolha a data')
# st.write(data)
# ```
# 
# - `.time_input()`
#     - Seletor de hora. Retorna a hora selecionada.
#     - Exemplo
# ```python
# horario = st.time_input('Escolha o horário')
# st.write(horario)
# ```
# - `.color_picker()`
#     - Permite ao usuário escolher uma cor. Retorna uma *string* com o código RBG em hexadecimal.
#     - Exemplo
# ```python
# cor = st.color_picker('Escolha uma cor')
# st.write(cor)
# ```
# 
# 
# ### escolha
# - `.radio()`
#     - Permite escolher alternativas, entre diversas opções. Retorna a opção escolhida.
#     - Exemplo
# ```python
# tipo = st.radio('Qual seu estilo de filme favorito?', ['Drama', 'Comédia','Suspense', 'Documentário'] )
# st.write('Tipo escolhido:', tipo)
# ```
# 
# ### seleção
# - `.selectbox()`
#     - Permite escolher uma entre diversas opções. Retorna a opção escolhida.
#     - Exemplo
# ```python
# filme = st.selectbox('Qual destes filmes é o seu predileto?', ['Matrix', 'Kill Bill', 'TeneT'])
# st.write('Filme escolhido:', filme)
# ```
# 
# 
# ### seleção múltipla
# - `.multiselect()`
#     - Semelhante ao `.selectbox()`, porém permite escolher várias opções, inclusive todas ou nenhuma. Retorna uma lista com as opções escolhidas.
#     - Exemplo
# ```python
# filmes = st.multiselect('Qual destes filmes você recomendaria?', ['Matrix', 'Kill Bill', 'TeneT'])
# st.write('Eu recomendaria:', filmes)
# ```
# 
# ### valores
# - `.slider()`
#     - Permite escolher um valor em um intervalo. Retorna o valor selecionado.
#     - Sintaxe:
#         - `st.slider(<mensagem>,<min>,<max>,<default>)`
#     - Exemplo
# ```python
# qtde = st.slider('Quantos filmes você assistiu no último ano?', 0, 20, 5)
# st.write(qtde)
# ```
# 
#     - Utilizando o `.slider()`, também é possível utilizar para obter intervalos. Para tal, basta incluir uma lista com dois valores padrão. Será retornada uma tupla com o valor inicial e final selecionado.
#     - Exemplo
# ```python
# qtde_ideal = st.slider('Escolha os valores inicial e final', 0, 20, [8,12])
# st.write('A quantidade ideal',qtde_ideal)
# ```
# 
# ### valores com destaque
# - `.metric()`
#     - Apresenta uma informação, com destaque.
#     - Sintaxe:
#         - `label`: texto apresentado
#         - `value`: valor apresentado em destaque
#         - `delta`: 
#     - Exemplo::
# ```python
# st.metric(label='Temperatura', value='22 °C', delta='4 °C')
# ```
# 

# ## Estruturas
# 
# ### Dataframes
# 
# Exemplo de DataFrame:
# ```python
# df_ex = pd.DataFrame(np.random.randn(15, 4),columns=['a', 'b', 'c', 'd'])
# ```
# 
# - `.dataframe()`
#     - Apresenta um DataFrame.
#     - Exemplo:
# ```python
# st.dataframe(df_ex)
# ```
# 
# - `.table()`
#     - Semelhante ao DataFrame, porém os valores são apresentados de maneira estática. Não há barras de rolagem, ou seja, todos os dados são apresentados.
#     - Exemplo:
# ```python
# st.table(df_ex)
# ```    
# 
# 

# ## Imagens
# 
# ### Figuras
# - `.image()`
#     - Mostra uma imagem.
#     - Parâmetros
#         - Endereço para imagem local ou link para uma imagem.
#     - Exemplo
# ```python
# st.image('https://p0.piqsels.com/preview/1013/231/679/adorable-animal-animal-photography-breed.jpg')
# ```
# 
# Fonte e créditos da imagem: [Piqsels](https://www.piqsels.com/en/public-domain-photo-jmmhv)

# ### Gráficos
# 
# É possível apresentar gráficos realizados diretamente na página. Muitos gráficos são dinâmicos, e permitem interação.
# 
# - `.line_chart()`
#     - Apresenta um gráfico de linhas.
#     - Exemplo:
# ```python
# st.line_chart(df_ex)
# ```
# 
# - `.bar_chart()`
#     - Apresenta um gráfico de barras.
#     - Exemplo:
# ```python
# st.bar_chart(df_ex)
# ```
# 
# - `.pyplot()`
#     - Permite apresentar gráficos gerados com outras bibliotecas.
#     - Exemplo
# ```python
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()           #Cria figura e a referência
# ax.scatter(df_ex['a'], df_ex['b']) #Gera o gráfico utilizando a referência
# ax.plot([0,2,5], [0,1,2], c='r')
# st.pyplot(fig)                     #Apresenta o gráfico
# ```
# 
# Mapas também podem ser apresentados utilizando a mesma lógica utilizada no matplotlib
# 
# ```python
# import geopandas as gpd
# import geobr
# 
# gdf_estados = geobr.read_state() #Obtém mapa
# 
# fig, ax = plt.subplots() #Cria figura e referência
# gdf_estados.plot(ax=ax)  #Gera o mapa utilizando a referência
# st.pyplot(fig)           #Apresenta o mapa
# ```
# 
# 

# ## Referências
# 
# [STREAMLIT. Streamlit.](https://streamlit.io)  
# [STREAMLIT. Streamlit API Reference.](http://docs.streamlit.io/en/stable/api.html)
# 
# ### Outros materiais
# [LaTeX](https://www.latex-project.org)  
# [CTAN. LaTeX Math for Undergrads. ](http://tug.ctan.org/info/undergradmath/undergradmath.pdf)

# In[ ]:




