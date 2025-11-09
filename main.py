"""
    So the bot logs the reply from quote bot, but now I need to send the image that 
quote bot is generating.

    Im still not sure as to why grok will not repost the image that quotebot generates.
It might be because I don't have the exact file type that is created with make it a quote.
"""

from discordBot import *
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

"""
    When the program executes, this sends a message to the console that 
lets you know that it logged in correctly.
"""

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



    
client.run(botToken)