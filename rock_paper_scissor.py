#voter ID - name age address 2 options register , view voters- print only name and contact number
import random
a = ['rock', 'paper', 'scissor']

userCount = int(input("How many rounds do you wanna play?? "))

def getF():
    return random.choice(a)



playerPoints = 0
computerPoints = 0

def checkSystem(userChoice):
    if userChoice == f:
        print("It's a TIE")
        return "tie"
    
    # Rock scenarios
    elif userChoice == 'rock' and f == 'paper':
        print("I WIN :]")
        return "computer"
    elif userChoice == 'rock' and f == 'scissors':
        print("You WIN :[")
        return "player"
        
    # Paper scenarios    
    elif userChoice == 'paper' and f == 'rock':
        print("You WIN :[")
        return "player"
    elif userChoice == 'paper' and f == 'scissors':
        print("I WIN :]")
        return "computer"
        
    # Scissors scenarios
    elif userChoice == 'scissors' and f == 'rock':
        print("I WIN :]")
        return "computer"
    elif userChoice == 'scissors' and f == 'paper':
        print("You WIN :[")
        return "player"
    
def displayScore(playerPoints, computerPoints):
    print("\nScore:")
    print(" ___________________________")
    print("|    PLAYER  |   COMPUTER   |")
    print("|    "+str(playerPoints)+"       |   "+str(computerPoints)+"          |")
    print("|____________|______________|")

for i in range(userCount):
    userChoice = input("\nEnter rock, paper or scissors| e to END: ")
    userChoice = userChoice.lower()
    if(userChoice=='e'):
        print("BYE See you next time...")
        break
    f= getF()
    print(f)
    print("I choose ",f)
    winner= checkSystem(userChoice)
    
    if (winner=='player'):
        playerPoints +=1
        print("\nPLAYER WINS\n")
    elif(winner=='computer'):
        computerPoints+=1
        print("\nCOMPUTER WINS\n")
    elif(winner=='tie'):
        print("\nTIE")
    else:
        print("\nInvalid Input!")
        

    displayScore(playerPoints,computerPoints)
    
        
        
        
