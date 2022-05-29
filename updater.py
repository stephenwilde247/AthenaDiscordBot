import urllib3
import urllib.request
import subprocess


def updateVersion():
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://wilde247.com/discordBot/version.txt')
    data = response.data.decode('utf-8')
    print (data)

    if data == '0.0.3\n':
        print("It matches continuing with program....")
        print(data)
    else:
        print("It don't match.. getting update......")
        url = 'https://github.com/stephenwilde247/AthenaDiscordBot/archive/refs/heads/master.zip'
        urllib.request.urlretrieve(url, 'AthenaDiscordBot-master.zip')
        subprocess.call('unzip AthenaDiscordBot-master.zip')
        print("Closing Program Please Reload")
        print(data)
        exit(0)

updateVersion()