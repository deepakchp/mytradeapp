from getdata import get_historical_data
from supertrend import get_supertrend
from strategy import implement_st_strategy

tsla = get_historical_data('TSLA', '2020-01-01')
tsla['st'], tsla['s_upt'], tsla['st_dt'] = get_supertrend(tsla['high'], tsla['low'], tsla['close'], 10, 3)
tsla = tsla[1:]
print(tsla.head())

#buy_price, sell_price, st_signal = implement_st_strategy(tsla['close'], tsla['st'])