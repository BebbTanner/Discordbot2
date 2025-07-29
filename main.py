from discordBot import *
import discord

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
    
    #This is getting the channelID and storing it to the new channel variable.
    newChannel = client.get_channel(1387221514553921626)

    #This is a loop that should be responding only to me in discord.
    if message.author.id == tannerID and newChannel == 1387221514553921626:
        targetChannel = client.get_channel(1309632891080413294)
        
        if targetChannel:
            await targetChannel.send("Fuck you")



client.run(botToken)