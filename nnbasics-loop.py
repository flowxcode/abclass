#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import time
from termcolor import colored
# Read in the data from the csv file
df = pd.read_csv('AAPL.csv')
# Reduce the column names to lower case
df.columns = ['date', 'open', 'high', 'low', 'close', 'adjclose', 'volume']
# compute the change to use as a guide in backtesting
df['change'] = df['close'] - df['open']
# populate the classifier
df['ind'] = (df['high']/df['open']) -1
# Initialize the weights
param = np.linspace(-6,6,len(df))
# Fire the neural network
eta = 0
while eta < 100:
    for i in param:
        alpha = 1/(1+np.exp(-i))
        test = df[df['ind'] >= alpha]
        if len(test) > 0:
            pos = test[test['change'] > 0]
            eta = len(pos)*100/len(test)
            #time.sleep(1)
            print(colored (i, 'green'), alpha, len(test), colored(eta, 'red'))
        else:
            pass
else:
    print('done classifying')


# In[ ]:




