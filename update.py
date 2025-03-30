import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import plotly.graph_objects as go

plt.style.use('ggplot')

peso = pd.read_csv('files/massa.txt')
weight = peso.iloc[:, 1]
dt = pd.to_datetime(peso.iloc[:,0], format='%d/%m/%Y')

fat = pd.read_csv('files/fat.txt')
fat_v = fat.iloc[:, 1]
fat_dt = pd.to_datetime(fat.iloc[:,0], format='%d/%m/%Y')

muscular_mass = pd.read_csv('files/muscular_mass.txt')
musc_v = muscular_mass.iloc[:,1]
musc_dt = pd.to_datetime(muscular_mass.iloc[:,0], format='%d/%m/%Y')

protein = pd.read_csv('files/protein.txt')
protein_v=protein.iloc[:,1]
protein_dt = pd.to_datetime(protein.iloc[:,0], format='%d/%m/%Y')

viceral_fat = pd.read_csv('files/viceral_fat.txt')
viceral_v=viceral_fat.iloc[:,1]
viceral_dt = pd.to_datetime(viceral_fat.iloc[:,0], format='%d/%m/%Y')

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
plt.close()

#protein
plt.plot(protein_dt, protein_v, color='black')
plt.ylabel('proteina (Kg)')
plt.title('daily protein')
plt.xlabel('Data')
#plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))  # Exemplo: 'Jan 2023'
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Colocar um marcador por mês
# Melhorar a visualização das labels no eixo X
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('image/daily_protein.png', dpi=300)
plt.close()

#muscular mass
plt.plot(musc_dt, musc_v, color='black')
plt.ylabel('musc')
plt.title('daily muscular')
plt.xlabel('Data')
#plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))  # Exemplo: 'Jan 2023'
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Colocar um marcador por mês
# Melhorar a visualização das labels no eixo X
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('image/daily_muscular.png', dpi=300)
plt.close()

#body fat
plt.plot(fat_dt, fat_v, color='black')
plt.ylabel('body fat')
plt.title('body fat')
plt.xlabel('Data')
#plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))  # Exemplo: 'Jan 2023'
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Colocar um marcador por mês
# Melhorar a visualização das labels no eixo X
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('image/body_fat.png', dpi=300)
plt.close()



