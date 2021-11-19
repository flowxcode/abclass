#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
import time
from IPython.display import display, HTML


# In[28]:


df = pd.read_csv('AAPL.csv')
df.head()


# In[29]:


df.columns = ['date', 'open', 'high', 'low', 'close', 'adjclose', 'volume']
df.head()


# In[30]:


pos = df[df['close'] > 48 ]
#display(HTML(pos.to_html()))
display(pos)


# In[31]:


df['change'] = df['close'] - df['open']
df['ind'] = (df['high']/df['open']) -1
df.head()


# In[32]:


tlen = len(df)
w = np.linspace(-6,6,len(df))
display(w)
alpha = 1/(1+np.exp(-w))
display(alpha)


# In[33]:


test = df[df['ind'] >= alpha]
eval = test[test['change'] > 0 ]
display(test)
display(eval)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



