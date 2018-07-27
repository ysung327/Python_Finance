
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"


# In[3]:


style.use('ggplot')


# In[4]:


df = pd.read_csv('../../res/tsla.csv', parse_dates=True, index_col=0)


# In[5]:


df['100ma'] = df['Adj Close'].rolling(window=100).mean()


# In[6]:


print(df.head())


# In[7]:


print(df.tail())


# In[8]:


df.dropna(inplace=True) #drop NA, 0


# In[9]:


print(df.head())


# min_periods=0 이용하기.

# In[10]:


df1 = pd.read_csv('../../res/tsla.csv', parse_dates=True, index_col=0)


# In[11]:


df1['100ma'] = df1['Adj Close'].rolling(window=100, min_periods=0).mean()


# In[12]:


print(df1.head())


# In[13]:


#graphing


# In[14]:


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

