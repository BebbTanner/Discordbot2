from discordBot import *
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#Global variables
botTesting = 1387221514553921626

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    #Keeps the bot from getting stuck in and infinite loop.
    if message.author == client.user:
        return

    """
        If a message starts with hello, the bot will reply with hello.
    """
    if message.content.startswith("hello"):
        await message.channel.send("hello")


client.run(botToken)