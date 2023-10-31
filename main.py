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
    print("Encrypt (1) or Decrypt (2)")
    usageChoice = input().upper()

    if checkString(usageChoice):

        if usageChoice == "1":

            message = input("What message would you like to encrypt? \n").lower()
            encryptMessage(message)
            print("".join(encryptedMessage))
            encryptedMessage.clear()
            optionalExit()
        elif usageChoice == "2":

            message = input("What message would you like to decrypt? \n").lower()
            decryptMessage(message)
            print("".join(decryptedMessage))
            decryptedMessage.clear()
            optionalExit()
    else:
        os.system('cls')
        print("Please choose a valid input")

def checkString(stringMessage):

    if len(stringMessage) == 1 and isinstance(stringMessage, str):
        
        if stringMessage == "1" or stringMessage == "2":
            
            return True

    return False

def optionalExit():

    choice = input("Exit program (1) or return to beginning (2)")
    if checkString(choice):

        if choice == "1":

            global inLoop
            inLoop = False
        else:

            os.system('cls')
            print("Returning to the start..")
    else:

        print("Please choose a valid input")

        

# ENCRYPTION FUNCTIONS #

def caeserEncrypt(message):

    for letter in message:

        if letter == " ":
            encryptedMessage.append("*")
        else:
            letterIndex = lowercaseLetters.index(letter)
            encryptedMessage.append(lowercaseLetters[(letterIndex + 1) % 26])
        




def encryptMessage(message):
    caeserEncrypt(message)


# DECRYPTION FUNCTIONS #

def caeserDecrypt(message):

    for letter in message:

        if letter == "*":
            decryptedMessage.append(" ")
        else:
            letterIndex = lowercaseLetters.index(letter)
            if (letterIndex - 1 == -1):
                letterIndex = 26
            decryptedMessage.append(lowercaseLetters[(letterIndex - 1)])

def decryptMessage(messsage):
    caeserDecrypt(messsage)


# PRIMARY CODE EXECUTION #

print("WELCOME TO FLOOD GATE")

while inLoop:
    start()
