# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:05:42 2026

@author: User
"""
#importing packages
import pandas as pd
import matplotlib.pyplot as plt

#loading data
df = pd.read_csv("ctd_seawater_properties.dat", sep="\t")

fig, ax = plt.subplots(1, 2, sharey=True)

#Temperature
ax[0].plot(df["temperature_C"], df["depth_m"], color="red")
ax[0].set_xlabel("Temperature (°C)")
ax[0].set_ylabel("Depth (m)")
ax[0].set_title("Temperature Profile")

#Salinity
ax[1].plot(df["salinity_psu"], df["depth_m"], color="blue")
ax[1].set_xlabel("Salinity (psu)")
ax[1].set_title("Salinity Profile")

plt.tight_layout()
plt.savefig("ctd_profiles.png", dpi=300)
plt.show()
