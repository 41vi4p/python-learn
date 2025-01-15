import random


def powerball_simulation():
   print("Welcome to the PowerBall Simulation App!")
   print("Enter 5 distinct numbers between 1 and 69 and 1 PowerBall number between 1 and 26.")


   # User Input
   user_numbers = []
   while len(user_numbers) < 5:
       try:
           num = int(input(f"Enter number {len(user_numbers) + 1} (1–69): "))
           if num < 1 or num > 69 or num in user_numbers:
               print("Invalid input. Enter a distinct number between 1 and 69.")
           else:
               user_numbers.append(num)
       except ValueError:
           print("Invalid input. Please enter an integer.")


   while True:
       try:
           user_powerball = int(input("Enter your PowerBall number (1–26): "))
           if 1 <= user_powerball <= 26:
               break
           else:
               print("Invalid input. Enter a number between 1 and 26.")
       except ValueError:
           print("Invalid input. Please enter an integer.")


   # Random Draw
   drawn_numbers = random.sample(range(1, 70), 5)
   drawn_powerball = random.randint(1, 26)


   # Sort numbers for display
   user_numbers.sort()
   drawn_numbers.sort()


   # Display Results
   print("\nYour Ticket Numbers:", user_numbers, "PowerBall:", user_powerball)
   print("Drawn Numbers:", drawn_numbers, "PowerBall:", drawn_powerball)


   # Check for a win
   if user_numbers == drawn_numbers and user_powerball == drawn_powerball:
       print("\nCongratulations! You won the PowerBall!")
   else:
       print("\nSorry, you didn't win. Better luck next time!")


if __name__ == "__main__":
   powerball_simulation()
