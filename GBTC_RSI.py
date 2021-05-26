# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:12:48 2021

@author: cesch
"""

import pandas as pd
import pandas_datareader as dr
import matplotlib.pyplot as plt

##download GBTC data##
GBTC = dr.data.get_data_yahoo('GBTC', start='2019-05-24', end='2021-05-21')
GBTC


#Plot GBTC
GBTC['Adj Close'].plot(figsize=(15,10), grid=True)
plt.title('GBTC Adj Close')
plt.show()

#Calculating RSI; RSI = 100-(100/(1+RS)); RS = avg gain/avg loss
#Difference in price from previous day
delta = GBTC['Adj Close'].diff(1)
delta
#Remove first NaN
delta = delta[1:]

#postive & negative gains
positive = delta.copy()
negative = delta.copy()
positive[positive < 0] = 0 
negative[negative > 0] = 0 

#14 Day RSI
time_period = 14
#Calc average gain and loss
AVG_Gain = positive.rolling(window=time_period).mean()
AVG_Loss = abs(negative.rolling(window=time_period).mean())
#Relative Strength
RS = AVG_Gain / AVG_Loss
#Relative Strength Index
RSI = 100.0 - (100.0/ (1.0 + RS))


#Plots
new_df = pd.DataFrame()
new_df['Adj Close'] = GBTC['Adj Close']
new_df['RSI'] = RSI

#Plot Adj Close
plt.figure(figsize=(12,4))
plt.plot(new_df.index, new_df['Adj Close'])
plt.title('GBTC Adj Close')
plt.ylabel('Adj Price USD',fontsize=12)
plt.legend(new_df.columns.values, loc='upper left')
plt.show()

#Plot RSI
plt.figure(figsize=(12,4))
plt.title('GBTC RSI Plot')
plt.plot(new_df.index, new_df['RSI'])
#Over sold
plt.axhline(30, linestyle='--',color = 'green')
#Over Bought
plt.axhline(70, linestyle='--', color = 'red')
plt.xlabel('May 2019 - May 2021',fontsize=12)
plt.ylabel('RSI Values (0 - 100)',fontsize=12)
plt.show()
