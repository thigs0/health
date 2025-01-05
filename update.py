import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go

peso = pd.read_csv('files/massa.txt')

dt = pd.to_datetime(peso.iloc[:,0], format='%d/%m/%Y')
weight = peso.iloc[:,1]

fig = go.Figure(data=go.Scatter(x=dt, y=weight, mode='markers', name='massa ao longo do tempo'))

# Configurando o layout do gráfico
fig.update_layout(
    title='massa ao longo do tempo',
    xaxis_title='Data',
    yaxis_title='Peso (Kg)',
    template='plotly_white'
)

# Salvando o gráfico como um arquivo HTML
fig.write_html("image/massa_diaria.html")


#exercicios de academia
df = pd.read_csv('files/academia.txt')
dt = pd.to_datetime(df.iloc[:,0], format='%d/%m/%Y')

now = pd.to_datetime(datetime.datetime.today().date())
ran = pd.date_range(start=dt[0], end=now)



