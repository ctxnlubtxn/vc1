import discord
import os
import requests  # Import the requests library
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

GUILD_ID = 274510773194063872
CHANNEL_ID = 1060555141310333060

# Define the Chrome user-agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
}

@client.event
async def on_ready():
    os.system('clear')
    print(f'Logged in as {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id=CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=False)
    print(f"Successfully joined {vc.name} ({vc.id})")

keep_alive()
client.run(os.environ['TOKEN'])
