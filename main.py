'''
    So I know that it has been awhile, but I would like to get back to this. 
    I think I might finially have an understanding as to how this works.

    The user will tag quotebot the a reply to the message the the user wants an image generated of

    Quotebot will send and initial image that says, "Generating image"

    Once quotebot has generated the image it will then edit the original message with the quote image that it has created.

    So, this entire time I have been attempting to grab the intial message the bot has been sending rather than tryhing to grab the image off of the updated message.
    Atleast that is how I see it, so I think the first place to start would be to see if I can get Gorp to grab an edited message from me.
    
    Once I have done that I think the next thing would to be to get gorp to recogonize and image that is sent from me.

    Then I think that I can then combine those two features still testing it using something that I sent.

    Once I have done that I think that I should be able to just change the user ID from me to quotebot then hopefully fully push out the feature.
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