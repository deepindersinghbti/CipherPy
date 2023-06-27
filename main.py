import sys
import random as rand

userChoice = int(input("Enter 1 for coding and 2 for decoding: "))
CHARS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

def GetMessage():
    if userChoice == 1:
        message = input("Enter your message to be coded: ")
    elif userChoice == 2:
        message = input("Enter your coded message: ")
    else:
        sys.exit(0)
    return message

def Code():
    message = GetMessage()
    words = message.split()  
    coded_words = []
    for word in words:
        if len(word) == 1:
            coded_word = word
        elif len(word) == 2:
            coded_word = word[::-1]
        else:
            coded_word = word[1:] + word[0]
            for _ in range(3):
                coded_word = rand.choice(CHARS) + coded_word + rand.choice(CHARS)
        coded_words.append(coded_word)
    return ' '.join(coded_words)  

def Decode():
    message = GetMessage()
    words = message.split()  
    decoded_words = []
    for word in words:
        if len(word) == 1:
            decoded_word = word
        elif len(word) == 2:
            decoded_word = word[::-1]
        elif len(word) > 2:
            decoded_word = word[3:-3]
            if len(decoded_word) > 0:
                decoded_word = decoded_word[-1] + decoded_word[:-1]
        else:
            decoded_word = '' 
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)  
if userChoice == 1:
    print("Coded message is: ", Code())
elif userChoice == 2:
    print("Decoded message is: ", Decode())
else:
    print("Invalid input.")
    sys.exit(0)
 