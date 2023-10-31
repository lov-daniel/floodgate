# IMPORTED LIBRARIES #
import string
import os

# VARIABLE SETUP

inLoop = True
lowercaseLetters = list(string.ascii_lowercase)

encryptedMessage = []
decryptedMessage = []


# MAIN FUNCTIONS #

def start():

    global encryptedMessage
    global decryptedMessage

    usageChoice = input("Encrypt (1) or Decrypt (2)\n").upper()

    if checkString(usageChoice):

        message = input("Enter the message: \n").lower()
        keyword = input("Enter a keyword:\n").lower()

        if checkChars(message) and checkChars(keyword):

            if usageChoice == "1":
                    encryptMessage(message, keyword)
                    encryptedMessage.clear()
                    optionalExit()

            elif usageChoice == "2":
                    decryptMessage(message, keyword)
                    decryptedMessage.clear()
                    optionalExit()
            
        else:
            os.system('cls')
            print("Keep your message/keyword alphabetical")
    else:
        os.system('cls')
        print("Please choose a valid input")

def checkString(stringMessage):

    if len(stringMessage) == 1 and isinstance(stringMessage, str):
        
        if stringMessage == "1" or stringMessage == "2":
            
            return True

    return False

def checkChars(string):

    for letter in string:
        if letter not in lowercaseLetters:

            if (letter == " " or letter == "*"):
                continue
            return False
    return True

def optionalExit():

    choice = input("Exit program (1) or return to beginning (2)\n")
    if checkString(choice):

        if choice == "1":

            global inLoop
            inLoop = False
        else:

            os.system('cls')
            print("Returning to the start..")
    else:

        print("Please choose a valid input")

def insertSpacings(message, spaceIndexes, method):

    if method == "encrypt":
        for spaces in spaceIndexes:
            message.insert(spaces, "*")
    if method == "decrypt":
        for spaces in spaceIndexes:
            message.insert(spaces, " ")
    
    return message


# ENCRYPTION FUNCTIONS #

def caeserEncrypt(message):
    global encryptedMessage

    for letter in message:
        
        if letter == " ":
            encryptedMessage.append("*")
        else:
            letterIndex = lowercaseLetters.index(letter)
            encryptedMessage.append(lowercaseLetters[(letterIndex + 1) % 26])

def vigenereEncrypt(message, keyword):
    global encryptedMessage

    usedKeyword = ""
    spaceIndex = []

    for charIndex in range(len(message)):
        if message[charIndex] == "*":
            spaceIndex.append(charIndex)
    
    for elements in spaceIndex:
        message.remove("*")

    while len(message) > len(usedKeyword):
        for letter in keyword:
            usedKeyword += letter
            if len(message) == len(usedKeyword):
                break
        
    for index in range(len(message)):
        encryptedMessage[index] = lowercaseLetters[((lowercaseLetters.index(message[index]) + lowercaseLetters.index(usedKeyword[index])) % 26)]
    
    message = insertSpacings(message, spaceIndex, "encrypt")
    print(message)

def encryptMessage(message, keyword):
    caeserEncrypt(message)
    vigenereEncrypt(encryptedMessage, keyword)
    
    


# DECRYPTION FUNCTIONS #

def caeserDecrypt(message):
    global decryptedMessage

    for letter in message:

        if letter == "*":
            decryptedMessage.append(" ")
        else:
            letterIndex = lowercaseLetters.index(letter)
            if (letterIndex - 1 == -1):
                letterIndex = 26
            decryptedMessage.append(lowercaseLetters[(letterIndex - 1)])

def vigenereDecrypt(message, keyword):
    global decryptedMessage

    usedKeyword = ""
    spaceIndex = []

    for charIndex in range(len(message)):
        if message[charIndex] == " ":
            spaceIndex.append(charIndex)
    
    for elements in spaceIndex:
        message.remove(" ")

    while len(message) > len(usedKeyword):
        for letter in keyword:
            usedKeyword += letter
            if len(message) == len(usedKeyword):
                break
        
    for index in range(len(message)):

        letterIndex = lowercaseLetters.index(message[index]) - lowercaseLetters.index(usedKeyword[index])
        if letterIndex < 0:
            letterIndex += 26

        decryptedMessage[index] = lowercaseLetters[(letterIndex) % 26]
    
    message = insertSpacings(message, spaceIndex, "decrypt")
    print(message)

def decryptMessage(messsage, keyword):
    caeserDecrypt(messsage)
    vigenereDecrypt(decryptedMessage, keyword)


# PRIMARY CODE EXECUTION #

print("WELCOME TO FLOOD GATE")

while inLoop:
    start()
