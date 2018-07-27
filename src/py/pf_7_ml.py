
# coding: utf-8

# In[1]:


#Machine Learning Tutorial


# In[16]:


get_ipython().run_line_magic('matplotlib', 'notebook')

from collections import Counter
import numpy as np
import pandas as pd
import pickle
from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier


# In[17]:


#해당날짜에 index에 존재하고 이 날짜를 기준으로 1일, 2일, ~ 7일 후의 가격변화를 계산해서 새로운 column으로 return하는 함수.


# In[18]:


def process_data_for_labels(ticker): 
    hm_days = 7
    df = pd.read_csv('sp500_joined_close.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)
    
    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]
    
    df.fillna(0, inplace=True)
    return tickers, df

    


# In[5]:


process_data_for_labels('AAPL')


# In[6]:


def buy_sell_hold(*args):
    cols = [c for c in args] #arg를 이용해서 dataframe의 column을 pass할 수 있음.
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1  #buy
        if col < -requirement:
            return -1  #sell
    return 0 #hold

    


# In[8]:


def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)
    
    df['{}_target'.format(ticker)] = list(map( buy_sell_hold, 
                                               df['{}_1d'.format(ticker)],
                                               df['{}_2d'.format(ticker)],
                                               df['{}_3d'.format(ticker)],
                                               df['{}_4d'.format(ticker)],
                                               df['{}_5d'.format(ticker)],
                                               df['{}_6d'.format(ticker)],
                                               df['{}_7d'.format(ticker)]
                                               ))
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data speard:', Counter(str_vals))
    
    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)
    
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)
    
    X = df_vals.values
    y = df['{}_target'.format(ticker)].values
    
    return X, y, df


# In[9]:


#extract_featuresets('AAPL')


# In[21]:


def do_ml(ticker):
    X, y, df = extract_featuresets(ticker)
    
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25)
    
    
    clf = neighbors.KNeighborsClassifier()
    
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    
    
    predictions = clf.predict(X_test)
    print('Predicted spread:', Counter(predictions))
    
    return confidence


# In[22]:


do_ml('AAPL')

