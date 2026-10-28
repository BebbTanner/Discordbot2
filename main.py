'''
    Current working features:
    Can forward an edited message from bot testing channel to quotes channel.
    Can forward an image from bot testing channel to quotes channel.

    So now that I have this image forwaring thingy working, I think the next thing to do is to nest this in the message edit event.
    I think the best current plan of action is to study this porition of the code because I just ripped it off of Gemini.
    Forgive for I have sinned and I stolen code, but unlike the others I must study this in order to properly manulipate it for my own desires.

    So now I need to very carefully find a way to combine those two features so that I can finally get the end result that I want.

    This is a funny tool that will help me later.
    content=f"📷 Image forwarded from {message.author.mention}",
'''



from discord.ext import commands
import random
import discord
import io



intents = discord.Intents.default()
intents.message_content = True
intents.messages = True



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
    if message.mentions and message.mentions[0].id == client.user.id:
        if 'rue' in message.content:
            randomint = random.randint(1,2)

            if randomint == 1:
                await message.channel.send(random.choice(trueResponses))

            elif randomint == 2:
                await message.channel.send(random.choice(falseResponses))
    '''

    '''
    if message.author.id == 205792085796716544:
        await message.channel.send(message.content)

    await client.process_commands(message)
    '''



@client.event
async def on_message_edit(before, after):

        target_channel = client.get_channel(1565036139310751795)

        if after.author.id == 205792085796716544:
            if before.content != after.content:
                await target_channel.send(f"{after.content}")

client.run()