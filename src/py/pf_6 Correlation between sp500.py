
# coding: utf-8

# In[24]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[25]:


from alpha_vantage.timeseries import TimeSeries
import time
import matplotlib.pyplot as plt
from matplotlib import style
import bs4 as bs
import datetime as dt
import os
import pandas as pd
import numpy as np
#import pandas_datareader.data as web
import pickle
import requests


# In[26]:


style.use('ggplot')


# In[27]:


def visualize_data():
    df = pd.read_csv('../../res/sp500_joined_close.csv')
    #df['AAPL'].plot()
    #plt.show()
    df_corr = df.corr()
    print(df_corr.head())
    
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    
    column_labels = df_corr.columns
    row_labels = df_corr.index
    
    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.show()
    


# In[28]:


visualize_data()

