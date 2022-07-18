import discord
import random
from randomReplies import *
from swearlist import *
from server_info import *
from startup_config import *
from discord.ext import commands, tasks
from emoji_wl import *
from discord.ext import tasks

client = discord.Client()
bot = commands.Bot('!') # ! = PREFIX

def inboundandReplies():
    print(f'****************** connected ********************\n{client}')
    print('Listening for commands...')
    @client.event
    async def on_message(inbound):
        username_allcase = str(inbound.author).split('#')[0]
        username = str(inbound.author).split('#')[0]
        user_inbound_message = inbound.content
        channel = str(inbound.channel.name)
        print(f'{username}: {user_inbound_message}: ({channel})')

        # Just in a channel you specify from a list in server_info.py
        if inbound.channel.name == channelNames[0]:  # This is just for lobby as its 1
            if user_inbound_message.lower() == 'cheese':
                print("This was just for the lobby only")

            elif user_inbound_message.lower() == 'pizza':
                print("This was just for the lobby only")

            elif user_inbound_message.lower() == '!ping':
                await inbound.channel.send(f'Pong @{username_allcase}')

        # all channels
        if inbound.content.find("ye ") >= 0:
            await inbound.channel.send(f"Ok, {username} ⬅ This person wants you to know its 'You're'\n"
                                       f"In a sentence 'your' is in the context of your dog pooed on the floor.\n"
                                       f"Whilst 'You're' context is: You're awesome.")
            print(f'Your educate used by {username} in channel: {channel}')
            return

        elif inbound.content.startswith("!calc "):
            names = inbound.content.split("!calc ", 1)[1]
            data = names.split("*")
            a = data[0]
            b = data[1]
            c = int(a) * int(b)
            r = str(c)
            em = discord.Embed(title=f"Calculator", description=f"Input\n```{a}*{b}```\n\nOutput\n```{r}```")
            await inbound.channel.send(embed=em)
            print("Calc Used")
            return

        elif user_inbound_message.lower() == '!hug':
            embed = discord.Embed(title=f"🤗I hug @{username}🤗", description=" Hopefully this makes you feel better!")  # ,color=Hex code
            await inbound.channel.send(embed=embed)
            print(f'Lotto used by {username} in channel: {channel}')
            return

        elif user_inbound_message.lower() == '!spotify':
            await inbound.channel.send(f'@{username_allcase} you can find our "clear your head" '
                                       f'Spotify playlist here: '
                                       f'https://open.spotify.com/playlist/5eZYtnuTU6wmZocuBtpdJE?si=07a64a0574204d12')
            print(f'Spotify used by {username} in channel: {channel}')
            return

        elif user_inbound_message.lower() == '!channel':  # When someone types !fight
            chan1 = channel.upper()
            nick2 = username.upper()
            await inbound.channel.send(f" Seriously dude please stop using my CPU for pointless stuff open your eyes "
                                       f"and see you are in: \n{chan1}.\nDo you even want me to tell you who you are??? "
                                       f" tuff ima do it anyway... its *drumroll*...... \n{nick2}")  # Replies with the string fightReplies
            print(f'!Fight Command used by {username} sent to {channel}')
            return  # ends this section

        elif user_inbound_message.lower() == 'hello':  # someone says hello in chat
            await inbound.channel.send(
                f"Hello how are you {username}")  # replies back with Hello how are you in  a formatted string with username
            return  # Ends this statement

        elif user_inbound_message.lower() == 'bye':
            await inbound.channel.send(f"See you soon! {username}")
            print(f'Said bye to {username} in channel: {channel}')
            return

        elif user_inbound_message.lower() == '!friends':
            friendReplies = f'Right {username} Our main friends are: Energize join thier discord too' \
                            f' - https://discord.gg/5GZnbvgk2K'
            await inbound.channel.send(friendReplies)
            print(f'!Friend Command used by {username} sent to {channel}')
            return

        elif user_inbound_message.lower() == '!fight':
            fightReplies = random.choice(fight)
            await inbound.channel.send(fightReplies)
            print(f'!Fight Command used by {username} sent to {channel}')
            return

        elif user_inbound_message.lower() == '!website':
            websiteReplies = random.choice(website)
            await inbound.channel.send(websiteReplies)
            print(f'!Website Command used by {username} sent to {channel}')
            return

        elif any(word in user_inbound_message.lower() for word in curses):
            #await inbound.channel.purge(limit=1)
            await inbound.channel.send(
                f"Oi {username}: We have detected that you used a banned word in our channel,\n"
                f"if I am wrong please just ignore this message and be happy I no longer delete the messages :rofl:")
            print("Working")
            return

        elif user_inbound_message.lower() == '!help-athena':  # When someone types !help
            await inbound.channel.send(helptxt)  # Help txt file
            return  # ends this section

