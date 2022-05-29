import urllib3
import urllib.request
import subprocess

file = open("VersionNumber.txt")
Version = (file.read())
file.close()
updateNow = False

def updateVersion():
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://wilde247.com/discordBot/version.txt')
    data = response.data.decode('utf-8')

    if data == Version:
        print(f"Your version is up to date: {data}")
    else:
        print("Your version is not up to date do you want to update now?")
        yesno = input('Type "yes" to update!: ')
        if yesno == 'yes':
            url = 'https://github.com/stephenwilde247/AthenaDiscordBot/archive/refs/heads/master.zip'
            urllib.request.urlretrieve(url, 'AthenaDiscordBot-master.zip')
            subprocess.call('unzip AthenaDiscordBot-master.zip')
            print("Closing Program Please Reload")
            print(f'Updating from {Version} to {data}')
            exit(0)
        else:
            print ('You chose no so continuing with outdated software')


updateVersion()