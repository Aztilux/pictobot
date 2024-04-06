from os import system
import json
clearcmd = lambda: system('cls')

from bot.Connection import Connection
from bot.WSMessages import WSMessages
from util.Commands import Commands


class Bot:
    def __init__(self, username: str, color: int):
        self.username = username
        self.color = color
        self.connection = Connection(self)
        self.wsmessages = WSMessages(self)
        self.commands = Commands(self)
        self.token = input('token: ')
        self.room = input('room_[a-e]: ')
        self.ws = None

    async def emit(self, msg):
        await self.ws.send(msg)

    async def login(self):
        clearcmd()
        await self.ws.send(f'{{"type":"cl_verifyName","player":{{"name":"{self.username}","color":{self.color}}},"token":"{self.token}"}}')
        print(f"Logging in as {self.username}, color: {self.color}, attempting token...")    

    async def join_room(self):
        await self.emit(f'{{"type":"cl_joinRoom","player":{{"name":"{self.username}","color":{self.color}}},"id":"{self.room}"}}')
        print(f"Joining {self.room}...")  

    async def sendmsg(self, drawing=[], textboxes=[], lines=5):
        await self.emit(f'{{"type":"cl_sendMessage","message":{{"player":{{"name":"{self.username}","color":{self.color}}},"drawing":{drawing},"textboxes":{textboxes},"lines":{lines}}}}}')    
    
    async def set_ws(self, ws): 
        self.ws = ws