import csv
import sys

# The password list - We start with it populated for testing purposes.
passwords = [['yahoo', 'XqffoZeo'], ['google', 'CoIushujSetu']]


# The password file name to store the passwords to.
passwordFileName = 'samplePasswordFile'

# The encryption key for the caesar cypher.
encryptionKey = 16


def passwordencrypt(unencryptedMessage, key):  # Caesar Cypher Encryption.

    #  We will start with an empty string as our encryptedMessage.
    encryptedmessage = ''

    # For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage.
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedmessage += chr(num)
        else:
            encryptedmessage += symbol

    return encryptedmessage


def loadpasswordfile(fileName):

    with new_func(fileName) as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordlist = list(passwordreader)

    return passwordlist

def new_func(fileName):
    return open(fileName, newline='')


def savepasswordfile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)


while True:
    print('What would you like to do:')
    print(' 1. Open password file')
    print(' 2. Lookup a password')
    print(' 3. Add a password')
    print(' 4. Save password file')
    print(' 5. Print the encrypted password list (for testing)')
    print(' 6. Quit program')
    print('Please enter a number (1-6)')
    choice = input()

    if choice == '1':  # Load the password list from a file.
        passwords = loadpasswordfile(passwordFileName)

    if choice == '2':  # Lookup at password.
        print('Which website do you want to lookup the password for?')
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

        for i in range(len(passwords)):  # 1. Loops through the list of passwords
            if passwordToLookup == passwords[i][0]:  # 2. Checks if the name is found
                print(passwordencrypt(passwords[i][1], -16))  # 3. Prints out decrypted password, if found.

    if choice == '3':
        print('What website is this password for?')
        website = input()
        print('What is the password?')
        unencryptedPassword = input()

        encryptedPassword = passwordencrypt(unencryptedPassword, 16)  # 1. Encrypts the new password.
        newPassword = [website, encryptedPassword]  # 2. Creates a list with website name and encrypted password.
        passwords.append(newPassword)  # 3. Adds new password to list.

    if choice == '4':  # Save the passwords to a file.
        savepasswordfile(passwords, passwordFileName)

    if choice == '5':  # Print encrypted password list.
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if choice == '6':  # Quit our program.
        sys.exit()

    print()
    print()
