from discordBot import botToken
import discord

TOKEN = botToken

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

"""
    This is an event that will reply hello when a user types hello.
"""
@client.event
async def on_message(message):

    """
        make it a quote id token = 949479338275913799
    """
    """
        If i remember correctly, this command keeps the bot from replying to itself.
    """
    if message.author == client.user:
        return
    
    """
        This is a set of commands that will forward a message to a specific channel.
    """
    if message.content.startswith('forward this'):
        #the parameters has the id for the bot testing channel.
        specificChannel = client.get_channel(1387221514553921626)
    
    """
        This is just a confirmation message that will send telling the user that there
    messages has been forwarded.
    """
    if specificChannel:
        await specificChannel.send(message.content)
        await message.channel.send("Message forwarded!")

@client.event
async def fowardMessage(image):
    """
        If statement that will ignore the bots input.
    """
    if image.author == client.user:
        return
    if image.author.id == 949479338275913799:
        """
            This is the channel ID for the quotes channel.
        """
        destinationId = client.get_channel(1309632891080413294)  

        """
            This should send the content to the destination channel.
        """
        await destinationId.send(f'{image.content}')  


client.run(TOKEN)