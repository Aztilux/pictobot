def emit(msg):
    # self.ws.send(msg)
    print('EMIT: ', msg)

async def login(self):
    await emit(f'{{"type":"cl_verifyName","player":{{"name":"{self.username}","color":{self.color}}},"token":"{self.token}"}}')
    print(f"Logging in as {self.username}, color: {self.color}, attempting token...")    

async def join_room(self):
    await self.ws.send(f'{{"type":"cl_joinRoom","player":{{"name":"{self.username}","color":{self.color}}},"id":"{self.room}"}}')
    print(f"Joining {self.room}...")  

async def sendmsg(self, drawing=[], textboxes=[], lines=5):
    await self.ws.send(f'{{"type":"cl_sendMessage","message":{{"player":{{"name":"{self.username}","color":{self.color}}},"drawing":{drawing},"textboxes":{textboxes},"lines":{lines}}}}}')   