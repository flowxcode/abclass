#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import time


# In[4]:


df = pd.read_csv('AAPL.csv')
df.head()

print(df.head())