#########################Suicide Commands########################
        elif user_inbound_message.lower() == '!uksuicide':
            await inbound.channel.send(f"@{username} Get help now!, we are all here to listen but if its past our help please see below: \n"
                                            f"Emergancy: 999 and 112\n"
                                            f"NHS mental health line: 111 then option 2\n"
                                            f"Shout – Text SHOUT to 85258\n"
                                            f"Samaritans: 116 123\n"
                                            f"More info here: https://mhmatters.life/viewtopic.php?t=7")
            print(f'!uksuicide Command used by {username} sent to {channel}')
            return  # ends this section

        elif user_inbound_message.lower() == '!usasuicide':
            await inbound.channel.send(f"@{username} Get help now!, we are all here to listen but if its past our help please see below: \n"
                                            f"Emergancy:  911\n"
                                            f"The national suicide prevention line: 1-800-273-8255\n"
                                            f"Veterens Crisis Line: 1-800-273-8255\n"
                                            f"Crisis Text Line: Text HOME to 741-741\n"
                                            f"More info here: https://mhmatters.life/viewtopic.php?t=8")
            print(f'!usasuicide Command used by {username} sent to {channel}')
            return  # ends this section

        elif user_inbound_message.lower() == '!canadasuicide':
            await inbound.channel.send(f"@{username} Get help now!, we are all here to listen but if its past our help please see below: \n"
                                            f"Emergancy:  911\n"
                                            f"Canada Suicide Prevention Service: 1-833-456-4566 or Text 45645\n"
                                            f"(Text only avaliable from 4pm until Midnight)\n\n"
                                            f"Trans Life Line: 1-877-330-6366\n"
                                            f"More info here: https://mhmatters.life/viewtopic.php?t=9")
            print(f'!canadasuicide Command used by {username} sent to {channel}')
            return  # ends this section

        elif user_inbound_message.lower() == '!aussuicide':
            await inbound.channel.send(f"@{username} Get help now!, we are all here to listen but if its past our help please see below: \n"
                                            f"Emergency:  000\n"
                                            f"Lifeline: 13 11 14\n"
                                            f"Suicide call back service: 1300 659 467\n"
                                            f"Talk Suicide: 1800 008 255\n"
                                            f"More info here: https://mhmatters.life/viewtopic.php?t=10")
            print(f'!canadasuicide Command used by {username} sent to {channel}')
            return  # ends this section

        elif user_inbound_message.lower() == '!nzsuicide':
            await inbound.channel.send(f"@{username} Get help now!, we are all here to listen but if its past our help please see below; \n"
                                            f"Emergancy:  111\n"
                                            f"(T1737: Call or Text 1737\n"
                                            f"The LockDown: Text 5626\n"
                                            f"More info here: https://mhmatters.life/viewtopic.php?t=11")
            print(f'!canadasuicide Command used by {username} sent to {channel}')
            return  # ends this section

        elif user_inbound_message.lower() == '!suicide':  # When someone types !fight
            await inbound.channel.send(f"@{username} Get help now!, we are all here to listen but if its past our help please see below: \n"
                                            f"https://mhmatters.life/viewforum.php?f=9")
            print(f'!suicide Command used by {username} sent to {channel}')
            return  # ends this section

##########################ADMIN COMMANDS##########################
        if user_inbound_message.lower() == '!defcon1':
            if inbound.author.guild_permissions.administrator:
                print(f"Username: {username} has purged the chat")
                await inbound.channel.purge(limit=100000000000)
                print(f"Username: {username} has purged the chat")
                await inbound.channel.send(f"{username}: Purged the chat! Now it's nice and clean {Discord_Emojis[0]}")
                return
            else:
                print('Not an admin')
                await inbound.channel.send(f"{username} You are not an admin")
                return

        elif user_inbound_message.lower() == '!defcon1+clean':
            if inbound.author.guild_permissions.administrator:
                await inbound.channel.purge(limit=100000000000)
                print(f"Username: {username} has purged the chat clean")
                return

            else:
                print('Not an admin')
                await inbound.channel.send(f"{username} You are not an admin")
                return

