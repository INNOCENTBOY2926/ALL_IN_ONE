from pyrogram import Client, enums, filters
#from config import *
import asyncio
from DAXXMUSIC import app as app

from pyrogram.handlers import MessageHandler


@app.on_message(filters.command("dice"))
async def dice(bot, message):
    x=await bot.send_dice(message.chat.id)
    m=x.dice.value
    await message.reply_text(f"ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs : {m}",quote=True)
  
@app.on_message(filters.command("dart"))
async def dart(bot, message):
    x=await bot.send_dice(message.chat.id, "🎯")
    m=x.dice.value
    await message.reply_text(f"ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs : {m}",quote=True)

@app.on_message(filters.command("basket"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🏀")
    m=x.dice.value
    await message.reply_text(f"ʜᴇʏ ʙᴀʙᴜ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs : {m}",quote=True)
@app.on_message(filters.command("jackpot"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎰")
    m=x.dice.value
    await message.reply_text(f"ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs : {m}",quote=True)
@app.on_message(filters.command("ball"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎳")
    m=x.dice.value
    await message.reply_text(f"ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs : {m}",quote=True)
@app.on_message(filters.command("football"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "⚽")
    m=x.dice.value
    await message.reply_text(f"ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs : {m}",quote=True)
__help__ = """
 Play Game With Emojis:
/dice - Dice 🎲.
/dart - Dart 🎯
/basket - Basket Ball 🏀
/ball - Bowling Ball 🎳
/football - Football ⚽
/jackpot - Spin slot machine 🎰
 """

__mod_name__ = "Dɪᴄᴇ"
