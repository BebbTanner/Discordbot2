from discordBot import *
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

"""
    When the program executes, this sends a message to the console that 
lets you know that it logged in correctly.
"""
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    #Keeps the bot from getting stuck in and infinite loop.
    if message.author == client.user:
        return

client.run(botToken)