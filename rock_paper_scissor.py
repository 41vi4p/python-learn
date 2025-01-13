#voter ID - name age address 2 options register , view voters- print only name and contact number

a = {'rock', 'paper', 'scissor'}

userCount = int(input("How many rounds do you wanna play?? "))

for e in a:
    f=a
    break

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
    

for i in range(userCount):
    userChoice = input("Enter rock, paper or scissor: ")
    userChoice = userChoice.lower()
    if (userChoice=='rock'):
        print("I choose ",f)
        if('ROCK'==f):
            
            print("It's a TIE")
        elif(userChoice=='paper'):
            print("I choose ",f)
            if('PAPER'==f):
                print("")
        elif(userChoice=='scissor'):
            print("I choose ",f)

