import random
import time
import requests
from DAXXMUSIC import app
from config import BOT_USERNAME

from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

@app.on_message(filters.command(["chatgpt","ai","ask","gpt","solve"],  prefixes=["+", ".", "/", "-", "", "$","#","&"]))
async def chat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "Example:\n\n/ᴄʜᴀᴛɢᴘᴛ ᴡʜᴇʀᴇ ɪs sᴀɪғ ᴅɪᴄᴛᴀᴛᴏʀ?"
            )
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://chatgpt.apinepdev.workers.dev/?question={a}')

            try:
                # Check if "results" key is present in the JSON response
                if "answer" in response.json():
                    x = response.json()["answer"]
                    end_time = time.time()
                    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                    await message.reply_text(
                        f" {x}      ᴀɴsᴡᴇʀɪɴɢ ʙʏ ➛  @{Bot_username}",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("ɴᴏ 'results' ᴋᴇʏ ғᴏᴜɴᴅ ɪɴ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ.")
            except KeyError:
                # Handle any other KeyError that might occur
                await message.reply_text("ᴇʀʀᴏʀ ᴀᴄᴄᴇssɪɴɢ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ.")
    except Exception as e:
        await message.reply_text(f"**ʜᴇʟʟᴏ: {e} ")
