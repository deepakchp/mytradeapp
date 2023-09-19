from getdatasmart import get_historical_data
from supertrend import get_supertrend
from strategy import implement_st_strategy
from position import get_position
from backtest import get_backtest

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (20,10)

symbol_token=["1660 ITC","4963 ICICIBANK","5900 AXISBANK","3045 SBIN","1394 HINDUNILVR","11536 TCS","1594 INFY"]
start_date=["2013-01-01 00:00","2014-01-01 00:00","2015-01-01 00:00","2016-01-01 00:00","2017-01-01 00:00","2018-01-01 00:00","2019-01-01 00:00","2020-01-01 00:00","2021-01-01 00:00","2022-01-01 00:00"]
end_date=["2013-12-31 00:00","2014-12-31 00:00","2015-12-31 00:00","2016-12-31 00:00","2017-12-31 00:00","2018-12-31 00:00","2019-12-31 00:00","2020-12-31 00:00","2021-12-31 00:00","2022-12-31 00:00"]
period="ONE_DAY"
datefr = pd.DataFrame(start_date,columns=['datetime']).set_index('datetime').astype(float)
final_list = []
for sindex in range(len(symbol_token)):
    total_profit_list = []
    profit_occurance_list = []
    loss_occurance_list = []
    res = pd.DataFrame()
    for dindex in range(len(start_date)):
        data = get_historical_data(symbol_token[sindex].split(" ")[0],start_date[dindex],end_date[dindex],period)
        data['st'], data['s_upt'], data['st_dt'] = get_supertrend(data['high'], data['low'], data['close'], 10, 3)
        data = data[1:]

        buy_price, sell_price, st_signal = implement_st_strategy(data['close'], data['st'])

        buy_signal = pd.DataFrame(buy_price).rename(columns = {0:'buy_signal'}).set_index(data.index)
        sell_signal = pd.DataFrame(sell_price).rename(columns = {0:'sell_signal'}).set_index(data.index)
        st_sign = pd.DataFrame(st_signal).rename(columns = {0:'st_signal'}).set_index(data.index)

        frames = [buy_signal, sell_signal, st_sign]
        strat = pd.concat(frames, join = 'inner', axis = 1)
        #print(strat)
        res = strat.query("`st_signal` == 1 | `st_signal` == -1")
        print(res)

        total_profit = 0
        profit_occurance = 0
        total_loss = 0
        loss_occurance = 0

        for i in range(len(res)):
            if (res['st_signal'][i] == 1 and i < (len(res)-1)):
                total_profit = total_profit + (res['sell_signal'][i+1] - res['buy_signal'][i])
                if res['sell_signal'][i+1] > res['buy_signal'][i]:
                    profit_occurance = profit_occurance + 1
                else:
                    loss_occurance = loss_occurance + 1

        total_profit_list.append(total_profit)
        profit_occurance_list.append(profit_occurance)
        loss_occurance_list.append(loss_occurance)

    total_profit_fr = pd.DataFrame(total_profit_list).rename(columns = {0:'total_profit_list'}).set_index(datefr.index)
    profit_occurance_fr = pd.DataFrame(profit_occurance_list).rename(columns = {0:'profit_occurance_list'}).set_index(datefr.index)
    loss_occurance_fr = pd.DataFrame(loss_occurance_list).rename(columns = {0:'loss_occurance_list'}).set_index(datefr.index)
        
    frames2 = [total_profit_fr, profit_occurance_fr, loss_occurance_fr]
    timebased = pd.concat(frames2, join = 'inner', axis = 1)
    final_list.append(timebased)

for xinx in range(len(symbol_token)):
    print("................... symbol ................",symbol_token[xinx].split(" ")[1])
    print(final_list[xinx])

#strategy = get_position(data,st_signal)
#strategy.head()
#print(strategy)

#get_backtest(data,strategy)

plt.plot(data['close'], linewidth = 2)
plt.plot(data['st'], color = 'green', linewidth = 2, label = 'ST UPTREND')
plt.plot(data['st_dt'], color = 'r', linewidth = 2, label = 'ST DOWNTREND')
plt.plot(data.index, buy_price, marker = '^', color = 'green', markersize = 12, linewidth = 0, label = 'BUY SIGNAL')
plt.plot(data.index, sell_price, marker = 'v', color = 'r', markersize = 12, linewidth = 0, label = 'SELL SIGNAL')
plt.title('data ST TRADING SIGNALS')
plt.legend(loc = 'upper left')
plt.show()
