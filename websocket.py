# pip install twelvedata[websocket]
 
from twelvedata import TDClient
 
def on_event(e):
    print(e.to_string())
 
td = TDClient(apikey="54724ac4515d4009a3cceb2b3f9c87e6")
ws = td.websocket(symbols="TSLA", on_event=on_event)
ws.connect()
ws.keep_alive()