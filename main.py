from getdatasmart import get_historical_data
from supertrend import get_supertrend
from strategy import implement_st_strategy
from position import get_position
from backtest import get_backtest

import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (20,10)

symbol_token="11536"
start_date="2022-01-01 00:00"
end_date="2023-01-01 00:00"
period="ONE_DAY"

data = get_historical_data(symbol_token,start_date,end_date,period)
data['st'], data['s_upt'], data['st_dt'] = get_supertrend(data['high'], data['low'], data['close'], 10, 3)
data = data[1:]
print(data.head())

#plt.plot(data['close'], linewidth = 2, label = 'CLOSING PRICE')
#plt.plot(data['st'], color = 'green', linewidth = 2, label = 'ST UPTREND 10,3')
#plt.plot(data['st_dt'], color = 'r', linewidth = 2, label = 'ST DOWNTREND 10,3')
#plt.legend(loc = 'upper left')
#plt.show()

buy_price, sell_price, st_signal = implement_st_strategy(data['close'], data['st'])

strategy = get_position(data,st_signal)
strategy.head()
#print(strategy)

get_backtest(data,strategy)

plt.plot(data['close'], linewidth = 2)
plt.plot(data['st'], color = 'green', linewidth = 2, label = 'ST UPTREND')
plt.plot(data['st_dt'], color = 'r', linewidth = 2, label = 'ST DOWNTREND')
plt.plot(data.index, buy_price, marker = '^', color = 'green', markersize = 12, linewidth = 0, label = 'BUY SIGNAL')
plt.plot(data.index, sell_price, marker = 'v', color = 'r', markersize = 12, linewidth = 0, label = 'SELL SIGNAL')
plt.title('data ST TRADING SIGNALS')
plt.legend(loc = 'upper left')
plt.show()