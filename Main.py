import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
client = discord.Client(intents=intents)



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("hello!")

keep_alive()
client.run(os.getenv('TOKEN', 'your_default_token_value_here'))
