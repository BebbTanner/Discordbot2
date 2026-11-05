'''
    So I think I now want to take the channel IDs, userIDs, and bot token and place it in a different file then make that file private
'''

# Libraries 

from discord.ext import commands
import random
import discord
import io

# Global varibles?

trueResponses = [
"CORRECT!",
"This is true.",
"All fax no printer.",
"Yeah it's true, Obamna said so."
]

falseResponses = [
"Kill yourself.",
"You could not be farther from the truth.",
"At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone is this room is now dumber for hearing it. I award you no points, and may God have mercy on your soul.",
"That is incorrect."
]


# Bot configuration

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)
random.seed()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    # Ignore bot respose

    if message.author == client.user:
        return

    # Resend image function

    if message.author.id == 205792085796716544:
        if message.attachments:
            for attachment in message.attachments:
                if attachment.content_type and "image" in attachment.content_type:
                    dest_channel = client.get_channel(1565036139310751795)
                    
                    # Fallback: If cache misses, try fetching over the API
                    if not dest_channel:
                        try:
                            dest_channel = await client.fetch_channel(1565036139310751795)
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

    # True or False function

    if message.mentions and message.mentions[0].id == client.user.id:
        if 'true' in message.content or 'TRUE' in message.content:
            randomint = random.randint(1,2)

            if randomint == 1:
                await message.channel.send(f"{message.author.mention} {random.choice(trueResponses)}")

            elif randomint == 2:
                await message.channel.send(f"{message.author.mention} {random.choice(falseResponses)}")
    

    # BDE function

    randomPercent = random.choice(range(101))

    if message.mentions and message.mentions[0].id == client.user.id:
        if 'bde' in message.content or 'BDE' in message.content:
            await message.channel.send(f"{message.author.mention} has {randomPercent}% bde.")

# Edit message resend function

@client.event
async def on_message_edit(before, after):

        target_channel = client.get_channel(1565036139310751795)

        if after.author.id == 205792085796716544:
            if before.content != after.content:
                await target_channel.send(f"{after.content}")

# Run function, bot token required

client.run()