from pyrogram import Client, filters
import requests
from DAXXMUSIC import app


TMDB_API_KEY = "23c3b139c6d59ebb608fe6d5b974d888"


@app.on_message(filters.command("movie"))
async def movie_command(client, message):
    try:
        # Check if the user provided a movie name after the /movie command
        if len(message.command) > 1:
            movie_name = " ".join(message.command[1:])

            # Fetch movie information from TMDb API
            movie_info = get_movie_info(movie_name)

            # Send the movie information as a reply
            await message.reply_text(movie_info)
        else:
            await message.reply_text("ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴀ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ᴀғᴛᴇʀ ᴛʜᴇ /movie ᴄᴏᴍᴍᴀɴᴅ.")
    except Exception as e:
        await message.reply_text(f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ: {str(e)}")

def get_movie_info(movie_name):
    tmdb_api_url = f"https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": movie_name}
    
    response = requests.get(tmdb_api_url, params=params)
    data = response.json()

    if data.get("results"):
        # Get information about the first movie in the results
        movie = data["results"][0]
        
        # Fetch additional details using the movie ID
        details_url = f"https://api.themoviedb.org/3/movie/{movie['id']}"
        details_params = {"api_key": TMDB_API_KEY}
        details_response = requests.get(details_url, params=details_params)
        details_data = details_response.json()
        
        # Extract relevant information
        title = details_data.get("title", "N/A")
        release_date = details_data.get("release_date", "N/A")
        overview = details_data.get("overview", "N/A")
        providers = details_data.get("providers", "N/A")
        vote_average = details_data.get("vote_average", "N/A")
        
        # Extract actor names
        cast_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits"
        cast_params = {"api_key": TMDB_API_KEY}
        cast_response = requests.get(cast_url, params=cast_params)
        cast_data = cast_response.json()
        actors = ", ".join([actor["name"] for actor in cast_data.get("cast", [])])
        
        # Extract total collection
        revenue = details_data.get("revenue", "N/A")
        
        # Format and return movie information
        info = (
            f"𝐓ɪᴛʟᴇ: {title}\n\n"
            f"𝐑ᴇʟᴇᴀsᴇ 𝐃ᴀᴛᴇ: {release_date}\n\n"
            f"𝐎ᴠᴇʀᴠɪᴇᴡ: {overview}\n\n"
            f"𝐕ᴏᴛᴇ 𝐀ᴠᴇʀᴀɢᴇ: {vote_average}\n\n"
            f"𝐀ᴄᴛᴏʀ 𝐍ᴀᴍᴇs: {actors}\n\n"
            f"𝐓ᴏᴛᴀʟ 𝐂ᴏʟʟᴇᴄᴛɪᴏɴ: {revenue}\n\n"
            f"𝐀ᴠᴀɪʟᴀʙʟᴇ 𝐏ʟᴀᴛғᴏʀᴍs: {providers}\n"
        )
        return info
    else:
        return "ᴍᴏᴠɪᴇ ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ᴀᴘɪ ʀᴇǫᴜᴇsᴛ ғᴀɪʟᴇᴅ."
