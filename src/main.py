import asyncio
import websockets
import json

from bot.Bot import Bot

async def init():
    BOTNAME = 'BOT'
    BOTCOLOR = 4849907
    bot = Bot(BOTNAME, BOTCOLOR)
    await bot.connection.connect()

if __name__ == "__main__":
    asyncio.run(init())
