# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:30:14 2023

@author: jksls
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as mpl
mpl.style.use('fivethirtyeight')



def check(sal,sp):
    if(float(sp/sal)>0.4):
        return False
    else: return True


df = pd.read_csv('dataset/used_car_prices.csv')
df.dropna(axis=0 , how='any' , inplace = True)

p_avg    = np.array(df['Average price'], dtype=str)
p_avg    = np.array([k.replace('\n EGP', '').replace(',', '').replace('\nEGP', '') for k in p_avg])
p_avg    = p_avg.astype(int)*15
name     = np.array(df['Car Model'])
date     = np.array(df['Month/Year'])

un_car = np.unique(name)

print(un_car)
print(len(un_car))

ind = []



year_percent  = 1.013
basic_percent = 0.2

cr_dur = int(input('Duration of the credit (in month)'))
salary = int(input('what is your salary'))
spend  = int(input('write the amount of money that you will spend'))

if(check):
    
else:
    print('u r getting nothing')