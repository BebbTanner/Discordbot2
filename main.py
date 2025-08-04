"""
    So the bot logs the reply from quote bot, but now I need to send the image that 
quote bot is generating.
"""

from discordBot import *
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

"""
tannerID = 205792085796716544
makeItAQuote = 949479338275913799

botTesting = 1387221514553921626
"""

"""
    When the program executes, this sends a message to the console that 
lets you know that it logged in correctly.
"""
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    tannerID = 205792085796716544
    makeItAQuote = 949479338275913799

    #Keeps the bot from getting stuck in and infinite loop.
    if message.author == client.user:
        return
    
    #Any time I type anything in any channel, This post my tag with my message 
    #in the bot testing channel.
    if message.author.id == makeItAQuote:#user id to foward this will be mine
        destination_channel = client.get_channel(1387221514553921626)#destination channel
        await destination_channel.send(f"{message.author.name}: {message.content}")
    
    await client.process_commands(message)

client.run(botToken)