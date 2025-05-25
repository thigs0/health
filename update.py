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
fat_v_obj = np.ones(len(fat_v))*12

muscular_mass = pd.read_csv('files/muscular_mass.txt')
musc_v = muscular_mass.iloc[:,1]
musc_dt = pd.to_datetime(muscular_mass.iloc[:,0], format='%d/%m/%Y')
musc_v_obj = np.ones(len(musc_v))*60

water = pd.read_csv('files/water.txt')
water_v = water.iloc[:,1]
water_dt = pd.to_datetime(water.iloc[:,0], format='%d/%m/%Y')
water_v_obj = np.ones(len(water_v))*60

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
fig, ax = plt.subplots(2, 2, figsize=(12, 8))  # Adiciona um tamanho apropriado à figura

# Plot 1
ax[0, 0].plot(dt, weight, color='red')
ax[0, 0].plot(dt, objetive, color='black')
ax[0, 0].set_ylabel('mass (Kg)')
ax[0, 0].set_title('Daily Mass')
ax[0, 0].set_xlabel('Date')
ax[0, 0].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 0].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 0].tick_params(axis='x', rotation=45)

# Plot 2
ax[0, 1].plot(dt, weight.rolling(30).mean(), color='red')  # Média móvel em vez de soma/60
ax[0, 1].set_ylabel('mass (Kg)')
ax[0, 1].set_title('R1 Daily Mass (30d avg)')
ax[0, 1].set_xlabel('Date')
ax[0, 1].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 1].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 1].tick_params(axis='x', rotation=45)

# Plot 3
ax[1, 0].plot(dt, weight.rolling(90).mean(), color='red')  # Média móvel em vez de soma/60
ax[1, 0].set_ylabel('mass (Kg)')
ax[1, 0].set_title('R3 Daily Mass (90d avg)')
ax[1, 0].set_xlabel('Date')
ax[1, 0].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[1, 0].xaxis.set_major_locator(mdates.MonthLocator())
ax[1, 0].tick_params(axis='x', rotation=45)

# Plot 4
ax[1, 1].plot(dt, weight.rolling(120).mean(), color='red')  # Média móvel em vez de soma/60
ax[1, 1].set_ylabel('mass (Kg)')
ax[1, 1].set_title('R6 Daily Mass (120d avg)')
ax[1, 1].set_xlabel('Date')
ax[1, 1].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[1, 1].xaxis.set_major_locator(mdates.MonthLocator())
ax[1, 1].tick_params(axis='x', rotation=45)


fig.tight_layout()

plt.savefig('image/massa_diaria.png', dpi=300)
plt.close()

#protein
fig, ax = plt.subplots(2, 2, figsize=(12, 8))  # Adiciona um tamanho apropriado à figura

# Plot 1
ax[0, 0].plot(protein_dt, protein_v, color='red')
ax[0, 0].set_ylabel('Protein (%)')
ax[0, 0].set_title('Tax daily protein (%)')
ax[0, 0].set_xlabel('Date')
ax[0, 0].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 0].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 0].tick_params(axis='x', rotation=45)
# Plot 2
ax[0, 1].plot(protein_dt, protein_v.rolling(30).mean(), color='red')
ax[0, 1].set_ylabel('Protein (%)')
ax[0, 1].set_title('R1 tax daily protein (%)')
ax[0, 1].set_xlabel('Date')
ax[0, 1].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 1].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('image/daily_protein.png', dpi=300)
plt.close()

#muscular mass
fig, ax = plt.subplots(2, 2, figsize=(12, 8))  # Adiciona um tamanho apropriado à figura

# Plot 1
ax[0, 0].plot(musc_dt, musc_v, color='red')
ax[0, 0].plot(musc_dt, musc_v_obj, color='red')
ax[0, 0].set_ylabel('muscular mass (Kg)')
ax[0, 0].set_title('Daily muscular mass (Kg)')
ax[0, 0].set_xlabel('Date')
ax[0, 0].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 0].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 0].tick_params(axis='x', rotation=45)
# Plot 2
ax[0, 1].plot(musc_dt, musc_v.rolling(30).mean(), color='red')
ax[0, 1].set_ylabel('muscular mass (Kg)')
ax[0, 1].set_title('R1 Daily muscular mass (Kg)')
ax[0, 1].set_xlabel('Date')
ax[0, 1].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 1].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 1].tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig('image/daily_muscular.png', dpi=300)
plt.close()

