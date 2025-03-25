# bot.py
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
import tts
import twitchBot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class DiscordBot(commands.Bot):
    def __init__(self, twitch_bot=None):
        super().__init__(command_prefix='$', intents=intents)
        self.setup_commands()
        self.twitch_bot = twitch_bot
        self.channel = None
        self.voice_client = None
    def setup_commands(self):
        @self.event
        async def on_ready():
            print("Discord bot is ready for use\n")
            print(f'Discord Twitch bot: {self.twitch_bot}')

        @self.command()
        async def join(ctx):
            print("Join Command Ran")

            if ctx.author.voice is None:
                await ctx.send("You are not in a Voice Channel!")
                return
            if self.channel != None:
                await self.voice_client.disconnect()

            
            self.channel = ctx.author.voice.channel
            self.voice_client = await self.channel.connect()
            await ctx.send('Joined Channel')
            

        @self.command()
        async def leave(ctx):
            print("Leave Command Ran")
            if self.voice_client is None:
                await ctx.send("I am not in a Voice Channel")
                return

            await self.voice_client.disconnect()
            self.voice_client = None
            self.channel = None

        @self.command()
        async def play(ctx, *, message):
            print("Play command ran")
            if not message:
                await ctx.send("Please provide a message")
                return

            await self.play_message(str(message))

        @self.command()
        async def link(ctx, channel):
            if channel:
                print("Linking Channel!")
                await self.twitch_bot.link(channel)
                await ctx.send(f'Joined channel: {channel}')
            else:
                print("No Channel Provided")

    async def play_message(self, msg):
        if self.voice_client is None:
            print("Cannot play audio, not connected to channel")
            return
        
        if self.voice_client.is_playing():
            print("Already playing audio")
            return
        
        print("Playing Audio")
        try:
            audio_file = await tts.get_audio(msg)
    
        except Exception as e:
            if e.status_code == 401:
                audio_file = await tts.get_gtts(msg)
                print(f'Out of credits, Using gTTS')

        await self.play_audio(audio_file=audio_file)

    async def play_audio(self, audio_file):
        try:
                self.voice_client.play(
                    discord.FFmpegPCMAudio(
                    executable="C:/ffmpeg/bin/ffmpeg.exe",  # Adjust path to ffmpeg
                    source=audio_file
                    )
                )
        except Exception as e:
            print(f'Error playing audio {e}')

        while self.voice_client.is_playing():
            print("Playing Message")
            await asyncio.sleep(0.5)

        print("Audio played successfully")
        twitchBot.audio_playing = False

    async def run_bot(self):
        await self.start(TOKEN)


bot = DiscordBot()

def run_discord_bot():
    asyncio.run(bot.run_bot())

if __name__ == "__main__":
    run_discord_bot()
