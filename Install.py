import os
from os import path

errorColor = "\033[31;40m"
boldText = "\033[1m"
defaultColor = "\033[m"
workingDirectory = os.getcwd()

print("Press [enter] to install, press [ctrl + c] to cancel")
pause = input()

def checkPathExist(path):
    if os.path.exists(path):
        return True
    else:
        return False

if checkPathExist("discord.tar.gz"):
    print("Found discord.tar.gz. The install can proceed.")
else:
    print(errorColor + "The file discord.tar.gz appears to be missing. Read the README file for help and information." + defaultColor)
    exit()
print("Checking if discord has already been installed...")
if checkPathExist("/usr/share/discord"):
    print(errorColor + "Discord has already been installed on this machine." + defaultColor)
    exit()
else:
    print("Starting install...")
    os.system("sudo dd if='discord.tar.gz' of='/usr/share/discord.tar.gz'")
    #os.system("sudo tar -xzf /usr/share/discord.tar.gz")
    os.system("sudo tar -C /usr/share/ -xzf /usr/share/discord.tar.gz")
    os.system("sudo rm /usr/share/discord.tar.gz")
    os.system("sudo mv '/usr/share/Discord' '/usr/share/discord'")
    os.system("sudo dd if='/usr/share/discord/discord.desktop' of='/usr/share/applications/discord.desktop'")
    print("Install completed")