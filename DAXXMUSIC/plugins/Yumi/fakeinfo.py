"""***
MIT License

Copyright (c) [2023] [SAIFDEAD]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.***
"""

import requests
from pyrogram import Client
from pyrogram import filters
from DAXXMUSIC import app


random_user_api_url = 'https://randomuser.me/api/'


@app.on_message(filters.command("fake", prefixes="/"))
def generate_fake_user_by_country(client, message):
    country_name = message.text.split("/fake ", maxsplit=1)[1]
    
    # Call the RandomUser API to get fake user information for the specified country
    response = requests.get(f'{random_user_api_url}?nat={country_name}')
    
    if response.status_code == 200:
        user_info = response.json()['results'][0]
        # Extract user details
        first_name = user_info['name']['first']
        last_name = user_info['name']['last']
        email = user_info['email']
        country = user_info['location']['country']
        state = user_info['location']['state']
        city = user_info['location']['city']
        street = user_info['location']['street']['name']
        zip_code = user_info['location']['postcode']
        # Reply with the generated fake user information for the specified country
        message.reply_text(f"𝗡ᴀᴍᴇ➪ {first_name} {last_name}\n\n𝗘ᴍᴀɪʟ➪ {email}\n\n𝗖ᴏᴜɴᴛʀʏ➪ {country}\n\n𝗦ᴛᴀᴛᴇ➪ {state}\n\n𝗖ɪᴛʏ: {city}\n\n𝐀ᴅᴅʀᴇss:➪{street}\n\n𝗭ɪᴘ ᴄᴏᴅᴇ➪ {zip_code}")
    else:
        message.reply_text(f"ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ғᴀᴋᴇ ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғᴏʀ {country_name}.")
