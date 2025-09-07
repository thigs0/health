import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr


#open files
fat = pd.read_csv('./files/fat.txt')
mass = pd.read_csv('./files/massa.txt')
prot = pd.read_csv('./files/protein.txt')
vic = pd.read_csv('./files/viceral_fat.txt')
water= pd.read_csv('./files/water.txt')
musc = pd.read_csv('./files/muscular_mass.txt')

for file in[fat, mass, prot, vic, water, musc]:#make datetime colum
    file.iloc[:, 0] = pd.to_datetime(file.iloc[:, 0], format='%d/%m/%Y')
    
out = fat.copy()
for file in [mass, prot, vic, water, musc]:#make datetime colum
    out = pd.merge(out, file, on='date', how='inner')
print(out)
out = xr.Dataset.from_dataframe(out)
out.to_netcdf('./files/joinned.nc') 

