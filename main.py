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
        This gets the message id for a message sent from a specific user, then
    sends Fuck you in a specific channel. This is going to be used to forward 
    messages to a specific channel.
    """
    if message.author.id == 949479338275913799:
        specificChannel = client.get_channel(1387221514553921626)
        await specificChannel.send("This is from user MakeItAQuote.")


client.run(TOKEN)