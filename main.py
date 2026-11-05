'''
    Current working features:
    Can forward an edited message from bot testing channel to quotes channel.
    Can forward an image from bot testing channel to quotes channel.
'''

from discord.ext import commands
import random
import discord
import io

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

client = discord.Client(intents=intents)

client = commands.Bot(command_prefix="!", intents=intents)

random.seed()

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

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

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


    '''
        I think that I need to disect this snipet.
        If I can rmember how this works I should be able to use it to figure out my BDE function.
        This is the function that was used it toddbot that I think would be really fun to have.
    '''

    if message.mentions and message.mentions[0].id == client.user.id:
        if 'rue' in message.content:
            randomint = random.randint(1,2)

            if randomint == 1:
                await message.channel.send(random.choice(trueResponses))

            elif randomint == 2:
                await message.channel.send(random.choice(falseResponses))

    '''
        Ok so this is set up to check and see if the user mentioned the bot and if the message contains a specific string.
        If it meets both of the parameters it will reply back to the use "bde confirmed"

        I am sure that there is a more efficent way to do this but I am unaware as to how to.
        So these two functions are set up to just confirm my test.

        Now I want set it up to generate a number from 0 to 100 and then output that to the channel.
    '''

    randomPercent = random.choice(range(101))

    if message.mentions and message.mentions[0].id == client.user.id:
        if 'bde' in message.content:
            await message.channel.send(f"{message.author.mention} has {randomPercent}% bde.")

    if message.mentions and message.mentions[0].id == client.user.id:
        if 'BDE' in message.content:
            await message.channel.send(f"{message.author.mention} has {randomPercent}% bde.")



'''
    This is to take an edited message from a specific user then send that edited message to a new text channel-
'''
@client.event
async def on_message_edit(before, after):

        target_channel = client.get_channel(1565036139310751795)

        if after.author.id == 205792085796716544:
            if before.content != after.content:
                await target_channel.send(f"{after.content}")

client.run()