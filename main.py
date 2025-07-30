from discordBot import *
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

"""
tannerID = 205792085796716544

botTesting = 1387221514553921626
"""

"""
    When the program executes, this sends a message to the console that 
lets you know that it logged in correctly.
"""
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    tannerID = 205792085796716544

    #Keeps the bot from getting stuck in and infinite loop.
    if message.author == client.user:
        return
    
    #This should reply to me and @ my discord account
    if message.author.id == tannerID:#user id to foward this will be mine
        destination_channel = client.get_channel(1387221514553921626)#destination channel
        await destination_channel.send(f"{message.author.name}: {message.content}")
    
    await client.process_commands(message)

client.run(botToken)