from os import system
clearcmd = lambda: system('cls')

from bot.Connection import Connection
from util.WSMessages import WSMessages
from util.Commands import Commands
from util.drawing.Draw import Draw


class Bot:
    def __init__(self, username: str, color: int):
        self.username = username
        self.color = color
        self.connection = Connection(self)
        self.wsmessages = WSMessages(self)
        self.commands = Commands(self)
        self.draw = Draw(self)

    async def login(self):
        clearcmd()
        await self.ws.send(f'{{"type":"cl_verifyName","player":{{"name":"{self.username}","color":{self.color}}},"token":"{self.token}"}}')
        print(f"Logging in as {self.username}, color: {self.color}, attempting token...")    

    async def join_room(self):
        await self.ws.send(f'{{"type":"cl_joinRoom","player":{{"name":"{self.username}","color":{self.color}}},"id":"{self.room}"}}')
        print(f"Joining {self.room}...")  

    async def sendmsg(self, drawing=[], textboxes=[], lines=5):
        await self.ws.send(f'{{"type":"cl_sendMessage","message":{{"player":{{"name":"{self.username}","color":{self.color}}},"drawing":{drawing},"textboxes":{textboxes},"lines":{lines}}}}}')    