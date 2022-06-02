from inbound_messages import *

def timed_messages():
    @client.event
    async def on_ready():
        print("Timed messages running")
        start_sending_messages.start()

    @tasks.loop(minutes=15)  # you can even use hours and minutes
    async def start_sending_messages():
        await client.get_channel(978854521281319015).send("I'm Timed Oh yeah!")
        print('working')
