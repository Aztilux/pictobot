import json
import asyncio


class Commands: 
    def __init__(self, bot):
        self.bot = bot

    async def handlecommand(self, username: str, raw, command: str):
        raw = json.loads(raw)
        if username != self.bot.username:
            if command.startswith(">mimic"):
                await self.mimic(raw)
            elif command.startswith(">line"):
                await self.line(command)
            elif command.startswith(">clear"):
                await self.clear()
            if command.startswith("!help") or command.startswith("!cmds"):
                await self.help()

    async def mimic(self, raw):
        for item in raw['message']['textboxes']:
          item["text"] = item["text"].replace('>mimic', '').strip()
        await asyncio.sleep(1)  
        #command troll fix
        if item["text"].startswith('!'):
          item["text"] = item["text"].replace('!', '').strip() 
        await self.bot.sendmsg(raw['message']['drawing'], raw['message']['textboxes'], raw['message']['lines'])

    async def line(self, command):
        args = command.split()
        try:
            try:
                x1 = int(args[1])
                y1 = int(args[2])
                x2 = int(args[3])
                y2 = int(args[4])
                type = int(args[5])
            except IndexError:
                msg = [{"text":"Not enough arguments!","x":113,"y":211}]
                await self.bot.sendmsg(textboxes=msg, lines=1)       
                return            
        except ValueError:
            msg = [{"text":"Argument is not number!","x":113,"y":211}]
            await self.bot.sendmsg(textboxes=msg, lines=1)
            return
        line = await self.bot.draw.line(x1, y1, x2, y2, type)
        for point in line:
            self.bot.draw.freecanvas.append(point)
        await self.bot.sendmsg(drawing=self.bot.draw.freecanvas)
    
    async def clear(self):
       self.bot.draw.freecanvas = []
       await self.bot.sendmsg(textboxes=[{"text":"Canvas clear!","x":113,"y":211}])    

    async def help(self):
        # help = help message (5 lines)
        help = [{"text":"pict.chat commands are:","x":113,"y":211},{"text":"!block/!unblock - hide messages of others.","x":27,"y":226.99999999999997},{"text":"!tripcode - unique code to identify yourself.","x":27,"y":243.00000000000003},{"text":"!list - lists online users.","x":27,"y":259},{"text":"Note: the tripcode is sent publicly.","x":27,"y":275}]
        await self.bot.sendmsg(textboxes=help)