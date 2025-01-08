#Find the 3rd Side of a Right Angled Traingle (using pythagoras theorem)
#AC^2 = AB^2 + BC^2

import math

def AC_and_AB(AC, AB):
    BC = math.sqrt(AC**2-AB**2)
    print(BC)

def AC_and_BC(AC, BC):
    AB= math.sqrt(AC**2 - BC**2)
    print(AB)

def AB_and_BC(AB, BC): #hypotenuse
    AC= math.sqrt(AB**2 - BC**2)
    print(AC)

def check_valid(a,b):
    if (a<=0 or b<=0):
        print("Invalid Input")
        return 1
    else:
        return 0
    

def main():
    choice = input("Which of the 2 values do you have?\n1. AC and BC\n2. AC and AB\n3. AB and BC")
    if choice==1:
        AC=int(input("Enter AC: ")) 
        BC=int(input("Enter BC: "))
        # if(check_valid(AC,BC)):
            # quit()
        # AC_and_BC(AC, BC)
        
    
    
main()