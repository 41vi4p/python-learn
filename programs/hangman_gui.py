import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hangman Game")
        self.window.geometry("900x500")
        self.window.configure(bg="#2C3E50")
        
        # Word bank
        self.words = ["PYTHON", "PROGRAMMING", "COMPUTER", "ALGORITHM", "DATABASE", 
                     "NETWORK", "INTERFACE", "SOFTWARE", "DEVELOPER", "LEARNING"]
        
        # Game variables
        self.max_attempts = 6
        self.remaining_attempts = self.max_attempts
        self.guessed_letters = set()
        
        self.setup_game()
        self.create_widgets()
        
    def setup_game(self):
        self.word = random.choice(self.words)
        self.guessed_letters.clear()
        self.remaining_attempts = self.max_attempts
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.window, text="Hangman Game", 
                             font=("Helvetica", 24, "bold"),
                             bg="#2C3E50", fg="white")
        title_label.pack(pady=20)
        
        # Game status frame
        self.status_frame = tk.Frame(self.window, bg="#2C3E50")
        self.status_frame.pack(pady=10)
        
        self.attempts_label = tk.Label(self.status_frame, 
                                     text=f"Remaining Attempts: {self.remaining_attempts}",
                                     font=("Helvetica", 14),
                                     bg="#2C3E50", fg="white")
        self.attempts_label.pack()
        
        # Word display
        self.word_display = tk.Label(self.window, 
                                   font=("Courier", 24, "bold"),
                                   bg="#2C3E50", fg="white")
        self.word_display.pack(pady=20)
        
        # Letter buttons frame
        letters_frame = tk.Frame(self.window, bg="#2C3E50")
        letters_frame.pack(pady=20)
        
        # Create letter buttons
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        row = 0
        col = 0
        self.letter_buttons = {}
        
        for letter in letters:
            button = tk.Button(letters_frame, text=letter,
                             width=4, height=2,
                             font=("Helvetica", 12, "bold"),
                             command=lambda l=letter: self.guess_letter(l),
                             bg="#3498DB", fg="white",
                             activebackground="#2980B9")
            button.grid(row=row, column=col, padx=2, pady=2)
            self.letter_buttons[letter] = button
            
            col += 1
            if col > 12:
                col = 0
                row += 1
        
        # New game button
        new_game_button = tk.Button(self.window, text="New Game",
                                  font=("Helvetica", 14, "bold"),
                                  command=self.new_game,
                                  bg="#27AE60", fg="white",
                                  activebackground="#219A52")
        new_game_button.pack(pady=20)
        
        self.update_display()
        
    def update_display(self):
        display_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        self.word_display.config(text=display_word)
        self.attempts_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")
        
    def guess_letter(self, letter):
        if letter not in self.guessed_letters:
            self.guessed_letters.add(letter)
            self.letter_buttons[letter].config(state="disabled", bg="#95A5A6")
            
            if letter not in self.word:
                self.remaining_attempts -= 1
            
            self.update_display()
            self.check_game_status()
            
    def check_game_status(self):
        if self.remaining_attempts == 0:
            messagebox.showinfo("Game Over", f"You lost! The word was: {self.word}")
            self.new_game()
        elif all(letter in self.guessed_letters for letter in self.word):
            messagebox.showinfo("Congratulations", "You won!")
            self.new_game()
            
    def new_game(self):
        self.setup_game()
        self.update_display()
        for button in self.letter_buttons.values():
            button.config(state="normal", bg="#3498DB")
            
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = HangmanGame()
    game.run()