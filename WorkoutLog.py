import os
import Exercises

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def readUserList():
    fileHandle = open('user.lis')
    listOfLines = fileHandle.readlines()
    fileHandle.close()
    return listOfLines

def userEntry(uName):
    username = {}
    username['Användarnamn'] = uName
    return username

def getUserInput():
    while True:
        userInput = input()
        if userInput:
            return userInput
        else:
            return "Felaktig inmatning"

def createUser():
    print("Skriv ditt namn: ")
    username = getUserInput()
    
    username = userEntry(username)
    print(username)
    
def printUser(username):
    uName = username ['Användarnamn']
    print(f"{uName}")
    
def welcomeMsg():
    print("\nVälkommen till din träningslogg!")
    print("Vad vill du göra?\n")
      
def main():
    welcomeMsg()
    while True:
        print("> Registrera användare - tryck R + enter")
        print("> Starta träningspasset - tryck T + enter")
        print("> Avsluta loggen - tryck S + enter")
        command = input(": ").lower()
        clear()
        if command == "r":
            createUser()
        elif command == "t":
            Exercises
            pass
        elif command == "s":
            print("Loggen avslutas")
            exit()
        else:
            print("Okänt kommando")      
  
main()