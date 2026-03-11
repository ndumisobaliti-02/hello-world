# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:15:56 2026

@author: User
"""
#importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing data
df = pd.read_csv(
    "SAA2_WC_2017_metocean_10min_avg.csv",
    parse_dates=True,
    index_col=0
)

#conversion
def ddmm2dd(ddmm):        
    thedeg = np.floor(ddmm/100.)     
    themin = (ddmm-thedeg*100.)/60.     
    return thedeg+themin

#print(df.head(5))
#print(df.columns)

df['TIME_SERVER'] = pd.to_datetime(df['TIME_SERVER'], errors='coerce')
df = df.set_index('TIME_SERVER')
df_subset = df.loc[:'2017-07-04']

#print(df_subset.head())

##Temperature time series
plt.style.use('grayscale')

plt.figure(figsize=(10,4))
plt.plot(df_subset.index, df_subset["TSG_TEMP"], linewidth=1)
plt.xlabel("Time")
plt.ylabel("TSG_TEMP (°C)")
plt.title("Temperature Time Series")

plt.tight_layout()
plt.savefig("temperature_timeseries.png", dpi=300)
plt.show()

##Histogram salinity
salinity = df_subset["TSG_SALINITY"].dropna()
bins = np.arange(30, 35.5, 0.5)
plt.figure(figsize=(8,4))
plt.hist(salinity, bins=bins, edgecolor="black")

plt.xlabel("Salinity (psu)")
plt.ylabel("Frequency")
plt.title("Salinity Distribution")

plt.tight_layout()
plt.savefig("salinity_histogram.png", dpi=300)
plt.show()

##mean, std and IQR for temperature and salinity
temp = df_subset["TSG_TEMP"].dropna()
sal = df_subset["TSG_SALINITY"].dropna()

temp_mean = temp.mean()
temp_std = temp.std()
temp_iqr = temp.quantile(0.75) - temp.quantile(0.25)

sal_mean = sal.mean()
sal_std = sal.std()
sal_iqr = sal.quantile(0.75) - sal.quantile(0.25)

stats_table = pd.DataFrame({
    "Mean":[temp_mean, sal_mean],
    "Std":[temp_std, sal_std],
    "IQR":[temp_iqr, sal_iqr]
},
index=["Temperature","Salinity"])

#print(stats_table)
stats_table.to_csv("statistics_table.csv")

##scatter plot of wind speed and air temperature
wind = df_subset["WIND_SPEED_TRUE"]
air_temp = df_subset["AIR_TEMPERATURE"]
latitude = df_subset["LATITUDE"]

latitude = ddmm2dd(df_subset["LATITUDE"])
latitude[df_subset["N_S"] == "S"] = -latitude[df_subset["N_S"] == "S"]
#print(latitude.head())

plt.figure(figsize=(8,5))
plt.scatter(wind, air_temp, c=latitude, cmap="viridis")

plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Air Temperature (°C)")
plt.title("Wind Speed vs Air Temperature")

plt.tight_layout()
plt.savefig("wind_airtemp_scatter.png", dpi=300)
plt.show()




