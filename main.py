from getdatasmart import get_historical_data
from supertrend import get_supertrend
from strategy import implement_st_strategy
from position import get_position
from backtest import get_backtest

import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (20,10)

#tsla = get_historical_data('TSLA', '2015-01-01')
tsla = get_historical_data()
tsla['st'], tsla['s_upt'], tsla['st_dt'] = get_supertrend(tsla['high'], tsla['low'], tsla['close'], 10, 3)
tsla = tsla[1:]
print(tsla.head())

#plt.plot(tsla['close'], linewidth = 2, label = 'CLOSING PRICE')
#plt.plot(tsla['st'], color = 'green', linewidth = 2, label = 'ST UPTREND 10,3')
#plt.plot(tsla['st_dt'], color = 'r', linewidth = 2, label = 'ST DOWNTREND 10,3')
#plt.legend(loc = 'upper left')
#plt.show()

buy_price, sell_price, st_signal = implement_st_strategy(tsla['close'], tsla['st'])

strategy = get_position(tsla,st_signal)
strategy.head()
print(strategy[20:25])

get_backtest(tsla,strategy)

plt.plot(tsla['close'], linewidth = 2)
plt.plot(tsla['st'], color = 'green', linewidth = 2, label = 'ST UPTREND')
plt.plot(tsla['st_dt'], color = 'r', linewidth = 2, label = 'ST DOWNTREND')
plt.plot(tsla.index, buy_price, marker = '^', color = 'green', markersize = 12, linewidth = 0, label = 'BUY SIGNAL')
plt.plot(tsla.index, sell_price, marker = 'v', color = 'r', markersize = 12, linewidth = 0, label = 'SELL SIGNAL')
plt.title('TSLA ST TRADING SIGNALS')
plt.legend(loc = 'upper left')
plt.show()