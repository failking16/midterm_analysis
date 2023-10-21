# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 05:54:01 2023

@author: jksls
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
import seaborn as sb

df = pd.read_csv('dataset/2/train-data.csv')
df = df.iloc[:, 1:]

print(df.describe())
df = df.dropna()

print(np.unique(np.array(df['Name'])))
print(np.unique(np.array(df['Location'])))
print(np.unique(np.array(df['Fuel_Type'])))
print(np.unique(np.array(df['Transmission'])))
print(np.unique(np.array(df['Owner_Type'])))

print(df)
df = df[df['Mileage'].notna()]
df = df[df['Engine'].notna()]
df = df[df['Power'].notna()]
df = df[df['Seats'].notna()]
print("Shape of train data After dropping Rows with NULL values  : ",df.shape)

df['Company']        = df['Name'].str.split(' ').str[0]
df['Mileage(km/kg)'] = df['Mileage'].str.split(' ').str[0]
df['Engine(CC)']     = df['Engine'].str.split(' ').str[0]
df['Power(bhp)']     = df['Power'].str.split(' ').str[0]

df['Mileage(km/kg)'] = df['Mileage(km/kg)'].astype(float)
df['Engine(CC)']     = df['Engine(CC)'].astype(float)

indices = df[df['Power'] == 'null'].index
df = df.drop(indices)

df['New_car_Price'] = df['New_Price'].str.split(' ').str[0]
        
df['New_car_Price'] = df['New_car_Price'].astype(float)

df.drop(["Name"],axis=1,inplace=True)
df.drop(["Mileage"],axis=1,inplace=True)
df.drop(["Engine"],axis=1,inplace=True)
df.drop(["Power"],axis=1,inplace=True)
df.drop(["New_Price"],axis=1,inplace=True)

df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
f, ax = mpl.subplots(figsize=(15, 8))
sb.histplot(df['Price'].dropna(), kde=True)  # Drop rows with NaN values
mpl.xlim([0, 160])

var = 'Fuel_Type'
data = pd.concat([df['Price'], df[var]], axis=1)
f, ax = mpl.subplots(figsize=(12, 8))
fig = sb.boxplot(x=var, y="Price", data=data)
fig.axis(ymin=0, ymax=165)

var = 'Fuel_Type'
fig, ax = mpl.subplots()
fig.set_size_inches(11.7, 8.27)
sb.swarmplot(x = var, y ='Price', data = df)

var = 'Year'
data = pd.concat([df['Price'], df[var]], axis=1)
f, ax = mpl.subplots(figsize=(20, 10))
fig = sb.boxplot(x=var, y="Price", data=data)
fig.axis(ymin=0, ymax=165);
mpl.xticks(rotation=90)

var = 'Owner_Type'
fig, ax = mpl.subplots()
fig.set_size_inches(11.7, 8.27)
sb.stripplot(x = var, y ='Price', data = df) 

var = "Company"
mpl.figure(figsize=(20, 10))
sb.catplot(x=var, kind="count", palette="ch:.25", height=8, aspect=2, data=df);
mpl.xticks(rotation=90)

var = 'Location'
df[var].value_counts()

sb.catplot(y='Price',x=var,data= df.sort_values('Price',ascending=False),kind="boxen",height=6, aspect=3)
mpl.show

Location = df[[var]]
Location = pd.get_dummies(Location,drop_first=True)
Location.head()

var = 'Fuel_Type'
df[var].value_counts()

sb.catplot(y='Price',x=var,data= df.sort_values('Price',ascending=False),kind="boxen",height=6, aspect=3)
mpl.show

Fuel_t = df[[var]]
Fuel_t = pd.get_dummies(Fuel_t,drop_first=True)
Fuel_t.head()

var = 'Transmission'
df[var].value_counts()

sb.catplot(y='Price',x=var,data= df.sort_values('Price',ascending=False),kind="boxen",height=6, aspect=3)
mpl.show

Transmission = df[[var]]
Transmission = pd.get_dummies(Transmission,drop_first=True)
Transmission.head()

var = 'Owner_Type'
df[var].value_counts()

df.replace({"First":1,"Second":2,"Third": 3,"Fourth & Above":4},inplace=True)
df.head()

var = 'Company'
df[var].value_counts()

sb.catplot(y='Price',x=var,data= df.sort_values('Price',ascending=False),kind="boxen",height=6, aspect=3)
mpl.show

df.drop(["Company"],axis=1,inplace=True)

final_train= pd.concat([df,Location,Fuel_t,Transmission],axis=1)
final_train.head()

final_train.drop(["Location","Fuel_Type","Transmission","New_car_Price"],axis=1,inplace=True)
final_train.head()