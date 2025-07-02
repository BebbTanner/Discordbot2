from discordBot import botToken
import discord

TOKEN = botToken
makeID = 949479338275913799
testingID = 1387221514553921626

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    """
        If i remember correctly, this command keeps the bot from replying to itself.
    """
    if message.author == client.user:
        return
    
    """
        This is a set of commands that will forward a message to a specific channel.
    """
    if message.content.startswith('forward this'):
        specificChannel = client.get_channel(testingID)
    
    """
        This is just a confirmation message that will send telling the user that there
    messages has been forwarded.
    """
    if specificChannel:
        await specificChannel.send(message.content)
        await message.channel.send("Message forwarded!")


client.run(TOKEN)