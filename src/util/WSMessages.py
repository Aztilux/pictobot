import json

class WSMessages:
    def __init__(self, bot):
       self.bot = bot

    async def handlemsg(self, msg: str):
        if msg == 'ping':
            # websockets has already heartbeat
            # await self.bot.ws.send('pong')
            return
        data = json.loads(msg)
        #on chat message  
        if data['type'] == 'sv_receivedMessage':
            await self.sv_receivedMessage(msg)
        #joins     
        elif data['type'] == 'sv_playerJoined':
            username = data['player']['name']
            await self.playerconnection(username, True)
        #leaves    
        elif data['type'] == 'sv_playerLeft':
            username = data['player']['name']
            await self.playerconnection(username, False)
        # verified / authed    
        elif data['type'] == 'sv_nameVerified':
            await self.sv_nameVerified()
        # room stats
        elif data['type'] == 'sv_roomIds':
            pass    
        # joined room  
        elif data['type'] == 'sv_roomData':
            pass             
        #unhandled messages  
        else:
            print(msg)    
    
    async def sv_receivedMessage(self, msg):
            data = json.loads(msg)
            data = data["message"]
            text = ""
            #handles different lines
            for item in data["textboxes"]:
                if text == "":
                    text = item["text"]
                else:
                    text = text + "; " + item["text"]
            username = data["player"]["name"]
            print(f">> [{username}]: {text}")
            #command handles
            if text.startswith(">"):
                await self.bot.commands.handlecommand(username, msg, text)
            if text.startswith("!"):
                await self.bot.commands.handlecommand(username, msg, text)

    async def playerconnection(self, username, connection: bool):
        if connection == True:
            print(f"[+] {username}")
        else:
            print(f"[-] {username}")
    
    async def sv_nameVerified(self):
        print(f'Logged in successfully as {self.bot.username}, color {self.bot.color}, to {self.bot.room}')
        await self.bot.join_room()