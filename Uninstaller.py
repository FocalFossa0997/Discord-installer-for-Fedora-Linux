import os
from os import path

errorColor = "\033[31;40m"
boldText = "\033[1m"
defaultColor = "\033[m"

print("Press [enter] to uninstall, press [ctrl + c] to cancel")
pause = input()

def checkPathExist(path):
    if os.path.exists(path):
        return True
    else:
        return False

if checkPathExist("/usr/share/discord"):
    os.system("sudo rm -rd /usr/share/discord")
    if checkPathExist("/usr/share/applications/discord.desktop"):
        os.system("sudo rm /usr/share/applications/discord.desktop")
    else:
        pass
    print("Uninstall finished")
else:
    print(errorColor + "Discord has not been installed on this machine" + defaultColor)