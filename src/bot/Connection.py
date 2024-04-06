import websockets

class Connection:
    def __init__(self, bot):
        self.bot = bot

    async def connect(self):
        async with websockets.connect('wss://pict.chat/') as ws:
            await self.bot.set_ws(ws)
            # await self.bot.emit('handshake')
            await self.bot.login()
            while True:
                try:
                    msg = await ws.recv()
                    await self.bot.wsmessages.handlemsg(msg)
                except websockets.exceptions.ConnectionClosed:
                    print("Websocket Died")
                    break    