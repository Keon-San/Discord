# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord

TOKEN = 'NDM4ODg2NDgzNDA4MTkxNTAw.DcLIfw.0zekzollKnAwZIO6YZnfqLEp9sI'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.name == "Our Supreme Overlord" and message.author.discriminator == "0357":
        tmp = "Our Holy Lord Guy Says: \n" + message.content
        msg = tmp.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
