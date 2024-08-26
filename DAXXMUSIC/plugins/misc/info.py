import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from DAXXMUSIC import app
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram.types import *
from typing import Union, Optional
import random

random_photo = [
    "https://te.legra.ph/file/20891672efabd974a1929.jpg",
    "https://te.legra.ph/file/76e15f09492b116bad823.jpg",
    "https://te.legra.ph/file/d52c48b6b12111d25a7a4.jpg",
    "https://te.legra.ph/file/6ce4a3837e01210b2955e.jpg",
    "https://te.legra.ph/file/da522c26240a8e6855e23.jpg",
    "https://te.legra.ph/file/038954fd6961240321205.jpg",
    "https://te.legra.ph/file/ac6645564893ce791c552.jpg",
    "https://te.legra.ph/file/00de9d17b0f828e50a7a5.jpg",
    "https://te.legra.ph/file/f6ca5b940cacff5dba316.jpg",
]

# --------------------------------------------------------------------------------- #


get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #


async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],    
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )


    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path
   

# --------------------------------------------------------------------------------- #

bg_path = "DAXXMUSIC/assets/userinfo.png"
font_path = "DAXXMUSIC/assets/hiroko.ttf"

# --------------------------------------------------------------------------------- #


INFO_TEXT = """**
❅─────✧❅✦❅✧─────❅
            ✦ ᴜsᴇʀ ɪɴғᴏ ✦

➻ 𝐔sᴇʀ 𝐈ᴅ ‣ **`{}`
**➻ 𝐅ɪʀsᴛ 𝐍ᴀᴍᴇ ‣ **{}
**➻ 𝐋ᴀsᴛ 𝐍ᴀᴍᴇ ‣ **{}
**➻ 𝐔sᴇʀɴᴀᴍᴇ ‣ **`{}`
**➻ 𝐌ᴇɴᴛɪᴏɴ ‣ **{}
**➻ 𝐋ᴀsᴛ 𝐒ᴇᴇɴ ‣ **{}
**➻ 𝐃ᴄ 𝐈ᴅ ‣ **{}
**➻ 𝐁ɪᴏ ‣ **`{}`

**❅─────✧❅✦❅✧─────❅**
"""

# --------------------------------------------------------------------------------- #

async def userstatus(user_id):
   try:
      user = await app.get_users(user_id)
      x = user.status
      if x == enums.UserStatus.RECENTLY:
         return "Recently."
      elif x == enums.UserStatus.LAST_WEEK:
          return "Last week."
      elif x == enums.UserStatus.LONG_AGO:
          return "Long time ago."
      elif x == enums.UserStatus.OFFLINE:
          return "Offline."
      elif x == enums.UserStatus.ONLINE:
         return "Online."
   except:
        return "**sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ !**"
    

# --------------------------------------------------------------------------------- #



@app.on_message(filters.command(["info", "userinfo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def userinfo(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if not message.reply_to_message and len(message.command) == 2:
        try:
            user_id = message.text.split(None, 1)[1]
            user_info = await app.get_chat(user_id)
            user = await app.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            first_name = user_info.first_name 
            last_name = user_info.last_name if user_info.last_name else "ɴᴏ ʟᴀsᴛ ɴᴀᴍᴇ"
            username = user_info.username if user_info.username else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
            mention = user.mention
            bio = user_info.bio if user_info.bio else "ɴᴏ ʙɪᴏ sᴇᴛ"
            
            if user.photo:
                # User has a profile photo
                photo = await app.download_media(user.photo.big_file_id)
                welcome_photo = await get_userinfo_img(
                    bg_path=bg_path,
                    font_path=font_path,
                    user_id=user.id,
                    profile_path=photo,
                )
            else:
                # User doesn't have a profile photo, use random_photo directly
                welcome_photo = random.choice(random_photo)
                
            await app.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, first_name, last_name, username, mention, status, dc_id, bio), reply_to_message_id=message.id)
        except Exception as e:
            await message.reply_text(str(e))        
      
    elif not message.reply_to_message:
        try:
            user_info = await app.get_chat(user_id)
            user = await app.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            first_name = user_info.first_name 
            last_name = user_info.last_name if user_info.last_name else "ɴᴏ ʟᴀsᴛ ɴᴀᴍᴇ"
            username = user_info.username if user_info.username else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
            mention = user.mention
            bio = user_info.bio if user_info.bio else "No bio set"
            
            if user.photo:
                # User has a profile photo
                photo = await app.download_media(user.photo.big_file_id)
                welcome_photo = await get_userinfo_img(
                    bg_path=bg_path,
                    font_path=font_path,
                    user_id=user.id,
                    profile_path=photo,
                )
            else:
                # User doesn't have a profile photo, use random_photo directly
                welcome_photo = random.choice(random_photo)
                
            await app.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, first_name, last_name, username, mention, status, dc_id, bio), reply_to_message_id=message.id)
        except Exception as e:
            await message.reply_text(str(e))

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        try:
            user_info = await app.get_chat(user_id)
            user = await app.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            first_name = user_info.first_name 
            last_name = user_info.last_name if user_info.last_name else "ɴᴏ ʟᴀsᴛ ɴᴀᴍᴇ"
            username = user_info.username if user_info.username else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
            mention = user.mention
            bio = user_info.bio if user_info.bio else "ɴᴏ ʙɪᴏ sᴇᴛ"
            
            if user.photo:
                # User has a profile photo
                photo = await app.download_media(user.photo.big_file_id)
                welcome_photo = await get_userinfo_img(
                    bg_path=bg_path,
                    font_path=font_path,
                    user_id=user.id,
                    profile_path=photo,
                )
            else:
                # User doesn't have a profile photo, use random_photo directly
                welcome_photo = random.choice(random_photo)
                
            await app.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, first_name, last_name, username, mention, status, dc_id, bio), reply_to_message_id=message.id)
        except Exception as e:
            await message.reply_text(str(e))
                
