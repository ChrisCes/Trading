# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:14:00 2021

@author: cesch
"""

#import pandas as pd
import pandas_datareader as dr
import matplotlib.pyplot as plt

##download GBTC data##
GBTC = dr.data.get_data_yahoo('GBTC', start='2019-05-24', end='2021-05-21')
GBTC


#Plot GBTC
GBTC['Adj Close'].plot(figsize=(15,10), grid=True)
plt.title('GBTC Adj Close')
plt.show()

GBTC_adj_close = GBTC['Adj Close']

#Simple moving average
short_sma = GBTC_adj_close.rolling(window=20).mean()
short_sma.head(20)
long_sma = GBTC_adj_close.rolling(window=100).mean()
long_sma.tail()

#Plot SMA
fig, sma = plt.subplots(figsize=(16,9))
sma.plot(GBTC_adj_close, label='Price')
sma.plot(short_sma, label='20 day SMA')
sma.plot(long_sma, label='100 day SMA')

sma.set_ylabel('Adj Price USD',fontsize=12)