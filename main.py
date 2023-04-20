import discord
from discord.ext import commands, tasks
import requests
import json
import asyncio
import random

TOKEN = 'your discord bot token here'
channel_id = #the channel id here
wait_time = random.randrange(3600 , 3600*2)

intents = discord.Intents.default()
intents.members = True
intents.messages = True
direct_messages = True
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)
QURAN_API_URL = 'http://api.alquran.cloud/v1/ayah/'




async def send_quran_quote():
    while True:
        # Make request to Quran API
        response = requests.get(QURAN_API_URL + str(random.randrange(1, 6236)))
        data = json.loads(response.content)

        # Get the Quranic verse and send it to the specified channel
        verse = data['data']['text']
        chapter = data['data']['surah']['name']
        message = f'**{chapter}**\n`{verse}`'

        await asyncio.sleep(wait_time)

        channel = client.get_channel(channel_id)
        await channel.send(message)

@client.event
async def on_ready():
    print(f'{client.user.name} is connected to Discord!')
    await send_quran_quote()

@client.command()
async def id(ctx):
    await ctx.send(f'This channel id is : {ctx.channel.id}')


client.run(TOKEN)
