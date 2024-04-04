import asyncio
import websockets
import json

from bot.Bot import Bot

BOTNAME = 'BOT'
BOTCOLOR = 4849907

# ----------------------------------------------- #          
        

async def main():
    bot = Bot(BOTNAME, BOTCOLOR)
    await bot.connection.connect()

if __name__ == "__main__":
    asyncio.run(main())
