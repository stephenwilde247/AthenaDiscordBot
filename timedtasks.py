from inbound_messages import *
from server_info import TimedChannel
import discord

file = open("txt_files/timed_txt.txt")
timed_messages_output = (file.read())
file.close()

file = open("txt_files/rules.txt")
rules = (file.read())
file.close()

file = open("txt_files/rulespt2.txt")
rulespt2 = (file.read())
file.close()

file = open("txt_files/admins.txt")
admins = (file.read())
file.close()

file = open("txt_files/socials.txt")
socials = (file.read())
file.close()

def timed_messages():
    @client.event
    async def on_ready():
        print("Timed messages running")
        start_sending_messages.start()


    @tasks.loop(hours=24.00)
    async def start_sending_messages():
        #await client.get_channel(TimedChannel).send(file=discord.File('images/logo.png'))
        #await client.get_channel(TimedChannel).send(timed_messages_output)

        logo = discord.File("images/logo.png")

        em = discord.Embed(color=discord.Colour.blue())
        em.set_thumbnail(url='https://mhmatters.life/fpics/forumsig.png')

        em.set_image(url='https://mhmatters.life/styles/basic/theme/images/logo.png')
        em.add_field(name='Welcome to MHmatters Discord', value=timed_messages_output, inline=False)
        em.add_field(name='Rules', value=rules, inline=True)
        em.add_field(name='..', value=rulespt2, inline=True)
        em.add_field(name='... MHmatters Stuff! ...', value=f"......................................................................"
                                       f"............................. ", inline=False)
        em.add_field(name='Our Team', value=admins, inline=True)
        em.add_field(name='Our Socials', value=socials, inline=True)

        em.set_footer(text=f'Enjoy your time here!\n'
                           f'Did you know you can type yourcounty and suicide to get help examples are:\n '
                           f'!uksuicide - !usasuicide - !nzsuicide - !canadasuicide - !aussuicide - !suicide\n'
                           f'Athena bot has been programmed to be helpful!')

        #em.set_image(url="attachment://filename.png")

        #em.add_image(url='https://mhmatters.life/ext/dmzx/imageupload/img-files/58/4511292/2322038/e128abb9a0ca9923fe606ee3fba0c63c.png')
        print('Sending 24 hour card')
        await client.get_channel(TimedChannel).send(embed=em)

        print('working')
