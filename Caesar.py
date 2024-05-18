#Caesar Cipher in python

def enc(PT, Shift):
    result=""
    for i in range(len(PT)):
        char = PT[i]

        if(char.isupper()):
            result += chr((ord(char) + Shift - 65) % 26 + 65)

        else :
            result += chr((ord(char) + Shift -97) % 26 + 97)

    return result

def dec(CT, Shift):
    result = ""
    for i in range(len(CT)):
        char = CT[i]

        if(char.isupper()):
            result += chr((ord(char) - Shift - 65 ) % 26 + 65)

        else:
            result += chr((ord(char) - Shift -97 ) % 26 +97)

    return result

x = True

while(x):
    choice = int(input("Enter 1 to encrypt and 2 to decrypt:"))
    text = input("Enter the text:")
    key = int(input("Enter Key:"))

    if (choice==1):
        answer = enc(text, key)
        print("Encrypted Text:" + answer)

    elif (choice==2):
        answer = dec(text, key)
        print("Decrypted Text:" + answer)

    cont = int(input("Press 3 to exit, any other number to continue:"))

    if (cont ==3):
        x = False