
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


# In[2]:


style.use('ggplot')


# In[4]:


df = pd.read_csv('../../res/tsla.csv')
print(df.head())


# In[6]:


df = pd.read_csv('../../res/tsla.csv', parse_dates = True, index_col = 0) 
#read_csv의 parse_dates, index_col docs 검색.
print(df.head())


# In[12]:


df.plot()
plt.show()


# In[11]:


df['Adj Close'].plot()
plt.show()


# In[9]:


print(df[['Open','High']].head())


# In[10]:


import matplotlib.rcsetup as rcsetup
print(rcsetup.all_backends)

