
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web


# In[3]:


style.use('ggplot')


# In[4]:


#resample data


# In[5]:


df = pd.read_csv('../../res/tsla.csv', parse_dates=True, index_col=0)


# In[6]:


df_ohlc = df['Adj Close'].resample('10D').ohlc() #panda resample function
df_volume = df['Volume'].resample('10D').sum()


# In[7]:


print(df_ohlc.head())


# In[8]:


df_ohlc.reset_index(inplace=True)
print(df_ohlc.head())


# In[9]:


df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


# In[10]:


print(df_ohlc.head())


# In[11]:


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()


# In[12]:


candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

