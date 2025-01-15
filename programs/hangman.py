import random

def guess_the_word_game():
    # List of words for the game
    word_list = ["python", "programming", "developer", "debugging", "hangman"]
    word = random.choice(word_list)
    guessed_word = ["_"] * len(word)
    attempts = 7  # Number of attempts allowed

    print("Welcome to the Guess the Word Game!")
    print("You have 7 attempts to guess the word.")
    
    while attempts > 0 and "_" in guessed_word:
        print("\nGuessed word so far:", " ".join(guessed_word))
        print(f"Attempts remaining: {attempts}")
        
        # Input guess from the player
        guess = input("Enter a letter: ").lower()
        
        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
            continue
        
        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            attempts -= 1

    # End of game
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nOut of attempts! The correct word was:", word)

if __name__ == "__main__":
    guess_the_word_game()
