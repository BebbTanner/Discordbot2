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

@client.event
async def on_message(message):

    '''
    This ignores any message that is sent by the bot.
    '''
    if message.author == client.user:
        return

    targetUserId = 185152706208464896

    if message.author.id == targetUserId:
        await message.channel.send("You are smelly")

    '''
    This will reply to anyone that mentions the discordbot.
    '''
    if message.mentions and message.mentions[0].id == client.user.id:
        await message.channel.send ("You called?")

    '''
    This is an if statement that will look for the word steve in a message.
    If it contains this keyword it will put in general kill steve.
    '''
    if 'steve' in message.content:
        await message.channel.send("Kill steve")

    if 'feet' in message.content:
        await message.channel.send("Kill steve")

client.run(botToken)