from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from DAXXMUSIC import app as DAXX


mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')


@DAXX.on_message(filters.command("mongochk"))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴍᴏɴɢᴏᴅʙ ᴜʀʟ ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ. ᴇxᴀᴍᴘʟᴇ: /mongochk your_ᴍᴏɴɢᴏᴅʙ_url")
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("𝗠𝗼𝗻𝗴𝗼𝗗𝗕 𝗨𝗥𝗟 𝗶𝘀 𝘃𝗮𝗹𝗶𝗱 𝗮𝗻𝗱 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹 ✅")
        except Exception as e:
            await message.reply(f"ғᴀɪʟᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴍᴏɴɢᴏᴅʙ: {e}")
    else:
        await message.reply("𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗠𝗼𝗻𝗴𝗼𝗗𝗕 𝗨𝗥𝗟 𝗳𝗼𝗿𝗺𝗮𝘁 ")
