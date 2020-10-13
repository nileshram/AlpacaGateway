# Created by nilesh at 09/10/2020

from configuration import ConfigurationFactory
import tornado
from tornado.ioloop import PeriodicCallback
from tornado.websocket import websocket_connect


class WebsocketClient:

    def __init__(self):
        self.api = ConfigurationFactory.create_config("app_config")["alpaca_api"]
        self._authenticate()
        self._init_buffer()

    def _authenticate(self):
        self._auth = self.api["cmds"]["authenticate"]

    def _init_buffer(self):
        self._buffer = []

    def _is_connected(self):
        pass

    async def _recv(self):
        return await self.conn.read_message()

    async def _send(self):
        pass

    async def read(self):
        return await self.conn.read_message()

    async def write(self):
        await self.conn.write_message(self._auth)

    async def connect(self):
        #test connection
        self.conn = await websocket_connect(self.api["endpoint"]["market_data"])

    async def disconnect(self):
        pass






