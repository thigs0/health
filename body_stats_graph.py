import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import polars as pl

df = xr.open_dataset('/files/joinned.nc')
body ={
    'Fat Mass':df['mass'].values*df['fat'].values*(1/100),
    'Muscular Mass':df['muscular_mass'].values,
    'Bone':np.ones(len(df['index']))*3.1,
    'Viceral Mass':df['viceral'].values
}
plt.style.use('ggplot')

fig, ax = plt.subplots()
ax.stackplot(df['date'], body.values(),
             labels=body.keys(), alpha=0.8)
ax.legend(loc='upper left', reverse=True)
ax.set_title('Body Mass over time')
ax.set_xlabel('Date')
ax.set_ylabel('Body Mass (Kg)')
fig.tight_layout()

plt.savefig('image/daily_body_stats.png', dpi=300)
plt.close()

mass = df['mass'] - df['mass'].rolling(index=7).mean()
n = mass.shape[0]
positive_mass, negative_mass = mass.copy(), mass.copy()
positive_mass[mass < 0], negative_mass[mass > 0] = 0, 0

plt.bar(df['date'].values, positive_mass, color='blue')
plt.bar(df['date'].values, negative_mass, color='red')
plt.title('Rolling week mass over time')
plt.xlabel('Date')
plt.ylabel('Mass changed (Kg')
plt.tight_layout()

plt.savefig('image/rolling_week_stats.png', dpi=300)
plt.close()
    