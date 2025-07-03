from discordBot import botToken
import discord

TOKEN = botToken
makeID = 949479338275913799
testingID = 1387221514553921626 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

"""
    I believe that my forward image function goes here without using an event modifier.
But it might need to go in the on_message event because I am detecting a message for it.

Just kidding the attachement modifer is only able to be used in the on_message event.
"""

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

    specificChannel = 1387221514553921626

    #Keeps the bot from getting stuck in and infinite loop.
    if message.author == client.user:
        return
    
    """
        If the message content starts with "foward this", the bot will then foward the message
    to the bot testing channel.
    """
    #if message.content.startswith('forward this'):
    #    specificChannel = client.get_channel(1387221514553921626)
    
    """
        This is is an if statement that will send the message in the previous if statement
    to the specified channel. In this case this is the bot testing channel.
    """
    #if specificChannel:
    #    await specificChannel.send(message.content)

    """
        This is a command that will forward and image in the bot testing channel.
    """
    if message.attachments:
        for attachment in message.attachments:
            if attachment.content_type.startswith('image'):
                targetChannel = client.get_channel(1387221514553921626)
                await targetChannel.send(attachment.url)

client.run(TOKEN)