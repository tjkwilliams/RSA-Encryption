import math
from typing import List
import random


def randomprime(limit):
    options = primenumlist(limit)
    choice = random.choice(options)
    return choice


# lcm(p - 1, q - 1)
def lcm(num1, num2):
    if num1 > num2:
        temp = num2
        num2 = num1
        num1 = temp

    oNum2 = num2
    i = 0

    while num2 % num1 != 0 and i != num1:
        num2 += oNum2
        i += 1

    return num2


def primenumlist(limit):
    # p_list= []
    p_list: List[int] = []

    for i in range(1, limit + 1):
        if isprime(i):
            p_list.append(i)

    return p_list


def isprime(number):
    if number == 1 or number == 0:
        return False

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False

    return True


# Assuming both numbers are prime
def ctotient(p, q):
    p = p - 1
    q = q - 1
    return lcm(p, q)


def etotient(p, q):
    return (p - 1) * (q - 1)


def mmi(e, tot):
    for X in range(1, tot):
        if ((e % tot) * (X % tot)) % tot == 1:
            return X
    return -1


def decrypt(ciphertext, hash):
    message = ""

    ct = ciphertext.split(" ")

    for c in ct:
        power = int(c) ** hash["d"]
        char = chr(power % hash["n"])

        message += str(char)

    return message

def decryptD(ciphertext, hash):
    message = ""

    for c in ciphertext:
        power = int(c) ** hash["d"]
        char = chr(power % hash["n"])

        message += str(char)

    return message

# Message is an array of integers
def encrypt(plaintext, hash):
    # coprime I've chosen for RSA encryption

    # c(m) = m^e mod n

    p_list: List[int] = []

    characters = []
    characters.extend(plaintext)

    ciphertext = ""

    for c in characters:
        i = ord(c)
        ciphertext = (i ** hash["e"]) % hash["n"]
        p_list.append(ciphertext)

    return p_list

def eprint(text):
    ret = ""
    for letter in text:
        ret += str(letter) + " "
    print("Encrypted Message: " + ret + "\n")

def hashfunc(p, q):
    hashmap = {"p": p, "q": q, "n": p * q, "tot": etotient(p, q), "d": 0}
    hashmap["e"] = randomprime(hashmap["tot"])
    hashmap["d"] = mmi(hashmap["e"], hashmap["tot"])
    return hashmap


def main():
    p = randomprime(200)
    q = randomprime(200)
    hash = hashfunc(13, 83)

    eList : List[int] = [] # List of Encrypted Messages
    dList : List[str] = [] # List of Decrypted Messages

    ans = input("\nWould you like to Encrypt or Decrypt a message?\n\nEncrypt: Press \"E\"\nDecrypt: Press \"D\"\nRecent Entries: \"R\"\nEncrypt Recent: \"ER\"\nDecrypt Recent: \"DR\"\nQuit: \"Q\"\nMessage: ").lower().rstrip()
    while ans != "q":
        print()
        if ans == "e":
            print("Encrypting...\n")

            plaintext = input("What message would you like to encrypt?\nMessage: ").rstrip()

            ciphertext = encrypt(plaintext,hash)

            eprint(ciphertext)

            if len(eList) == 5:
                eList.pop(0)

            eList.append(ciphertext)

        elif ans == "d":
            print("Decrypting...\n")

            ciphertext = input("What message would you like to decrypt? Please separate numbers with a space!\nExample: \"488 1050 563 563 436 955 464 436 400 563 529\"\n\nMessage: ").rstrip()

            # come back and make sure this is a valid input.

            ciphertext = ciphertext.replace(",", "")

            plaintext = decrypt(ciphertext,hash)

            print("Ciphertext: " + plaintext + "\n")

            if len(dList) == 5:
                dList.pop(0)

            dList.append(plaintext)

        elif ans == "r":

            if len(eList) > 0:
                print("Encryption Entries:")
                i = 1
                for e in eList:
                    print("\t" + str(i) + "] " + str(e))
                    i += 1
                print()
            else:
                print("No Encryption Entries yet.")

            if len(dList) > 0:
                print("Decryption Entries:")
                i = 1
                for d in dList:
                    print("\t" + str(i) + "] " + d)
                    i += 1
                print()
            else:
                print("No Decryption Entries yet.\n")
        elif ans == "er":

            i = 1
            if len(dList) > 0:
                print("Decryption Entries:")
                for d in dList:
                    print("\t" + str(i) + "] " + d)
                    i += 1
                if len(dList) == 1:

                    print("There's only one message to decrypt!")

                    plaintext = dList[0]

                    ciphertext = encrypt(plaintext, hash)

                    eprint(ciphertext)

                else:

                    done = False
                    while done == False:
                        n = input("Select the number of the option you'd like to Encrypt: ").rstrip()

                        if n.isnumeric() == True:
                            num = int(n) - 1

                            if num > 0 and num < len(dList) + 1:
                                done = True

                                plaintext = dList[num]

                                ciphertext = encrypt(plaintext, hash)

                                eprint(ciphertext)

                            else:
                                print("Please use a valid number.")

                        else:
                            print("\"" + n + "\" is not a number.")


            else:
                print("No recent entries to encrypt.")

        elif ans == "dr":
            i = 1
            if len(eList) > 0:
                print("Encryption Entries:")
                for e in eList:
                    print("\t" + str(i) + "] " + str(e))
                    i += 1
                if len(eList) == 1:

                    print("There's only one message to decrypt!")

                    ciphertext = eList[0]

                    plaintext = decryptD(ciphertext, hash)

                    print("Decrypted Message: " + plaintext)

                else:
                    num = 0

                    n = "Wow"

                    while num > len(eList) or num == 0 or n.isnumeric():
                        n = input("Select the number of the option you'd like to Decrypt: ").rstrip()

                        num = int(n) - 1

                    ciphertext = eList[num]

                    plaintext = decryptD(ciphertext, hash)

                    print("Decrypted Message: " + plaintext)

            else:
                print("No recent entries to decrypt.")

        else:
            print("\"" + ans + "\" is not an option!\n")

        ans = input("\nWould you like to Encrypt or Decrypt a message?\n\nEncrypt: Press \"E\"\nDecrypt: Press \"D\"\nRecent Entries: \"R\"\nEncrypt Recent: \"ER\"\nDecrypt Recent: \"DR\"\nQuit: \"Q\"\nMessage: ").lower().rstrip()

    print("\nThanks for playing!")


if __name__ == '__main__':

    main()

# Have the player choose an e
