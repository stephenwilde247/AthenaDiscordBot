import urllib3

def updateVersion():
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://wilde247.com/discordBot/version.txt')
    data = response.data.decode('utf-8')

    if data == "version: 0.0.1\n":
        print("It matches continuing with program....")
    else:
        print("It dont match")
