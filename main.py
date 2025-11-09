from discordBot import *
from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

random.seed()

trueResponses = [
    "CORRECT!",
    "This is true.",
    "All fax no printer."
]

falseResponses = [
    "Kill yourself.",
    "You could not be farther from the truth.",
    "At no point in your rambling, incoherent response were ryou even close to anything that could be considered a rational thought. Everyone is this room is now dumber for hearing it. I award you no points, and may God have mercy on your soul.",
]

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

    '''
    This will reply to anyone that mentions the discordbot.
    '''
    if message.mentions and message.mentions[0].id == client.user.id:
        if 'true' in message.content:
            await message.channel.send(random.choice(trueResponses))
        
        if 'True' in message.content:
            await message.channel.send(random.choice(trueResponses))

        if 'false' in message.content:
            await message.channel.send(random.choice(falseResponses))

        if 'False' in message.content:
            await message.channel.send(random.choice(falseResponses))

    '''
    This is an if statement that will look for the word steve in a message.
    If it contains this keyword it will put in general kill steve.
    '''
    if 'steve' in message.content:
        await message.channel.send("Kill steve")

    if 'feet' in message.content:
        await message.channel.send("Kill steve")

client.run(botToken)