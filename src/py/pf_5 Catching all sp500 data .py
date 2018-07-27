
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[5]:


from alpha_vantage.timeseries import TimeSeries
import time
import bs4 as bs
import datetime as dt
import os
import pandas as pd
#import pandas_datareader.data as web
import pickle
import requests


# In[6]:


def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class' : 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    with open("../../res/sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    print(tickers)
    return tickers
        


# In[7]:


#save_sp500_tickers()


# In[8]:


def get_data_from_alpha_vantage(reload_sp500=False):
    ts = TimeSeries(key='ZGZ5EP3PB1XHI563', output_format='pandas', indexing_type='date')
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("../../res/sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('../../res/stock_dfs'):
        os.makedirs('../../res/stock_dfs')
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2016,12,31)
    cnt = 0
    
    for ticker in tickers:
        if((cnt%5 == 0) and (cnt!=0)):
            time.sleep(65)
        print(ticker)
        if not os.path.exists('../../res/stock_dfs/{}.csv'.format(ticker)):
            data, meta_data = ts.get_daily_adjusted(symbol=ticker)
            data.to_csv('../../res/stock_dfs/{}.csv'.format(ticker))
            cnt = cnt + 1
        else:
            print('Already have {}'.format(ticker))
        


# In[9]:


get_data_from_alpha_vantage()


# In[10]:


#combine all the data into one dataframe.


# In[29]:


def compile_data():
    with open("../../res/sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)
    
    main_df = pd.DataFrame()
    
    for count, ticker in enumerate(tickers):
        df = pd.read_csv('../../res/stock_dfs/{}.csv'.format(ticker))
        df.set_index('date', inplace=True)
        
        df.rename(columns = {'5. adjusted close': ticker}, inplace=True)
        df.drop(['1. open','2. high','3. low','4. close','6. volume', '8. split coefficient', '7. dividend amount'], 1, inplace=True)
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')
        if count % 10 == 0:
            print(count)
            
    print(main_df.head())
    main_df.to_csv('../../res/sp500_joined_close.csv')
        


# In[30]:


compile_data()

