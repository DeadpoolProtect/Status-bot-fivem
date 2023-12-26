import discord
from discord.ext import commands
import json
import asyncio
import requests


client = commands.Bot(
  command_prefix='+',
  case_insensitive=False,
  description=None,
  intents=discord.Intents.all(),
  help_command=None
)


async def change_status():
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            # ici faut changer
            response = requests.get('http://51.68.44.72:30120/players.json')
            data = json.loads(response.text)
            player_count = len(data)
            
            activity = discord.Activity(type=discord.ActivityType.watching, name=f"{player_count} joueurs connectés | .gg/y9kepwYc")
            await client.change_presence(status=discord.Status.online, activity=activity)
        except:
            print("Erreur lors de la récupération du nombre de joueurs connectés.")
        
        await asyncio.sleep(60) 


@client.event
async def on_ready():
    print('[EVENT] Bot connecté !')
    client.loop.create_task(change_status())

# ici token du bot
client.run("")