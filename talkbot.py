import discord
import random
from randomReplies import *
from swearlist import *
from intro import *
from server_info import *
from startup_config import *

intro()
token_config()

client = discord.Client()

print(f'****************** connected ********************\n{client}')
print('Listening for commands...')

channelNames = [
    'welcome',  # used as context channelNames[1] on line 27 :-)
    '💬︱lobby'  # This will be channelNames[2] when you expend and so on add them as you like
    # When adding channels a lot of people forget about the "," comma sign please don't do this or it breaks
]

@client.event
async def on_message(inbound):
    username_allcase = str(inbound.author).split('#')[0]
    username = str(inbound.author).split('#')[0]
    user_inbound_message = inbound.content
    channel = str(inbound.channel.name)

    print(f'{username}: {user_inbound_message}: ({channel})')

    if inbound.channel.name == channelNames[0]:  # This is just for lobby as its 1
        if user_inbound_message.lower() == 'cheese':
            print("This was just for the lobby only")

        elif user_inbound_message.lower() == 'pizza':
            print("This was just for the lobby only")

        #elif user_inbound_message.lower() == '!lotto':
         #   numbers = f'My guess to the UK lotto numbers this week are:\n{random.randrange(1, 59)} : : {random.randrange(1, 59)} : : {random.randrange(1, 59)} :: {random.randrange(1, 59)} :: {random.randrange(1, 59)} :: Bonus ball: {random.randrange(1, 59)}  \nIf you win please donate to us a little ;-)'
          #  await inbound.channel.send(numbers)
           # print(f'Lotto used by {username} in channel: {channel}')
            #return

        # This is the random function code

        elif user_inbound_message.lower() == '!ping':
            await inbound.channel.send('Pong')
            print(f'Lotto used by {username} in channel: {channel}')
            return

#all channels
    if inbound.content.find("ye ") >= 0:
        await inbound.channel.send(f"Ok, {username} ⬅ This person wants you to know its 'You're'\n"
                                   f"In a sentence 'your' is in the context of your dog pooed on the floor.\n"
                                   f"Whilst 'You're' context is: You're awesome.")
        print(f'Your educate used by {username} in channel: {channel}')
        return

    elif user_inbound_message.lower() == '!uksuicide':  # When someone types !fight
        ukSuicideReply = f'{username} Get help now!, we are all here to listen but if its past our help ' \
                         f'please please please go here: https://mhmatters.life/viewtopic.php?t=7'
        await inbound.channel.send(ukSuicideReply)  # Replies with the string fightReplies
        print(f'!Friend Command used by {username} sent to {channel}')
        return  # ends this section

    elif user_inbound_message.lower() == '!hug':
        await inbound.channel.send(f'I Hug @{username_allcase} everything is going to be ok :)')
        print(f'Lotto used by {username} in channel: {channel}')
        return

    elif user_inbound_message.lower() == '!channel':  # When someone types !fight
        chan1 = channel.upper()
        nick2 = username.upper()
        await inbound.channel.send(f" Seriously dude please stop using my CPU for pointless stuff open your eyes "
                                   f"and see you are in: \n{chan1}.\nDo you even want me to tell you who you are??? "
                                   f" tuff ima do it anyway... its *drumroll*...... \n{nick2}")  # Replies with the string fightReplies
        print(f'!Fight Command used by {username} sent to {channel}')
        return  # ends this section

    elif user_inbound_message.lower() == 'hello':  # somone says hello in chat
        await inbound.channel.send(
            f"Hello how are you {username}")  # replies back with Hello how are you in  a formatted string with username
        return  # Ends this statement

    elif user_inbound_message.lower() == 'bye':
        await inbound.channel.send(f"See you soon! {username}")
        print(f'Said bye to {username} in channel: {channel}')
        return

    elif user_inbound_message.lower() == '!friends':  # When someone types !fight
        friendReplies = f'Right {username} Our main friends are: Energize join thier discord too' \
                        f' - https://discord.gg/5GZnbvgk2K'  # makes fightReplies a random Choice from "fight" wordlist
        await inbound.channel.send(friendReplies)  # Replies with the string fightReplies
        print(f'!Friend Command used by {username} sent to {channel}')
        return  # ends this section

    elif user_inbound_message.lower() == '!fight':  # When someone types !fight
        fightReplies = random.choice(fight)  # makes fightReplies a random Choice from "fight" wordlist
        await inbound.channel.send(fightReplies)  # Replies with the string fightReplies
        print(f'!Fight Command used by {username} sent to {channel}')
        return  # ends this section

    elif user_inbound_message.lower() == '!website':  # When someone types !fight
        websiteReplies = random.choice(website)  # makes fightReplies a random Choice from "fight" wordlist
        await inbound.channel.send(websiteReplies)  # Replies with the string fightReplies
        print(f'!Fight Command used by {username} sent to {channel}')
        return  # ends this section

    elif any(word in user_inbound_message.lower() for word in curses):
        await inbound.channel.send(f"Oi {username}: We have detected that you used a banned word in our channel, please refrain from doing that")
        print("Working")
        return
    
client.run(TOKEN)


