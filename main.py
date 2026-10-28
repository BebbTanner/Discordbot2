'''
    So I know that it has been awhile, but I would like to get back to this. 
    I think I might finially have an understanding as to how this works.

    The user will tag quotebot the a reply to the message the the user wants an image generated of

    Quotebot will send and initial image that says, "Generating image"

    Once quotebot has generated the image it will then edit the original message with the quote image that it has created.

    So, this entire time I have been attempting to grab the intial message the bot has been sending rather than tryhing to grab the image off of the updated message.
    Atleast that is how I see it, so I think the first place to start would be to see if I can get Gorp to grab an edited message from me.
    
    Once I have done that I think the next thing would to be to get gorp to recogonize and image that is sent from me.

    Then I think that I can then combine those two features still testing it using something that I sent.

    Once I have done that I think that I should be able to just change the user ID from me to quotebot then hopefully fully push out the feature.
'''

from discord.ext import commands
import random
import discord

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

client = commands.Bot(command_prefix="!", intents=intents)

random.seed()

'''
    These are the responses for the true or false commands.
    For now I will be commenting out this command in the main function because I will not be working on it.
'''
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



'''
    This will print message to the console letting me know that gorp has logged in.
'''
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



'''
    This is the main function that will execute all of the message commands.
    This will be were the quotebot command will be built.
'''
@client.event
async def on_message(message):

    '''
        This will check to see if the message came from the bot.
        If it came from the bot it will ignore that message.
        This is to prevent the bot from getting stuck in an infinite loop.
    '''
    if message.author == client.user:
        return




    '''
        If some one mentions the bot and asks if something is true or false, this command will trigger.
        It will take a random message for the true or false resposes and send it back in the channel it was tagged it.
        Eventually, I would like to make it to where it tags the user that asked the initiaal question.

        I am going to comment this out for now because it is not the main feature that I want to be working on.
    '''
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
        So this nested if-else statement should be checking to see if a specific user has sent and image attachement.
        Once it has detected that from that user it should send a message that says "attachement received".
        Currently, it is not working and I have no idae as to why.

        I am going to comment this out.
        I think that it can still be useful, but I don't really know.
    '''
    '''
    if message.author.id == 205792085796716544:
        if message.attachments:
            for attachement in message.attachments:
                if attachement.content_type and attachement.content_type.startswith('image/'):
                    await message.channel.send("Attachment received!")
    '''


    '''
        This is going to check to see if the message was sent from me.
        Once it confirms that it was sent from me it will take the content of that message and send it back to the user.
    '''
    if message.author.id == 205792085796716544:
        await message.channel.send(message.content)

    # Required to let the bot process standard commands alongside on_message
    await client.process_commands(message)



'''
    In theory this should be listening to see if the message that I originally sent was edited.
    If it was edited the bot should resend the new updated message to the same channel that it was edited in.
'''
@client.event
async def on_message_edit(before, after):

        # Check if the message was edited by the specific user
        if after.author.id == 205792085796716544:
            # Check if the content actually changed (ignoring embed/pin changes)
            if before.content != after.content:
                # Send the new content to the same channel where it was edited
                await after.channel.send(
                    f"**{after.author.name}** just edited their message to:\n{after.content}"
                )

                # ALTERNATIVE: Send to a specific channel instead
                # target_channel = bot.get_channel(YOUR_CHANNEL_ID_HERE)
                # await target_channel.send(f"New text: {after.content}")



'''
    This is my bot token needed to make calls to the discord API
    I will eventually have to move this to a different file so that it is not accessbile to the public.

    test
'''
client.run()
