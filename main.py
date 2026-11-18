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
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)
random.seed()

@client.event
async def on_ready():
    print('Gorp 1.0 is online.')

@client.event
async def on_message(message):

    '''
    # Resend image function
    if message.author.id == uncleFungusID:
        if message.attachments:
            for attachment in message.attachments:
                if attachment.content_type and "image" in attachment.content_type:
                    dest_channel = client.get_channel(quotesChannelID)
                    
                    # Fallback: If cache misses, try fetching over the API
                    if not dest_channel:
                        try:
                            dest_channel = await client.fetch_channel(quotesChannelID)
                        except discord.HTTPException:
                            print("Could not find the destination channel.")
                            continue

                    try:
                        # Safer method: Read bytes directly to create the file object
                        file_bytes = await attachment.read()
                        file_to_send = discord.File(
                            fp=io.BytesIO(file_bytes), 
                            filename=attachment.filename
                        )
                        
                        # Content is explicitly provided to prevent the 50006 error
                        await dest_channel.send(
                            file=file_to_send
                        )
                    except Exception as e:
                        print(f"Failed to forward image: {e}")

    await client.process_commands(message)
    '''


'''
This function is not finished, I am tryihng to combine this with the resend image function.

# Edit message resend function

@client.event
async def on_message_edit(before, after):

        target_channel = client.get_channel(quotesChannelID)

        # Eventually this ID will need to be changed to the quotebot ID.

        if after.author.id == uncleFungusID:
            if before.content != after.content:
                await target_channel.send(f"{after.content}")
'''

# Run function, bot token required

client.run(botToken)
