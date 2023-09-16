import pandas as pd
import numpy as np
from math import floor
from termcolor import colored as cl

def get_backtest(tsla,strategy):
    tsla_ret = pd.DataFrame(np.diff(tsla['close'])).rename(columns = {0:'returns'})
    st_strategy_ret = []

    for i in range(len(tsla_ret)):
        returns = tsla_ret['returns'][i]*strategy['st_position'][i]
        st_strategy_ret.append(returns)
    
    st_strategy_ret_df = pd.DataFrame(st_strategy_ret).rename(columns = {0:'st_returns'})
    investment_value = 100000
    number_of_stocks = floor(investment_value/tsla['close'][-1])
    st_investment_ret = []

    for i in range(len(st_strategy_ret_df['st_returns'])):
        returns = number_of_stocks*st_strategy_ret_df['st_returns'][i]
        st_investment_ret.append(returns)

    st_investment_ret_df = pd.DataFrame(st_investment_ret).rename(columns = {0:'investment_returns'})
    total_investment_ret = round(sum(st_investment_ret_df['investment_returns']), 2)
    profit_percentage = floor((total_investment_ret/investment_value)*100)
    print(cl('Profit gained from the ST strategy by investing $100k in TSLA : {}'.format(total_investment_ret), attrs = ['bold']))
    print(cl('Profit percentage of the ST strategy : {}%'.format(profit_percentage), attrs = ['bold']))