#body fat
fig, ax = plt.subplots(2, 2, figsize=(12, 8))  # Adiciona um tamanho apropriado à figura
# Plot 1
ax[0, 0].plot(fat_dt, fat_v, color='red')
ax[0, 0].plot(fat_dt, fat_v_obj, color='red', label="objective")
ax[0, 0].set_ylabel('Body fat (%)')
ax[0, 0].set_title('Daily percentage of body fat')
ax[0, 0].set_xlabel('Date')
ax[0, 0].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 0].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 0].tick_params(axis='x', rotation=45)
## Plot 1
ax[0, 1].plot(fat_dt, fat_v.rolling(30).mean(), color='red')
ax[0, 1].set_ylabel('Body fat (%)')
ax[0, 1].set_title('R1 Daily percentage of body fat')
ax[0, 1].set_xlabel('Date')
ax[0, 1].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 1].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 1].tick_params(axis='x', rotation=45)

# Plot 3
ax[1, 0].plot(fat_dt, fat_v.rolling(90).mean(), color='red')  # Média móvel em vez de soma/60
ax[1, 0].set_ylabel('Body fat (%)')
ax[1, 0].set_title('R3 Daily percentage of body fat (90d avg)')
ax[1, 0].set_xlabel('Date')
ax[1, 0].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[1, 0].xaxis.set_major_locator(mdates.MonthLocator())
ax[1, 0].tick_params(axis='x', rotation=45)


plt.tight_layout()
plt.savefig('image/body_fat.png', dpi=300)
plt.close()

#water
fig, ax = plt.subplots(2, 2, figsize=(12, 8))  # Adiciona um tamanho apropriado à figura

# Plot 1
ax[0, 0].plot(water_dt, water_v, color='red')
ax[0, 0].set_ylabel('water (Kg)')
ax[0, 0].set_title('Daily water')
ax[0, 0].set_xlabel('Date')
ax[0, 0].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 0].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 0].tick_params(axis='x', rotation=45)
# Plot 2
ax[0, 1].plot(water_dt, water_v.rolling(30).mean(), color='red')
ax[0, 1].set_ylabel('water')
ax[0, 1].set_title('R1 Daily water')
ax[0, 1].set_xlabel('Date')
ax[0, 1].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 1].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 1].tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig('image/daily_water.png', dpi=300)
plt.close()

#body fat
fig, ax = plt.subplots(2, 2, figsize=(12, 8))  # Adiciona um tamanho apropriado à figura
# Plot 1
ax[0, 0].plot(fat_dt, fat_v, color='red')
ax[0, 0].plot(fat_dt, fat_v_obj, color='red', label="objective")
ax[0, 0].set_ylabel('Body fat (%)')
ax[0, 0].set_title('Daily percentage of body fat')
ax[0, 0].set_xlabel('Date')
ax[0, 0].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 0].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 0].tick_params(axis='x', rotation=45)
## Plot 1
ax[0, 1].plot(fat_dt, fat_v.rolling(30).mean(), color='red')
ax[0, 1].set_ylabel('Body fat (%)')
ax[0, 1].set_title('R1 Daily percentage of body fat')
ax[0, 1].set_xlabel('Date')
ax[0, 1].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 1].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('image/body_fat.png', dpi=300)
plt.close()

#Viceral fat
fig, ax = plt.subplots(2, 2, figsize=(12, 8))  # Adiciona um tamanho apropriado à figura
# Plot 1
ax[0, 0].plot(viceral_dt, viceral_v, color='red')
ax[0, 0].set_ylabel('viceral fat')
ax[0, 0].set_title('Daily viceral fat')
ax[0, 0].set_xlabel('Date')
ax[0, 0].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 0].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 0].tick_params(axis='x', rotation=45)
## Plot 1
ax[0, 1].plot(fat_dt, fat_v.rolling(30).mean(), color='red')
ax[0, 1].set_ylabel('Viceral fat')
ax[0, 1].set_title('R1 Daily viceral fat')
ax[0, 1].set_xlabel('Date')
ax[0, 1].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax[0, 1].xaxis.set_major_locator(mdates.MonthLocator())
ax[0, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('image/viceral_fat.png', dpi=300)
plt.close()



