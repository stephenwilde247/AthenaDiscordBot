import urllib3
import webbrowser

file = open("txt_files/VersionNumber.txt")
Version = (file.read())
file.close()

def updateVersion():
    http = urllib3.PoolManager()
<<<<<<< HEAD
    response = http.request('GET', 'http://wilde247.com/discordBot/version.txt')
=======
    response = http.request('GET', 'https://wilde247.com/discordBot/version.txt')
>>>>>>> c31cf7bd20fde46b6c7ed2194f923819561f5b74
    data = response.data.decode('utf-8')

    if data == Version:
        print(f"Your version is up to date: {data}")
    else:
        print("Your version is not up to date do you want to update now?")
        yesno = input('Type "yes" to visit the GitHub Repo update!: ')
        if yesno == 'yes':
            webbrowser.open('https://github.com/stephenwilde247/AthenaDiscordBot', new=2)
            print("Please remember to view the readme as updating can remove any code you have added to respond too")


