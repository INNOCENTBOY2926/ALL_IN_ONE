from ... import *
from pyrogram import *
from pyrogram.types import *


@app.on_message(filters.command(["bin", "ccbin", "bininfo"], [".", "!", "/"]))
async def check_ccbin(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b>ᴘʟᴇᴀsᴇ ɢɪᴠᴇ Me ᴀ ʙɪɴ ᴛᴏ\nɢᴇᴛ ʙɪɴ ᴅᴇᴛᴀɪʟs !</b>"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("<b>ᴄʜᴇᴄᴋɪɴɢ ...</b>")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("<b> ᴡʀᴏɴɢ ʙɪɴ❗...</b>")
    try:
        resp = await api.bininfo(bin)
        await aux.edit(f"""
<b> 𝗩ᴀʟɪᴅ ʙɪɴ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ✅</b>

<b>🏦 𝗕ᴀɴᴋ ➪</b> <tt>{resp.bank}</tt>
<b>💳 𝗕ɪᴍ ➪</b> <tt>{resp.bin}</tt>
<b>🏡 𝗖ᴏᴜɴᴛʀʏ ➪</b> <tt>{resp.country}</tt>
<b>🇮🇳 𝗙ʟᴀɢ ➪</b> <tt>{resp.flag}</tt>
<b>🧿 𝗜sᴏ ➪</b> <tt>{resp.iso}</tt>
<b>⏳ 𝗟ᴇᴠᴇʟ ➪</b> <tt>{resp.level}</tt>
<b>🔴 𝗣ʀᴇᴘᴀɪᴅ ➪</b> <tt>{resp.prepaid}</tt>
<b>🆔 𝗧ʏᴘᴇ ➪</b> <tt>{resp.type}</tt>
<b>ℹ️ 𝗩ᴇɴᴅᴏᴏʀ➪</b> <tt>{resp.vendor}</tt>"""
        )
    except:
        return await aux.edit(f"""
🚫 ʙɪɴ ɴᴏᴛ ʀᴇᴄᴏɢɴɪᴢᴇᴅ. ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴀ ᴠᴀʟɪᴅ ʙɪɴ.""")
