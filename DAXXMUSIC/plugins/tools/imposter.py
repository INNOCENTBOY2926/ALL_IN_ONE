import random 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from DAXXMUSIC.plugins.tools.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from DAXXMUSIC import app

MISHI = [
"https://te.legra.ph/file/18a754b9c1df61427992e.jpg",
"https://te.legra.ph/file/68a5a003282b353609828.jpg",
"https://te.legra.ph/file/fa87b2f47ed6d2a2641f6.jpg",
"https://te.legra.ph/file/7e5d608a1437fabc22fca.jpg",
"https://te.legra.ph/file/b7c2c0beac656f78a1ead.jpg",
"https://te.legra.ph/file/ce7ee90be3a77b49c1be5.jpg",
"https://te.legra.ph/file/6d2c3d854f54da97f31f7.jpg",
"https://te.legra.ph/file/43b6190d401bf57276220.jpg",
"https://te.legra.ph/file/0e52c40be2b6fc8d092ce.jpg",
"https://te.legra.ph/file/194474140c27f63bc6b65.jpg",
"https://te.legra.ph/file/12d545bd67b81d12140e0.jpg",
"https://te.legra.ph/file/42e5d1916e97eff7cfe87.jpg",
"https://te.legra.ph/file/610ee36e620d86422c13c.jpg",
"https://te.legra.ph/file/3317f8331e0f4e0a4348a.jpg",
"https://te.legra.ph/file/1ef296f0e545422c57747.jpg",
"https://te.legra.ph/file/8719feedf475f42185c7a.jpg",
"https://te.legra.ph/file/ef46323bd0a99826c1860.jpg",
"https://te.legra.ph/file/a9a30166d484436b13276.jpg",
"https://te.legra.ph/file/5a80607332f06333503a7.jpg",    
"https://te.legra.ph/file/18a754b9c1df61427992e.jpg",
"https://te.legra.ph/file/68a5a003282b353609828.jpg",
"https://te.legra.ph/file/fa87b2f47ed6d2a2641f6.jpg",
"https://te.legra.ph/file/7e5d608a1437fabc22fca.jpg",
"https://te.legra.ph/file/b7c2c0beac656f78a1ead.jpg",
"https://te.legra.ph/file/ce7ee90be3a77b49c1be5.jpg",
"https://te.legra.ph/file/6d2c3d854f54da97f31f7.jpg",
"https://te.legra.ph/file/43b6190d401bf57276220.jpg",
"https://te.legra.ph/file/7c442fd2ecf5b53ebcc53.jpg",
"https://te.legra.ph/file/194474140c27f63bc6b65.jpg",
"https://te.legra.ph/file/12d545bd67b81d12140e0.jpg",
"https://te.legra.ph/file/42e5d1916e97eff7cfe87.jpg",
"https://te.legra.ph/file/610ee36e620d86422c13c.jpg",
"https://te.legra.ph/file/3317f8331e0f4e0a4348a.jpg",
"https://te.legra.ph/file/1ef296f0e545422c57747.jpg",
"https://te.legra.ph/file/8719feedf475f42185c7a.jpg",
"https://te.legra.ph/file/ef46323bd0a99826c1860.jpg",
"https://te.legra.ph/file/a9a30166d484436b13276.jpg",
"https://te.legra.ph/file/5a80607332f06333503a7.jpg",
]


ROY = [
    [
        InlineKeyboardButton(
            text="•─╼⃝𖠁 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ 𖠁⃝╾─•",
            url=f"https://t.me/HINATA_N_BOT?startgroup=true"),
        InlineKeyboardButton(text="𝐔ᴘᴅᴀᴛᴇ", url=f"https://t.me/SAIFALLBOT")
    ],
]


@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**♥︎ 𝐔sᴇʀ 𝐒ʜᴏʀᴛ 𝐈ɴғᴏʀᴍᴀᴛɪᴏɴ ♥︎**

**๏ 𝐍ᴀᴍᴇ** ➛ {message.from_user.mention}
**๏ 𝐔sᴇʀ 𝐈ᴅ** ➛ {message.from_user.id}
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**♥︎ 𝐂ʜᴀɴɢᴇᴅ 𝐔sᴇʀɴᴀᴍᴇ ♥︎**

**๏ 𝐁ᴇғᴏʀᴇ** ➛ {bef}
**๏ 𝐀ғᴛᴇʀ** ➛ {aft}
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**♥︎ 𝐂ʜᴀɴɢᴇs 𝐅ɪʀsᴛ 𝐍ᴀᴍᴇ ♥︎**

**๏ 𝐁ᴇғᴏʀᴇ** ➛ {bef}
**๏ 𝐀ғᴛᴇʀ** ➛ {aft}
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**♥︎ 𝐂ʜᴀɴɢᴇs 𝐋ᴀsᴛ 𝐍ᴀᴍᴇ ♥︎**

**๏ 𝐁ᴇғᴏʀᴇ** ➛ {bef}
**๏ 𝐀ғᴛᴇʀ** ➛ {aft}
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo(random.choice(MISHI), caption=msg, reply_markup=InlineKeyboardMarkup(ROY),)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    else:
        await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")

    
