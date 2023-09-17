from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp
import pandas as pd



def get_historical_data(symbol_token,start_date,end_date,period):
    api_key = 'mqIs2kuD'
    clientId = 'D133990'
    pwd = '1985'
    smartApi = SmartConnect(api_key)
    token = "Z6J3K6ON5ADK6MUDGPXZ3LSM2I"
    totp=pyotp.TOTP(token).now()
    correlation_id = "abc123"

    # login api call

    data = smartApi.generateSession(clientId, pwd, totp)
    # print(data)
    authToken = data['data']['jwtToken']
    refreshToken = data['data']['refreshToken']

    # fetch the feedtoken
    feedToken = smartApi.getfeedToken()
    #Historic api
    try:
        historicParam={
            "exchange": "NSE",
            "symboltoken": symbol_token,
            "interval": period,
            "fromdate": start_date, 
            "todate": end_date
        }
        data = smartApi.getCandleData(historicParam)
        #df = pd.DataFrame(data['data'],columns=['datetime','open', 'high','low','close','volume']).iloc[::-1].set_index('datetime').astype(float)
        df = pd.DataFrame(data['data'],columns=['datetime','open', 'high','low','close','volume']).set_index('datetime').astype(float)
        df.index = pd.to_datetime(df.index)
        return df
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))

