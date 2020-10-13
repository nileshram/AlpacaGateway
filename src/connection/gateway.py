# Created by nilesh at 09/10/2020

from configuration import ConfigurationFactory
import tornado
from tornado.ioloop import PeriodicCallback
from tornado.websocket import websocket_connect


class WebsocketClient:

    def __init__(self):
        self.api = ConfigurationFactory.create_config("app_config")["alpaca_api"]
        self.buffer = []

    def _authenticate(self):
        self._auth = self.api["cmds"]["authenticate"]

    def _is_connected(self):
        pass

    async def _recv(self):
        return await self.ws.read_message()

    async def _send(self):
        pass

    async def connect(self):
        #test connection
        self.ws = await websocket_connect(self.api["endpoint"]["market_data"])

    async def disconnect(self):
        pass






