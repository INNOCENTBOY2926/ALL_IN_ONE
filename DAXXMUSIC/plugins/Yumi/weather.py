from pyrogram import Client, filters
from DAXXMUSIC import app


@app.on_message(filters.command("weather"))
def weather(client, message):
    try:
        # Get the location from user message
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"
        
        # Reply with the weather information as a photo
        message.reply_photo(photo=weather_url, caption="ʜᴇʀᴇ's ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ғᴏʀ ʏᴏᴜʀ ʟᴏᴄᴀᴛɪᴏɴ")
    except IndexError:
        # User didn't provide a location
        message.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʟᴏᴄᴀᴛɪᴏɴ. ᴜsᴇ /weather ʙɪʜᴀʀ")
