import os
import platform

def clearTerminal():
    system_platform = platform.system()
    if system_platform == 'Darwin':  # macOS
        os.system('clear')
    elif system_platform == 'Linux':
        os.system('clear')
    elif system_platform == 'Windows':
        os.system('cls')

#converts a list into a string
def listToString(list):
    listToStr = ','.join(map(str, list))
    return listToStr

#converts a string to a list
def stringToList(str):
    strToList = list(str.split(','))
    return strToList