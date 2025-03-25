import os
from twitchio.ext import commands, routines
from dotenv import load_dotenv
import asyncio
import tts
import re

load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
CHANNEL_NAME = 'mrsqueeg'
CURSES = []

class TwitchBot(commands.Bot):
    def __init__(self, discord_bot=None):  # Accept Discord bot
        super().__init__(token=ACCESS_TOKEN, prefix='!', initial_channels=['creatorcreepy'])
        self.discord_bot = discord_bot  # Store Discord bot reference
        self.channel = None
        self.audio_playing = False
        self.require_cheer = True
        print(f"Twitch Bot initialized Bot: {self.discord_bot}")

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        # Store channel reference and start routine
        self.channel = self.get_channel(CHANNEL_NAME)

    async def event_message(self, msg):
        if msg.echo:
            return
        if self.audio_playing == True:
            print('Audio message already playing')
            return
        
        # Check messages for cheers if required
        print(f'{msg.author} - {msg.content}')
        if self.require_cheer == True:
            match = re.search(r'Cheer\d+',msg.content)
            if match:
                # Check value after 'Cheer' is greater than 0 so that real cheers are played
                print('Match Found')
                if (msg.content[match.start()+5] != '0') and (msg.content[match.start()+5] != '-'):
                    print('Playing Chat Message')
                    self.audio_playing = True
                    await self.play(msg.content)
                    return
                
        # Run if we dont need cheer in message
        else:
            print('Playing Chat Message')
            await self.play(msg.content)
        
        # Handle commands
        await self.handle_commands(msg)

    async def play(self, msg):
        try:  
            # Message Exists
            if not msg:
                return
            
            # No bad words
            if any(curse in msg.lower() for curse in CURSES):
                print("Message contained curse word")
                return
            
            # Bot Linked and play
            if self.discord_bot:
                await self.discord_bot.play_message(msg)
            
        except Exception as e:
            print(f"Error in play command: {e}")

    async def link(self, channel):
        if not channel:
            return
        
        print(f"Twitch Joining: {channel}")

        await self.connected_channels.append(channel)

async def run_bot(discord_bot=None):
    bot = TwitchBot(discord_bot)
    await bot.start()

def run_twitch_bot(discord_bot=None):
    asyncio.run(run_bot(discord_bot))

if __name__ == "__main__":
    run_twitch_bot()
    