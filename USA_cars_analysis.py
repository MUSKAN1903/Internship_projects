#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv(r"C:\Users\DELL\Downloads\USA_cars_datasets.csv")


# In[6]:


df.head()


# In[7]:


del df['Unnamed: 0']
del df['vin']
del df['lot']
del df['condition']


# In[8]:


df.head()


# # Q1. Top 5 Car brands in terms of number of cars

# In[9]:


data = []

for brand in df['brand'].unique():
    data.append([brand , len(df[df['brand']  == brand])])

pd.DataFrame(data,columns = ['brand','freq']).sort_values(by='freq', ascending=False).head().plot(x = 'brand', y = 'freq', kind = 'bar', figsize = (5,5))


# # 2.Car brand based on Frequency of Cars

# In[10]:


data = []

for brand in df['brand'].unique():
    data.append([brand , len(df[df['brand']  == brand])])

pd.DataFrame(data,columns = ['brand','freq']).sort_values(by='freq', ascending=False).plot(x = 'brand', y = 'freq', kind = 'bar', figsize = (10,5))


# # 3.Car Industry Trend

# In[11]:



data = []

for year in df['year'].unique():
    data.append([year , len(df[df['year']  == year])])

pd.DataFrame(data,columns = ['year','freq']).sort_values(by='year', ascending = True).plot(x = 'year', y = 'freq', kind = 'line', figsize = (5,5))


# # 4. Most Popular Car Colours

# In[12]:


data = []

for color in df['color'].unique():
    data.append([color , len(df[df['color']  == color])])

pd.DataFrame(data,columns = ['color','freq']).sort_values(by='freq', ascending=False).plot(x = 'color', y = 'freq', kind = 'bar', figsize = (20,5))


# # Q5. Which car brand is having Maximum Average Price

# In[13]:


df.groupby('brand').mean()['price'].sort_values(ascending = False).plot.bar()


# # Q6. Which State is having most expensive cars

# In[14]:


df.groupby('state').mean()['price'].sort_values(ascending = False).plot.bar(figsize = (15,5))


# # In Which year most expensive cars were produced?

# In[15]:


df.groupby('year').mean()['price'].sort_values(ascending = False).plot.bar(figsize = (15,5))

