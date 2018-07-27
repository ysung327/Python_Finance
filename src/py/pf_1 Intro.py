
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
#import pandas_datareader.data as web
#import datetime as dt


# In[2]:


style.use('ggplot')


# In[4]:


'''
start = dt.datetime(2000,1,1)
end = dt.datetime(2018,6,25)
df = web.DataReader('TSLA','yahoo',start,end) 
야후 api에서 데이터프레임 형태로 데이터 받아오기. 이제 안됨.
alphavantage를 쓰든지 기존에 받았던 csv를 가져오든지.
'''
df = pd.read_csv('../../res/tsla.csv')


# In[5]:


print(df.head())
#뒤에꺼부터 출력.


# In[6]:


print(df.head(6))


# In[7]:


print(df.tail(6))

