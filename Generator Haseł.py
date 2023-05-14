# -*- coding: utf-8 -*-
import random

def generatePassword(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = [] 

    for i in pwlength:
        
        password = "" 
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
        passwords.append(password) 
    
    return passwords


def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword



def main():
    
    numPasswords = int(input("Ile haseł chcesz wygenerować? "))
    
    print("Generowanie " +str(numPasswords)+" haseł")
    
    passwordLengths = []

    print("Minimalna długość hasła powinna wynosić 3")

    for i in range(numPasswords):
        length = int(input("Podaj długość hasła #" + str(i+1) + " "))
        if length<3:
            length = 3
        passwordLengths.append(length)
    
    
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Hasło #"+str(i+1)+" = " + Password[i])



main()