####bot-amnesia####
        watch = 998258908600737793
        if inbound.channel.name == channelNames[2]:
            if user_inbound_message.lower() == 'helpme':

                await client.get_channel(watch).send(f'{username} has used the helpme suicide commands\n'
                                                     f'We are awaiting to see what country the user is from\n'
                                                     f'Please ensure we watch this user as much as we can.')
                print("This was just for the bot forgeting only")
                await inbound.channel.purge(limit=1)
                await inbound.channel.send(f"Where are you from, UK, USA, CANADA, AUS, NZ or Other?")
                return

            if user_inbound_message.lower() == 'uk':
                await inbound.channel.purge(limit=2)
                await client.get_channel(watch).send(f'{username} has told me their location is UK 🇬🇧')
                await inbound.channel.send(
                    f"We are all here to listen but if its past our help please see below: \n"
                    f"Emergancy: 999 and 112\n"
                    f"NHS mental health line: 111 then option 2\n"
                    f"Shout – Text SHOUT to 85258\n"
                    f"Samaritans: 116 123\n"
                    f"More info here: https://mhmatters.life/viewtopic.php?t=7\n\n"
                    f"Type 'done' without the quotes to forget this ever happened")
                print(f'!uksuicide Command used by {username} sent to {channel}')
                return

            if user_inbound_message.lower() == 'usa':
                await client.get_channel(watch).send(f'{username} has told me their location is USA 🇺🇸')
                await inbound.channel.purge(limit=2)
                await inbound.channel.send(f"Get help now!, we are all here to listen but if its past our help please see below: \n"
                                            f"Emergancy:  911\n"
                                            f"The national suicide prevention line: 1-800-273-8255\n"
                                            f"Veterens Crisis Line: 1-800-273-8255\n"
                                            f"Crisis Text Line: Text HOME to 741-741\n"
                                            f"More info here: https://mhmatters.life/viewtopic.php?t=8"
                                            f"Type 'done' without the quotes to forget this ever happened")
                print(f'!uksuicide Command used by {username} sent to {channel}')
                return

            if user_inbound_message.lower() == 'canada':
                await client.get_channel(watch).send(f'{username} has told me their location is CANADA 🇨🇦')
                await inbound.channel.purge(limit=2)
                await inbound.channel.send(
                    f"Get help now!, we are all here to listen but if its past our help please see below: \n"
                                        f"Emergancy:  911\n"
                                        f"Canada Suicide Prevention Service: 1-833-456-4566 or Text 45645\n"
                                        f"(Text only avaliable from 4pm until Midnight)\n\n"
                                        f"Trans Life Line: 1-877-330-6366\n\n"
                                        f"More info here: https://mhmatters.life/viewtopic.php?t=9\n\n"
                    f"Type 'done' without the quotes to forget this ever happened")
                print(f'!uksuicide Command used by {username} sent to {channel}')
                return

            if user_inbound_message.lower() == 'aus':
                await client.get_channel(watch).send(f'{username} has told me their location is AUSTRALIA 🇦🇺')
                await inbound.channel.purge(limit=2)
                await inbound.channel.send(
                    f"Get help now!, we are all here to listen but if its past our help please see below: \n"
                                            f"Emergency:  000\n"
                                            f"Lifeline: 13 11 14\n"
                                            f"Suicide call back service: 1300 659 467\n"
                                            f"Talk Suicide: 1800 008 255\n"
                                            f"More info here: https://mhmatters.life/viewtopic.php?t=10\n\n"
                    f"Type 'done' without the quotes to forget this ever happened")
                print(f'!uksuicide Command used by {username} sent to {channel}')
                return

            if user_inbound_message.lower() == 'nz':
                await client.get_channel(watch).send(f'{username} has told me their location is New Zealand 🇳🇿')
                await inbound.channel.purge(limit=2)
                await inbound.channel.send(
                    f"Get help now!, we are all here to listen but if its past our help please see below: \n"
                                            f"Emergancy:  111\n"
                                            f"(T1737: Call or Text 1737\n"
                                            f"The LockDown: Text 5626\n"
                                            f"More info here: https://mhmatters.life/viewtopic.php?t=11\n\n"
                    f"Type 'done' without the quotes to forget this ever happened")
                print(f'!uksuicide Command used by {username} sent to {channel}')
                return

            if user_inbound_message.lower() == 'other':
                await client.get_channel(watch).send(f'{username} has told me their location is Other (Not Known by us) ❓')
                await inbound.channel.purge(limit=2)
                await inbound.channel.send("Get help now!, we are all here to listen but if its past our help please see below: \n"
                        f"https://mhmatters.life/viewforum.php?f=9")

                print(f'!uksuicide Command used by {username} sent to {channel}')
                return

            if user_inbound_message.lower() == 'done':
                await inbound.channel.purge(limit=1000000)

                return

    client.run(TOKEN)
