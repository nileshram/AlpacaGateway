# Created by nilesh at 09/10/2020

import tornado
from tornado.websocket import websocket_connect

conn = yield websocket_connect("wss://data.alpaca.markets/stream")
while True:
    msg = yield conn.read_message()
    if msg is None:
        break
    else:
        print(msg)
