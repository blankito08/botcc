#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 18008747, #get it from https://my.telegram.org/auth
    api_hash="5dccb5200b10b11e2afa3d31025f8efd", #get it from https://my.telegram.org/auth
    bot_token="5789891604:AAG-006PlEo4pFm_OqwDe6vocTIN0qr3pdw", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
