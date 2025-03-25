import os
from dotenv import load_dotenv
from gtts import gTTS
import discord
import asyncio
from discord.ext import commands
from elevenlabs import save
from elevenlabs.client import AsyncElevenLabs
import discordBot

load_dotenv()

eleven_client = AsyncElevenLabs(
    api_key=os.getenv('ELEVEN_KEY'),
)

async def get_audio(msg):
    print(f"Getting Audio: {msg}")
    audio = await eleven_client.generate(
        text=msg,
        voice="Callum",
        model="eleven_multilingual_v2",
    )

    out = b''
    async for value in audio:
        out += value

    save(out, 'chatMessage.mp3')

    return 'chatMessage.mp3'

async def get_gtts(msg):
    ttsObj = gTTS(text=msg, lang='en', tld='co.uk', slow=False)
    ttsObj.save('gttsMessage.mp3')
    return 'gttsMessage.mp3'