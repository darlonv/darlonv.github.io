#!/usr/bin/env python
# coding: utf-8

# # Cronograma
# 
# Cronograma dos projetos de pesquisa, extensão e inovação vigentes.

# In[1]:


#Bibliotecas
import plotly.express as px
import pandas as pd
from datetime import date

#Leitura de dados
df = pd.read_csv('projetos.csv')

#Converte para data
df['Start'] = df['Start'].apply(pd.to_datetime) 
df['Finish'] = df['Finish'].apply(pd.to_datetime) 

#Cria a coluna da carga horária com o texto
hora = lambda x : str(x)+' horas' if (x>1) else str(x)+' hora' #Coloca hora no plural ou singular
df['Carga horaria'] = df['Carga'].apply(hora)

#Apenas projetos ainda não finalizados
df = df[df['Finish'] > pd.to_datetime(date.today())] 



fig = px.timeline(df, 
                  title='Cronograma',
                  x_start="Start", 
                  x_end="Finish", 
                  y="Task", 
                  color="Tipo",
                  hover_name='Titulo',
                  hover_data={
                      'Task': False,
                      'Start': False,
                      'Finish': False,
                      'Tipo': False,
                      'Função': True,
                      'Carga horaria': True,
                      'Titulo': False,
                      
                  }
                 )
fig.update_yaxes(autorange="reversed", title_text='Projeto')
fig.update_xaxes(title_text='Tempo')
# fig.update_layout(showlegend=True, 
#                   legend=dict(orientation:'h'))

fig.update_layout(
    legend=dict(
        orientation="h",
        yanchor="top",
        y=1.1,
        xanchor="center",
        x=0.5,
        title=''
        )
    )


fig.show()


# In[ ]:


print('ok')


# In[ ]:




