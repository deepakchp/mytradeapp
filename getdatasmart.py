from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp
import pandas as pd



def get_historical_data():
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
            "symboltoken": "8479",
            "interval": "ONE_DAY",
            "fromdate": "2020-01-01 00:00", 
            "todate": "2023-01-01 00:00"
        }
        data = smartApi.getCandleData(historicParam)
        df = pd.DataFrame(data['data'],columns=['datetime','open', 'high','low','close','volume']).iloc[::-1].set_index('datetime').astype(float)
        df.index = pd.to_datetime(df.index)
        return df
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))

