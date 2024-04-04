import websockets

class Connection:
    def __init__(self, bot):
        self.bot = bot

    async def connect(self):
        token = input('token: ')
        room = 'room_a'
        # input('(room_[a-e]): ')
        self.bot.token, self.bot.room = token, room
        async with websockets.connect('wss://pict.chat/') as ws:
            self.bot.ws = ws
            await self.bot.ws.send("handshake")
            await self.bot.login()
            while True:
                try:
                    msg = await ws.recv()
                    await self.bot.wsmessages.handlemsg(msg)
                except websockets.exceptions.ConnectionClosed:
                    print("Websocket Died")
                    break    