# IMPORTED LIBRARIES #
import string

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

        if checkChars(message, "skip") and checkChars(keyword, ""):

            if usageChoice == "1":
                    encryptMessage(message, keyword)
                    encryptedMessage.clear()
                    optionalExit()

            elif usageChoice == "2":
                    decryptMessage(message, keyword)
                    decryptedMessage.clear()
                    optionalExit()
            
        else:
            print("Keep your message/keyword alphabetical")
    else:
        print("Please choose a valid input")

def checkString(stringMessage):

    if len(stringMessage) == 1 and isinstance(stringMessage, str):
        
        if stringMessage == "1" or stringMessage == "2":
            
            return True

    return False

def checkChars(string, usageChoice):

    if usageChoice == "skip":
        return True

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
        letterIndex = (lowercaseLetters.index(message[index]) + lowercaseLetters.index(usedKeyword[index]))
        encryptedMessage[index] = lowercaseLetters[(letterIndex % 26)]
    
    message = insertSpacings(message, spaceIndex, "encrypt")

def tsunamiEncrypt():
    global encryptedMessage

    for index in range(len(encryptedMessage)):
        encryptedMessage[index] = str(round(ord(encryptedMessage[index]) / 42, 3))
        
def endEncryption():
    finalMessage = " ".join(encryptedMessage)
    print(finalMessage)

def encryptMessage(message, keyword):
    caeserEncrypt(message)
    vigenereEncrypt(encryptedMessage, keyword)
    tsunamiEncrypt()
    endEncryption()

# DECRYPTION FUNCTIONS #

def caeserDecrypt():
    global decryptedMessage

    for index in range(len(decryptedMessage)):

        if decryptedMessage[index] == " ":
            decryptedMessage[index] = " "
        else:
            letterIndex = lowercaseLetters.index(decryptedMessage[index])
            if (letterIndex - 1 == -1):
                letterIndex = 26
            decryptedMessage[index] = (lowercaseLetters[(letterIndex - 1)])

def vigenereDecrypt(message, keyword):
    global decryptedMessage

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

        letterIndex = lowercaseLetters.index(message[index]) - lowercaseLetters.index(usedKeyword[index])
        if letterIndex < 0:
            letterIndex += 26

        decryptedMessage[index] = lowercaseLetters[(letterIndex) % 26]
    
    message = insertSpacings(message, spaceIndex, "decrypt")

def tsunamiDecrypt(message):
    
    global decryptedMessage

    decryptedMessage = message.split(" ")

    for index in range(len(decryptedMessage)):
        decryptedMessage[index] = chr(int(round(float(decryptedMessage[index]) * 42, 0)))

def endDecryption():
    finalMessage = "".join(decryptedMessage)
    print(finalMessage)

def decryptMessage(message, keyword):
    tsunamiDecrypt(message)
    vigenereDecrypt(decryptedMessage, keyword)
    caeserDecrypt()
    endDecryption()


# PRIMARY CODE EXECUTION #

print("WELCOME TO FLOOD GATE")

while inLoop:
    start()