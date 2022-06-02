from inbound_messages import *
from server_info import TimedChannel

def timed_messages():
    @client.event
    async def on_ready():
        print("Timed messages running")
        start_sending_messages.start()

    @tasks.loop(minutes=15)  # you can even use hours and minutes
    async def start_sending_messages():
        await client.get_channel(TimedChannel).send("I'm Timed Oh yeah!")
        print('working')
