import base64
import httpx
import os
from pyrogram import filters
from config import BOT_USERNAME
from DAXXMUSIC import app
from pyrogram import filters
import pyrogram
from uuid import uuid4
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


######### sticker id

@app.on_message(filters.command("st"))
def generate_sticker(client, message):
    if len(message.command) == 2:
        sticker_id = message.command[1]
        try:
            client.send_sticker(message.chat.id, sticker=sticker_id)
        except Exception as e:
            message.reply_text(f"Error: {e}")
    else:
        message.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ sᴛɪᴄᴋᴇʀ ɪᴅ ᴀғᴛᴇʀ /st ᴄᴏᴍᴍᴀɴᴅ.")


#---------





@app.on_message(filters.command("packkang"))
async def _packkang(app :app,message):  
    txt = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ....**")
    if not message.reply_to_message:
        await txt.edit('ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ')
        return
    if not message.reply_to_message.sticker:
        await txt.edit('ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ')
        return
    if message.reply_to_message.sticker.is_animated or  message.reply_to_message.sticker.is_video:
        return await txt.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ɴᴏɴ-ᴀɴɪᴍᴀᴛᴇᴅ sᴛɪᴄᴋᴇʀ")
    if len(message.command) < 2:
        pack_name =  f'{message.from_user.first_name}_sticker_pack_by_@{BOT_USERNAME}'
    else :
        pack_name = message.text.split(maxsplit=1)[1]
    short_name = message.reply_to_message.sticker.set_name
    stickers = await app.invoke(
        pyrogram.raw.functions.messages.GetStickerSet(
            stickerset=pyrogram.raw.types.InputStickerSetShortName(
                short_name=short_name),
            hash=0))
    shits = stickers.documents
    sticks = []
    
    for i in shits:
        sex = pyrogram.raw.types.InputDocument(
                id=i.id,
                access_hash=i.access_hash,
                file_reference=i.thumbs[0].bytes
            )
        
        sticks.append(
            pyrogram.raw.types.InputStickerSetItem(
                document=sex,
                emoji=i.attributes[1].alt
            )
        )

    try:
        short_name = f'stikcer_pack_{str(uuid4()).replace("-","")}_by_{app.me.username}'
        user_id = await app.resolve_peer(message.from_user.id)
        await app.invoke(
            pyrogram.raw.functions.stickers.CreateStickerSet(
                user_id=user_id,
                title=pack_name,
                short_name=short_name,
                stickers=sticks,
            )
        )
        await txt.edit(f"**ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴋᴀɴɢᴇᴅ ʟɪɴᴋ**!\n**ᴛᴏᴛᴀʟ sᴛɪᴄᴋᴇʀ **: {len(sticks)}",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝐏ᴀᴄᴋ 𝐋ɪɴᴋ",url=f"http://t.me/addstickers/{short_name}")]]))
    except Exception as e:
        await message.reply(str(e))


###### sticker id =
@app.on_message(filters.command(["stickerid","stid"]))
async def sticker_id(app: app, msg):
    if not msg.reply_to_message:
        await msg.reply_text("𝐑𝐞𝐩𝐥𝐚𝐲 ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ")        
    elif not msg.reply_to_message.sticker:
        await msg.reply_text("𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚 𝐬𝐭𝐢𝐜𝐤𝐞𝐫")        
    st_in = msg.reply_to_message.sticker
    await msg.reply_text(f"""
⊹ <u>**sᴛɪᴄᴋᴇʀ ɪɴғᴏ**</u> ⊹
**⊚ sᴛɪᴄᴋᴇʀ ɪᴅ **: `{st_in.file_id}`\n
**⊚ sᴛɪᴄᴋᴇʀ ᴜɴɪǫᴜᴇ ɪᴅ **: `{st_in.file_unique_id}`
""")


#####
