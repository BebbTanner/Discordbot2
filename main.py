'''
I want to get back to the quote bot fowarding feature.
Aaron brought up that the message is edited to send the image.
So I think that there is a feature that deletes and edited message
    then resends the edited message in another channel. This could 
    be the piece of information that I was missing all this time.
    Aaron was really helpful with pointing that out. So now maybe 
    I can start moving in the right direction.
'''

from discordBot import *
from discord.ext import commands
import discord
import random
import logging

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

random.seed()

trueResponses = [
    "CORRECT!",
    "This is true.",
    "All fax no printer.",
    "Yeah it's true, Obamna said so."
]

falseResponses = [
    "Kill yourself.",
    "You could not be farther from the truth.",
    "At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone is this room is now dumber for hearing it. I award you no points, and may God have mercy on your soul.",
    "That is incorrect."
]

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
        if 'rue' in message.content:
            randomint = random.randint(1,2)

            if randomint == 1:
                await message.channel.send(random.choice(trueResponses))

            elif randomint == 2:
                await message.channel.send(random.choice(falseResponses))
    
    '''
    This is an if statement that will look for the word steve in a message.
    If it contains this keyword it will put in general kill steve.
    '''
    if 'steve' in message.content:
        await message.channel.send("Kill steve")

    
    '''Detecting an image'''
    #if message.author.id == 205792085796716544:
    #    if message.attachments:
    #        for attachement in message.attachments:
    #            if attachement.content_type and attachement.content_type.startswith('image/'):
    #                await message.channel.send("Attachment received!")

    '''Sending a message to a specific channel'''

    '''Deleting and edited message and resending it to another channel'''

client.run(botToken)