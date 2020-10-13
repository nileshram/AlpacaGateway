# Created by nilesh at 13/10/2020

from connection.gateway import WebsocketClient
import json
import tornado
from tornado.ioloop import PeriodicCallback
from tornado.websocket import websocket_connect

class Alpaca:

    def __init__(self):
        self.ws_client = WebsocketClient()
        self.callback = PeriodicCallback(self.get_market, 1000)
        self.callback.start()

    async def get_market(self):
        if self.ws_client:
            await self.ws_client.connect()
        await self.ws_client.write()
        res = await self.ws_client.read()
        print(res)


if __name__ == "__main__":
    alpaca = Alpaca()
    tornado.ioloop.IOLoop.current().start()


