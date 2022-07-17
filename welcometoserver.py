import discord
intents = discord.Intents.default()
intents.members = True
intents.presences = True

from inbound_messages import *
from server_info import TimedChannel

client2 = discord.Client(intents=intents)

def welcome():
    @client2.event
    async def on_member_join(member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        await channel.send(f"{member} has arrived!")

def onJoin_hello():
    @client2.event
    async def on_member_update(before, after):
        if after.status.name == 'online':
            await client.get_channel(id=978854521281319015).send('Hello, Welcome back')
            print("When user join online")

def printclient():
    print(client2)