import asyncio
import threading
from discordBot import run_discord_bot, DiscordBot
from twitchBot import run_twitch_bot, TwitchBot
from dotenv import load_dotenv
import os
import azure

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

discord_bot = DiscordBot()
twitch_bot = TwitchBot(discord_bot=discord_bot)

discord_bot.twitch_bot = twitch_bot

# Start wait loop so twitch bot gets active discord bot
def start_discord():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(discord_bot.start(TOKEN))

def start_twitch():
    while not discord_bot.is_ready():  # Wait until Discord bot is fully ready
        pass

    print("Discord bot is ready! Starting Twitch bot...")
    discord_bot.twitch_bot = twitch_bot
    run_twitch_bot(discord_bot)  # Pass the instance

if __name__ == "__main__":
    discord_thread = threading.Thread(target=start_discord)
    twitch_thread = threading.Thread(target=start_twitch)

    discord_thread.start()
    twitch_thread.start()

    discord_thread.join()
    twitch_thread.join()

    tts_manager = azure.AzureTTSManager()