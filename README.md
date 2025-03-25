# VC-Link
Connect your twitch channels messages to a discord servers Voice Chat!

## Preface
Currently the bot needs to be setup yourself locally however I plan on adding multi-guild, and multi-channel support. Once those are setup there will be a Discord Invite link for my bot that you can simply use to connect your server and chat together. You will need to have some programming expierence to get setup and I will not personally reach out to help you if you are having issues.



# Setup

> [!IMPORTANT]
> You will need to setup your own discord bot and twitch bot in order to use this. There are many tutorials online to set them up so please do this before you get started as it will not be explained here

### Requirements
There are a few things required to be able to use this bot. I will not be going over how to setup any of the items listed here so you will be expected to set all these inital items yourself if you want to use this code base.

+ Discord Bot
+ Twitch Bot
+ FFmpeg
  - Either install this under the "C:/ffmpeg/bin/ffmpeg.exe" File path or go to the play_audio function in the discordBot script (line 99) and adjust the path to where you installed it
- Eleven Labs API (Optional)


Assuming you have gone through the note above and have setup all the listed requirements we can get started.

## 1. Clone the Repo
   - Click the green button at the top of the repository and then click download zip and extract the folder somewhere on your pc
## 2. Setup API Keys
   - After downloading navigate towards the extracted folder and create a ".env" file, inside this file you will want to add in your personal API keys as following:

     
![image](https://github.com/user-attachments/assets/40b7ace6-5230-456e-a3fd-9a68dcee7537)


> [!NOTE]
> the "ACCESS_TOKEN" comes from your twitch bot.

## 3. Connect Channel
  - In the twitchBot.py script change the variable "CHANNEL_NAME" (line 10) To your own personal channels name.
  - Next go to the class setup (line 15) and change the "initial_channels" name to the channel you want messages to be read from.

> [!WARNING]
> If you do not change this the twitch bot you setup will not join your stream and instead will join the defaults stream and listen to that chatroom instead and will not work.

# Running
After this your bot should be all ready to go as long as your discord bot is connected to your discord server with the valid voice chat properties.

1. In your IDE of choice run the "main.py" script
```
python .\main.py
```

2. Connect your discord bot to the voice channel by running the "$join" command

> [!NOTE]
> You must be connected to the voice channel you wish the bot to join, and the bot must have permissions to join the channel you are connected to. Also if you recently shut off the bot or manually kicked it from the voice channel you will need to re-run the join command as if you restart the program or kick the bot it wont know that it is or isnt in a voice channel.
