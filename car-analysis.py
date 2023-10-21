# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:29:50 2023

@author: jksls
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as mpl
mpl.style.use('fivethirtyeight')

df = pd.read_csv('dataset/used_car_prices.csv')
df.dropna(axis=0 , how='any' , inplace = True)

p_min    = np.array(df['Minimum price'], dtype = str)
p_max    = np.array(df['Maximum price'], dtype = str)
p_avg    = np.array(df['Average price'], dtype = str)
p_avg    = np.array([k.replace('\n EGP', '').replace(',', '').replace('\nEGP', '').replace('EGP', '') for k in p_avg])
p_min    = np.array([k.replace('\n EGP', '').replace(',', '').replace('\nEGP', '').replace('EGP', '') for k in p_min])
p_max    = np.array([k.replace('\n EGP', '').replace(',', '').replace('\nEGP', '').replace('EGP', '') for k in p_max])
p_min    = p_min.astype(int)*15
p_max    = p_max.astype(int)*15
p_avg    = p_avg.astype(int)*15
name     = np.array(df['Car Model'])

print(p_min,p_max,p_avg)
