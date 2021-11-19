#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import time

import matplotlib.pyplot as plt



# In[4]:


df = pd.read_csv('AAPL.csv')
df.head()

#print(df.head())
 
# data to be plotted
x = np.arange(1, 11)
y = x * x
 
# plotting
# plt.title("Line graph")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.plot(x, y, color ="red")
# plt.show()

nx = df.values

plt.plot(nx)
plt.show()