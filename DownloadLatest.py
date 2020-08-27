import os
from os import path

workingDirectory = os.getcwd()
errorColor = "\033[31;40m"
boldText = "\033[1m"
defaultColor = "\033[m"

print("Press [enter] to download the latest discord.tar.gz version, press [ctrl + c] to cancel")
pause = input()

def checkPathExist(path):
    if os.path.exists(path):
        return True
    else:
        return False

if checkPathExist("discord.tar.gz"):
    print("The file discord.tar.gz already exists.")
    selection = input("Do you want to redownload it? [N,y] ")
    if selection == "" or selection == "N" or selection == "n":
        print("Abort.")
        exit(0)
    elif selection == "y" or selection == "Y":
        print("Starting Redownload...")
        os.system("curl --output 'discord.tar.gz.redownload' 'https://dl.discordapp.net/apps/linux/0.0.11/discord-0.0.11.tar.gz'")
        if checkPathExist("discord.tar.gz.redownload"):
            os.system("rm 'discord.tar.gz'")
            os.system("mv 'discord.tar.gz.redownload' 'discord.tar.gz'")
            print("Successfully redownloaded file!")
        else:
            print(errorColor + "Failed to redownload file! Aborting..." + defaultColor)
            exit()
else:
    print("Starting Download...")
    os.system("curl --output 'discord.tar.gz' 'https://dl.discordapp.net/apps/linux/0.0.11/discord-0.0.11.tar.gz'")
    if checkPathExist("discord.tar.gz"):
        print("Successfully downloaded file!")
    else:
        print(errorColor + "Failed to download file! Aborting..." + defaultColor)