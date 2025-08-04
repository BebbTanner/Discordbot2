"""
    So the bot logs the reply from quote bot, but now I need to send the image that 
quote bot is generating.

    Im still not sure as to why grok will not repost the image that quotebot generates.
It might be because I don't have the exact file type that is created with make it a quote.
"""

from discordBot import *
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

"""
tannerID = 205792085796716544
makeItAQuote = 949479338275913799

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
    makeItAQuote = 949479338275913799

    #Keeps the bot from getting stuck in and infinite loop.
    if message.author == client.user:
        return
    
    #Any time I type anything in any channel, This post my tag with my message 
    #in the bot testing channel.
    if message.author.id == makeItAQuote:
        destination_channel = client.get_channel(1387221514553921626)#destination channel
        await destination_channel.send("Image from quotebot is generating.")
  

    
    # Check if the message has attachments (potential images)
    if message.attachments:
        for attachment in message.attachments:
            # Check if the attachment is an image (you might want more robust checks)
            if attachment.content_type and 'PNG' in attachment.content_type:
                target_channel = client.get_channel(1387221514553921626)
                if target_channel:
                    # Convert the attachment to a discord.File and send it
                    await target_channel.send(f"Image from {message.author.display_name}:", file=await attachment.to_file())
                else:
                    print(f"Target channel with ID {1387221514553921626} not found.")
    
    await client.process_commands(message) # Important for command handling

client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return



    
client.run(botToken)