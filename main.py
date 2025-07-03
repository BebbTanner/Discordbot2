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

    """
        Variables that are being used in this local scope.
    """


    #Keeps the bot from getting stuck in and infinite loop.
    if message.author == client.user:
        return
    
    """
        If the message content starts with "foward this", the bot will then foward the message
    to the bot testing channel and also send th
    """
    if message.content.startswith('forward this'):
        specificChannel = client.get_channel(1387221514553921626)
    
    """
        This is just a confirmation message that will send telling the user that there
    messages has been forwarded.
    """
    if specificChannel:
        await specificChannel.send(message.content)


client.run(TOKEN)