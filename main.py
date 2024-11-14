import twitchAPI
from gtts import gTTS
import discord
import os
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '$', intents=intents)

@client.event
async def on_ready():
    print("Ready for use\n")

@client.command()
async def join(ctx):
    print("Join Command Ran")
    print(ctx)
    if ctx.author.voice == None:
        await ctx.send("You are not in a Voice Channel!")
        return
    
    if ctx.voice_client != None and ctx.voice_client == ctx.author.voice.channel:
        await ctx.send("Im already connected to this channel")
        return

    if ctx.voice_client != None:
        await ctx.voice_client.disconnect()

    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    print("Leave Command Ran")
    if ctx.voice_client == None:
        await ctx.send("I am not in a Voice Channel")
        return
        
    await ctx.voice_client.disconnect()

@client.command()
async def link(ctx):
    print("Link Twitch Command Ran")
    await ctx.send("Linking Twitch!")

client.run(TOKEN)