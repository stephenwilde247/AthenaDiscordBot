from inbound_messages import *
from server_info import TimedChannel

file = open("txt_files/timed_txt.txt")
timed_messages_output = (file.read())
file.close()

def timed_messages():
    @client.event
    async def on_ready():
        print("Timed messages running")
        start_sending_messages.start()

    @tasks.loop(hours=1.00)
    async def start_sending_messages():
        await client.get_channel(TimedChannel).send(file=discord.File('images/logo.png'))
        await client.get_channel(TimedChannel).send(timed_messages_output)
        print('working')
