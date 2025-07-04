from discordBot import *
import discord

TOKEN = botToken

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
        await specificChannel.send("Fuck you")
    

    """
        This is a command that will forward and image in the bot testing channel.
    """
    if message.attachments:
        for attachment in message.attachments:
            if attachment.content_type.startswith('image'):
                targetChannel = client.get_channel(1387221514553921626)
                await targetChannel.send(attachment.url)

    """
        This is for the on get_message_from_user
    """
    if message.author.id == 949479338275913799:
        message_id = message.id
        print(f"Message ID from user: {message_id}")


"""
    This is a function that should get the message id of the previous message sent in chat. 
This will be needed in order to foward a reply to a specific channel.
"""
@client.event
async def get_message_from_user(ctx, user: discord.member):
    channel = 1387221514553921626
    messages = await channel.history(limit=100).flatten()

    #This is my user ID for my discord profile, this will be changed later.
    user_messages = [msg for msg in messages if msg.author == 949479338275913799]

    for msg in user_messages:
        print(f"Message ID: {msg.id}")

client.run(TOKEN)