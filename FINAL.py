#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('googleplaystore.csv')
a = df.groupby(['Type', 'Genres'])['Rating'].mean()
print(a)
a.plot()
