from telethon import __version__, events, Button

from config import X1


START_BUTTON = [
    [
        Button.url(" 𝐌ᴜsɪᴄ ", "https://t.me/RUHI_X_MUSICBOT"),
        Button.url("𝐎ᴡɴᴇʀ", "https://t.me/its_innocent_boy_8202")
    ],
    [
        Button.url(" 𝐂н𝙰𝙽𝙽𝙴𝙻 ", "https://t.me/THE_FUCKING_BOT_2926"),
        Button.url(" 𝐒𝚄𝙿𝙿𝙾𝚃  ", "https://t.me/THE_FUCKER_BOTS_2926")
    ],
]


@X1.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n"
        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/c6abb12b29b471031ace1.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
