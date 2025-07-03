from discordBot import botToken
import discord

TOKEN = botToken
makeID = 949479338275913799
testingID = 1387221514553921626 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

    #Keeps the bot from getting stuck in and infinite loop.
    if message.author == client.user:
        return
    
    """
        If the message content starts with "foward this", the bot will then foward the message
    to the bot testing channel.
    """
    if message.content.startswith('forward this'):
        specificChannel = client.get_channel(1387221514553921626)
        await specificChannel.send(message.content)
    
    
    """
        This is a command that will forward and image in the bot testing channel.
    """
    if message.attachments:
        for attachment in message.attachments:
            if attachment.content_type.startswith('image'):
                targetChannel = client.get_channel(1387221514553921626)
                await targetChannel.send(attachment.url)

client.run(TOKEN)