import re
from dotenv import load_dotenv
from pyrogram import filters
import random
from pyrogram.types import Message
from pyrogram import Client, filters
from DAXXMUSIC import app



# "/gn" command ka handler
@app.on_message(filters.command("oodnight", prefixes="g"))
def goodnight_command_handler(client: Client, message: Message):
    # Randomly decide whether to send a sticker or an emoji
    send_sticker = random.choice([True, False])
    
    # Send a sticker or an emoji based on the random choice
    if send_sticker:
        client.send_sticker(message.chat.id, get_random_sticker())
    else:
        client.send_message(message.chat.id, get_random_emoji())

# Function to get a random sticker
def get_random_sticker():
    stickers = [
        "CAACAgUAAx0Cc_auxAABAkRzZeS6kOKDfQE4aDQqEGWq0OgemDwAAlsGAAIcpaFWjn5NcfNnKX40BA",
        "CAACAgUAAx0Cc_auxAABAkR0ZeS6kUK0sp8inx9WQy11ErvbNqQAAksFAALDr6FWmkJMXlo4A2Y0BA",
        "CAACAgUAAx0Cc_auxAABAkR1ZeS6lurEQDM6X7yUnws7fU9QSk0AAg8GAALKWnBV6GH7ln3-kcw0BA",
        "CAACAgUAAx0Cc_auxAABAkR2ZeS6pB2LJqLfCYc6Kyo0Gl1pNMUAAnUKAAKLoEhVTw5Jk7rmsTc0BA",
        "CAACAgUAAx0Cc_auxAABAkR3ZeS6qGV4JtskSQ9sgR1HBMxrQKQAAk8HAALCu0hVa0Z2OjQ2iTA0BA",
        "CAACAgUAAx0Cc_auxAABAkR4ZeS6qZFzI8EZqXITWuRgr550HY0AAvYIAALaXkhVRTThG9g16V00BA",
    ]
    return random.choice(stickers)

# Function to get a random emoji
def get_random_emoji():
    emojis = [
        "😴",
        "😪", 
        "💤",
        
    ]
    return random.choice(emojis)
