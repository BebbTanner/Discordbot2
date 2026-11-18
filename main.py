'''
    So it looks like with make it a quote I can just get the bot itself to target a specific channel.
    I am going to mess with those settings today, and if that works then I guess I can just use gorp for something else.

    So you can redirect quote messages with the quotebot.
    Which means I can now just do what I want with gorp.
'''

# Libraries

from discord.ext import commands
from tokens import *
from dataFile import *
from assets import *
import random
import discord
import io

# assets\lolbom.png

# Bot configuration

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
Gorp = discord.Client(intents=intents)
Gorp = commands.Bot(command_prefix="!", intents=intents)
random.seed()

@Gorp.event
async def on_ready():
    print('Gorp 1.0 is online.')

@Gorp.event
async def on_message(message):

    # Ignore bot respose
    if message.author == Gorp.user:
        return

    # True or False function
    if message.mentions and message.mentions[0].id == Gorp.user.id:
        if 'true' in message.content or 'TRUE' in message.content:
            randomint = random.randint(1,2)

            if randomint == 1:
                await message.channel.send(f"{message.author.mention} {random.choice(trueResponses)}")

            elif randomint == 2:
                await message.channel.send(f"{message.author.mention} {random.choice(falseResponses)}")
    
    # BDE function
    randomPercent = random.choice(range(101))

    if message.mentions and message.mentions[0].id == Gorp.user.id:
        if 'bde' in message.content or 'BDE' in message.content:
            await message.channel.send(f"{message.author.mention} has {randomPercent}% big dick energy.")

    # Get her got damned name right.
    if 'abby' in message.content or 'Abby' in message.content:
        await message.channel.send('*Abi')

    # She's not coming back.
    if 'more alcohol' in message.content:
        await message.channel.send("She's not coming back.")

# Run function, bot token required
Gorp.run(botToken)