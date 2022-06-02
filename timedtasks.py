from inbound_messages import *
from server_info import TimedChannel

def timed_messages():
    @client.event
    async def on_ready():
        print("Timed messages running")
        start_sending_messages.start()

    @tasks.loop(hours=1.00)
    async def start_sending_messages():
        await client.get_channel(TimedChannel).send("Check out our website! https://mhmatters.life\nYou can download"
                                                    " our apps on Apple and Google play just search MHmatters\n\nOur admins"
                                                    " here are:\n"
                                                    "WildeSte\n"
                                                    "Christos103\n"
                                                    "Emma:grin:")
        print('working')
