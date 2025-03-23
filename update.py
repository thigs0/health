import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import plotly.graph_objects as go

plt.style.use('ggplot')

peso = pd.read_csv('files/massa.txt')

dt = pd.to_datetime(peso.iloc[:,0], format='%d/%m/%Y')
weight = peso.iloc[:,1]
objetive = np.ones(len(dt))*80

fig = go.Figure(data=go.Scatter(x=dt, y=weight, mode='markers', name='massa ao longo do tempo'))

# Configurando o layout do gráfico
fig.update_layout(
    title='massa ao longo do tempo',
    xaxis_title='Data',
    yaxis_title='Peso (Kg)',
    template='plotly_white'
)

# Salvando o gráfico como um arquivo HTML
#fig.write_html("image/massa_diaria.html")

#plt.scatter(dt, weight, marker='o', color='red')
plt.plot(dt, weight, color='red')
plt.plot(dt, objetive, color='black')
plt.ylabel('massa (Kg)')
plt.title('Massa diária')
plt.xlabel('Data')
#plt.legend()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))  # Exemplo: 'Jan 2023'
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Colocar um marcador por mês

# Melhorar a visualização das labels no eixo X
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('image/massa_diaria.png', dpi=300)

#exercicios de academia
df = pd.read_csv('files/academia.txt')
dt = pd.to_datetime(df.iloc[:,0], format='%d/%m/%Y')

now = pd.to_datetime(datetime.datetime.today().date())
ran = pd.date_range(start=dt[0], end=now)



