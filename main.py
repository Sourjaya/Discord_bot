import discord
import os
client=discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if msg.content.startswith('$hello'):
        await msg.channel.send('Hello!')
TOKEN=os.getenv('TOKEN')
client.run(TOKEN)
