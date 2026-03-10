# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:49:09 2026

@author: User
"""

import pandas as pd
df = pd.read_csv("for_nitpicker.dat", sep='\t')
print(df.head())
df.columns = ["date", "time", "depth_m", "temperature_C", "salinity_psu"]
print(df.head())
df.to_csv("ctd_seawater_properties.dat", sep='\t', index=False)
print(df)
